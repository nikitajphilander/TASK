# student_register.py

num_students = int(input("How many students are registering? "))

with open("reg_form.txt", "w") as file:
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        
        file.write(student_id + "\n")
        file.write("--------------------\n")

print("Registration form created successfully.")
