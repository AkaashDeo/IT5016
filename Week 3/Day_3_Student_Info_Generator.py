def student_info():
    """
    Input student information and generate a username based on the student ID and last name.
    If the university matches specific criteria, a welcome message is displayed.
    """
    # Input student information
    studentID = input("Enter your student ID: ")
    student_firstName = input("Enter your first name: ")
    student_lastName = input("Enter your last name: ")
    university = input("Which university do you attend?: ").lower()
    
    # Generate username from the first 2 characters of studentID and the first 3 characters of student_lastName
    username = studentID[:2] + student_lastName[:3]
    
    # Check if the university input contains both "whitecliffe" and "college"
    if "whitecliffe" in university and "college" in university:
        print(f"Welcome to Whitecliffe College! Your username is {username}.")
    else:
        print(f"Your generated username is {username}. Please ensure it aligns with your university's requirements.")

def main():
    """
    Main function to execute the student_info function.
    """
    student_info()

# Directly call the main function
main()
