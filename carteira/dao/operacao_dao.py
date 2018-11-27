from conexao import db_connect as db
from datetime import datetime

class OperacaoDAO():

    def __init__(self):
        self.erro = None
        self.conn = None
        self.erro_msg = None

    def insert_operacao(self, desc, val, id_cat, id_tipo, id_conta):
        data = datetime.now()
        try:
            self.conn = db.DbConnect.get_conn(self)
            cur = self.conn.cursor()
            cur.execute("insert into operacao(descricao, valor, id_categoria, id_tipo, id_conta, data)values(%s, %s, %s, %s, %s, %s)",
                        (desc, val, id_cat, id_tipo, id_conta, data))
            self.conn.commit()
        except db.pg.Error as e:
            self.erro_msg = e
        finally:
            self.conn.close_conn(self.conn, cur)

    def get_error(self):
        return self.erro_msg