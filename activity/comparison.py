# add your get_student_with_more_classes function here!

def get_student_with_more_classes(student_1, student_2):

    # Taking in consideration names are unique:
    if student_1.name == student_2.name:
        raise ValueError("This is the same student, please make sure to enter a different one!")

    if student_1.get_num_classes() == student_2.get_num_classes():
        return None
    elif student_1.get_num_classes() > student_2.get_num_classes():
        return student_1.name
    else:
        return student_2.name
    