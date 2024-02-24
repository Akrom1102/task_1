from classes import (Student, Mentor, Country, City, Address, Payment, PaymentType, CourseMentor, CourseStudent,Course,Modul, Lesson)

def services_course():
    print("Siz course tablega kirdiz")
    """
        ushbu funksiya course uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in Course.select("course"):
            print(i)
        return services_course()

    elif services == "0":
        return main()

    elif services == "2":
        title = input("Kurs nomi: ")
        description = input("Kurs haqida ma'lumot: ")
        price = float(input("Kurs narxi: "))
        language = input("Kurs tili : ")
        create_date = input("Create_date: ")
        course = Course(title, description, price, language, create_date)
        print(course.insert("course"))

        return services_course()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "course_id":
            print(Course.delete(column, data, "course"))

        else:
            print(Course.delete_id(column, data, "course"))

        return services_course()

    elif services == "4":
        course = input('new course_id: ')
        course_id = int(input('old course_id: '))
        query = f"""UPDATE course SET course_id = '{course}' WHERE course_id = {course_id}"""
        Course.update(query)

        return services_course()

def services_mentor():
    print("Siz Mentor tablega kirdiz")
    """
        ushbu funksiya mentor uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in Mentor.select("mentor"):
            print(i)
        return services_mentor()

    elif services == "0":
        return main()

    elif services == "2":
        first_name = input("Ism : ")
        last_name = input("Familiya : ")
        username = input("Username : ")
        password = input("Parol : ")
        gmail = input("Email : ")
        create_date = input("Yaratilgan sana : ")
        address_id = int(input("Address_id : "))
        mentor = Mentor(first_name, last_name, gmail, password, create_date, username, address_id)
        print(mentor.insert("mentor"))

        return services_mentor()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "mentor_id":
            print(Mentor.delete(column, data, "mentor"))

        else:
            print(Mentor.delete_id(column, data, "mentor"))

        return services_mentor()

    elif services == "4":
        mentor = input('new mentor_id: ')
        mentor_id = int(input('old mentor_id: '))
        query = f"""UPDATE mentor SET mentor_id = '{mentor}' WHERE mentor_id = {mentor_id}"""
        Mentor.update(query)

        return services_mentor()

def services_course_mentor():
    print("Siz Course mentor tablega kirdiz")
    """
        ushbu funksiya course mentor uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in CourseMentor.select("course_mentor"):
            print(i)
        return services_course_mentor()

    elif services == "0":
        return main()

    elif services == "2":
        course_id = int(input("Kurs_id (kurs tableda bor id ni kiriting): "))
        mentor_id = int(input("Mentor_id (mentor tableda bor id ni kiriting): "))
        course_mentor = CourseMentor(course_id, mentor_id)

        print(course_mentor.insert("course_mentor"))

        return services_course_mentor()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "course_mentor_id":
            print(CourseMentor.delete(column, data, "course_mentor"))

        else:
            print(CourseMentor.delete_id(column, data, "course_mentor"))

        return services_course_mentor()

    elif services == "4":
        mentor = input('new course_mentor_id: ')
        mentor_id = int(input('old course_mentor_id: '))
        query = f"""UPDATE course_mentor SET course_mentor_id = '{mentor}' WHERE course_mentor_id = {mentor_id}"""
        CourseMentor.update(query)

        return services_course_mentor()

def services_course_student():
    print("Siz Course student tablega kirdiz")
    """
        ushbu funksiya course student uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in CourseStudent.select("course_student"):
            print(i)
        return services_course_student()

    elif services == "0":
        return main()

    elif services == "2":
        course_id = int(input("Kurs_id (kurs tableda bor id ni kiriting): "))
        student_id = int(input("Mentor_id (mentor tableda bor id ni kiriting): "))
        course_student = CourseStudent(student_id, course_id)

        print(course_student.insert("course_student"))

        return services_course_student()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "course_student_id":
            print(CourseStudent.delete(column, data, "course_student"))

        else:
            print(CourseStudent.delete_id(column, data, "course_student"))

        return services_course_student()

    elif services == "4":
        mentor = input('new course_student_id: ')
        mentor_id = int(input('old course_student_id: '))
        query = f"""UPDATE course_student SET course_student_id = '{mentor}' WHERE course_student_id = {mentor_id}"""
        CourseStudent.update(query)

        return services_course_student()

def services_student():
    print("Siz Student tablega kirdiz")
    """
        ushbu funksiya student uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in Student.select("student"):
            print(i)
        return services_student()

    elif services == "0":
        return main()

    elif services == "2":
        first_name = input("Ism : ")
        last_name = input("Familiya : ")
        username = input("Username : ")
        password = input("Parol : ")
        gmail = input("Email : ")
        create_date = input("Yaratilgan sana : ")
        balance = float(input("Balans : "))
        active_courses = int(input("Aktiv kurslar: "))
        student = Student(first_name, last_name, gmail, password, create_date, username, balance, active_courses)
        print(student.insert("student"))

        return services_student()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "student_id":
            print(Student.delete(column, data, "student"))

        else:
            print(Student.delete_id(column, data, "student"))

        return services_student()

    elif services == "4":
        student = input('new student_id: ')
        student_id = int(input('old student_id: '))
        query = f"""UPDATE student SET student_id = '{student}' WHERE student_id = {student_id}"""
        Student.update(query)

        return services_student()

def services_country():
    print("Siz Country tablega kirdiz")

    """
        ushbu funksiya country uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in Country.select("country"):
            print(i)
        return services_country()

    elif services == "0":
        return main()

    elif services == "2":
        name = input("Mamlakatingizni nomini kiriting: ")
        create_date = input("Create date yyyy-mm-dd: ")
        country = Country(name, create_date)
        print(country.insert("country"))

        return services_country()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "country_id":
            print(Country.delete(column, data, "country"))

        else:
            print(Country.delete_id(column, data, "country"))

        return services_country()

    elif services == "4":
        country = input('new Country_id: ')
        country_id = int(input('old Country_id: '))
        query = f"""UPDATE country SET country_id = '{country}' WHERE country_id = {country_id}"""
        Country.update(query)

        return services_country()

def services_city():
    print("Siz city tablega kirdiz")

    """
        ushbu funksiya city uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in City.select("city"):
            print(i)
        return services_city()

    elif services == "0":
        return main()

    elif services == "2":
        name = input("Shahringizni nomini kiriting: ")
        country_id = input("Country_id: ")
        create_date = input("Create date yyyy-mm-dd: ")


        city = City(name,create_date, country_id)
        print(city.insert("city"))

        return services_city()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "city_id":
            print(City.delete(column, data, "city"))

        else:
            print(City.delete_id(column, data, "city"))

        return services_city()

    elif services == "4":
        city = input('new City_id: ')
        city_id = int(input('old City_id: '))
        query = f"""UPDATE city SET city_id = '{city}' WHERE city_id = {city_id}"""
        City.update(query)

        return services_city()

def services_address():
    print("Siz address tablega kirdiz")

    """
        ushbu funksiya address uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in Address.select("address"):
            print(i)
        return services_address()

    elif services == "0":
        return main()

    elif services == "2":
        name = input("Mahalla nomini kiriting: ")
        city_id = input("City_id: ")
        create_date = input("Create date yyyy-mm-dd: ")


        address = Address(name,  city_id,create_date)
        print(address.insert("address"))

        return services_address()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "address_id":
            print(Address.delete(column, data, "address"))

        else:
            print(Address.delete_id(column, data, "address"))

        return services_address()

    elif services == "4":
        address = input('new address_id: ')
        address_id = int(input('old address_id: '))
        query = f"""UPDATE address SET address_id = '{address}' WHERE address_id = {address_id}"""
        Address.update(query)

        return services_address()

def services_modul():
    print("Siz modul tablega kirdiz")

    """
        ushbu funksiya modul uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in Modul.select("modul"):
            print(i)
        return services_modul()

    elif services == "0":
        return main()

    elif services == "2":
        name = input("Modul nomi: ")
        lesson_count = input("Lesson count: ")
        course_id = input("Course id (cours tableda bor idni yozing): ")
        create_date = input("Create date yyyy-mm-dd: ")


        modul = Modul(name, lesson_count, course_id, create_date)
        print(modul.insert("modul"))

        return services_modul()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "modul_id":
            print(Modul.delete(column, data, "modul"))

        else:
            print(Modul.delete_id(column, data, "modul"))

        return services_modul()

    elif services == "4":
        modul = input('new modul_id: ')
        modul_id = int(input('old modul_id: '))
        query = f"""UPDATE modul SET modul_id = '{modul}' WHERE modul_id = {modul_id}"""
        Modul.update(query)

        return services_modul()

def services_lesson():
    print("Siz lesson tablega kirdiz")

    """
        ushbu funksiya lesson uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in Lesson.select("lesson"):
            print(i)
        return services_lesson()

    elif services == "0":
        return main()

    elif services == "2":
        name = input("lesson nomi: ")
        modul_id = input("modul id (modul tableda bor idni yozing): ")
        create_date = input("Create date yyyy-mm-dd: ")


        lesson = Lesson(name, modul_id, create_date)
        print(lesson.insert("lesson"))

        return services_lesson()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "modul_id":
            print(Lesson.delete(column, data, "lesson"))

        else:
            print(Lesson.delete_id(column, data, "lesson"))

        return services_lesson()

    elif services == "4":
        lesson = input('new lesson_id: ')
        lesson_id = int(input('old lesson_id: '))
        query = f"""UPDATE lesson SET lesson_id = '{lesson}' WHERE lesson_id = {lesson_id}"""
        Lesson.update(query)

        return services_lesson()

def services_payment():
    print("Siz payment tablega kirdiz")
    """
        ushbu funksiya payment uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in Payment.select("payment"):
            print(i)
        return services_payment()

    elif services == "0":
        return main()

    elif services == "2":
        student_id = int(input("Mentor_id (mentor tableda bor id ni kiriting): "))
        course_id = int(input("Kurs_id (kurs tableda bor id ni kiriting): "))
        amount = float(input("Amount: "))
        payment_type_id = int(input("Payment_type_id (payment_type_id tableda bor id ni yozing: "))
        create_date = input("Create Date: ")
        payment = Payment(student_id, course_id, amount, payment_type_id, create_date)

        print(payment.insert("payment"))

        return services_payment()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "payment_id":
            print(Payment.delete(column, data, "payment"))

        else:
            print(Payment.delete_id(column, data, "payment"))

        return services_payment()

    elif services == "4":
        payment = input('new payment_id: ')
        payment_id = int(input('old payment_id: '))
        query = f"""UPDATE payment SET payment_id = '{payment}' WHERE payment_id = {payment_id}"""
        Payment.update(query)

        return services_payment()

def services_payment_type():
    print("Siz payment_type tablega kirdiz")
    """
        ushbu funksiya payment_type uchun insert update delete select qib beradi
    """
    services = input("""Servis turini tanlang: 
        1. Select
        2. Insert
        3. Delete
        4. Update
        0. back🚪🏃
            >>>""")

    if services == "1":
        for i in PaymentType.select("payment_type"):
            print(i)
        return services_payment_type()

    elif services == "0":
        return main()

    elif services == "2":
        name = input("Naqd yoki Plastik: ")
        create_date = input("Create_date: ")
        payment_type = PaymentType(name, create_date)

        print(payment_type.insert("payment_type"))

        return services_payment_type()

    elif services == "3":
        column = input("Column : ")
        data = input("Data : ")
        if column != "payment_id":
            print(PaymentType.delete(column, data, "payment_type"))

        else:
            print(PaymentType.delete_id(column, data, "payment_type"))

        return services_payment()

    elif services == "4":
        payment_type = input('new payment_type_id: ')
        payment_type_id = int(input('old payment_type_id: '))
        query = f"""UPDATE payment SET payment_type_id = '{payment_type}' WHERE payment_type_id = {payment_type_id}"""
        PaymentType.update(query)

        return services_payment_type()

def main():
    tables = input("""Jadvallar ro'yxati👇: 
        1. Country 
        2. City
        3. Address
        4. Course
        5. Student
        6. Mentor
        7. Course_mentor
        8. Course_student
        9. Payment_type
        10.Payment
        11.Modul
        12. Lesson
            >>> """)

    if tables == '1':
        return services_country()

    elif tables == '2':
        return services_city()

    elif tables == '3':
        return services_address()

    elif tables == '4':
        return services_course()

    elif tables == '5':
        return services_student()

    elif tables == '6':
        return services_mentor()

    elif tables == '7':
        return services_course_mentor()

    elif tables == '8':
        return services_student()

    elif tables == '9':
        return services_payment_type()

    elif tables == '10':
        return services_payment()

    elif tables == '11':
        return services_modul()

    elif tables == '12':
        return services_lesson()

    else:
        print('Bunday jadval mavjud emas boshqattan kiriting')
        return main()

if __name__ == '__main__':
    main()