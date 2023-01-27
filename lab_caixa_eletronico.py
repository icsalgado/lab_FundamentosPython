menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#print(menu)

valor_zerado = "Deposito minimo de R$ 1.00"

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print(valor_zerado)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite =  valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiete")
        elif excedeu_limite:
            print("Valor acima do limite permitido")
        elif excedeu_saques:
            print("Quantidade de saques excedida")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print(valor_zerado)
    elif opcao == "e":
        print("Extrato")
        print("Sem moviemntacoes" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
    elif opcao == "q":
        break
    else:
        print("Opcao invalida")