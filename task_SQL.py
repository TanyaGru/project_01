import sqlite3
#connection = sqlite3.connect('teachers.db')
#cursor=connection.cursor()
#query = '''CREATE TABLE Students (
#Student_Id INTEGER NOT NULL PRIMARY KEY,
#Student_Name TEXT NOT NULL,
#School_Id INTEGER NOT NULL
#);'''
#cursor.execute(query)
#connection.commit()
#connection.close()

#connection = sqlite3.connect('teachers.db')
#cursor=connection.cursor()
#query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
#VALUES
#('201', 'Иван', 1),
#('202', 'Петр', 2),
#('203', 'Анастасия', 3),
#('204', 'Игорь', 4);"""
#cursor.execute(query)
#connection.commit()
#connection.close()

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor=connection.cursor()
    select_query="""SELECT * FROM School WHERE School_Id= ? """
    cursor.execute(select_query,(school_id,))
    record=cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

def get_student_school(student_id):
  try:
    connection = get_connection()
    cursor=connection.cursor()
    select_query="""SELECT * FROM Students WHERE Student_Id= ? """
    cursor.execute(select_query,(student_id,))
    records=cursor.fetchone()
    school_name=get_school_name(records[2])
    print(f'\nСтудент ID={student_id} из школы', school_name)
    print("ID студента: ", records[0])
    print("Имя студента: ", records[1])
    print("ID школы: ", records[2])
    print("Название школы: ", school_name, '\n')           
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

id_student=int(input("\nВведите ID студента(201, 202, 203, 204): "))
print('\nВариант №1')  
get_student_school(id_student) 



def get_student_school_join(student_id):
  try:
    connection = get_connection()
    cursor=connection.cursor()
    select_query="""SELECT * FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id=? """
    cursor.execute(select_query,(student_id,))
    records=cursor.fetchone()
    school_name=get_school_name(records[2])
    print(f'\nСтудент ID={student_id} из школы', school_name)
    print("ID студента: ", records[0])
    print("Имя студента: ", records[1])
    print("ID школы: ", records[2])
    print("Название школы: ", school_name, '\n')           
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

print('\nВариант №2') 
get_student_school_join(id_student)