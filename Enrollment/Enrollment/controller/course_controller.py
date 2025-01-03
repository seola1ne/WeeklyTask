from flask import render_template, request, redirect, url_for, Blueprint
from util.dto import CourseFormDto
from service.course_service import CourseService

course_blueprint = Blueprint('course', __name__)
course_service = CourseService()

@course_blueprint.route('/register_course', methods=['POST'])
def post():    
    course_dto = CourseFormDto(
                                    name=request.form['name'],
                                    credit=int(request.form['credit']),
    )
    course_service.add_course(course_dto)
    return redirect(url_for('course.gets'))

@course_blueprint.route('/course_management', methods=['GET'])
def gets():
    courses = course_service.get_all_course()
    return render_template('course_management.html', courses = courses)
