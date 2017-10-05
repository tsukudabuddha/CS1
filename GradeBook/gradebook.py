"""Gradebook OOP Assingment."""
from student import Student
# Need to have at least two classes
# Roster of students
# Use lists in Dictionaries


class Classroom():
    """Classroom object.

    Track all info required for class
    """

    classes = []

    def __init__(self, name, students):
        """Initialize the classroom with a name."""
        self.name = name
        self.student_dir = {}
        self.student_count = 0
        for student in students:
            self.student_dir[self.student_count] = student
            self.student_count += 1
        super().classes.append(self)  # Add classroom object to class list

    def add_student(self, student):
        """Add student to classroom."""
        self.students_dir[len(self.students_dir)] = student.name

    def remove_student(self, name):  # Receive student name, not whole student
        """Remove student from class."""
        if name in self.students_dir.values():
            for index in range(len(self.students_dir) - 2):
                if self.students_dir[index] == name:
                    del self.students_dir[index]

    def to_string(self):
        """Print out class gradebook."""
        print("%s Class", self.name)
        print("there are %i students in %s class" %
              len(self.students), self.name)


def runMenu():
    """Print text menu and take in input."""
    print("Menu")
    print("1. Create a new classroom")
    print("2. Add new student to class")
    print("3. Remove student from class ")
    print("4. Add new assignment")
    print("5. Remove assignment")
    answer = int(input("Enter your choice: "))
    return answer


def main():
    """Run main function of game."""
    command = runMenu()
    if command == 1:
        class_name = input("What is the name of the classroom " +
                           " you want to create?")

    elif command == 2:
        name = input("What is the name of the student that you'd like to "
                     + " add to the class?: ")
        print("Which classroom would you like to add %s to?" % name)
        print("Your options are: ", Classroom.classes)
        chosen_class = int(input("Enter the index of the class"
                                 + " that you'd like to edit: "))
        chosen_class.add_student(Student(name, len(chosen_class.student_dir)))
    elif command == 2:
        print("Which classroom would you like to add %s to?" % student)
        print("Your options are: ", Classroom.classes)
        chosen_class = int(input("Enter the index of the class"
                                 + " that you'd like to edit: "))
        student = input("What is the name of the student that you'd like to "
                        + " remove from the class?: ")
        Classroom.classes[chosen_class].remove_student(student)

main()
