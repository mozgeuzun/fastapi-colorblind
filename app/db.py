import json
from smtplib import SMTPResponseException
import mysql.connector
class db:
    @staticmethod
    def conn() :
            return mysql.connector.connect(
                host="mysqldevelopment",
                user="root",
                password="helloworld",
                database="testapp",
             
        )
    @staticmethod
    def list(count:int):
        print("CONN ONCESI 1")
        conn = db.conn()
        print("2")
        mycursor = conn.cursor()
        sql = "SELECT picture.picture_id FROM picture LIMIT "+str(count)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()
        return myresult