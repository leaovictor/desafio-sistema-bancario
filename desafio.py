class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
        self.limite_saque = 500.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\nValor de depósito inválido. Tente novamente.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques_diarios:
            print("\nLimite de saques diários atingido!")
        elif valor > self.limite_saque:
            print(f"\nO limite de saque é de R$ {self.limite_saque:.2f} por operação.")
        elif valor > self.saldo:
            print("\nSaldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("\nExtrato Bancário")
        print("Depósitos:")
        for deposito in self.depositos:
            print(f"R$ {deposito:,.2f}")
        
        print("\nSaques:")
        for saque in self.saques:
            print(f"R$ {saque:,.2f}")

        print(f"\nSaldo atual: R$ {self.saldo:,.2f}")

    def resetar_saques_diarios(self):
        self.saques_diarios = 0


# Função para exibir o menu
def exibir_menu():
    print("\nEscolha uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")


# Inicializando o sistema bancário
conta = ContaBancaria()

while True:
    exibir_menu()
    opcao = input("\nDigite a opção desejada: ")

    if opcao == '1':
        valor = float(input("Digite o valor a depositar: R$ "))
        conta.depositar(valor)

    elif opcao == '2':
        valor = float(input("Digite o valor a sacar: R$ "))
        conta.sacar(valor)

    elif opcao == '3':
        conta.exibir_extrato()

    elif opcao == '4':
        print("\nSaindo do sistema bancário...")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
