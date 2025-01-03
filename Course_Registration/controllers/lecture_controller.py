from flask import render_template, request, redirect, url_for, Blueprint
from Course_Registration.services.professor_service import ProfessorService
from Course_Registration.services.course_service import CourseService

from services.lecture_service import LectureService
from util.dto import LectureFormDto

lecture_blueprint = Blueprint('lecture', __name__)

professor_service = ProfessorService()
course_service = CourseService()
lecture_service = LectureService()

@lecture_blueprint.route('/')
def index():
    return render_template('index.html')

@lecture_blueprint.route('/lecture_management', methods=['GET'])
def gets():
    if request.method == 'GET':
        professors = professor_service.get_all()
        courses = course_service.get_all()
        lectures = lecture_service.get_all()
        return render_template('lecture_management.html', professors = professors, courses = courses, lectures = lectures)

@lecture_blueprint.route('/register_lecture', methods=['POST'])
def add():
    lecture_dto = LectureFormDto(
                                    professor_id = int(request.form['professor_id']),
                                    course_id = int(request.form['course_id']),
                                    day = request.form['day'],
                                    start_time = request.form['start_time'],
                                    end_time = request.form['end_time'],
    )
    lecture_service.add(lecture_dto)
    return redirect(url_for('lecture.gets'))