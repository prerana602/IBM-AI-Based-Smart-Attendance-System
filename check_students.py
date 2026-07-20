import sqlite3

conn = sqlite3.connect("database/attendance.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("\nStudents Table:\n")

for row in rows:
    print(row)

conn.close()