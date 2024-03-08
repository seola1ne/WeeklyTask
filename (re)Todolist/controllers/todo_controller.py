from flask import render_template, request, redirect, url_for, Blueprint
# from index import app
from services.todo_service import TodoService

todo_blueprint = Blueprint('todo', __name__)
todo_service = TodoService()

@todo_blueprint.route('/')
def index():
    tasks = todo_service.get_tasks()
    return render_template('tasks.html', tasks=tasks)

@todo_blueprint.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    todo_service.add_tasks({'name': task, 'completed': False})
    return redirect(url_for('todo.index')) # todo.index : todo_blueprint의 index() 실행

@todo_blueprint.route('/complete/<int:index>')
def complete_task(index):
    print(index)
    todo_service.complete_task(index)
    return redirect(url_for('todo.index'))

@todo_blueprint.route('/delete/<int:index>')
def delete_task(index):
    print(index)
    todo_service.delete_task(index)
    return redirect(url_for('todo.index'))