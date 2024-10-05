

# Resume Filtration System

A Flask-based API that allows users to upload resumes in CSV or PDF format and filters them based on the provided skills. The system dynamically extracts skills from the resumes and returns the frequency of the requested skill along with all identified skills.

## Features

- **Resume Upload**: Supports both CSV and PDF file uploads.
- **Skill Extraction**: Dynamically extracts skills from resumes.
- **Skill Frequency**: Counts the frequency of a given skill in the uploaded resume.
- **Formats**: Accepts resumes in CSV and PDF formats.

## Technologies Used

- **Flask**: For creating the API.
- **NLTK**: For text tokenization and natural language processing.
- **PyPDF2**: For extracting text from PDF files.
- **Pandas**: For handling CSV data.

## Prerequisites

- Python 3.x
- Pip package manager

### Install the Required Libraries

To install the required libraries, run the following:

```bash
pip install -r requirements.txt
```

If using a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Required Libraries

- Flask
- NLTK
- PyPDF2
- Pandas

## Setting Up

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/resume-filtration.git
   cd resume-filtration
   ```

2. **Install Dependencies**:

   Make sure the required dependencies are installed by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK Data**:

   Download the required NLTK data (tokenizer):

   ```python
   import nltk
   nltk.download('punkt')
   ```

4. **Run the Application**:

   Start the Flask application:

   ```bash
   python app.py
   ```

   By default, the app runs on `http://127.0.0.1:5000/`.

## API Usage

### 1. Upload Resume via cURL

To upload a resume using **cURL**, run the following command:

#### Upload a PDF File

```bash
curl -X POST http://127.0.0.1:5000/parseresume \
  -F "file=@/path/to/your/resume.pdf" \
  -F "skill=python"
```

#### Upload a CSV File

```bash
curl -X POST http://127.0.0.1:5000/parseresume \
  -F "file=@/path/to/your/resume.csv" \
  -F "skill=javascript"
```

#### Sample Response:

```json
{
    "filename": "resume.pdf",
    "skill": "python",
    "frequency": 2,
    "skills": ["html", "css", "python", "javascript", "react", "sql"]
}
```

### 2. Upload Resume via Postman

To upload a resume using **Postman**, follow these steps:

1. Open Postman and create a new `POST` request.
2. Set the URL to:
   ```
   http://127.0.0.1:5000/parseresume
   ```

3. In the **Body** tab, select `form-data` and add the following fields:
   - **Key**: `file` (Select the resume file)
   - **Key**: `skill` (Enter the skill you want to search for)

4. Click **Send** to upload the resume and see the response.

#### Sample Postman Configuration

- **Method**: `POST`
- **URL**: `http://127.0.0.1:5000/parseresume`
- **Body**: Form-Data

| Key   | Type   | Value                           |
|-------|--------|---------------------------------|
| file  | File   | Choose your PDF or CSV file     |
| skill | Text   | The skill you want to search    |

#### Example Response:

```json
{
    "filename": "resume.csv",
    "skill": "javascript",
    "frequency": 3,
    "skills": ["html", "css", "javascript", "python", "sql"]
}
```

## Directory Structure

```
.
├── app.py                 # Main Flask application
├── uploads/               # Directory where uploaded resumes are stored
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```



---

### Notes:
- Make sure to replace the repository URL (`https://github.com/yourusername/resume-filtration.git`) with the actual URL of your GitHub repository.
- The `requirements.txt` should include all necessary dependencies, and you can generate it by running:

  ```bash
  pip freeze > requirements.txt
  ```

This `README.md` should help you provide clear instructions on how to run and use your Resume Filtration project with both cURL and Postman! Let me know if you need further changes or additions.
