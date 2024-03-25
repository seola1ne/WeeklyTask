from flask import Flask
from controllers.course_controller import course_blueprint
from controllers.student_controller import student_blueprint
from controllers.enroll_controller import enrollment_blueprint

app = Flask(__name__)

app.register_blueprint(course_blueprint)
app.register_blueprint(student_blueprint)
app.register_blueprint(enrollment_blueprint)

if __name__ == '__main__':
    app.run(debug=True)