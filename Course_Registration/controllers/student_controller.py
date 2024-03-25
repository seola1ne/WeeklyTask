from flask import render_template, request, redirect, url_for, Blueprint

from services.student_service import StudentService
from util.dto import StudentFormDto

student_blueprint = Blueprint('student', __name__)
student_service = StudentService()

@student_blueprint.route('/')
def index():
    return render_template('index.html')

@student_blueprint.route('/student_management', methods=['GET'])
def gets():
    students = student_service.get_all()
    return render_template('student_management.html', students = students)

@student_blueprint.route('/register_student', methods=['POST'])
def add():
    student_dto = StudentFormDto(
                                number=int(request.form['number']),
                                name=request.form['name'],
                                gender=request.form['gender'],
    )
    student_service.add(student_dto)
    print(student_dto)
    return redirect(url_for('student.gets'))