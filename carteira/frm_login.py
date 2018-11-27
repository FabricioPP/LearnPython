from tkinter import *
from tkinter import messagebox

from conexao import db_connect as db
import frm_carteira as cart


class Login(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lb_user = Label(self, text="Usuário: ")
        self.lb_senha = Label(self, text="Senha: ")

        self.ed_user = Entry(self)
        self.ed_senha = Entry(self, show="*")

        self.btn_entrar = Button(self, width=10, text="Entrar", command=self.click_btn_entrar)
        self.btn_sair = Button(self, width=10, text="Sair", command=self.click_btn_sair)

        self.lb_user.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        self.ed_user.grid(row=0, column=1, pady=10, padx=10)

        self.lb_senha.grid(row=1, column=0,padx=10, sticky=W)
        self.ed_senha.grid(row=1, column=1,padx=10)

        self.btn_entrar.grid(row=2, column=0,pady=10, padx=10)
        self.btn_sair.grid(row=2, column=1,pady=10, padx=10, sticky=E)

    def click_btn_entrar(self):
        user = self.ed_user.get()
        senha = self.ed_senha.get()
        conn = db.DbConnect.connect(self)
        cur = conn.cursor()

        cur.execute('select id_pessoa from pessoa where usuario = %s and pass = %s', (user, senha))

        #row = conn.query('select id_pessoa from pessoa where nome = %s', (user,))
        id_pessoa = cur.fetchone()

        try:
            if id_pessoa is None:
                messagebox.showerror("Erro!", 'Usuário ou senha errado.')

            else:

                self.destroy()

                with open('configuracoes\id_pessoa.txt', 'a') as arq:
                    arq.write(str(id_pessoa[0]))

                cart.CarteiraApp(master=root)



        except db.pg.Error as e:
            print('Erro' + e)
        finally:
            conn.close()

        conn.close()

    def click_btn_sair(self):
        self.quit()


root = Tk()

login = Login(master=root)

login.master.title('Login')
#login.master.geometry('250x150+200+200')

arq = open("id_pessoa.txt", 'r')
id = arq.read()
if int(id) > 0:
    login.destroy()

    cart.CarteiraApp(master=root)

login.mainloop()



