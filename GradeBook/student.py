"""Student class."""


class Student():
    """Store data for individual students."""

    def __init__(self, name, ID):
        """Initialize student object."""
        self.name = name
        self.first_name = name.split(" ")[0]
        self.last_name = name.split(" ")[1]
        self.ID = ID
        self.assignments = []
        self.grade = None

    def add_assignment(self, assignment):
        """Add new assignment to student's list."""
        self.assignments.append(assignment)

    def remove_assignment(self, assignment):
        """Remove assignment from student's assignment list."""
        del self.assignments[assignment.name]  # Assignment name should be key


# class Assignment():
#     """Store data for Assignments."""
#
#     def __init__(self, name, student_name, grade):
#
