from tkinter import *
from tkinter.ttk import Combobox
from conexao import db_connect as db
from datetime import datetime
from tkinter import messagebox
from dao import operacao_dao as opdao

class OperacaoApp(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.id_tipo = None
        self.grid()
        self.master.title('Operação.')
        self.createWidgets()
        self.set_cmb_categoria(self.id_tipo)

    # TODO Arruma o cmb
    def createWidgets(self):
        self.lb_tipo = Label(self, text="Operação", bg='green', font=('bold', 15), fg='white')
        lb_descricao = Label(self, text="Descrição:", font=13, )
        lb_valor = Label(self, text="Valor:", font=13)
        lb_categoria = Label(self, text='Categoria', font=13)

        btn_salvar = Button(self, text="Salvar", width=20, font=13, command=self.click_btn_salvar)
        btn_cancelar = Button(self, text="Cancelar", width=20, font=13, command=self.click_btn_cancelar)

        self.ed_descricao = Entry(self, font=13)
        self.ed_valor = Entry(self, font=13)
        self.cmb_categoria = Combobox(self, width=20, values=['Comida', 'Gasolina', 'Hotel', 'Passagem'], font=13,
                                      state='readonly', )


        self.lb_tipo.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky=EW)
        lb_descricao.grid(row=1, column=0, pady=10, padx=10)
        lb_valor.grid(row=2, column=0, pady=10, padx=10)
        lb_categoria.grid(row=3, column=0, pady=10, padx=10)

        self.ed_descricao.grid(row=1, column=1, pady=10, padx=10, sticky=EW)
        self.ed_valor.grid(row=2, column=1, pady=10, padx=10, sticky=EW)
        self.cmb_categoria.grid(row=3, column=1, pady=10, padx=10)

        btn_salvar.grid(row=4, column=0, pady=10, padx=10, )
        btn_cancelar.grid(row=4, column=1, pady=10, padx=10)

    def click_btn_salvar(self):
        op = opdao.OperacaoDAO()
        try:
            op.insert_operacao(self.ed_descricao.get(), int(self.ed_valor.get()), 1, 1, 1)
        except Exception as e:
            messagebox.showerror('Erro!', op.get_error())
        #TODO arrumar erro q esta dando q cadastra certo a operacao, mas dps chama o except..


    def click_btn_cancelar(self):
        print(self.cmb_categoria.get())

    def set_cmb_categoria(self, id_categoria):
        conn = None
        cur = None
        try:
            conn = db.DbConnect.get_conn(self)
            cur = conn.cursor()
            cur.execute('select nome from categoria where id_tipo = %s', (id_categoria,))
            valores = cur.fetchall()
            list = []
            for val in valores:
                list.append(val[0])

            self.cmb_categoria['value'] = list
            print(list)


        except db.pg.Error as e:
            messagebox.showerror('Error:', e)
        finally:
            db.DbConnect.close_conn(self, conn, cur)

    def set_id_tipo(self, id):
        self.id_tipo = id
        if id == 1:
            self.lb_tipo['bg'] = 'green'
            self.lb_tipo['text'] = 'Entrada'
        else:
            self.lb_tipo['bg'] = 'red'
            self.lb_tipo['text'] = 'Saída'
            self.set_cmb_categoria(id)

root = Tk()

app = OperacaoApp(master=root)

app.set_id_tipo(2)

app.mainloop()






