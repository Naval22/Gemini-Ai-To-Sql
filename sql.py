import sqlite3

#connect to sqlite
connection = sqlite3.connect("student.db")

## create a curser object insert record , create table,retrive

cursor = connection.cursor()

## create a table
table_info = """Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert record's

cursor.execute('''Insert Into STUDENT values('Taksheel','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('jay','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('pratik','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('rahul','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

## Display the record's

print("The inserted records are:")
data = cursor.execute("""SELECT * FROM STUDENT""")
for row in data:
    print(row)


## commit your changes into the database
connection.commit()
connection.close()        