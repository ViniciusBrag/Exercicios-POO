def criar_conta(numero, titular, saldo, limite):
    conta = {'Número': numero, 'Saldo': saldo, 'Limite': limite}
    return conta


def deposita(conta, valor):
    conta['Saldo'] += valor


def saca(conta, valor):
    conta['Saldo'] -= valor


def extrato(conta):
    print(f'Número: {conta["Número"]} \n Saldo: {conta["Saldo"]}')




if __name__ == '__main__':
    conta = criar_conta('123-7', 'Vinicius',200.00, 2000)
    deposita(conta, 100)
    extrato(conta)

