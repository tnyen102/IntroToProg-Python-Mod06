# ------------------------------------------------------------------------------------------ #
# Title: Assignment06 Functions
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   PNguyen,5/28/25,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = ("---- Course Registration Program ----.\nSelect from the following menu:.\n1. Register a Student for a Course..\n"
             "2. Show current data.\n3. Save data to a file.\n4. Exit the program.\n----------------------------------------- ")
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []
menu_choice: str

# Processing #
class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        #This function is to read the data from the json file and load it into list of dictionary rows#
        file = None
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        #This function writes data to a json file#
        file = None
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There is a problem writing to the file."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()

# Presentation
class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        # This function will display an error if applicable #
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        # This function displays the menu choice #
            print(menu)

    @staticmethod
    def input_menu_choice():
        # This function prompts the user for an input #
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please enter only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        # This function displays the student course and name to users #
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        # This function gets inputs from the users #
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
           IO.output_error_messages(message="One of the values is incorrect", error=e)
        except Exception as e:
           IO.output_error_messages(message="There is a problem with your entered data", error=e)
        return student_data

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while (True):

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
