from flask import render_template, request, redirect, url_for, Blueprint

from service.enrollment_service import EnrollmentService

from util.dto import EnrollmentFormDto

enrollment_blueprint = Blueprint('enrollment', __name__)
enrollment_service = EnrollmentService()

@enrollment_blueprint.route('/enrollment_management', methods=['GET'])
def gets():
    enrollments = enrollment_service.get_all_enrollment()
    students = enrollment_service.get_all_student() 
    lectures = enrollment_service.get_all_lecture() 
    return render_template('enrollment_management.html', enrollments=enrollments, students=students, lectures=lectures)

@enrollment_blueprint.route('/register_enrollment', methods=['POST'])
def post():
    student_id = int(request.form['student_id'])
    lecture_id = int(request.form['lecture_id'])
    course_id = enrollment_service.get_course_by_id(lecture_id)
    enrollment_dto = EnrollmentFormDto(student_id=student_id, course_id=course_id, lecture_id=lecture_id)
    enrollment_service.add_enrollment(enrollment_dto)
    return redirect(url_for('enrollment.gets'))

@enrollment_blueprint.route('/cancel_enrollment', methods=['POST'])
def delete():
    enrollment_id = request.form['enrollment_id']
    enrollment_service.delete_enrollment(enrollment_id)
    return redirect(url_for('enrollment.gets'))
