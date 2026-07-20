import sqlite3

conn = sqlite3.connect("database/attendance.db")

cursor = conn.cursor()

# For Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id TEXT,

    name TEXT,

    course TEXT,

    year TEXT,

    session TEXT,

    email TEXT,

    phone TEXT,

    photo TEXT

)
""")

# For Attendance Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id TEXT,

    name TEXT,

    date TEXT,

    time TEXT,

    status TEXT

)
""")

# It saves changes
conn.commit()

# It closes the connection 
conn.close()

print("Database tables created successfully.")