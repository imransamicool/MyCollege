from MyCollege.controllers import StudentsC
from MyCollege.exceptions import *


def opr_menu():
    option = int(input("Please choose an option below: \n 1. Admit a Student \n 2. View all students"
                       " \n 0. Quit the program \n Enter your choice:  "))
    #Get the option and act accordingly
    if option == 1:
        #Creating an empty stud dictionary
        stud = {}

        #Taking id as input and check the id is not a duplicate one before adding the id to stud dictionary
        try:
            id_inp = int(input("\nEnter Students's id: "))
            is_id_exist = StudentsC.check_id(id_inp)
            if is_id_exist:
                raise IdCheckException(f"Id {id_inp} already exists, Please re-run the program to enter a new student with unique id")
            else:
                stud['Id'] = id_inp
        finally:
            pass

        #Asking input for student's name and storing the same as no check required
        n = input("Enter Student's name: ")
        stud['name'] = n


        #Asking for age input and checking before admitting that age > 8
        try:
            age_inp = int(input("Enter Students's age: "))
            check_age = StudentsC.age_check(age_inp)
            if check_age:
                raise AgeCheckException(f"Student with age < 8 is not allowed to be admitted, Sorry!")
            else:
                stud['age'] = age_inp
        finally:
            pass

        #Taking one or more subjects for the student
        subjects_input = input("Please enter subject(s) separated by space alone: ")
        stud['subjects'] = '|'.join(subjects_input.split())

        is_added_successfully = StudentsC.add_to_csv(stud)
        if is_added_successfully:
            print(f"Your entered student {stud} added successfully")

    elif option == 2:
        StudentsC.fetch_print_csv()
    elif option == 0:
        print("You chose to exit!")
    else:
        print("Seems you entered wrong option, kindly rerun the program and re-enter correct option, Thanks!")

