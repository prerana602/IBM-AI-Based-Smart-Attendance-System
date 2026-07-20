from flask import Blueprint, render_template
import sqlite3

auth= Blueprint("auth", __name__)


@auth.route("/")
def login():
    return render_template("login.html")


@auth.route("/dashboard")
def dashboard():

    import sqlite3
    import os
    from datetime import date

    conn = sqlite3.connect("database/attendance.db")
    cursor = conn.cursor()

    # Total Students
   
    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    total_students = cursor.fetchone()[0]

    # Today's Attendance
    
    today = date.today().strftime("%Y-%m-%d")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE date=?
        """,
        (today,)
    )

    today_attendance = cursor.fetchone()[0]

    # Total Attendance Records

    cursor.execute(
        "SELECT COUNT(*) FROM attendance"
    )

    total_records = cursor.fetchone()[0]

    # Students Ready
    
    ready_students = 0

    cursor.execute(
        """
        SELECT student_id
        FROM students
        """
    )

    students = cursor.fetchall()

    for student in students:

        folder = os.path.join(
            "student_images",
            str(student[0])
        )

        if os.path.exists(folder):

            images = [

                f for f in os.listdir(folder)

                if f.endswith(".jpg")

            ]

            if len(images) >= 100:

                ready_students += 1

    conn.close()

    return render_template(

        "dashboard.html",

        total_students=total_students,

        today_attendance=today_attendance,

        total_records=total_records,

        ready_students=ready_students

    )