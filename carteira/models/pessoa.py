class Pessoa:
    def __init__(self, nome, cpf, nasc, email):
        self.nome = nome
        self.cpf = cpf
        self.nasc = nasc
        self.email = email

    def __str__(self):
        return self.nome
