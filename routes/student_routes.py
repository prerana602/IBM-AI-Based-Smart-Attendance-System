from flask import (Blueprint, render_template, request, redirect,url_for,flash)
import sqlite3
import os
import shutil

student = Blueprint("student", __name__)


@student.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        student_id = request.form["student_id"]
        name = request.form["name"]
        course = request.form["course"]
        year = request.form["year"]
        session = request.form["session"]
        email = request.form["email"]
        phone = request.form["phone"]

        conn = sqlite3.connect("database/attendance.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO students
            (student_id, name, course, year, session, email, phone, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            student_id,
            name,
            course,
            year,
            session,
            email,
            phone,
            ""
        ))

        conn.commit()
        conn.close()

        flash("Student Registered Successfully!", "success")

        return redirect(url_for("student.register"))

    return render_template("register.html")

@student.route("/students")
def student_list():

    conn = sqlite3.connect("database/attendance.db")
    cursor = conn.cursor()

    # Search text
    search = request.args.get("search", "").strip()

    if search:

        cursor.execute("""
            SELECT student_id, name, course
            FROM students
            WHERE student_id LIKE ?
               OR name LIKE ?
            ORDER BY student_id
        """, (
            f"%{search}%",
            f"%{search}%"
        ))

    else:

        cursor.execute("""
            SELECT student_id, name, course
            FROM students
            ORDER BY student_id
        """)

    student_rows = cursor.fetchall()

    students = []

    for row in student_rows:

        student_id = row[0]

        # -----------------------------
        # Face Dataset Status
        # -----------------------------
        folder = os.path.join(
            "student_images",
            str(student_id)
        )

        if os.path.exists(folder):

            images = [

                f for f in os.listdir(folder)

                if f.endswith(".jpg")

            ]

            if len(images) >= 100:

                status = "Ready"

            else:

                status = f"{len(images)}/100"

        else:

            status = "Not Captured"

        # -----------------------------
        # Attendance Percentage
        # -----------------------------
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM attendance
            WHERE student_id=?
            """,
            (student_id,)
        )

        total_classes = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM attendance
            WHERE student_id=?
            AND status='Present'
            """,
            (student_id,)
        )

        present_classes = cursor.fetchone()[0]

        if total_classes == 0:

            percentage = 0

        else:

            percentage = round(
                (present_classes / total_classes) * 100,
                1
            )

        students.append({

            "student_id": row[0],

            "name": row[1],

            "course": row[2],

            "status": status,

            "attendance": percentage

        })

    conn.close()

    return render_template(

        "student_list.html",

        students=students

    )
    

@student.route("/edit_student/<student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    conn = sqlite3.connect("database/attendance.db")
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        course = request.form["course"]
        year = request.form["year"]
        session = request.form["session"]
        email = request.form["email"]
        phone = request.form["phone"]

        cursor.execute("""
            UPDATE students
            SET
                name=?,
                course=?,
                year=?,
                session=?,
                email=?,
                phone=?
            WHERE student_id=?
        """, (
            name,
            course,
            year,
            session,
            email,
            phone,
            student_id
        ))

        conn.commit()
        conn.close()

        flash("Student Updated Successfully!", "success")

        return redirect(url_for("student.student_list"))

    cursor.execute("""
        SELECT
            student_id,
            name,
            course,
            year,
            session,
            email,
            phone
        FROM students
        WHERE student_id=?
    """, (student_id,))

    student = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_student.html",
        student=student
    )

@student.route("/delete_student/<student_id>")
def delete_student(student_id):

    conn = sqlite3.connect("database/attendance.db")
    cursor = conn.cursor()

    # Delete student
    cursor.execute(
        "DELETE FROM students WHERE student_id=?",
        (student_id,)
    )

    # Delete attendance records
    cursor.execute(
        "DELETE FROM attendance WHERE student_id=?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    # Delete face dataset folder
    folder = os.path.join(
        "student_images",
        str(student_id)
    )

    if os.path.exists(folder):
        shutil.rmtree(folder)
 
    flash("Student Deleted Successfully!", "success")

    return redirect(url_for("student.student_list"))