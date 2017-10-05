"""Test Student for gradebook."""

from student import Student


def setup_for_test():
    """Return Student instance."""
    student = Student("Student Person", 0)
    return student


def test_setup():
    """Setup test."""
    student = setup_for_test()
    assert student.name == "Student Person"
    assert student.ID == 0
    assert student.grade is None
    assert len(student.assignments) == 0


def test_add_assignment():
    """Test the add assignment function."""
    student = setup_for_test()
    student.add_assignment("HW1", 100)
    assert student.assignments["HW1"] == 100
    assert len(student.assignments) == 1


def test_remove_assignment():
    """Test the remove assignment function."""
    student = setup_for_test()
    # Add assignment before deleting
    student.add_assignment("HW1", 100)
    assert student.assignments["HW1"] == 100
    assert len(student.assignments) == 1
    student.remove_assignment("HW1")
    assert len(student.assignments) == 0


def test_grade():
    """Test the grade function."""
    student = setup_for_test()
    student.add_assignment("HW1", 100)
    assert student.grade == 100
