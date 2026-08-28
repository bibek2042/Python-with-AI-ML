
print("Welcome to DPLMS Student Register System")
courses = ["Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"]
print( "All available Course :")
for course in courses:
    print(course)
student_name = input("Enter Student Name: ")
email = input("Enter Email: ")
age = int(input("Enter Age: "))
selected_course = input("Enter Selected Course: ")


student = {
    "Student Name": student_name,
    "Email": email,
    "Age": age,
    "Selected Course": selected_course
}

# Display the dictionary
print("\nStudent Information:")
print(student)



# Check if the course exists
if selected_course in courses:
    print("Registration Successful!")
else:
    print("Course not available.")
 

print("\n ***** Student Registration Details *****")
print("Student Name:", student_name)
print("Email:", email)
print("Age:", age)
print("Selected Course:", selected_course)
