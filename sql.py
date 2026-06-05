import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('student.db')

# Create a cursor object to insert record,create table,retrieve data
cursor = connection.cursor()

# Create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT); """

cursor.execute(table_info)

# Insert a record into the table

cursor.execute("""Insert Into STUDENT values('Krish','Data Science','A',90)""")
cursor.execute("""Insert Into STUDENT values('Sudhanshu','Data Science','B',100)""")
cursor.execute("""Insert Into STUDENT values('Darius','Data Science','A',86)""")
cursor.execute("""Insert Into STUDENT values('Vikash','DEVOPS','A',50)""")
cursor.execute("""Insert Into STUDENT values('Dipesh','DEVOPS','A',35)""")

cursor.execute("""Insert Into STUDENT values('Aarav','Data Science','B',78)""")
cursor.execute("""Insert Into STUDENT values('Rohan','Data Science','C',88)""")
cursor.execute("""Insert Into STUDENT values('Priya','Data Science','A',92)""")
cursor.execute("""Insert Into STUDENT values('Ananya','Data Science','B',81)""")
cursor.execute("""Insert Into STUDENT values('Sneha','Data Science','C',75)""")

cursor.execute("""Insert Into STUDENT values('Rahul','DEVOPS','B',65)""")
cursor.execute("""Insert Into STUDENT values('Karan','DEVOPS','C',72)""")
cursor.execute("""Insert Into STUDENT values('Neha','DEVOPS','A',84)""")
cursor.execute("""Insert Into STUDENT values('Sakshi','DEVOPS','B',91)""")
cursor.execute("""Insert Into STUDENT values('Yash','DEVOPS','C',58)""")

cursor.execute("""Insert Into STUDENT values('Aditya','Machine Learning','A',95)""")
cursor.execute("""Insert Into STUDENT values('Pooja','Machine Learning','B',82)""")
cursor.execute("""Insert Into STUDENT values('Tanmay','Machine Learning','C',77)""")
cursor.execute("""Insert Into STUDENT values('Shreya','Machine Learning','A',89)""")
cursor.execute("""Insert Into STUDENT values('Aman','Machine Learning','B',69)""")

cursor.execute("""Insert Into STUDENT values('Nikhil','Cyber Security','A',87)""")
cursor.execute("""Insert Into STUDENT values('Isha','Cyber Security','B',79)""")
cursor.execute("""Insert Into STUDENT values('Harsh','Cyber Security','C',68)""")
cursor.execute("""Insert Into STUDENT values('Ritika','Cyber Security','A',93)""")
cursor.execute("""Insert Into STUDENT values('Dev','Cyber Security','B',74)""")

cursor.execute("""Insert Into STUDENT values('Mohit','Cloud Computing','A',85)""")
cursor.execute("""Insert Into STUDENT values('Riya','Cloud Computing','B',80)""")
cursor.execute("""Insert Into STUDENT values('Siddharth','Cloud Computing','C',71)""")
cursor.execute("""Insert Into STUDENT values('Kavya','Cloud Computing','A',96)""")
cursor.execute("""Insert Into STUDENT values('Aryan','Cloud Computing','B',67)""")

cursor.execute("""Insert Into STUDENT values('Meera','Artificial Intelligence','A',94)""")
cursor.execute("""Insert Into STUDENT values('Arjun','Artificial Intelligence','B',88)""")
cursor.execute("""Insert Into STUDENT values('Diya','Artificial Intelligence','C',76)""")
cursor.execute("""Insert Into STUDENT values('Rakesh','Artificial Intelligence','A',83)""")
cursor.execute("""Insert Into STUDENT values('Vaishnavi','Artificial Intelligence','B',91)""")

cursor.execute("""Insert Into STUDENT values('Saurabh','Software Engineering','A',79)""")
cursor.execute("""Insert Into STUDENT values('Palak','Software Engineering','B',85)""")
cursor.execute("""Insert Into STUDENT values('Om','Software Engineering','C',64)""")
cursor.execute("""Insert Into STUDENT values('Khushi','Software Engineering','A',90)""")
cursor.execute("""Insert Into STUDENT values('Parth','Software Engineering','B',73)""")

cursor.execute("""Insert Into STUDENT values('Akash','Big Data','A',82)""")
cursor.execute("""Insert Into STUDENT values('Nisha','Big Data','B',87)""")
cursor.execute("""Insert Into STUDENT values('Tushar','Big Data','C',69)""")
cursor.execute("""Insert Into STUDENT values('Simran','Big Data','A',93)""")
cursor.execute("""Insert Into STUDENT values('Jay','Big Data','B',78)""")

cursor.execute("""Insert Into STUDENT values('Vedant','Web Development','A',88)""")
cursor.execute("""Insert Into STUDENT values('Mansi','Web Development','B',75)""")
cursor.execute("""Insert Into STUDENT values('Rudra','Web Development','C',62)""")
cursor.execute("""Insert Into STUDENT values('Aditi','Web Development','A',95)""")
cursor.execute("""Insert Into STUDENT values('Pratik','Web Development','B',83)""")

cursor.execute("""Insert Into STUDENT values('Aniket','Python','A',91)""")
cursor.execute("""Insert Into STUDENT values('Pallavi','Python','B',84)""")
cursor.execute("""Insert Into STUDENT values('Abhishek','Python','C',71)""")
cursor.execute("""Insert Into STUDENT values('Komal','Python','A',89)""")
cursor.execute("""Insert Into STUDENT values('Rohini','Python','B',76)""")

cursor.execute("""Insert Into STUDENT values('Manish','Java','A',80)""")
cursor.execute("""Insert Into STUDENT values('Swati','Java','B',92)""")
cursor.execute("""Insert Into STUDENT values('Deepak','Java','C',66)""")
cursor.execute("""Insert Into STUDENT values('Bhavna','Java','A',87)""")
cursor.execute("""Insert Into STUDENT values('Varun','Java','B',74)""")

cursor.execute("""Insert Into STUDENT values('Nitin','SQL','A',93)""")
cursor.execute("""Insert Into STUDENT values('Ayesha','SQL','B',86)""")
cursor.execute("""Insert Into STUDENT values('Kunal','SQL','C',72)""")
cursor.execute("""Insert Into STUDENT values('Priti','SQL','A',90)""")
cursor.execute("""Insert Into STUDENT values('Rajat','SQL','B',77)""")

cursor.execute("""Insert Into STUDENT values('Shivam','Data Analytics','A',88)""")
cursor.execute("""Insert Into STUDENT values('Payal','Data Analytics','B',79)""")
cursor.execute("""Insert Into STUDENT values('Gaurav','Data Analytics','C',68)""")
cursor.execute("""Insert Into STUDENT values('Sonali','Data Analytics','A',94)""")
cursor.execute("""Insert Into STUDENT values('Hemant','Data Analytics','B',82)""")

cursor.execute("""Insert Into STUDENT values('Chetan','Networking','A',85)""")
cursor.execute("""Insert Into STUDENT values('Monika','Networking','B',78)""")
cursor.execute("""Insert Into STUDENT values('Ashish','Networking','C',70)""")
cursor.execute("""Insert Into STUDENT values('Rupal','Networking','A',92)""")
cursor.execute("""Insert Into STUDENT values('Mayur','Networking','B',74)""")

cursor.execute("""Insert Into STUDENT values('Tejas','Blockchain','A',89)""")
cursor.execute("""Insert Into STUDENT values('Poonam','Blockchain','B',81)""")
cursor.execute("""Insert Into STUDENT values('Sahil','Blockchain','C',65)""")
cursor.execute("""Insert Into STUDENT values('Nandini','Blockchain','A',97)""")
cursor.execute("""Insert Into STUDENT values('Umesh','Blockchain','B',76)""")

cursor.execute("""Insert Into STUDENT values('Ramesh','Computer Vision','A',90)""")
cursor.execute("""Insert Into STUDENT values('Divya','Computer Vision','B',83)""")
cursor.execute("""Insert Into STUDENT values('Chirag','Computer Vision','C',72)""")
cursor.execute("""Insert Into STUDENT values('Lavanya','Computer Vision','A',95)""")
cursor.execute("""Insert Into STUDENT values('Samar','Computer Vision','B',79)""")

cursor.execute("""Insert Into STUDENT values('Ganesh','NLP','A',88)""")
cursor.execute("""Insert Into STUDENT values('Irfan','NLP','B',80)""")
cursor.execute("""Insert Into STUDENT values('Reshma','NLP','C',69)""")
cursor.execute("""Insert Into STUDENT values('Suraj','NLP','A',92)""")
cursor.execute("""Insert Into STUDENT values('Tanvi','NLP','B',84)""")

cursor.execute("""Insert Into STUDENT values('Kishore','IoT','A',87)""")
cursor.execute("""Insert Into STUDENT values('Rekha','IoT','B',75)""")
cursor.execute("""Insert Into STUDENT values('Anil','IoT','C',64)""")
cursor.execute("""Insert Into STUDENT values('Bharti','IoT','A',93)""")
cursor.execute("""Insert Into STUDENT values('Madhav','IoT','B',81)""")

# Display all the records from the table
print("The inserted records are:")

data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
    
# Close the connection

connection.commit()  # Commit the changes to the database
connection.close()