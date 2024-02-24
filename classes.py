from main import Database

class Users:
    def __init__(self, first_name: str, last_name: str, gmail: str, password: str, create_date):
        self.first_name = first_name
        self.last_name = last_name
        self.gmail = gmail
        self.password = password
        self.create_date = create_date

    @staticmethod
    def select(table="users"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="users"):
        query = f"""INSERT INTO {table}(first_name, last_name, gmail, password, create_date) VALUES('{self.first_name}', '{self.last_name}', '{self.gmail}', '{self.password}', '{self.create_date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="users"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="users"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Student(Users):
    def __init__(self, first_name, last_name, gmail, password, create_date, username: str, balance: float, active_courses: int):
        super().__init__(first_name, last_name, gmail, password, create_date)
        self.username = username
        self.balance = balance
        self.active_courses = active_courses

    def insert(self, table="student"):
        query = f"""INSERT INTO {table}(first_name, last_name, gmail, password, create_date, username, balance, active_courses) 
                    VALUES('{self.first_name}', '{self.last_name}', '{self.gmail}', '{self.password}', 
                    '{self.create_date}', '{self.username}', '{self.balance}', '{self.active_courses}')"""
        return Database.connect(query, "insert")


class Mentor(Users):
    def __init__(self, first_name, last_name, gmail, password, create_date, username: str,
                 address_id: int):
        super().__init__(first_name, last_name, gmail, password, create_date)
        self.username = username
        self.address_id = address_id

    def insert(self, table="mentor"):
        query = f"""INSERT INTO {table}(first_name, last_name, gmail, password, create_date, username, status, address_id) 
                    VALUES('{self.first_name}', '{self.last_name}', '{self.gmail}', '{self.password}', 
                    '{self.create_date}', '{self.username}', '{self.address_id}')"""
        return Database.connect(query, "insert")


class Country:
    def __init__(self, name: str, create_date: str):
        self.name = name
        self.create_date = create_date

    @staticmethod
    def select(table="country"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="country"):
        query = f"""INSERT INTO {table}(name, create_date) VALUES('{self.name}', '{self.create_date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="country"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="country"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class City(Country):
    def __init__(self, name: str, create_date, country_id):
        super().__init__(name, create_date)
        self.country_id = country_id

    def insert(self, table="city"):
        query = f"""INSERT INTO {table}(name, country_id, create_date) VALUES('{self.name}', '{self.country_id}', '{self.create_date}')"""
        return Database.connect(query, "insert")


class Address(Country):
    def __init__(self, name, city_id, create_date):
        super().__init__(name, create_date)
        self.city_id = city_id

    def insert(self, table="address"):
        query = f"""INSERT INTO {table}(name, city_id, create_date) VALUES('{self.name}', '{self.city_id}', '{self.create_date}')"""
        return Database.connect(query, "insert")


class PaymentType(Country):
    def __init__(self, name, create_date):
        super().__init__(name, create_date)

    @staticmethod
    def select(table="payment_type"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")
class CourseStudent:
    def __init__(self, student_id: int,  course_id: int,):
        self.course_id = course_id
        self.student_id = student_id

    @staticmethod
    def select(table="course_student "):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="course_student"):
        query = f"""INSERT INTO {table}(course_id, student_id) VALUES('{self.course_id}', '{self.student_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="course_student"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="course_student"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Payment(CourseStudent):
    def __init__(self, student_id, course_id, amount: float,payment_type_id: int, create_date: str):
        super().__init__(student_id, course_id)
        self.amount = amount
        self.payment_type_id = payment_type_id
        self.create_date = create_date

    def insert(self, table="payment"):
        query = f"""INSERT INTO {table}(student_id, course_id, amount, payment_type_id, create_date) VALUES('{self.student_id}', '{self.course_id}', '{self.amount}', '{self.payment_status_id}', '{self.payment_type_id}', '{self.create_date}')"""
        return Database.connect(query, "insert")


class Course:
    def __init__(self, title: str, description: str, price: float, language: str, create_date: str):
        self.title = title
        self.description = description
        self.price = price
        self.language = language
        self.create_date = create_date

    @staticmethod
    def select(table="course"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="course"):
        query = f"""INSERT INTO {table}(title, description, price, language, create_date) VALUES('{self.title}', '{self.description}', '{self.raiting}', '{self.price}', '{self.price_status}', '{self.language}', '{self.create_date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="course"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="course"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")



class CourseMentor:
    def __init__(self, course_id, mentor_id):
        self.mentor_id = mentor_id
        self.course_id = course_id

    @staticmethod
    def select(table="course_mentor "):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="course_mentor"):
        query = f"""INSERT INTO {table}(course_id, mentor_id) VALUES('{self.course_id}', '{self.mentor_id}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="course_mentor"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="course_mentor"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Modul:
    def __init__(self, name, lesson_count, course_id, create_date):
        self.name = name
        self.lesson_count = lesson_count
        self.course_id = course_id
        self.create_date = create_date

    @staticmethod
    def select(table="modul"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="modul"):
        query = f"""INSERT INTO {table}(name, lesson_count, course_id, create_date) VALUES('{self.name}', '{self.lesson_count}', '{self.course_id}', '{self.create_date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="modul"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="modul"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class Lesson:
    def __init__(self, name, modul_id, create_date):
        self.name = name
        self.modul_id = modul_id
        self.create_date = create_date

    @staticmethod
    def select(table="lesson"):
        query = f"""SELECT * FROM {table}"""
        return Database.connect(query, "select")

    def insert(self, table="lesson"):
        query = f"""INSERT INTO {table}(name, modul_id, create_date) VALUES('{self.name}', '{self.modul_id}', '{self.create_date}')"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="lesson"):
        query = f"""DELETE FROM {table} WHERE {column} = '{data}'"""
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(column, data, table="lesson"):
        query = f"""DELETE FROM {table} WHERE {column} = {data}"""
        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")