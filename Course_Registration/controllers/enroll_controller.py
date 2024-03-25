from flask import render_template, request, redirect, url_for, Blueprint

from services.enrollment_service import EnrollmentService
from util.dto import EnrollmentFormDto

enrollment_blueprint = Blueprint('enrollment', __name__)
enrollment_service = EnrollmentService()

@enrollment_blueprint.route('/')
def index():
    return render_template('index.html')

@enrollment_blueprint.route('/enrollment_management', methods=['GET'])
def gets():
    students = enrollment_service.get_students()
    courses = enrollment_service.get_courses()
    enrollments = enrollment_service.get_all()
    return render_template('enrollment_management.html', 
                           students = students, courses = courses, enrollments = enrollments)


@enrollment_blueprint.route('/register_enrollment', methods=['POST'])
def post():
    enrollment_dto = EnrollmentFormDto(
                                    student_id=int(request.form['student_id']),
                                    course_id=int(request.form['course_id']),
    )
    enrollment_service.add(enrollment_dto)
    return redirect(url_for('enrollment.gets'))

@enrollment_blueprint.route('/cancel_enrollment', methods=['POST'])
def delete():
    enrollment_id = int(request.form['enrollment_id']),
    print(enrollment_id)
    enrollment_service.delete(enrollment_id) 
    return redirect(url_for('enrollment.gets'))