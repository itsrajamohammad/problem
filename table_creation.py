import sqlite3
from sqlite3 import Error
 

def sql_connection():
   try:
     conn = sqlite3.connect('mydatabase.db')
     return conn
   except Error:
     print(Error)
 
def sql_table(conn):
   cursorObj = conn.cursor()
#DROP TABLE [IF EXISTS]
   cursorObj.execute("DROP TABLE Employee")
   cursorObj.execute("DROP TABLE Department")
   cursorObj.execute("DROP TABLE Project")
   print("table droped")
   conn.commit()
# Create Employee table
   cursorObj.execute("CREATE TABLE Employee(emp_id n(5), emp_name char(30), salary n(10));")
# Insert records
   cursorObj.executescript("""
   INSERT INTO Employee VALUES(1,'a', 25000);
   INSERT INTO Employee VALUES(2,'b', 25000);
   INSERT INTO Employee VALUES(3,'c', 15000);
   INSERT INTO Employee VALUES(4,'d', 25000);
   INSERT INTO Employee VALUES(5,'e', 15000);
   """)
   
   conn.commit()
# Create Department table
   cursorObj.execute("CREATE TABLE Department( dep_name char(30),emp_id n(5) ,foreign key(emp_id) references Employee(emp_id));")
# Insert records
   cursorObj.executescript("""
   INSERT INTO Department VALUES('MANAGER',1);
   INSERT INTO Department VALUES('MANAGER',2);
   INSERT INTO Department VALUES('ANALYST',3);
   INSERT INTO Department VALUES('MANAGER',4);
   INSERT INTO Department VALUES('ANALYST',7);
   """)
   conn.commit()

# Create Project table
   cursorObj.execute("CREATE TABLE Project( pro_name char(30),emp_id n(5),foreign key(emp_id) references Employee(emp_id) );")
# Insert records
   cursorObj.executescript("""
   INSERT INTO Project VALUES('car Parking',1);
   INSERT INTO Project VALUES('Ticket booking',2);
   INSERT INTO Project VALUES('Eaadhar update',3);
   INSERT INTO Project VALUES('government tenter',4);
   INSERT INTO Project VALUES('product booking',6);
   """)
   conn.commit()
   cursorObj.execute("SELECT * FROM Employee")
   rows = cursorObj.fetchall()
   print("Employee details:")
   for row in rows:
       print(row)
    
   cursorObj.execute("SELECT * FROM Department")
   rows = cursorObj.fetchall()
   print("Department details:")
   for row in rows:
       print(row)

   cursorObj.execute("SELECT * FROM Project")
   rows = cursorObj.fetchall()
   print("Project details:")
   for row in rows:
       print(row)
   cursorObj.execute("select Employee.emp_id,Employee.emp_name,Project.pro_name from(Employee inner join Project on Employee.emp_id=Project.emp_id)")
   print(cursorObj.fetchall())
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")