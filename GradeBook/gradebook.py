"""Gradebook OOP Assingment."""
# Need to have at least two classes
# Roster of students


class Classroom():
    """Classroom object.

    Track all info required for class
    """

    classes = []

    def __init__(self, name, students):
        """Initialize the classroom with a name."""
        self.name = name
        self.students = students
        self.student_count = 0
        self.student_dir = {}
        for student in self.students:
            self.student_dir[self.student_count] = student
            self.student_count += 1
        super().classes.append(self)  # Add classroom object to class list

    def add_student(self, student):
        """Add student to classroom."""
        self.students.append(student)

    def to_string():
        """Print out class gradebook."""


def runMenu():
    """Print text menu and take in input."""
    print("Menu")
    print("1. Create a new classroom")
    print("2. Add new student to class")
    print("3. Remove student from class ")
    print("4. Add new assignment")
    print("5. Remove assignment")
    return input("Enter your choice: ")


def main():
    """Run main function of game."""
    command = runMenu()
    if command == 1:
        student = input("What is the name of the student that you'd like to "
                        + " add to the class?: ")
        print("Which classroom would you like to add %s to?", student)
        print("Your options are: ", Classroom.classes)
        chosen_class = input("Enter the index of the class"
                             + " that you'd like to edit: ")
        Classroom.classes[chosen_class].add_student(student)
