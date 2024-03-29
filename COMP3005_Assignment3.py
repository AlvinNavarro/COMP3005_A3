import psycopg2

connection = psycopg2.connect(
        dbname="A3",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

#Retrieves and displays all records from the students table
def getAllStudents():
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM students ORDER BY student_id")
        students = cursor.fetchall()
        for student in students:
           print(student)
    except psycopg2.Error as e:
        print("Error getting student records", e)
        connection.rollback()
    finally:
        cursor.close()

#Inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        connection.commit()
        print("Student data has been added") 
    except psycopg2.Error as e:
        print("Error adding student record ", e)
        connection.rollback()
    finally:
        cursor.close()

#Updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE students SET email = %s WHERE student_ID = %s", (new_email, student_id))
        connection.commit()
        print("Student email has been updated ") 
    except psycopg2.Error as e:
        print("Error updating student email ", e)
        connection.rollback()
    finally:
        cursor.close()

#Deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        connection.commit()
        print("Student data has been deleted")
    except psycopg2.Error as e:
        print("Error deleting student record ", e)
        connection.rollback()
    finally:
        cursor.close()

#Uncomment for testing
#getAllStudents()
#print("\n")

#addStudent("Joe", "Schmoe", "joeschmoe@gmail.com", "2024-01-01")
#getAllStudents()
#print("\n")

#updateStudentEmail(4, "schmoejoe@gmail.com")
#getAllStudents()
#print("\n")

#deleteStudent(4)
#getAllStudents()
#print("\n")
connection.close()
