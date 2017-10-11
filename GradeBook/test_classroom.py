"""Test Classroom for Gradebook."""
from gradebook import Classroom
from student import Student


def setup_for_test():
    """Return Classroom instance."""
    classroom = Classroom("Math101")
    return classroom


def test_setup():
    """Setup test."""
    classroom = setup_for_test()
    assert classroom.name == "Math101"
    assert len(classroom.student_dir) == 0


def test_add_student():
    """Test the add student function."""
    classroom = setup_for_test()
    student = Student("Andrew Tsukuda")
    classroom.add_student(student)
    assert len(classroom.student_dir) == 1
    assert classroom.student_dir[0].ID == 1


def test_remove_students():
    """Test the remove student function."""
    classroom = setup_for_test()
    student = Student("Andrew Tsukuda")
    classroom.add_student(student)
    assert len(classroom.student_dir) == 1
    assert classroom.student_dir[0].ID == 1
    classroom.remove_student("Andrew Tsukuda")
    assert len(classroom.student_dir) == 0
