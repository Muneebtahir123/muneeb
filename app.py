from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_report():
    student_name = input['student_name']
    num_subjects = int(input['num_subjects'])

    subjects = []
    total_full = 0
    total_obtained = 0

    for i in range(num_subjects):
        subject = request.form[f'subject_{i}']
        full_marks = int(request.form[f'full_{i}'])
        obtained = int(request.form[f'obtained_{i}'])

        subjects.append((subject, full_marks, obtained))
        total_full += full_marks
        total_obtained += obtained

    percentage = (total_obtained / total_full) * 100

    return render_template('result.html',
                           student_name=student_name,
                           subjects=subjects,
                           total_full=total_full,
                           total_obtained=total_obtained,
                           percentage=round(percentage, 2))

if __name__ == '__main__':
    app.run(debug=True)
