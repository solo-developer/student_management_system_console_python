# Student Management System
"""
Fields :- ['Number', 'SurName', 'Name', 'UnitMark']
1. Add  Student
2. View ALL
3. Search Student
4. Delete Student
5. Load Student
6. Save Student
7. Quit
"""
 
import csv
import re
import os
import numpy as np
import matplotlib.pyplot as plt
# Define global variables
student_fields = ['Number', 'SurName', 'Name', 'UnitMark']
student_data = arr = np.empty((0,4), str)



 
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
    print("7. Display Grade Distribution")
    print("8. Display Mark Distribution")
    print("9. Quit")
 

      
def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_data
  
    new_student =[]
    for field in student_fields:
        value = input("Enter " + field + ": ")
        new_student.append(value)
    
    for row in student_data:
        if len(row) > 0 and new_student[0] == row[0]:
               print("Student with Number :("+new_student[0]+")already exist")
               input("Press any key to continue")
               return

    student_data =np.append(student_data, np.array([new_student]), axis=0)
    print("Data saved successfully")
    input("Press any key to continue")
    return
 
 
def view_students():
    global student_fields
    global student_data
 
    print("--- Student Records ---")
 

    for x in student_fields:
        print(x, end='\t |')
    print("\n-----------------------------------------------------------------")

    for row in student_data:
        grade = get_grade(row[3])
        print(row[0], '\t |',row[1], '\t |',row[2], '\t |',grade)
        print("\n")
 
    input("Press any key to continue")
 
 
def search_student():
    global student_fields
    global student_data

    search_result = np.empty((0,4), str)
    print("--- Search Student ---")
    search = input("Enter Student Number /Name to search: ")
   
    for row in student_data:
        if len(row) > 0:
            if search == row[0] or re.search(search, row[2], re.IGNORECASE):
               search_result = np.append(search_result, np.array([row]), axis=0)


    if len(search_result)>0:
           for x in student_fields:
               print(x, end='\t |')
           print("\n-----------------------------------------------------------------")

           for row in search_result:
              grade = get_grade(row[3])
              print(row[0], '\t |',row[1], '\t |',row[2], '\t |',grade)
           print("\n")
    else:
          print("student of given number/name not found")
    input("Press any key to continue")
 
 
def delete_student():
    global student_data
 
    print("--- Delete Student ---")
    student_no = input("Enter student no. to delete: ")
    student_found = False
    counter =0
    for item in student_data:
        if len(student_data) > 0:
           counter +=1
           if item[0]== student_no:
              student_data =np.delete(student_data, counter-1, 0)
              student_found = True
              break
 
    if student_found is True:
       print("Student of Student No:", student_no, "deleted successfully")
    else:
       print("Student. not found")
 
    input("Press any key to continue")


def load_students():
    global student_data
    file = input("enter file location of csv file: ")
    is_file_exists= os.path.isfile(file)
    if not is_file_exists:
        print("file does not exists")
        input("Press any key to continue")
        return
    
    with open(file,"r", encoding="utf-8") as f:
          reader = csv.reader(f)
          for  row in reader:
               if  not row[0].isnumeric():
                   continue
               if  any(student[0] == row[0] for student in student_data):
                   continue   
               student_data =np.append(student_data, np.array([row]), axis=0)
    print("Students loaded successfully")
    input("Press any key to continue")
       

def save_students():
    file = input("enter file location of csv file to save students: ")
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

def save_data(filepath,mode):
    global student_fields
    global student_data
    with open(filepath, mode, encoding="utf-8") as f:
         writer = csv.writer(f)
         for data in student_data:   
             writer.writerow(data)
         print("Data saved successfully")

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


def display_grade_distribution():
    global student_data
    Ngrade_count =0
    Pgrade_count = 0
    Cgrade_count =0
    Dgrade_count =0
    HDgrade_count =0
    for data in student_data:
        if len(data[3])==0 or not data[3].isnumeric():
            continue
        grade = get_grade(data[3])
        if grade=="N":
            Ngrade_count +=1
        elif grade =="P":
            Pgrade_count +=1
        elif grade =="C":
            Cgrade_count +=1
        elif grade =="D":
            Dgrade_count +=1
        elif grade == "HD":
            HDgrade_count +=1

    y = np.array([Ngrade_count,Pgrade_count,Cgrade_count,Dgrade_count,HDgrade_count])
    mylabels = ["N", "P", "C", "D","HD"]
    myexplode = [0.1, 0.1, 0.1, 0.1,0.1]

    plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
    plt.legend(title = "Grade distribution:")
    plt.show() 
        

def display_marks_distribution():
    global student_data
    zeroTo29markcount = 0
    thirtyto39markcount =0
    fortyto49markcount =0
    fiftyto59markcount =0
    sixtyto69markcount =0
    seventyto79markcount =0
    eightyto89markcount =0
    ninetyto100markcount =0

    for data in student_data:
        if len(data[3])==0 or not data[3].isnumeric():
            continue
        mark = int(data[3])
        if mark <30:
           zeroTo29markcount +=1
        elif mark >29 and mark <40:
            thirtyto39markcount +=1
        elif mark >39 and mark <50:
            fortyto49markcount +=1
        elif mark >49 and mark <60:
            fiftyto59markcount +=1
        elif mark >59 and mark <70:
            sixtyto69markcount +=1
        elif mark >69 and mark <80:
            seventyto79markcount +=1
        elif mark >79 and mark <90:
            eightyto89markcount +=1
        elif mark >89 :
            ninetyto100markcount +=1

    x = np.array(["0-29", "30-39", "40-49", "50-59","60-69","70-79","80-89","90-100"])
    y = np.array([zeroTo29markcount,thirtyto39markcount,fortyto49markcount,fiftyto59markcount,sixtyto69markcount,seventyto79markcount,eightyto89markcount,ninetyto100markcount])
 
    plt.bar(x, y)
    plt.show()    
    
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
    elif choice =='6':
        save_students()
    elif choice == '7':
        display_grade_distribution()
    elif choice =='8':
        display_marks_distribution()
    else:
        break
 
print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
