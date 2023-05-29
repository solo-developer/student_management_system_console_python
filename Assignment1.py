# Student Management System
"""
Fields :- ['Number', 'SurName', 'Name', 'UnitMark']
1. Add  Student
2. View ALL
3. Search Student
4. Delete Student
5. Quit
"""
 
import csv
import re
# Define global variables
student_fields = ['Number', 'SurName', 'Name', 'UnitMark']
student_data =[]



"""
Function displays all the available options for manipulation
"""
def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add Student")
    print("2. View ALL")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Quit")
 

"""
This function is used to add student to the list
Takes student detail as input and adds the data to the list
"""
def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_data
    try:
        new_student ={}
        for field in student_fields:
            value = input("Enter " + field + ": ")
            new_student[field] =value


        if len(new_student["UnitMark"]) >0 and not new_student["UnitMark"].isnumeric():
                   raise Exception("Unit marks should be in numeric form")
                   
        for row in student_data:
            print(new_student["UnitMark"])
            if len(row) > 0 and new_student["Number"] == row["Number"]:
                   raise Exception("Student with Number :("+new_student["Number"]+")already exist")
            

        student_data.append(new_student)
        print("Data saved successfully")
        input("Press any key to continue")
        return
    except Exception as error:
         print("An error occurred:", type(error).__name__, "–", error)
 
"""
Displays all the students that have been added to the list
Displays Number,Surname,Name and Grade in a line, each field separated by a tab character
"""
def view_students():
    global student_fields
    global student_data
 
    print("--- Student Records ---")
 
    try:
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in student_data:
            grade = get_grade(row["UnitMark"])
            print(row["Number"], '\t |',row["SurName"], '\t |',row["Name"], '\t |',grade)
            print("\n")
     
        input("Press any key to continue")
    except Exception as error:
         print("An error occurred:", type(error).__name__, "–", error)
 
 
"""
Searches and displays the student based on a search string with search being case-insensitive and partial match
Displays all matching detail of students viz,  Number,Surname,Name and Grade in a line, each field separated by a tab character
"""
def search_student():
    global student_fields
    global student_data

    search_result =[]
    print("--- Search Student ---")
    search = input("Enter Student Number /Name to search: ")
    try:
        for row in student_data:
            if len(row) > 0:
                if search == row["Number"] or re.search(search, row["Name"], re.IGNORECASE):
                   search_result.append(row)


        if len(search_result)>0:
               for x in student_fields:
                   print(x, end='\t |')
               print("\n-----------------------------------------------------------------")

               for row in student_data:
                  grade = get_grade(row["UnitMark"])
                  print(row["Number"], '\t |',row["SurName"], '\t |',row["Name"], '\t |',grade)
               print("\n")
        else:
              print("student of given number/name not found")
        input("Press any key to continue")
    except Exception as error:
         print("An error occurred:", type(error).__name__, "–", error)
 
 
"""
Deletes a student based on the student number that is inputted by the user.
Displays Not Found message if student with provided number doesnot exist.
"""
def delete_student():
    global student_data
 
    print("--- Delete Student ---")
    student_no = input("Enter student no. to delete: ")
    student_found = False
    try:
        for item in student_data.copy():
            if len(student_data) > 0:
               if item.get("Number")== student_no:
                  student_data.remove(item)
                  student_found = True
                  break
     
        if student_found is True:
           print("Student of Student No:", student_no, "deleted successfully")
        else:
           print("Student. not found")
     
        input("Press any key to continue")
    except Exception as error:
         print("An error occurred:", type(error).__name__, "–", error)
 



"""
This function is used to get grade equivalent to the marks obtained
Used Murdoch University's grade system to convert marks to grades.
"""
def get_grade(marks):
    if len(marks) ==0 or not marks.isnumeric():
       return "no grade"
    percentage = (int(marks)/100) *100
    grade = "N"
    if percentage >49 and percentage <60:
        grade ="P"
    elif percentage>59 and percentage <70:
        grade="C"
    elif percentage>69 and percentage <80:
        grade ="D"
    elif percentage >79:
         grade ="HD"
    return grade

"""
Entry point of the program.
Displays lists of all available choices
Based on the choice input by the user, operation is performed
"""
while True:
    display_menu()
 
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    else:
        break
 
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
