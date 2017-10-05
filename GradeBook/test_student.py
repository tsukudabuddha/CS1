"""Test Student for gradebook."""

from student import Student


def setup_for_test():
    """Return Student instance."""
    student = Student("Student Person", 0)
    return student


def test_setup():
    student = setup_for_test()
    assert student.name == "Student Person"
    assert student.ID == 0
    assert student.grade == None
    assert len
