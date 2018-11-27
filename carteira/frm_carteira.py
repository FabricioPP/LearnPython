from functools import partial
from tkinter import *
from models import conta
import frm_operacao as op


class CarteiraApp(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Carteira')
        self.grid()
        #self.master.geometry('330x200+200+200')
        self.arq = open('configuracoes\id_pessoa.txt', 'r')
        self.id_pessoa = self.arq.read()
        self.c = conta.Conta(int(self.id_pessoa))
        self.createWidgets(self.c)
        self.set_label_saldo(self.c)


    def createWidgets(self, conta):
        #===============================CRIANDO OS WIDGETS============================================#
        self.lb_user = Label(self, text=self.set_user().upper(), bg="blue", font=('bold', 15), fg='white', )
        self.lb_saldo = Label(self, text='Label', bg='green', font=('bold', 13))
        lb_saldo2 = Label(self, text="SALDO: ", font=13)
        self.btn_saida = Button(self, width=15, text="Add Saída", font=13)
        self.btn_entrada = Button(self, width=15, text="Add Entrada", font=13)

        #=================passando os paramentros para a função click_btn_retirar================================#
        args_btn_saida = partial(self.click_btn_saida, conta)
        self.btn_saida['command'] = args_btn_saida

        #=================passando os paramentros para a função click_btn_deposito==============================#
        args_btn_entrada = partial(self.click_btn_entrada, conta)
        self.btn_entrada['command'] = args_btn_entrada

        #====================SETANDO OS WIDGETS NA TELA==============================================#
        self.lb_user.grid(row=0, column=0, columnspan=2, sticky=EW, pady=10, padx=10)
        lb_saldo2.grid(row=1, column=0, pady=10, padx=10, sticky=E)
        self.lb_saldo.grid(row=1, column=1, pady=10, padx=10, sticky=EW)
        self.btn_saida.grid(row=2, column=0, pady=10, padx=10)
        self.btn_entrada.grid(row=2, column=1, pady=10, padx=10)

    #=====================ATUALIZA O LABEL SALDO=========================#
    def set_label_saldo(self, conta):
        self.lb_saldo['text'] = conta.get_saldo()
        if conta.get_saldo() < 0:
            self.lb_saldo['bg'] = "red"
        else:
            self.lb_saldo['bg'] = 'green'

    #======================FUNÇÃO DO CLICK NO BOTAO SAIDA===================#
    def click_btn_saida(self, conta):
        #conta.retirar(100)
        #self.set_label_saldo(conta)
        self.destroy()
        opApp = op.OperacaoApp(master=root)
        opApp.set_id_tipo(2)
        opApp.set_cmb_categoria(2)




    #====================FUNÇÃO CLICK DO BOTAO ENTRADA===================#
    def click_btn_entrada(self, conta):
        conta.deposito(200)
        self.set_label_saldo(conta)

    def set_user(self):
        return self.c.get_dono()

root = Tk()

app = CarteiraApp(master=root)

app.mainloop()


