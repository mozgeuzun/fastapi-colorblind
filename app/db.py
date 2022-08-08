
import mysql.connector
import base64

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
        sql = "SELECT picture.picture_id,picture.picture_value FROM picture LIMIT "+str(count)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()
        return myresult
    @staticmethod
    def image (id:int):
        conn = db.conn()
        mycursor = conn.cursor()
        sql = "SELECT picture.picture_picture FROM picture where picture.picture_id="+str(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        conn.close()
        if ( len(data)>0 and len(data[0])>0 ):
            b64str = base64.b64encode(data[0][0])
            print(b64str)
            return {
                "picture_id":id,
                "picture_data":b64str
            }
        else:
            return {
                "picture_id":id,
                "picture_data":None
            }