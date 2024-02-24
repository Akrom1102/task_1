from main import Database

def create_table():
    country_table = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_date DATE);
        """

    city_table = f"""
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_date DATE,
            country_id INT REFERENCES country(country_id));
        """

    address_table = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_date DATE,
            city_id INT REFERENCES city(city_id));
        """

    course_table = f"""
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            title VARCHAR(50),
            description TEXT,
            price NUMERIC,
            language VARCHAR(15),
            create_date DATE);
    """

    student_table = f"""
        CREATE TABLE student(
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(25),
            gmail VARCHAR(50),
            password VARCHAR(8),
            create_date DATE,
            username VARCHAR(20),
            balance INT,
            active_courses INT);
        """

    mentor_table = f"""
        CREATE TABLE mentor(
            mentor_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(25),
            gmail VARCHAR(50),
            password VARCHAR(8),
            create_date DATE,
            username VARCHAR(20),
            address_id INT REFERENCES address(address_id));
        """


    course_mentor_table = f"""
        CREATE TABLE course_mentor(
            course_mentor_id SERIAL PRIMARY KEY,
            mentor_id INT REFERENCES mentor(mentor_id),
            course_id INT REFERENCES course(course_id));
    """

    course_student_table = f"""
        CREATE TABLE course_student(
            course_student_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES student(student_id),
            course_id INT REFERENCES course(course_id));
    """

    payment_type_table = f"""
        CREATE TABLE payment_type(
            payment_type_id SERIAL PRIMARY KEY,
            name VARCHAR(40),
            create_date DATE);
    """

    payment_table = f"""
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES student(student_id),
            course_id INT REFERENCES course(course_id),
            amount INT NOT NULL,
            payment_type_id INT REFERENCES payment_type(payment_type_id),
            create_date DATE);    """

    modul_table = f"""
        CREATE TABLE modul(
            modul_id SERIAL PRIMARY KEY,
            name VARCHAR(40),
            lesson_count INT,
            course_id INT REFERENCES course(course_id),
            create_date DATE);
    """

    lesson_table = f"""
        CREATE TABLE lesson(
            lesson_id SERIAL PRIMARY KEY,
            name VARCHAR(40),
            modul_id INT REFERENCES modul(modul_id),
            create_date DATE);
    """

    data_table = {
        "country_table": country_table,
        "city_table": city_table,
        "address_table": address_table,
        "course_table": course_table,
        "student_table": student_table,
        "mentor_table": mentor_table,
        "course_mentor_table": course_mentor_table,
        "course_student_table": course_student_table,
        "payment_type_table": payment_type_table,
        "payment_table": payment_table,
        "modul_table": modul_table,
        "lesson_table": lesson_table,
    }


    for i in data_table:
        print(f"{i}: {Database.connect(data_table[i], "create") }")

if __name__ == "__main__":
    create_table()
    print('_____________________________________________________')