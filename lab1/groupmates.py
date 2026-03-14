groupmates = [
    {
        "name": "Альберт",
        "group": "БСТ2253",
        "age": 23,
        "marks": [4, 3, 4, 5, 5]
    },
    {
        "name": "Полина",
        "group": "БСТ2253",
        "age": 23,
        "marks": [4, 3, 3, 4, 5]
    },
    {
        "name": "Полина",
        "group": "БСТ2253",
        "age": 31,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": "Сергей",
        "group": "БСТ2253",
        "age": 28,
        "marks": [4, 3, 5, 4, 5]
    }
]


def print_students(students):
    print("Имя студента".ljust(15),
          "Группа".ljust(10),
          "Возраст".ljust(8),
          "Оценки".ljust(20))

    for student in students:
        print(student["name"].ljust(15),
              student["group"].ljust(10),
              str(student["age"]).ljust(8),
              str(student["marks"]).ljust(20))

    print("\n")

print_students(groupmates)

#Фильтрация по среднему баллу
def filter_by_avg(students, min_avg):
    result = []
    for s in students:
        avg = sum(s["marks"]) / len(s["marks"])
        if avg >= min_avg:
            result.append(s)
    return result

min_avg = int(input("Введите минимальный средний балл (целое число): "))
filtered = filter_by_avg(groupmates, min_avg)
print(f"Студенты со средним баллом >= {min_avg}:")
print_students(filtered)