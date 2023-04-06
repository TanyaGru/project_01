# Создание БД
#import sqlite3
#connection = sqlite3.connect('teachers.db')
#cursor=connection.cursor()
#query = '''CREATE TABLE School (
#School_Id INTEGER NOT NULL PRIMARY KEY,
#School_Name TEXT NOT NULL,
#Place_Count INTEGER NOT NULL
#);'''

#cursor.execute(query)
#connection.commit()
#connection.close()

#import sqlite3
#connection = sqlite3.connect('teachers.db')
#cursor=connection.cursor()
#query = '''CREATE TABLE Teatcher (
#Teatcher_Id INTEGER NOT NULL PRIMARY KEY,
#Teatcher_Name TEXT NOT NULL,
#School_Id INTEGER NOT NULL,
#Joining_Date TEXT NOT NULL,
#Speciality TEXT NOT NULL,
#Salary INTEGER NOT NULL,
#Experience INTEGER
#);
#'''

#cursor.execute(query)
#connection.commit()
#connection.close()

#import sqlite3
#connection = sqlite3.connect('teachers.db')
#cursor=connection.cursor()
#query = '''CREATE TABLE Teatcher (
#Teatcher_Id INTEGER NOT NULL PRIMARY KEY,
#Teatcher_Name TEXT NOT NULL,
#School_Id INTEGER NOT NULL,
#Joining_Date TEXT NOT NULL,
#Speciality TEXT NOT NULL,
#Salary INTEGER NOT NULL,
#Experience INTEGER
#);
#'''

#cursor.execute(query)
#connection.commit()
#connection.close()

#import sqlite3
#connection = sqlite3.connect('teachers.db')
#cursor=connection.cursor()
#query = """INSERT INTO Teatcher (Teatcher_Id, Teatcher_Name, School_Id,
#Joining_Date, Speciality, Salary, Experience)
#VALUES
#('101', 'Галина', '1', '2021-2-10', 'Физик', '40000', NULL),
#('102', 'Мария', '1', '2018-07-23', 'Химик', '20000', NULL),
#('103', 'Ольга', '2', '2022-05-19', 'Информатик', '25000', NULL),
#('104', 'Полина', '2', '2017-12-28', 'Физик ', '28000', NULL),
#('105', 'Лидия', '3', '2015-06-04', 'Информатик', '42000', NULL),
#('106', 'Анастасия', '3', '2019-09-11', 'Учитель трудов', '30000',NULL),
#('107', 'Ирина', '4', '2020-08-21', 'Информатик', '32000',NULL),
#('108', 'Виктория', '4', '2017-10-17', 'Географ', '30000', NULL);"""
#cursor.execute(query)
#connection.commit()
#connection.close()


#import sqlite3
#connection = sqlite3.connect('teachers.db')
#cursor=connection.cursor()
#query = """INSERT INTO School (School_Id, School_Name, Place_Count)
#VALUES
#('1', 'Протон', 200),
#('2', 'Преспектива', 300),
#('3', 'Спектр', 400),
#('4', 'Содружество', 500);"""
#cursor.execute(query)
#connection.commit()
#connection.close()

#Gjlrk.x и вывести версию ЬД
import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def read_db_ver():
  try:
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute("SELECT sqlite_version();")
    db_ver=cursor.fetchone()
    print(db_ver)
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

print("задача 2")
#read_db_ver()

# появился опыт зад 3

#import sqlite3
connection = sqlite3.connect('teachers.db')
cursor=connection.cursor()
update_query="UPDATE Teatcher SET Experience = 5 WHERE School_Id = 1"
cursor.execute(update_query)
connection.commit()
connection.close()

# 4 зад вывести данные

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_detail(school_id):
  try:
    connection = get_connection()
    cursor=connection.cursor()
    select_query="""SELECT * FROM School WHERE School_Id= ? """
    cursor.execute(select_query,(school_id,))
    records=cursor.fetchall()
    print('Данные по школе')
    for row in records:
      print("ID школы: ", row[0])
      print("Название школы: ", row[1])
      print("Количество мест: ", row[2])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

def get_teacher_detail(teacher_id):
  try:
    connection = get_connection()
    cursor=connection.cursor()
    select_query="""SELECT * FROM Teatcher WHERE Teatcher_Id= ? """
    cursor.execute(select_query,(teacher_id,))
    records=cursor.fetchall()
    print('Данные по учителям')
    for row in records:
      print("Teatcher_Id: ", row[0])
      print("Имя учителя: ", row[1])
      print("ID школы: ", row[2])
      print("Нач. работы: ", row[3])
      print("Спец-ия: ", row[4])
      print("Зарплата: ", row[5])
      print("Опыт работы: ", row[6])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

print("Задача 4")  
get_school_detail(1) 

get_teacher_detail(101)

# зад 5

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_spec_teacher_list(speciality, salary):
  try:
    connection = get_connection()
    cursor=connection.cursor()
    select_query="""SELECT * FROM Teatcher WHERE Speciality= ? and Salary>?"""
    cursor.execute(select_query,(speciality, salary))
    records=cursor.fetchall()
    print('Учителя по спец-ти',speciality, "c зарплатой больше",salary, "\n")
    for row in records:
      print("Teatcher_Id: ", row[0])
      print("Имя учителя: ", row[1])
      print("ID школы: ", row[2])
      print("Нач. работы: ", row[3])
      print("Спец-ия: ", row[4])
      print("Зарплата: ", row[5])
      print("Опыт работы: ", row[6])      
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

print("Зад 5 \n")
get_spec_teacher_list("Физик", 30000)


# задача 6
import sqlite3

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
    #close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

def get_teacher(school_id):
  try:
    school_name=get_school_name(school_id)
    connection = get_connection()
    cursor=connection.cursor()
    select_query="""SELECT * FROM Teatcher WHERE School_Id= ? """
    cursor.execute(select_query,(school_id,))
    records=cursor.fetchall()
    print('Учителя из школы', school_name)
    for row in records:
      print("Teatcher_Id: ", row[0])
      print("Имя учителя: ", row[1])
      print("ID школы: ", row[2])
      print("Название школы: ", school_name)
      print("Нач. работы: ", row[3])
      print("Спец-ия: ", row[4])
      print("Зарплата: ", row[5])
      print("Опыт работы: ", row[6])      
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка", error)

print("Задача 6")  
get_teacher(1) 
