import datetime
import numpy as np 
# Input student 
student_list = [] 
def class_size():
    numberOfStudents = int(input("How many students are in the class? "))
    return numberOfStudents

def students ():
    studentID = str(input("Student ID: "))
    studentName = str(input("Student name: "))
    DoB = str(input("DoB (YYYY-MM-DD): ")) 
    students_dict = {"ID": studentID, "name": studentName, "DoB":DoB, "mark": {}} 
    student_list.append(students_dict)

total_students = class_size() 
for i in range(total_students): 
    students() 

def list_students():
    for students in student_list:
        print(students)
list_students()


# Input course 
course_info = []
def course_size():
    numberOfCourse = int(input("How many course do you study? "))
    return numberOfCourse

def course():
    courseID = str(input("Course ID: "))
    courseName = str(input("Course name: "))
    courseCredit = int(input("ETCS: "))
    course_dict = {"courseID":courseID, "courseName":courseName, "Credit": courseCredit}
    course_info.append(course_dict)

totalCourse = course_size()
for i in range(totalCourse):
    course()

def list_courses():
    for course_dict in course_info:
        print(course_dict)
list_courses()


# Input marks 
# math.floor(x) rounds a number down to the nearest whole integer 
# math.floor(12.78) gives 12 
# 1 digit decimal --> math.floor(score * 10) / 10.0 --> 12.7
import math 
def input_marks():
    continue_mark = "yes"
    while continue_mark.lower() == "yes": # use for comparison (checking if two values are equal), lower() --> case sensitive 
        selected_course_id = str(input("Which course ID you want to enter marks for? "))
        for students in student_list: 
            raw_mark = float(input(f"Mark for {students["name"]}: "))
            floored_mark = float(math.floor(raw_mark * 10) / 10.0) 
            students["mark"][selected_course_id] = floored_mark
        continue_mark = input("Do you want to enter marks for another course? (yes/no): ")
input_marks()

def show_mark():
    selected_id = str(input("Which course ID you want to see? "))
    for students in student_list:
        print(f"{students["name"]}:{students["mark"][selected_id]}")
show_mark()


# Calculate GPA 
# gpa = [sum of (course_mark * credit) / total credit]
def gpa_calculation(students):
    marks_list = []
    credits_list = []

    # get values out of dictionaries into the lists
    for course_dict in course_info:
        course_id = course_dict["courseID"] # retrive the value in dictionary
        if course_id in students["mark"]:
            marks_list.append(students["mark"][course_id])
            credits_list.append(course_dict["Credit"])

    marks_array = np.array(marks_list)
    credits_array = np.array(credits_list)

    earned_points = marks_array * credits_array
    total_earned_points = np.sum(earned_points)
    total_credits = np.sum(credits_array)
    gpa = total_earned_points / total_credits
    floored_gpa = math.floor(gpa * 10) / 10.0 
    print(f"GPA of {students["name"]} is: {floored_gpa}")
    return floored_gpa
gpa_calculation()

def sort_gpa(students):
    floored_gpa = gpa_calculation(students)
    students["gpa"] = floored_gpa 
    student_list.sort(key=lambda student: student["gpa"], reverse=True)
    for students in student_list:
        print(f"GPA of {students["name"]}: {students["gpa"]}")
sort_gpa()


