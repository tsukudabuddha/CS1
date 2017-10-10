"""Student class."""


class Student():
    """Store data for individual students."""

    roster = []

    def __init__(self, name):
        """Initialize student object."""
        self.name = name
        self.first_name = name.split(" ")[0]
        self.last_name = name.split(" ")[1]
        self.ID = len(Student.roster) + 1
        self.assignments = {}
        self.grade = None

    def add_assignment(self, assignment_name, score):
        """Add new assignment to student's list."""
        self.assignments[assignment_name] = score
        self.update_grade()

    def remove_assignment(self, assignment_name):
        """Remove assignment from student's assignment list."""
        del self.assignments[assignment_name]
        if len(self.assignments) == 0:
            self.grade = None
        else:
            self.update_grade()

    def update_grade(self):
        """Update student's grade."""
        assignment_number = len(self.assignments)
        total_score = 0
        for assignment in self.assignments:
            total_score += self.assignments[assignment]
        grade = total_score / assignment_number
        self.grade = grade
