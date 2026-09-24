import datetime
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
    course_dict = {"courseID":courseID, "courseName":courseName, "Credit":courseCredit}
    course_info.append(course_dict)

totalCourse = course_size()
for i in range(totalCourse):
    course()

def list_courses():
    for course_dict in course_info:
        print(course_dict)
list_courses()


# Input marks 
def input_marks():
    continue_mark = "yes"
    while continue_mark.lower() == "yes": # use for comparison (checking if two values are equal), lower() --> case sensitive 
        selected_course_id = str(input("Which course ID you want to enter marks for? "))
        for students in student_list:
            students["mark"][selected_course_id] = float(input(f"Mark for {students["name"]}: ")) # access the student name for students dict
        continue_mark = input("Do you want to enter marks for another course? (yes/no): ")
input_marks()

def show_mark():
    selected_id = str(input("Which course ID you want to see? "))
    for students in student_list:
        print(f"{students["name"]}:{students["mark"][selected_id]}")
show_mark()