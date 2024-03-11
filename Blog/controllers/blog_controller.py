# 수정사항 없음 - 예시로 제공된 기존 코드가 잘 구성되어 있음
from flask import render_template, request, redirect, url_for, Blueprint
from services.blog_service import BlogService

blog_blueprint = Blueprint('blog', __name__)
blog_service = BlogService()

@blog_blueprint.route('/')
def index():
    posts = blog_service.get_posts()
    return render_template('index.html', posts=posts)

@blog_blueprint.route('/new_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'GET':
        return render_template('create.html')
    
    elif request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        blog_service.add_post(title, content, author)
        return redirect(url_for('blog.index'))

@blog_blueprint.route('/update/<int:id>', methods=['GET', 'POST'])
def update_post(id):
    post = blog_service.get_post(id)
    
    if request.method == 'GET':
        return render_template('update.html', post=post)
    
    elif request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        blog_service.update_post(title, content, author, id)
        return redirect(url_for('blog.index'))

@blog_blueprint.route('/delete/<int:id>')  
def delete_post(id):
   blog_service.delete_post(id)
   return redirect(url_for('blog.index'))