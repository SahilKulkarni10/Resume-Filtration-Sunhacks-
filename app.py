import os
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
import re
from collections import Counter
import string
import PyPDF2  


app = Flask(__name__)


UPLOAD_FOLDER = './uploads/resume/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


COMMON_SKILLS = [
    "html", "css", "javascript", "react", "node", "python", "java", "c++",
    "sql", "mongodb", "ai", "ml", "data analysis", "machine learning", "deep learning", "mern", "docker"
]


@app.route('/parseresume', methods=['POST'])
def uploadResume():
    
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400


    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)


    def read_pdf(file_path):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + ' '
        return text.strip()


    if file.filename.endswith('.csv'):
        df = pd.read_csv(filepath, encoding='latin1')
        resume_text = df.iloc[:, 0].astype(str).str.cat(sep=' ') 
    elif file.filename.endswith('.pdf'):
        resume_text = read_pdf(filepath)
    else:
        return jsonify({"error": "Unsupported file type. Please upload a CSV or PDF file."}), 400

    def cleanResume(resumeText):
        resumeText = re.sub('http\S+\s*', ' ', resumeText) 
        resumeText = re.sub('RT|cc', ' ', resumeText)  
        resumeText = re.sub('#\S+', '', resumeText)  
        resumeText = re.sub('@\S+', '  ', resumeText)  
        resumeText = re.sub('[%s]' % re.escape(string.punctuation), ' ', resumeText)  
        resumeText = re.sub(r'[^\x00-\x7f]', r' ', resumeText)  
        resumeText = re.sub('\s+', ' ', resumeText)  
        return resumeText.lower()  

    cleaned_resume = cleanResume(resume_text)

    
    skill_count = {skill: cleaned_resume.count(skill.lower()) for skill in COMMON_SKILLS}

    
    req_skill = request.form.get('skill', '').lower()

    
    skill_frequency = skill_count.get(req_skill, 0)

    return jsonify(
        filename=file.filename,
        skill=req_skill,
        frequency=skill_frequency,
        skills=skill_count  
    )

if __name__ == '__main__':
    app.run(debug=True)
