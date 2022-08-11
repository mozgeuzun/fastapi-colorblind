
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
    def list(count:int,types:str):
        conn = db.conn()
        mycursor = conn.cursor()
        # red,green,blue
        # 'red','grean','blue'
        tt = ""
        cl = types.split(",")
        for i in range(len(cl)):
            if i > 0:
                tt += ","
            tt += "'"+cl[i]+"'"

        sql = """SELECT to_base64(p.picture_picture),p.picture_id,p.picture_value , group_concat(t.type_color) as types
        FROM picture p 
        inner join type t on t.picture_id = p.picture_id and t.type_color in ({types}) 
        group by p.picture_picture,p.picture_id,p.picture_value
        order by RAND() limit {limit}""".format(types=tt,limit=str(count))
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