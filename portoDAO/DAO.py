import mysql.connector

class DAO:

    db_params = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'porto'
    }

    def __init__(self):
        DAO.conn = mysql.connector.connect(**DAO.db_params)

    def delete_all_papers(self):
        cursor = DAO.conn.cursor()
        sql = "TRUNCATE paper"
        cursor.execute(sql)
        DAO.conn.commit()
        cursor.close()


    def create_paper(self, paper):

        cursor = DAO.conn.cursor()

        sql = (
            "INSERT IGNORE INTO PAPER ("
            "eprintid, title, `date`, `type`, types, abstract, "
            "is_wos, impact_wos, is_scopus, impact_scopus, "
            "issn, isbn, "
            "publisher, event_title, book_title, publication, "
            "DOI) " +
            "VALUES ( %s, %s, %s, %s, %s, %s, "
            "%s, %s, %s, %s, "
            "%s, %s, "
            "%s, %s, %s, %s,"
            "%s)" )

        cursor.execute(sql, (paper.eprintid, paper.title, paper.date, paper.type.type, paper.type.types, paper.abstract,
                             paper.is_wos, paper.impact_wos, paper.is_scopus, paper.impact_scopus,
                             paper.issn, paper.isbn,
                             paper.publisher, paper.event_title, paper.book_title, paper.publication,
                             paper.DOI) )

        DAO.conn.commit()
        cursor.close()

    def create_author(self, author):
        cursor = DAO.conn.cursor()

        sql = (
            "INSERT IGNORE INTO author (id , lastname, firstname) "
            "VALUES ( %s, %s, %s )" )

        cursor.execute(sql, (author.id, author.lastname, author.firstname))

        DAO.conn.commit()
        cursor.close()

    def create_paper_author(self, paper, author):
        cursor = DAO.conn.cursor()

        sql = ( "INSERT IGNORE INTO creator (eprintid, authorid) "
            "VALUES ( %s, %s )" )

        cursor.execute(sql, (paper.eprintid, author.id))

        DAO.conn.commit()
        cursor.close()

    def close(self):
        DAO.conn.close()
