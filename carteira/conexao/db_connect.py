import psycopg2 as pg


class DbConnect():
    def __init__(self):
        self.erro_con = None
        self.conn = None

    def get_conn(self):
        try:
            conn = pg.connect('dbname=carteira user=postgres password=masterkey')
            return conn
        except pg.Error as e:
            self.erro_con = str(e)

    def close_conn(self, conn, cur):
        try:
            conn.close()
            cur.close()
        except pg.Error as e:
            self.erro_con = str(e)

    def get_erros(self):
        return self.erro_con