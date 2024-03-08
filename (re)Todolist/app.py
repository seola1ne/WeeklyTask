from flask import Flask
from controllers.todo_controller import todo_blueprint
app = Flask(__name__)

app.register_blueprint(todo_blueprint)

if __name__ == '__main__':
    app.run(debug=True)