import sqlite3

conn = sqlite3.connect("database/attendance.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM students WHERE student_id='102'")

conn.commit()

print("Duplicate students deleted successfully!")

conn.close()