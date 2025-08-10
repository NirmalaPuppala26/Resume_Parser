📄 Resume Parser & Job Recommendation Website
A Flask-based company career portal that helps HR teams quickly identify top candidates. Applicants can upload their resumes, get AI-powered job suggestions, and take a short eligibility test. Only candidates who pass the test can be shortlisted by HR.

🚀 Features
📂 Resume Parsing – Extract skills, experience, and qualifications from uploaded resumes.

💼 Job Suggestions – AI-powered matching with relevant job openings.

📝 Eligibility Test – Quick quiz to verify if the candidate meets the job requirements.

👥 HR-Friendly – Helps recruiters focus on resumes that pass the eligibility test.

🌐 User-Friendly Interface – Simple and responsive design for both applicants and HR.

🛠 Tech Stack
Backend: Python (Flask)

Frontend: HTML, CSS (Jinja Templates)

Data Handling: CSV for test questions, PDF parsing for resumes

📌 How It Works
Candidate visits the Career Page.

Uploads their resume.

System analyzes and suggests relevant jobs.

Candidate takes a short eligibility test.

HR receives resumes of candidates who pass the test.

📥 Installation & Setup

# Clone the repository
git clone https://github.com/YourUsername/resume_parser.git

# Navigate into the project folder
cd resume_parser

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
