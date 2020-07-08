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

    #insert employees
    emp = pd.read_csv('data\employees.csv')
    data_emp = pd.DataFrame(emp, columns = ["fname", 'lname','address', 'age'])
    for row in data_emp.itertuples():
        cursor.execute('insert into employees(fname,lname,address,age) values (%s, %s, %s, %s)', (row.fname, row.lname, row.address, row.age))
    # insert operators
    op = pd.read_csv('data\Operators.csv')
    data_op = pd.DataFrame(op, columns = ["employeeID", 'workShift'])
    for row in data_op.itertuples():
        cursor.execute('insert into operators(employeeID,workShift) values (%s, %s)', (row.employeeID, row.workShift))

    # insert teachers
    teachers = pd.read_csv('data\Teachers.csv')
    data_teachers = pd.DataFrame(teachers, columns = ["employeeID", "quality","classID"])
    for row in data_teachers.itertuples():
        cursor.execute('insert into teachers(employeeID,quality,classID) values (%s, %s, %s)', (row.employeeID, row.quality, row.classID))

    # insert result
    res = pd.read_csv('data\Result.csv')
    data_result = pd.DataFrame(res, columns=['studentID','result'])
    for row in data_result.itertuples():
        cursor.execute('insert into result(studentID, result) values(%s, %s)', (row.studentID, row.result))
        
    # insert salary
    sal = pd.read_csv('data\Salary.csv')
    data_sal = pd.DataFrame(sal, columns=['employeeID','salary'])
    for row in data_sal.itertuples():
        cursor.execute('insert into salary(employeeID, salary) values(%s, %s)', (row.employeeID, row.salary))

    # insert students
    std = pd.read_csv('data\Students.csv')
    data_std = pd.DataFrame(std, columns = ["fname","lname","address","age",'classID'])
    for row in data_std.itertuples():
        cursor.execute('insert into students(fname,lname,address,age,classID) values (%s, %s, %s, %s, %s)', (row.fname, row.lname, row.address, row.age, row.classID))
    # insert classes
    classes = pd.read_csv('data\Classes.csv')
    data_class = pd.DataFrame(classes, columns = ["classname","subjectID","schedule","timestart",'timeend','teacherID','fee'])
    for row in data_class.itertuples():
        cursor.execute('insert into classes(classname,subjectID,schedule,timestart,timeend,teacherID,fee) values (%s, %s, %s, %s, %s, %s, %s)', (row.classname, row.subjectID, row.schedule, row.timestart,row.timeend,row.teacherID, row.fee)) 
    # insert subject
    # subject = pd.read_csv("data\Subjects.csv")
    # data_subj = pd.DataFrame(subject, columns = ['name'])
    cursor.execute('insert into subjects(name) values("ADS")')
    cursor.execute('insert into subjects(name) values("DIP")')
    cursor.execute('insert into subjects(name) values("DB")')
    cursor.execute('insert into subjects(name) values("OS")')
    conn.commit()
except:
    print("oops")
