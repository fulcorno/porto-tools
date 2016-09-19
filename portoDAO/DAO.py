import mysql.connector

class DAO:

    db_params = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'porto'
    }

    conn = mysql.connector.connect(db_params)

    def create_paper(self, paper):
        cursor = DAO.conn.cursor()

        sql = "INSERT INTO "