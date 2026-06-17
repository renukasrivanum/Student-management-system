import json
import os
class Student:
    def __init__(self, name,marks,student_Id,attendance):
        self.name= name
        self.marks= marks
        self.student_Id =student_Id
        self.attendance = attendance
    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}, ID: {self.student_Id}, Attendance: {self.attendance}" 
students = { 
  

}
if os.path.exists(r'C:\Users\renuk\student.json'):
    try:
        with open(r'C:\Users\renuk\student.json', "r") as file:
            data = json.load(file)
            

            for student_id, student_data in data.items():
                students[int(student_id)] = Student(
                    student_data["name"],
                    student_data["marks"],
                    student_data["student_id"],
                    student_data["attendance"]
                )

    except (json.JSONDecodeError, FileNotFoundError):
        print("Error reading file. Starting with empty records.")
        students = { }
print('1. add student' )
print('2. search student')
print('3. view student')
print('4. delete student')
print('5. exit')
while True:
    print('\n----Welcome to Stundent management----')
   
    try:
        operator = int(input("Enter operator: "))
    except ValueError:
        print("Please enter a number from 1 to 5")
        continue
    if operator == 1:
        name = input('Enter name:')
        marks = int(input('Enter the student marks:'))
        student_Id= int(input('Enter the stundent id:'))
        attendance= int(input('Enter the student attendance:'))
        if student_Id in students:
            print("Student ID already exists.")
        else:
            students[student_Id] = Student(
                name,
                marks,
                student_Id,
                attendance
            )
            print("Student added successfully!")
    elif operator == 2:
       student_Id = int(input('enter the student_Id:'))
       if student_Id in students:
           print(students[student_Id])
       else:
            print('Student Id not found')
    elif  operator == 3:
        if not students:
            print("No students available.")
        else:
            print("\nStudent Records:")
            for student in students.values():
                print(student)
                
    elif operator == 4:
        del_Id = int(input('enter the student Id for del data:'))
        if del_Id in students:
            del students[del_Id]
            print('succesfull deleted the student Id')
        else:
            print('Student ID not found. Please check the ID.')
    elif operator == 5:
        print('exit to the student management system')
        save_data = { }

        for student_id, student in students.items():
            save_data[student_id] = {
            "name": student.name,
            "marks": student.marks,
            "student_id": student.student_Id,
            "attendance": student.attendance
        }
        with open (r'C:\Users\renuk\student.json','w') as file:
            json.dump(save_data, file)
        print("Data saved successfully!")
        #print(students)
        print(save_data)
        break
    else:
        print('please entry vaild number(1-5)')

        