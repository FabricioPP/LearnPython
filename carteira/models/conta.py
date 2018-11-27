from conexao import db_connect as db


class Conta:
    def __init__(self, id_pessoa):
        self.id_pessoa = id_pessoa
        self.saldo = None
        self.conn = None

    def get_saldo(self):

        try:
            self.conn = db.DbConnect.get_conn(self)
            cur = self.conn.cursor()
            cur.execute('select * from conta where id_pessoa = %s', (self.id_pessoa,))
            self.saldo = cur.fetchone()[1]

        except db.pg.Error as e:
            print("Erro.", e)

        finally:
            self.conn.close_conn(self.conn, cur)
        return self.saldo

    def get_dono(self):
        try:
            self.get_conn()
            self.cur.execute('select pessoa.nome from pessoa where id_pessoa = %s', (self.id_pessoa,))
            pessoa = self.cur.fetchone()[0]
        except db.pg.Error as e:
            print('Erro:', e)
        finally:
            self.close_conn()
        return pessoa
