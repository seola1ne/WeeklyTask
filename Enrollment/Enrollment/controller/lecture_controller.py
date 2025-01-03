from flask import render_template, request, redirect, url_for, Blueprint
from util.dto import LectureFormDto
from service.lecture_service import LectureService

lecture_blueprint = Blueprint('lecture', __name__)
lecture_service = LectureService()

@lecture_blueprint.route('/lecture_management')
def gets():
    professors = lecture_service.get_all_professor() 
    courses = lecture_service.get_all_course() 
    lectures = lecture_service.get_all_lecture() 
    return render_template('lecture_management.html', professors=professors,courses=courses, lectures=lectures)

@lecture_blueprint.route('/register_lecture', methods=['POST'])
def register_lecture():
    professor_id = int(request.form['professor_id'])
    course_id = int(request.form['course_id'])
    day = request.form['day']
    start_time = request.form['start_time']
    lecture_dto = LectureFormDto(professor_id=professor_id, course_id=course_id, day=day, start_time=start_time)
    lecture_service.add_lecture(lecture_dto)
    return redirect(url_for('lecture.gets'))

@lecture_blueprint.route('/cancel_lecture', methods=['POST'])
def delete():
    lecture_id = int(request.form['lecture_id'])
    lecture_service.delete_lecture(lecture_id)
    return redirect(url_for('lecture.gets'))
