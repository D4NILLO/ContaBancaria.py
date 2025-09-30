# ContaBancaria.py

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Encapsulamento: atributo privado
        self.__saldo = saldo_inicial  # Encapsulamento: saldo privado
        self.__numero_conta = None  # Encapsulamento: número da conta privado

    # Métodos para acessar informações protegidas
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")


# Extensão: Conta Universitária
class ContaUniversitaria(ContaBancaria):
    def __init__(self, titular, saldo_inicial=0):
        super().__init__(titular, saldo_inicial)
        self.__taxa_manutencao = 0  # Conta gratuita

    def mostrar_info(self):
        print(f"Titular: {self.get_titular()}")
        print(f"Saldo: R${self.get_saldo()}")
        print(f"Taxa de manutenção: R${self.__taxa_manutencao}")


# Exemplo de uso do código
if __name__ == "__main__":
    conta = ContaUniversitaria("Danillo", 100)
    conta.depositar(50)
    conta.sacar(30)
    conta.mostrar_info()