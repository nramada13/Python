# Noor Ramadan
# File Name: deanslist_honorroll.py
# This program accepts student names and GPAs, then determines whether
# each student qualifies for the Dean's List or the Honor Roll.
# The program stops asking for input if the last name entered is 'ZZZ'.

def main():
    last_name = ""

    while last_name != "ZZZ":
        # Ask for last name
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")

        if last_name == "ZZZ":
            print("Exiting program...")
            break

        # Ask for first name
        first_name = input("Enter student's first name: ")

        # Ask for GPA
        gpa = float(input("Enter student's GPA: "))

        # Check GPA requirements
        if gpa >= 3.5:
            print(first_name, last_name, "has made the Dean's List!")
        elif gpa >= 3.25:
            print(first_name, last_name, "has made the Honor Roll.")
        else:
            print(first_name, last_name, "did not qualify for Dean's List or Honor Roll.")


main()
