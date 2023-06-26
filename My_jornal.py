class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.lecture_grades:
                lecture.lecture_grades[course] += [grade]
            else:
                lecture.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _get_average(self):
        sum_of_grades = sum([sum(self.grades[i]) for i in self.grades])
        sum_of_lens = sum([len(self.grades[i]) for i in self.grades])
        return sum_of_grades / sum_of_lens

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self._get_average()}\n" \
               f"Курсы в процессе изучения: {' '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {' '.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравниваемый объект не является студентом")
            return
        return self._get_average() < other._get_average()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def _get_average(self):
        sum_of_grades = sum([sum(self.lecture_grades[i]) for i in self.lecture_grades])
        sum_of_lens = sum([len(self.lecture_grades[i]) for i in self.lecture_grades])
        return sum_of_grades / sum_of_lens

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self._get_average()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Сравниваемый объект не является лектором")
            return
        return self._get_average() < other._get_average()

class Reviewer(Mentor):

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# Экземпляры студентов
student_1 = Student('Stud_name_1', 'Stud_surname_1', 'Stud_gen_1')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Stud_name_2', 'Stud_surname_2', 'Stud_gen_2')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

# Экземпляры лекторов
lector_1 = Lecturer('Lec_name_1', 'Lec_surname_1')
lector_1.courses_attached += ['Python', 'Git']
lector_2 = Lecturer('Lec_name_2', 'Lec_surname_2')
lector_2.courses_attached += ['Python']

# Экземпляры проверяющих
reviewer_1 = Reviewer("Rev_name_1", "Rev_surname_1")
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2 = Reviewer("Rev_name_2", "Rev_surname_2")
reviewer_2.courses_attached += ['Git']

# Выставление оценок лекторам
student_1.rate_lecture(lector_1, 'Python', 9)
student_1.rate_lecture(lector_1, 'Python', 8)
student_1.rate_lecture(lector_1, 'Python', 7)
student_1.rate_lecture(lector_1, 'Git', 6)
student_1.rate_lecture(lector_1, 'Git', 5)
student_1.rate_lecture(lector_1, 'Git', 4)
student_2.rate_lecture(lector_2, 'Python', 3)
student_2.rate_lecture(lector_2, 'Python', 4)
student_2.rate_lecture(lector_2, 'Python', 5)
student_2.rate_lecture(lector_2, 'Git', 10)   # Оценка не выставится, т.к. у лектора_2 нет Git курса в активе
student_2.rate_lecture(lector_2, 'Git', 10)   # Оценка не выставится, т.к. у лектора_2 нет Git курса в активе
student_2.rate_lecture(lector_2, 'Git', 10)   # Оценка не выставится, т.к. у лектора_2 нет Git курса в активе

# Выставление оценок студентам
reviewer_1.rate_student(student_1, 'Python', 9)
reviewer_1.rate_student(student_1, 'Python', 8)
reviewer_1.rate_student(student_1, 'Python', 7)
reviewer_1.rate_student(student_1, 'Git', 6)
reviewer_1.rate_student(student_1, 'Git', 5)
reviewer_1.rate_student(student_1, 'Git', 4)
reviewer_1.rate_student(student_2, 'Python', 10)
reviewer_1.rate_student(student_2, 'Python', 10)
reviewer_1.rate_student(student_2, 'Python', 10)
reviewer_2.rate_student(student_2, 'Git', 4)
reviewer_2.rate_student(student_2, 'Git', 4)
reviewer_2.rate_student(student_2, 'Git', 4)

# Проверочные принты
print("______________")
print(reviewer_1)
print("______________")
print(reviewer_2)
print("______________")
print(lector_1)
print("______________")
print(lector_2)
print("______________")
print(student_1)
print("______________")
print(student_2)
print("______________")
print(f"Сравнение по средней оценке: student_1 < student_2 -> {student_1 < student_2}")
print("______________")
print(f"Сравнение по средней оценке: lector_1 < lector_2 -> {lector_1 < lector_2}")

# Реализация функций по подсчету средней оценки всех студентов и лекторов по выбранному курсу
students_list = [student_1, student_2]
lectors_list = [lector_1, lector_2]

def average_students(list, course):
    all_grades = []
    for student in students_list:
        for subject in student.grades:
            if subject == course:
                all_grades.extend(student.grades[subject])
    return f'Средняя оценка студентов по курсу {course}: {sum(all_grades) / len(all_grades)}'

def average_lectors(list, course):
    all_grades = []
    for lector in lectors_list:
        for subject in lector.lecture_grades:
            if subject == course:
                all_grades.extend(lector.lecture_grades[subject])
    return f'Средняя оценка лекторов по курсу {course}: {sum(all_grades) / len(all_grades)}'

print("______________")
print(average_students(students_list, "Python"))
print(average_students(students_list, "Git"))
print(average_lectors(lectors_list, "Python"))
print(average_lectors(lectors_list, "Git"))
print("______________")
