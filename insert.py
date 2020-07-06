import mysql.connector as connector
import pandas as pd

try:
    conn = connector.connect(
    host ='localhost',
    user= 'root',
    password='123456'
    )
    cursor = conn.cursor()
    cursor.execute('use project2020;')
    # insert operators
    op = pd.read_csv('data\Operators.csv')
    data_op = pd.DataFrame(op, columns = ["fname", 'lname','phonenumber','address'])
    for row in data_op.itertuples():
        cursor.execute('insert into operators(fname, lname, phonenumber, address) values (%s, %s, %s, %s)', (row.fname, row.lname, row.phonenumber, row.address))
    # insert students
    std = pd.read_csv('data\Students.csv')
    data_std = pd.DataFrame(std, columns = ["fname","lname","address","age",'classID','result'])
    for row in data_std.itertuples():
        cursor.execute('insert into students(fname,lname,address,age,classID,result) values (%s, %s, %s, %s, %s, %s)', (row.fname, row.lname, row.address, row.age, row.classID, row.result))
    # insert teachers
    teachers = pd.read_csv('data\Teachers.csv')
    data_teachers = pd.DataFrame(teachers, columns = ["fname","lname","age","phonenumber",'address','quality','classID', 'wage'])
    for row in data_teachers.itertuples():
        cursor.execute('insert into teachers(fname,lname,age,phonenumber,address,quality,classID,wage) values (%s, %s, %s, %s, %s, %s, %s, %s)', (row.fname, row.lname, row.age, row.phonenumber,row.address,row.quality, row.classID, row.wage))
    # insert classes
    classes = pd.read_csv('data\Classes.csv')
    data_class = pd.DataFrame(classes, columns = ["classname","subject","day","timestart",'timeend','teacherID','fee'])
    for row in data_class.itertuples():
        cursor.execute('insert into classes(classname,subject,day,timestart,timeend,teacherID,fee) values (%s, %s, %s, %s, %s, %s, %s)', (row.classname, row.subject, row.day, row.timestart,row.timeend,row.teacherID, row.fee)) 

    conn.commit()
except:
    print("oops")

def create_new_schema():
    cursor.execute("drop schema if exists project2020;")
    cursor.execute('create schema project2020;')
