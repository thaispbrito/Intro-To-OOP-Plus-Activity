from activity.student import Student
from activity.comparison import get_student_with_more_classes
import pytest 

NAME_1 = "Samara"
GRADE_1 = "junior"
CLASSES_1 = [
    "Pre-Calc", 
    "English III", 
    "World History", 
    "Gym", 
    "Chemistry",
    "Music Composition"
]

NAME_2 = "Claire"
GRADE_2 = "freshman"
CLASSES_2 = [
    "Algebra", 
    "Writing", 
    "Contemporary World Issues", 
    "Gym", 
    "Earth Science"
]

def test_get_student_name_with_more_classes():
    name_1 = NAME_1
    grade_1 = GRADE_1
    classes_1 = list(CLASSES_1)
    student_1 = Student(name_1, grade_1, classes_1)

    name_2 = NAME_2
    grade_2 = GRADE_2
    classes_2 = list(CLASSES_2)
    student_2 = Student(name_2, grade_2, classes_2)

    result = get_student_with_more_classes(student_1, student_2)

    assert result == "Samara"

# Extra test case #1
def test_get_no_student_when_tied():
    name_1 = NAME_1
    grade_1 = GRADE_1
    classes_1 = list(CLASSES_1)
    student_1 = Student(name_1, grade_1, classes_1)

    name_2 = NAME_2
    grade_2 = GRADE_2
    classes_2 = list(CLASSES_1)
    student_2 = Student(name_2, grade_2, classes_2)

    result = get_student_with_more_classes(student_1, student_2)

    assert result == None

# Extra test case #2
def test_same_student_raises_value_error():
    message_error = "This is the same student, please make sure to enter a different one!"

    name_1 = NAME_1
    grade_1 = GRADE_1
    classes_1 = list(CLASSES_1)
    student_1 = Student(name_1, grade_1, classes_1)

    name_2 = NAME_1
    grade_2 = GRADE_1
    classes_2 = list(CLASSES_1)
    student_2 = Student(name_2, grade_2, classes_2)

    with pytest.raises(ValueError, match = message_error):
        get_student_with_more_classes(student_1, student_2)