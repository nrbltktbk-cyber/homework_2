import sqlite3

def create_table(connection):
    connection.execute('''DROP TABLE IF EXISTS users''')
    connection.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        age INTEGER,
        city TEXT
    )
    ''')
def add_student(connection, student_name, age, city):
    connection.execute('''
    INSERT INTO students
    (student_name, age, city) VALUES
    (?, ?, ?)
    ''', (student_name, age, city))
    connection.commit()

def delete_student(connection, student_id):
    connection.execute(
        'DELETE FROM students WHERE student_id = ?',
        (student_id,)
    )
    connection.commit()

def delete_student_by_name(connection, student_name):
     connection.execute(
          "DELETE FROM students WHERE student_name = ?",
         (student_name,)
     )
     connection.commit()



if __name__ == '__main__':
    conn = sqlite3.connect("database.db")
    add_student(conn, "Данил", 18, "Бишкек")
    add_student(conn, "Игорь", 18, "Каракол")
    delete_student(conn, 4)
    delete_student(conn, 5)
    delete_student(conn, 6)
