from conexao import db_connect as db


class Operacao():
    def __init__(self):
        self.nome = None
        self.id_tipo = None
        self.conn = None
        self.cur = None
        self.error = None

    def set_id_tipo(self, id):
        try:
            self.conn = db.DbConnect.get_conn(self)
            self.cur = self.conn.cursor()
            self.cur.execute('select id_tipo from categoria where id_categoria = %s', (id,))
            self.id_tipo = self.cur.fetchone()[0]
            print(self.id_tipo)
        except db.pg.Error as e:
            print('erro', e)
        finally:
            db.DbConnect.close_conn(self, self.conn, self.cur)


    def set_nome(self, id):
        try:
            self.conn = db.DbConnect.get_conn(self)
            self.cur = self.conn.cursor()
            self.cur.execute('select nome from categoria where id_categoria = %s', (id,))
            self.nome = self.cur.fetchone()[0]
            print(self.nome)
        except db.pg.Error as e:
            self.error = e
        finally:
            db.DbConnect.close_conn(self, self.conn, self.cur)

    def get_nome(self):
        return self.nome

    def get_id_tipo(self):
        return self.id_tipo


