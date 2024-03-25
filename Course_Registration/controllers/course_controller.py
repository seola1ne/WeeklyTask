from flask import render_template, request, redirect, url_for, Blueprint

from services.course_service import CourseService
from util.dto import CourseFormDto

course_blueprint = Blueprint('course', __name__)
course_service = CourseService()

@course_blueprint.route('/')
def index():
    return render_template('index.html')

@course_blueprint.route('/course_management', methods=['GET'])
def gets():
    courses = course_service.get_all()
    return render_template('course_management.html', courses = courses)

@course_blueprint.route('/register_course', methods=['POST'])
def post():
    course_dto = CourseFormDto(
                                name=request.form['name'],
                                professor=(request.form['professor']),
                                credit=int(request.form['credit']),
    )
    course_service.add(course_dto)
    return redirect(url_for('course.gets'))