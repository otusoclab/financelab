from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(9), nullable=False)
    course_id = db.Column(db.String(20), nullable=False)
    access_date = db.Column(db.String(10), nullable=False)
    access_time = db.Column(db.String(5), nullable=False)
    purpose = db.Column(db.String(50), nullable=False)
    other_purpose_text = db.Column(db.String(200))
    role = db.Column(db.String(50), nullable=False) 

# Create the database tables within the application context
with app.app_context():
    db.create_all()

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    student_id = request.form['studentID']
    course_id = request.form['courseID']
    access_date = request.form['accessDate']
    access_time = request.form['accessTime']
    purpose = request.form['purpose']
    other_purpose_text = request.form.get('otherPurposeText', '')
    role = request.form['role'] # Get the selected role

    name_regex = re.compile(r'^[A-Za-z\s]+$')
    student_id_regex = re.compile(r'^\d{9}$')
    course_id_regex = re.compile(r'^[A-Za-z0-9]+$')

    if not name_regex.match(name):
        return "Full Name must contain only letters and spaces."

    if not student_id_regex.match(student_id):
        return "Student ID must be a 9-digit number."

    if not course_id_regex.match(course_id):
        return "Course ID must contain only letters and numbers."

    student = Student(
        name=name,
        student_id=student_id,
        course_id=course_id,
        access_date=access_date,
        access_time=access_time,
        purpose=purpose,
        other_purpose_text=other_purpose_text,
        role=role # Set the role value
    )

    db.session.add(student)
    db.session.commit()

    return redirect(url_for('form'))

# Route to handle barcode scanning
@app.route('/scan', methods=['POST'])
def scan():
    # Get the barcode from the request
    barcode = request.form['barcode']
    
    # Connect to the database and fetch student details based on the barcode
    student = Student.query.filter_by(student_id=barcode).first()
    
    if student:
        # Return the student details as JSON
        return jsonify({'name': student.name, 'student_id': student.student_id})
    else:
        # Return an error if the student is not found
        return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)

