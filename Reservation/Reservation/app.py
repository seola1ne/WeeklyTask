from flask import Flask
from controllers.reservation_controller import reservation_blueprint


app = Flask(__name__)

app.register_blueprint(reservation_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5001)