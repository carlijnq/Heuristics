"""

Object representing a single student

"""
class Student(object):
    def __init__(self, id, last_name, first_name, *args):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.subjects = args

"""

Object representing a room/place where e.g. lectures are given.

"""
class Room(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

"""

Object representing Subjects (E.G. Advanced Heuristics)
Each class has x amounts of lectures, seminars, students, practicums
Seminars and practicums can have a max size too

"""
class Course(object):
    # English for: Werkcollege?
    # q = quantity
    def __init__(self, name, q_lecture, q_seminar, seminar_max_students, q_practicum, practicum_max_students):
        self.name = name
        self.q_lecture = q_lecture
        self.q_seminar = q_seminar
        self.seminar_max_students = seminar_max_students
        self.q_practicum = q_practicum
        self.practicum_max_students = practicum_max_students
        self.student_list = {}
        self.activities = int(q_lecture) + int(q_practicum) + int(q_seminar)

    def set_students(self, student_list):
        try:
            for student in student_list:
                student = student_list[student]
                for i in student.subjects:
                    if i.lower() == self.name.lower():
                        self.student_list[student.id] = student
        except:
            print 'Could not load students to subjects!'

