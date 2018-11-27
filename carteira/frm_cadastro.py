from tkinter import *
import frm_carteira
from models import pessoa


class MyApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.lbNome = Label(self, text="Nome: ")
        self.edNome = Entry(self, width=50)

        self.lbCpf = Label(self, text="CPF: ")
        self.edCpf = Entry(self, width=50)

        self.lbDataNasc = Label(self, text="Data Nascimento: ")
        self.edDataNasc = Entry(self, width=30)

        self.lbEmail = Label(self, text="Email: ")
        self.edEmail = Entry(self, width=50)

        self.btCadastrar = Button(self, width=20, text="Cadastrar", command=self.btnCadastrar)

        self.lbNome.grid(row=0, column=0, pady=10)
        self.edNome.grid(row=0, pady=10, column=1)

        self.lbEmail.grid(row=1, column=0)
        self.edEmail.grid(row=1, column=1)

        self.lbDataNasc.grid(row=2, column=0, pady=10, padx=5)
        self.edDataNasc.grid(row=2, column=1, pady=10, sticky=W)

        self.lbCpf.grid(row=3, column=0)
        self.edCpf.grid(row=3, column=1)

        self.btCadastrar.grid(row=4, column=1, pady=10, sticky=W)

    def btnCadastrar(self):
        p = pessoa.Pessoa(self.edNome.get(), self.edCpf.get(), self.edDataNasc.get(), self.edEmail.get())
        print(p)
        self.destroy()

        car = frm_carteira.CarteiraApp(master=root)
        car.mainloop()


root = Tk()
app = MyApp(master=root)

app.master.title('Cadastrar')
app.master.geometry('440x200+200+200')
app.mainloop()




        
        
