from oo import teste_conta
from datetime import datetime

class Conta:
    def __init__(self, numero, titular, saldo, limite= 2000):
        self.limite = limite
        self.saldo = saldo
        self.titular = titular
        self.numero = numero
        self.historico = Historico()


    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Deposito:{valor}')


    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'Saque: {valor}')



    def extrato(self):
        print(f'Número: {self.numero} \n Saldo: {self.saldo}')
        self.historico.transacoes.append(f'Tirou extrado - saldo de {self.saldo}')


    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
            print('Vocẽ não tem saldo suficiente')
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'Tranferência de {valor} para {destino.titular.nome}')
            return True


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.cpf = cpf
        self.sobrenome = sobrenome
        self.nome = nome

    class Conta:
        def __init__(self, numero, cliente, saldo, limite= 1000):
            self.limite = limite
            self.saldo = saldo
            self.cliente = cliente
            self.numero = numero



class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'Data da abertura da conta: {self.data_abertura}')
        print('Transações: ')
        for t in self.transacoes:
            print('-', t)



if __name__ == '__main__':
    cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
    cliente2 = Cliente('José', 'Azevedo', '222222222-22')
    conta1 = Conta('123-4', cliente1, 1000.0)
    conta2 = Conta('123-5', cliente2, 1000.0)
    conta1.deposita(100.0)
    conta1.saca(50.0)
    conta1.transfere_para(conta2, 200.0)
    conta1.historico.imprime()
    conta2.historico.imprime()


