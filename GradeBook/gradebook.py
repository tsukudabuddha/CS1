"""Gradebook OOP Assingment."""
from student import Student
# Need to have at least two classes
# Roster of students
# Use lists in Dictionaries


class Classroom():
    """Classroom object.

    Track all info required for class
    """

    all_classes = []

    def __init__(self, name, students=[]):
        """Initialize the classroom with a name."""
        self.name = name
        self.student_dir = {}
        student_count = 0
        if len(students) > 0:
            for student in students:
                self.student_dir[student_count] = student
                student_count += 1
        Classroom.all_classes.append(self)  # Add classroom object to classlist

    def add_student(self, student):
        """Add student to classroom."""
        self.student_dir[len(self.student_dir)] = student

    def remove_student(self, name):  # Receive student name, not whole student
        """Remove student from class."""
        for value in self.student_dir.values():
            if name == value.name:
                number = find_id(self, name)
                pass
        del self.student_dir[number]

    def to_string(self):
        """Print out class gradebook."""
        print("%s Class" % self.name)
        print("there are %i students in %s class" %
              len(self.students), self.name)


def find_id(classroom, name):
        """Find id of student."""
        for k, v in classroom.student_dir.items():
            if v.name == name:
                return k


def runMenu():
    """Print text menu and take in input."""
    print("Menu")
    print("1. Create a new classroom")
    print("2. Add new student to class")
    print("3. Remove student from class ")
    print("4. Add new assignment")
    print("5. Remove assignment")
    print("6. Quit")
    answer = int(input("Enter your choice: "))
    return answer


def main():
    """Run main loop."""
    run = True
    while run:
        command = runMenu()
        if command == 1:
            class_name = input("What is the name of the classroom " +
                               " you want to create? ")
            Classroom(class_name)  # Automatically adds to master class list

        elif command == 2:
            name = input("What is the name of the student that you'd like to"
                         + " add to the class?: ")
            print("Which classroom would you like to add %s to?" % name)
            print("Your options are: ", Classroom.all_classes)
            class_index = int(input("Enter the index of the class"
                                    + " that you'd like to edit: "))
            chosen_class = Classroom.all_classes[class_index]
            chosen_class.add_student(Student(name,
                                             len(chosen_class.student_dir)))
        elif command == 2:
            name = input("What is the name of the student that you'd like to "
                         + " add to the class?: ")
            print("Which classroom would you like to add %s to?" % name)
            print("Your options are: ", Classroom.classes)
            chosen_class = int(input("Enter the index of the class"
                                     + " that you'd like to edit: "))
            student = input("What is the name of the student that you'd like"
                            + " to  remove from the class?: ")
            Classroom.classes[chosen_class].remove_student(student)
        elif command == 6:
            run = False
            pass


classroom = Classroom("Math101")
student = Student("Andrew Tsukuda")
classroom.add_student(student)
classroom.remove_student("Andrew Tsukuda")
