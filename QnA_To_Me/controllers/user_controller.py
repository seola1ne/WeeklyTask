from flask import render_template, request, redirect, url_for, Blueprint

from services.user_service import UserService
from util.dto import UserFormDto

user_blueprint = Blueprint('user', __name__)
user_service = UserService()

@user_blueprint.route('/')
def index():
    return render_template('index.html')

@user_blueprint.route('/user_management', methods=['GET'])
def gets():
    users = user_service.get_all()
    return render_template('user_management.html', users = users)

@user_blueprint.route('/user_add', methods=['POST'])
def add():
    user_dto = UserFormDto(
                                name=request.form['name'],
                                email=request.form['email'],
                                join_date=request.form['joinDate'],
    )
    user_service.add(user_dto)
    print(user_dto)
    return redirect(url_for('user.gets'))