from flask import Flask

from routes.auth_routes import auth
from routes.student_routes import student
from routes.attendance_routes import attendance
from routes.camera_routes import camera

app = Flask(__name__)
app.secret_key = "attendance_system_secret_key_2026"

app.register_blueprint(auth)
app.register_blueprint(student)
app.register_blueprint(attendance)
app.register_blueprint(camera)

if __name__ == "__main__":
    app.run(debug=True)