import psycopg2 as db
import os


class Database:
    @staticmethod
    def connect(query, type):
        database = db.connect(
            database="learning_center",
            host="localhost",
            user="postgres",
            password="akrom_1102"
        )

        cursor = database.cursor()
        cursor.execute(query)
        data_type = ["insert", "create", 'update', "delete", "drop"]
        if type in data_type:
            database.commit()

        if type == "create":
            return "Created Successfully"

        elif type == "insert":
            return "Inserted Successfully"

        elif type == "delete":
            return "Deleted Successfully"

        elif type == "update":
            return "Updated Successfully"

        elif type == "drop":
            return "Dropped Successfully"

        else:
            return cursor.fetchall()