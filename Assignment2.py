# Student Management System
"""
Fields :- ['Number', 'SurName', 'Name', 'UnitMark']
1. Add  Student
2. View ALL
3. Search Student
4. Delete Student
5. Load Student
6. Save Student
5. Quit
"""
 
import csv
import re
import os
# Define global variables
student_fields = ['Number', 'SurName', 'Name', 'UnitMark']
student_database = 'students.csv'
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
    print("5. Load Students")
    print("6. Save Students")
    print("7. Quit")
 

"""
This function is used to add student in memory
Takes student detail as input and adds the data to the list
"""
def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_data
      
    new_student ={}
    try:
        for field in student_fields:
            value = input("Enter " + field + ": ")
            new_student[field] =value
            
        if len(new_student["UnitMark"]) >0 and not new_student["UnitMark"].isnumeric():
                   raise Exception("Unit marks should be in numeric form")
                   
                
        for row in student_data:
            if len(row) > 0 and new_student["Number"] == row["Number"]:
                   raise Exception("Student with Number :("+new_student["Number"]+")already exist")
                   

        student_data.append(new_student)
        print("Data saved successfully")
        input("Press any key to continue")
        return
    except Exception as error:
         print("An error occurred:", type(error).__name__, "–", error)
 
 
"""
Displays all the students that are present in memory
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
Loads the data into memory from file, file location is inputted by the user
If the record in file is already present in memory, the data from file is ignored and rest of the data are added to student list in memory
"""
def load_students():
    global student_data
    file = input("enter file location of csv file: ")
    try:
        is_file_exists= os.path.isfile(file)
        if not is_file_exists:
            raise Exception("file does not exists")
        
        with open(file,"r", encoding="utf-8") as f:
              reader = csv.reader(f)
              for  row in reader:
                   if  not row[0].isnumeric():
                       continue
                   if  any(student["Number"] == row[0] for student in student_data):
                       continue   
                   new_student = {
                    "Number":row[0],
                    "SurName":row[1],
                    "Name":row[2],
                    "UnitMark":row[3]
                       }
                   student_data.append(new_student)
        print("Students loaded successfully")
        input("Press any key to continue")
    except Exception as error:
         print("An error occurred:", type(error).__name__, "–", error)   

"""
Saves the data from Memory into the excel file
Excel file path is taken as input from the user
If the file exists, the user is warned and given the user the option of either changing the file name, overwriting the file, or cancel the operation.
"""
def save_students():
    global student_data
    file = input("enter file location of csv file to save students: ")
    try:
        is_file_exists= os.path.isfile(file)
        if is_file_exists:
            print("----File already exists---")
            print("1. Change File Name")
            print("2. OverWrite File")
            print("3. Cancel")

            choice = input("Enter Choice: ")
            if choice =='1':
               save_students()
               
            elif choice == '2':
                save_data(file,"w")
                return
            else:
                return

        save_data(file,"a")
        input("Press any key to continue")
        return
    except Exception as error:
         print("An error occurred:", type(error).__name__, "–", error)

"""
Function used to save data into csv file. 
uses Python's builtin module csv to handle CSV files.
First parameter to the function is the file path for storing the csv file and the second parameter being the mode of operation
"""
def save_data(filepath,mode):
    global student_fields
    global student_data
    with open(filepath, mode, encoding="utf-8") as f:
         writer = csv.DictWriter(f,student_fields)
         writer.writerows(student_data)
         print("Data saved successfully")
        
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
    elif choice =='5':
        load_students()
    elif choice =="6":
        save_students()
    else:
        break
 
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
