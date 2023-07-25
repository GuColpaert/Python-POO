#  Classe

class Conta:
    #  pass > serve para desconsiderar o campo vazio da classe

    def __init__(self, numero, titular, saldo, limite):  # Método construtor da aplicação
        print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
