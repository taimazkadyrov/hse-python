# Задание 15: Комплексная задача с использованием файлов
# Реализуйте систему учета студентов


class Student:
    """
    Класс для представления студента
    """

    def __init__(self, student_id, name, age, courses=None):
        """
        Инициализирует студента с указанными параметрами
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = courses or []

    def add_course(self, course):
        """
        Добавляет курс студенту
        """
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Удаляет курс у студента
        """
        if course in self.courses:
            self.courses.remove(course)

    def to_dict(self):
        """
        Преобразует студента в словарь для сохранения
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "courses": self.courses,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Создает студента из словаря
        """
        return cls(
            data["student_id"], data["name"], data["age"], data.get("courses", [])
        )


class StudentRegistry:
    """
    Класс для управления списком студентов
    """

    def __init__(self, file_path):
        """
        Инициализирует реестр студентов с указанным путем к файлу
        """
        self.file_path = file_path
        self.students = {}
        self.load_students()

    def load_students(self):
        """
        Загружает студентов из файла
        """
        # Ваш код здесь
        pass

    def save_students(self):
        """
        Сохраняет студентов в файл
        """
        # Ваш код здесь
        pass

    def add_student(self, student):
        """
        Добавляет студента в реестр
        """
        # Ваш код здесь
        pass

    def remove_student(self, student_id):
        """
        Удаляет студента из реестра по ID
        """
        # Ваш код здесь
        pass

    def get_student(self, student_id):
        """
        Возвращает студента по ID
        """
        # Ваш код здесь
        pass

    def get_all_students(self):
        """
        Возвращает список всех студентов
        """
        # Ваш код здесь
        pass

    def find_students_by_course(self, course):
        """
        Возвращает список студентов, изучающих указанный курс
        """
        # Ваш код здесь
        pass

    def get_student_count(self):
        """
        Возвращает количество студентов в реестре
        """
        # Ваш код здесь
        pass
