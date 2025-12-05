groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Сидорова",
        "exams": ["Математика", "Физика", "Химия"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Анна",
        "surname": "Кузнецова",
        "exams": ["Биология", "География", "Литература"],
        "marks": [3, 4, 4]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


def filter_students_by_average(students, min_average):
    filtered_students = []
    for student in students:
        average_mark = sum(student["marks"]) / len(student["marks"])
        if average_mark >= min_average:
            filtered_students.append(student)
    return filtered_students


if __name__ == "__main__":
    print("Все студенты:")
    print_students(groupmates)

    print("\n" + "=" * 50)

    try:
        min_average = float(input("\nВведите минимальный средний балл для фильтрации: "))
        filtered = filter_students_by_average(groupmates, min_average)

        if filtered:
            print(f"\nСтуденты со средним баллом >= {min_average}:")
            print_students(filtered)
        else:
            print(f"\nНет студентов со средним баллом >= {min_average}")
    except ValueError:
        print("Ошибка! Введите числовое значение для среднего балла.")