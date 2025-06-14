'''
Desafio DIO BACK-END PYTHON
Criando um sistema bancario simples
Com operacoes de saque, deposito e extrato
Autor: Fábio Gonçalves
Data: 13/06/2025 Versão 1.0 
'''

# Importar biblioteca time
# Usar o metodo sleep para pausar entre intervalos de avisos
from time import sleep

LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500
limite_saque = 0
quantidade_saque = 0
exibir_quantidade_saque = 3
saldo_conta = 0.00
extrato = ""

# Loop principal do sistema
while True:
    opcoes_menu = '''
    ---------- BANCO DAS NOTAS ---------
    [1] - DEPOSITAR
    [2] - SACAR
    [3] - EXTRATO
    [0] - SAIR
    -------------------------
    Selecione uma das opções acima!
    '''

    print(opcoes_menu)
    print(f"Saldo atual: R${saldo_conta: .2f}" ,end="\n")

    # Tratamento de erro, caso o usuario
    # Digitar um valor do tipo String
    try:
        opcao_de_operacao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção invalida!")
        sleep(1)
        continue
    
    # Condicional 1 - Deposito
    if (opcao_de_operacao == 1):
        print("-" * 10, "DEPOSITO", "-" * 10)
        valor_deposito = float(input("Digite o valor do deposito: "))
        saldo_conta += valor_deposito
        extrato += f"\n Deposito: R${valor_deposito: .2f}"
        print(f"Você depositou na sua conta: R${valor_deposito: .2f}")
        sleep(1)
    # Condicional 2 - SAQUE
    elif (opcao_de_operacao == 2):
        print("-" * 10, "SAQUE", "-" * 10)
        print(f"Voçê só podera sacar apenas 3 vezes: {exibir_quantidade_saque} restantes!")
        print(f"Você tem um limite de saque de R${LIMITE_VALOR_SAQUE: .2f}")
        valor_saque = float(input("Digite o valor a ser sacado: "))

        # Validar os limite de saque e valor do saque
        if (quantidade_saque < LIMITE_SAQUE):
            if (limite_saque < LIMITE_VALOR_SAQUE):
                quantidade_saque += 1
                limite_saque += valor_saque
                exibir_quantidade_saque -= 1
                if (saldo_conta >= valor_saque):
                    saldo_conta -= valor_saque
                    extrato += f"\n Saque: R${valor_saque}"
                    print(f"Você acabou de sacar: R${valor_saque}")
                    sleep(1)
                else:
                    print("Saldo Insuficiente!")
                    sleep(1)
            else:
                print("Limite de valor do saque atingido!")
                sleep(1)
        else:
            print("Limite de saque atingido!")
            sleep(1)
    # Condicional 3 - Extrato
    elif (opcao_de_operacao == 3):
        if (extrato != ""):
            print("-" * 10, "Extrato", "-" * 10)
            print(f"{extrato} \n Saldo atual: R${saldo_conta}")
            sleep(3)
        else:
            print("Não foram realizadas movimentações!")
            sleep(1)
    # Condicional 0 - Encerrar
    elif (opcao_de_operacao == 0):
        print("\nObrigado por usar nossos serviços !...")
        sleep(1)
        break
    else:
        print("Algo deu errado. Tente novamente!")
