from flask import Flask, render_template, request, redirect
from models import db, Subject, Schedule

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subject', methods=['GET', 'POST'])
def subject():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            new_subject = Subject(name=name)
            db.session.add(new_subject)
            db.session.commit()
    subjects_list = Subject.query.all()
    return render_template('subjects.html', subjects=subjects_list)

@app.route('/delete_subject/<int:subject_id>', methods=['POST'])
def delete_subject(subject_id):
    subject = Subject.query.get(subject_id)
    if subject:
        db.session.delete(subject)
        db.session.commit()
    return redirect('/subject')


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        day = request.form.get('day')
        num = request.form.get('number')
        subject_id = request.form.get('subject_id')
        if day and num and subject_id:
            new_lesson = Schedule(day=day, number=num, subject_id=subject_id)
            db.session.add(new_lesson)
            db.session.commit()
    subjects = Subject.query.all()
    lessons = Schedule.query.all()
    return render_template('schedule.html', subjects=subjects, lessons = lessons)


@app.route('/delete_lesson/<int:lesson_id>', methods=['POST'])
def delete_lesson(lesson_id):
    lesson = Schedule.query.get(lesson_id)
    if lesson:
        db.session.delete(lesson)
        db.session.commit()
    return redirect('/schedule')


if __name__ == '__main__':
    app.run(debug=True)