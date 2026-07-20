from flask import Blueprint, redirect, url_for,flash
import subprocess
import sys

camera = Blueprint("camera", __name__)


@camera.route("/capture/<student_id>")
def capture(student_id):

    subprocess.Popen([
        sys.executable,
        "utils/capture_faces.py",
        student_id
    ])

    flash("Face dataset captured started.", "success")
    return redirect(url_for("student.student_list"))


@camera.route("/recognize")
def recognize():

    subprocess.Popen([
        sys.executable,
        "utils/recognize_faces.py"
    ])

    return redirect(url_for("auth.dashboard"))