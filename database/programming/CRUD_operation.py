import sqlite3
import os


if os.path.exists("school.db"): # removing the files if already exists
    os.remove("school.db")

# accessing database
conn = sqlite3.connect('school.db')
c = conn.cursor()

# Creating Table Student
c.execute('''create table student(ID integer primary key, NAME varchar(15), AGE integer, SEX varchar(15), GRADE integer)''')
c.execute('insert into student values(2019101, "Amar", 6, "Male", 1)')
c.execute('insert into student values(2019102, "Anil", 6, "Male", 1)')
c.execute('insert into student values(2019103, "Anusha", 6, "Female", 1)')
c.execute('insert into student values(2019104, "Akbar", 6, "Male", 1)')

# Creating Table teacher
c.execute('''create table teacher(ID varchar(8) primary key, NAME varchar(15), AGE integer, SEX varchar(15), SUBJECT varchar(15))''')
c.execute('insert into teacher values("2015T01", "Kamala", 26, "Female", "Maths")')
c.execute('insert into teacher values("2015T02", "Ajith Kumar", 32, "Male", "Science")')
c.execute('insert into teacher values("2015T03", "Shivkumar", 33, "Male", "Social")')
c.execute('insert into teacher values("2015T04", "Ranganath", 33, "Male", "Sports")')

conn.commit()


# Reading table Student
c.execute("SELECT * FROM student")
print(c.fetchall())


# Reading table teacher
c.execute("SELECT * FROM Student")
print(c.fetchall())

conn.commit()

# Updataion
c.execute('update teacher set NAME = "Ramesh" WHERE ID = "2015T04"') 
print("Upadated the table teacher, Changing the Name to Ramesh where ID = 2015T04")

c.execute('update student set NAME = "Anthony" WHERE ID = 2019104')
print("Upadated the table teacher, Changing the Name to Ramesh where ID = 2015T04")

conn.commit()

print("Reading table Student after updation")
c.execute("SELECT * FROM student")
print(c.fetchall())

print("Reading table teacher after updation")
c.execute("SELECT * FROM teacher")
print(c.fetchall())

conn.commit()

conn.close()