import mysql.connector

class delete:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Sakhiya@123$",
                database = "bank"
                )
    def mydelete(self,table_name,cusid):
        cur = self.conn.cursor()
        if table_name=='personal_details' or table_name=='bank_details':
            cur.execute(f"DELETE FROM {table_name} where customerid={cusid}")
            self.conn.commit()
            print("Data has been deleted successfully")
