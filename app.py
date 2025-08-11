from flask import Flask, render_template, request
from pyresparser import ResumeParser
import os
import csv
import random



def load_questions_for_role(role_name):
    questions = []
    with open('questions.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['role'].lower().replace(" ", "_") == role_name.lower():
                questions.append({
                    'question': row['question'],
                    'option_a': row['option_a'],
                    'option_b': row['option_b'],
                    'option_c': row['option_c'],
                    'option_d': row['option_d'],
                    'answer': row['answer']
                })
    return questions

JOB_ROLES = {
    'Python Developer': {'python', 'django', 'flask'},
    'Data Scientist': {'python', 'machine learning', 'pandas', 'numpy'},
    'Frontend Developer': {'html', 'css', 'javascript', 'react'},
    'Backend Developer': {'nodejs', 'express', 'sql'},
    'DevOps Engineer': {'docker', 'kubernetes', 'ci/cd'},
}

def match_roles(user_skills):
    matched = []
    for role, required_skills in JOB_ROLES.items():
        if required_skills.intersection(set(s.lower() for s in user_skills)):
            matched.append(role)
    return matched


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/career', methods=['GET', 'POST'])
def index():
    skills = []
    name = ""
    email = ""
    error = ""
    matched_roles = []

    if request.method == 'POST':
        file = request.files['resume']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            try:
                data = ResumeParser(file_path).get_extracted_data()
                skills = data.get('skills', [])
                name = data.get('name', '')
                email = data.get('email', '')
                matched_roles = match_roles(skills)
            except Exception as e:
                error = str(e)

    return render_template(
        'index.html',
        skills=skills,
        name=name,
        email=email,
        error=error,
        matched_roles=matched_roles
    )

@app.route('/test/<role>', methods=['GET', 'POST'])
def take_test(role):
    all_questions = load_questions_for_role(role)
    
    # Select 20 random questions without repetition
    selected_questions = random.sample(all_questions, min(20, len(all_questions)))
    
    result = None
    passed = False

    if request.method == 'POST':
        correct = 0
        for i, q in enumerate(selected_questions):
            user_answer = request.form.get(f'q{i}')
            if user_answer == q['answer']:
                correct += 1

        score = correct / len(selected_questions)
        if score >= 0.5:
            result = f"You passed the test! ({correct}/{len(selected_questions)})"
            passed = True
        else:
            result = f"You did not pass the test. ({correct}/{len(selected_questions)})"

        return render_template('test.html', role=role, result=result, passed=passed)

    return render_template('test.html', role=role, questions=selected_questions)
if __name__ == '__main__':
    app.run(debug=True)
