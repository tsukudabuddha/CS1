"""Gradebook OOP Assingment."""
# Need to have at least two classes
# Roster of students


class Classroom():
    """Classroom object.

    Track all info required for class
    """

    def __init__(self, name):
        """Initialize the classroom with a name."""
        self.name = name


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
