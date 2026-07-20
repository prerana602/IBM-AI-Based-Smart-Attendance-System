from flask import Blueprint, render_template, request, Response
import sqlite3
import csv
import io

attendance = Blueprint("attendance", __name__)

# -----Attendance Page-----
@attendance.route("/attendance")
def attendance_page():
    return render_template("attendance.html")


@attendance.route("/reports")
def reports():

    # Get search values from the URL
    search = request.args.get("search", "")
    date = request.args.get("date", "")

    # Connect to database
    conn = sqlite3.connect("database/attendance.db")
    cursor = conn.cursor()

    # SQL query
    query = """
    SELECT student_id, name, date, time, status
    FROM attendance
    WHERE 1=1
    """

    parameters = []

    # Search by Student ID or Name
    if search:
        query += """
        AND (student_id LIKE ? OR name LIKE ?)
        """
        parameters.append(f"%{search}%")
        parameters.append(f"%{search}%")

    # Filter by Date
    if date:
        query += " AND date=?"
        parameters.append(date)

    # Sort newest records first
    query += " ORDER BY date DESC, time DESC"

    # Execute query
    cursor.execute(query, parameters)

    records = cursor.fetchall()

    conn.close()

    # Send data to HTML page
    return render_template(
        "reports.html",
        records=records,
        total=len(records),
        search=search,
        date=date
    )

# -----Exporting Attendance Report as CSV-----
@attendance.route("/export_csv")
def export_csv():

    conn = sqlite3.connect("database/attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT student_id,
           name,
           date,
           time,
           status
    FROM attendance
    ORDER BY date DESC, time DESC
    """)

    records = cursor.fetchall()

    conn.close()

    output = io.StringIO()

    writer = csv.writer(output)

    # CSV Header
    writer.writerow([
        "Student ID",
        "Name",
        "Date",
        "Time",
        "Status"
    ])

    # CSV Data
    writer.writerows(records)

    csv_data = output.getvalue()

    output.close()

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=attendance_report.csv"
        }
    )