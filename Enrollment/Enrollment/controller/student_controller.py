from flask import render_template,redirect,url_for, request, Blueprint, jsonify, Response, json
from service.student_service import StudentService
from util.dto import StudentFormDto

student_blueprint = Blueprint('student', __name__)
student_service = StudentService()

@student_blueprint.route('/')
def index():
    return render_template('index.html')

@student_blueprint.route('/timetable')
def timetable():
    return render_template('timetable.html')

@student_blueprint.route('/register_student', methods=['POST'])
def post():    
    reservation_dto = StudentFormDto(
                                    number=int(request.form['number']),
                                    name=request.form['name'],
                                    gender=request.form['gender'],
    )
    student_service.add_student(reservation_dto)
    return redirect(url_for('student.gets'))

@student_blueprint.route('/student_management', methods=['GET'])
def gets():
    students = student_service.get_all_student()
    return render_template('student_management.html', students = students)

@student_blueprint.route('/students', methods=['GET'])
def get_students():
    students = student_service.get_all_student()
    return Response(json.dumps(students, ensure_ascii=False), mimetype='application/json; charset=utf-8')
    
@student_blueprint.route('/schedule/student/<int:student_id>', methods=['GET'])
def get_schedule(student_id):
    schedule = student_service.get_schedule_student(student_id)
    return Response(json.dumps(schedule, ensure_ascii=False), mimetype='application/json; charset=utf-8')