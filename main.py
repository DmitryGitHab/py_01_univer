class Student:
    instances = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.__class__.instances.append(self)
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка!'

    def median_grades(self):
        if self.grades != {}:
            grades_list = []
            for k in self.grades.values():
                grades_list += k
            return sum(grades_list)/len(grades_list)
        else:
            return 'Оценки не найдены'

    def __lt__(self, other):
        return self.median_grades() < other.median_grades()
        # вариант кода для обозначения экземпляра класса с более высоким баллом
        # if self.median_grades() > other.median_grades():
        #     return (f'{self.name} имеет более высокий средней балл, чем {other.name}')
        # elif self.median_grades() < other.median_grades():
        #     return (f'{other.name} имеет более высокий средней балл, чем {self.name}')
        # elif self.median_grades() == other.median_grades():
        #     return (f'{self.name} и {other.name} имеют одинаковый средней балл {self.median_grades()} ')


    def __str__(self):
        return (f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за ДЗ: {self.median_grades()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}''')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    instances = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.__class__.instances.append(self)

    def median_grades(self):
        if self.grades != {}:
            grades_list = []
            for k in self.grades.values():
                grades_list += k
            return sum(grades_list)/len(grades_list)
        else:
            return 'Оценки не найдены'

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.median_grades()}")

    def __lt__(self, other):
        return self.median_grades() < other.median_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка!'

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}")

students_list = Student.instances
lecturer_list = Lecturer.instances

best_student = Student('Max', 'Black', 'Real_man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.add_courses('Введение в програмирование')
best_student.add_courses('Продвинутое введение в програмирование')

best_student_2 = Student('Den', 'Simple', 'Real_man')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Git']
best_student_2.add_courses('Введение в програмирование')
best_student_2.add_courses('Продвинутое введение в програмирование')

cool_reviewer = Reviewer('Alex', 'Couch')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_mentor_2 = Reviewer('Sanders', 'Trainer')
cool_mentor_2.courses_attached += ['Python']
cool_mentor_2.courses_attached += ['Git']

cool_lector = Lecturer('Ivan', 'Silver')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['Git']

cool_lector_2 = Lecturer('Steve', 'Jobs')
cool_lector_2.courses_attached += ['Python']
cool_lector_2.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(best_student, 'Git', 11)
cool_reviewer.rate_hw(best_student, 'Git', 11)
cool_reviewer.rate_hw(best_student, 'Git', 11)
cool_reviewer.rate_hw(best_student, 'Git', 11)

cool_reviewer.rate_hw(best_student_2, 'Python', 16)
cool_reviewer.rate_hw(best_student_2, 'Python', 16)
cool_reviewer.rate_hw(best_student_2, 'Python', 16)
cool_reviewer.rate_hw(best_student_2, 'Python', 16)

cool_reviewer.rate_hw(best_student_2, 'Git', 17)
cool_reviewer.rate_hw(best_student_2, 'Git', 17)
cool_reviewer.rate_hw(best_student_2, 'Git', 17)
cool_reviewer.rate_hw(best_student_2, 'Git', 17)

best_student.rate_hw(cool_lector, 'Python', 20)
best_student.rate_hw(cool_lector, 'Python', 20)
best_student.rate_hw(cool_lector, 'Python', 20)
best_student.rate_hw(cool_lector, 'Python', 20)

best_student.rate_hw(cool_lector, 'Git', 21)
best_student.rate_hw(cool_lector, 'Git', 21)
best_student.rate_hw(cool_lector, 'Git', 21)
best_student.rate_hw(cool_lector, 'Git', 21)

best_student.rate_hw(cool_lector_2, 'Python', 26)
best_student.rate_hw(cool_lector_2, 'Python', 26)
best_student.rate_hw(cool_lector_2, 'Python', 26)
best_student.rate_hw(cool_lector_2, 'Python', 26)

best_student.rate_hw(cool_lector_2, 'Git', 27)
best_student.rate_hw(cool_lector_2, 'Git', 27)
best_student.rate_hw(cool_lector_2, 'Git', 27)
best_student.rate_hw(cool_lector_2, 'Git', 27)


print(cool_lector.grades)
print(cool_lector_2.grades)

print(best_student.median_grades())
print(best_student.median_grades())
print(cool_lector.median_grades())
print(cool_lector.median_grades())

print(cool_lector)
print(cool_reviewer)
print(best_student)
print(best_student_2 < best_student)
print(cool_lector_2 < cool_lector)

print('_____________________________________')


def all_grade_student(course):
    length = 0
    amount = 0
    for i in students_list:
        for k in i.grades[course]:
            length += 1
            amount += k
    mid = amount/length
    print(f'Средний балл всех студентов по программе {course}: {mid}')

all_grade_student('Python')
all_grade_student('Git')

def all_grade_lecturer(course):
    length = 0
    amount = 0
    for i in lecturer_list:
        for k in i.grades[course]:
            length += 1
            amount += k
    mid = amount/length
    print(f'Средний балл всех лекторов по программе {course}: {mid}')

all_grade_lecturer('Python')
all_grade_lecturer('Git')