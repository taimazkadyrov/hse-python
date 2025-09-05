import pytest
import os
import json
import tempfile
from .solution import Student, StudentRegistry


@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp()
    yield path
    os.close(fd)
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def sample_students():
    return [
        Student(1, "Иван Иванов", 20, ["Математика", "Физика"]),
        Student(2, "Мария Петрова", 19, ["Информатика", "Английский"]),
        Student(3, "Алексей Сидоров", 21, ["Физика", "Информатика"]),
    ]


def test_student_init():
    student = Student(1, "Иван Иванов", 20, ["Математика", "Физика"])

    assert student.student_id == 1, "ID студента должен быть 1"
    assert student.name == "Иван Иванов", "Имя студента должно быть 'Иван Иванов'"
    assert student.age == 20, "Возраст студента должен быть 20"
    assert student.courses == [
        "Математика",
        "Физика",
    ], "Курсы студента должны быть ['Математика', 'Физика']"

    # Проверка значения по умолчанию для курсов
    student = Student(2, "Мария Петрова", 19)
    assert student.courses == [], "По умолчанию список курсов должен быть пустым"


def test_student_add_course():
    student = Student(1, "Иван Иванов", 20, ["Математика"])

    student.add_course("Физика")
    assert "Физика" in student.courses, "Курс 'Физика' должен быть добавлен"

    # Проверка добавления существующего курса
    student.add_course("Математика")
    assert student.courses.count("Математика") == 1, "Курс не должен дублироваться"


def test_student_remove_course():
    student = Student(1, "Иван Иванов", 20, ["Математика", "Физика"])

    student.remove_course("Математика")
    assert "Математика" not in student.courses, "Курс 'Математика' должен быть удален"

    # Проверка удаления несуществующего курса
    student.remove_course("Химия")
    assert student.courses == ["Физика"], "Список курсов не должен измениться"


def test_student_to_dict():
    student = Student(1, "Иван Иванов", 20, ["Математика", "Физика"])

    student_dict = student.to_dict()
    assert student_dict == {
        "student_id": 1,
        "name": "Иван Иванов",
        "age": 20,
        "courses": ["Математика", "Физика"],
    }, "Словарь должен содержать все атрибуты студента"


def test_student_from_dict():
    data = {
        "student_id": 1,
        "name": "Иван Иванов",
        "age": 20,
        "courses": ["Математика", "Физика"],
    }

    student = Student.from_dict(data)
    assert student.student_id == 1, "ID студента должен быть 1"
    assert student.name == "Иван Иванов", "Имя студента должно быть 'Иван Иванов'"
    assert student.age == 20, "Возраст студента должен быть 20"
    assert student.courses == [
        "Математика",
        "Физика",
    ], "Курсы студента должны быть ['Математика', 'Физика']"

    # Проверка без курсов
    data = {"student_id": 2, "name": "Мария Петрова", "age": 19}

    student = Student.from_dict(data)
    assert student.courses == [], "Если курсы не указаны, список должен быть пустым"


def test_registry_init(temp_file):
    # Создаем файл с данными студентов
    students_data = [
        {
            "student_id": 1,
            "name": "Иван Иванов",
            "age": 20,
            "courses": ["Математика", "Физика"],
        },
        {
            "student_id": 2,
            "name": "Мария Петрова",
            "age": 19,
            "courses": ["Информатика", "Английский"],
        },
    ]

    with open(temp_file, "w") as f:
        json.dump(students_data, f)

    registry = StudentRegistry(temp_file)

    assert len(registry.students) == 2, "Реестр должен содержать 2 студента"
    assert 1 in registry.students, "Студент с ID 1 должен быть в реестре"
    assert 2 in registry.students, "Студент с ID 2 должен быть в реестре"


def test_registry_add_student(temp_file):
    registry = StudentRegistry(temp_file)
    student = Student(1, "Иван Иванов", 20, ["Математика", "Физика"])

    registry.add_student(student)

    assert 1 in registry.students, "Студент должен быть добавлен в реестр"
    assert (
        registry.students[1].name == "Иван Иванов"
    ), "Имя студента должно быть 'Иван Иванов'"


def test_registry_remove_student(temp_file, sample_students):
    registry = StudentRegistry(temp_file)

    for student in sample_students:
        registry.add_student(student)

    registry.remove_student(2)

    assert 2 not in registry.students, "Студент с ID 2 должен быть удален"
    assert len(registry.students) == 2, "В реестре должно остаться 2 студента"


def test_registry_get_student(temp_file, sample_students):
    registry = StudentRegistry(temp_file)

    for student in sample_students:
        registry.add_student(student)

    student = registry.get_student(2)

    assert student is not None, "Метод должен вернуть студента"
    assert student.name == "Мария Петрова", "Имя студента должно быть 'Мария Петрова'"

    student = registry.get_student(100)
    assert student is None, "Для несуществующего ID должен вернуться None"


def test_registry_get_all_students(temp_file, sample_students):
    registry = StudentRegistry(temp_file)

    for student in sample_students:
        registry.add_student(student)

    all_students = registry.get_all_students()

    assert len(all_students) == 3, "Должны быть возвращены все 3 студента"
    assert all(
        isinstance(s, Student) for s in all_students
    ), "Все элементы должны быть экземплярами класса Student"


def test_registry_find_students_by_course(temp_file, sample_students):
    registry = StudentRegistry(temp_file)

    for student in sample_students:
        registry.add_student(student)

    physics_students = registry.find_students_by_course("Физика")

    assert (
        len(physics_students) == 2
    ), "Должно быть найдено 2 студента, изучающих физику"
    assert all(
        isinstance(s, Student) for s in physics_students
    ), "Все элементы должны быть экземплярами класса Student"
    assert all(
        "Физика" in s.courses for s in physics_students
    ), "У всех найденных студентов должен быть курс 'Физика'"


def test_registry_get_student_count(temp_file, sample_students):
    registry = StudentRegistry(temp_file)

    assert registry.get_student_count() == 0, "Изначально реестр должен быть пустым"

    for student in sample_students:
        registry.add_student(student)

    assert (
        registry.get_student_count() == 3
    ), "После добавления 3 студентов, счетчик должен быть 3"


def test_registry_save_and_load(temp_file, sample_students):
    # Создаем реестр и добавляем студентов
    registry1 = StudentRegistry(temp_file)

    for student in sample_students:
        registry1.add_student(student)

    # Сохраняем данные
    registry1.save_students()

    # Создаем новый реестр и загружаем данные
    registry2 = StudentRegistry(temp_file)

    # Проверяем, что данные загружены корректно
    assert len(registry2.students) == 3, "Должно быть загружено 3 студента"
    assert all(
        id in registry2.students for id in [1, 2, 3]
    ), "Все студенты должны быть загружены"

    # Проверяем данные конкретного студента
    student = registry2.get_student(1)
    assert student.name == "Иван Иванов", "Имя студента должно быть 'Иван Иванов'"
    assert "Математика" in student.courses, "У студента должен быть курс 'Математика'"


if __name__ == "__main__":
    pytest.main()
