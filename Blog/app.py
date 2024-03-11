from flask import Flask
from controllers.blog_controller import blog_blueprint

app = Flask(__name__)
app.register_blueprint(blog_blueprint)

if __name__ == '__main__':
    app.run(debug=True)