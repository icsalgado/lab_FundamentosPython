import os #biblioteca para ajudar a limpar a tela
import time #biblioteca para implementar um timeout, só funciona em unix

#41
cabecalho_menu = """
    ===== SISTEMA BANCARIO GENERICO =====
"""

menu = """
    [1] Deposito                Saque [2]
    [3] Extrato                  Sair [4]

    =====================================

Teclado => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#print(menu)

erro = " OPERACAO NAO CONCLUIDA "
fecha_bloco = ""
sucesso = " OPERACAO CONCLUIDA COM SUCESSO "

while True:
    os.system('clear') or None #Isso limpa a tela
    print(cabecalho_menu)
    print((f"Saldo: R$ {saldo:.2f}").center(41, " "))
    opcao = input(menu)

    if opcao == "1":
        os.system('clear') or None
        print((" DEPOSITO ").center(41, "=") + "\n")

        try:
            valor = float(input("valor do deposito:\n=> "))
        except:
            os.system('clear') or None
            print(erro.center(41, "="))
            print("\n" + ("Entrada invalida para deposito de valores").center(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3)
            continue

        if valor > 0:
            saldo += valor
            extrato += (f"\n [+] Deposito: R$ {valor:.2f}\n" + (f"Saldo na data: R$ {saldo:.2f}").rjust(41, " "))
            os.system('clear') or None
            print(sucesso.center(41, "="))
            print("\n" + (f"R$ {valor} depositado").rjust(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3)
        else:
            os.system('clear') or None
            print(erro.center(41, "="))
            print("\n" + ("Deposito minimo R$ 1.00").center(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3) #trava a execução em segundos no unix - OBS windows não deve funcionar
    elif opcao == "2":
        os.system('clear') or None
        print((" SAQUE ").center(41, "=") + "\n")
        print((f"Saldo: R$ {saldo:.2f}").rjust(41, " "))
        
        try:
            valor = float(input("valor do saque:\n=> "))
        except:
            os.system('clear') or None
            print(erro.center(41, "="))
            print("\n" + ("Entrada invalida para saque de valores").center(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3)
            continue

        excedeu_saldo = valor > saldo
        excedeu_limite =  valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            os.system('clear') or None
            print(erro.center(41, "="))
            print("\n" + ("Saldo Insuficiete!").center(41, " "))
            print((f"Valor Disponivel R$: {saldo:.2f}").center(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3)
        elif excedeu_limite:
            os.system('clear') or None
            print(erro.center(41, "="))
            print("\n" + ("Saque acima do limite permitido!").center(41, " "))
            print((f"Limite atual R$: {limite:.2f}").center(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3)
        elif excedeu_saques:
            os.system('clear') or None
            print(erro.center(41, "="))
            print("\n" + ("Limite de quantidade de saques excedido!").center(41, " "))
            print((f"Limite atual de saques: {numero_saques}").center(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3)
        elif valor > 0:
            saldo -= valor
            extrato += (f"\n [-] Saque: R$ {valor:.2f}\n" + (f"Saldo na data: R$ {saldo:.2f}").rjust(41, " "))
            numero_saques += 1
            os.system('clear') or None
            print(sucesso.center(41, "="))
            print("\n" + (f"R$ {valor:.2f} sacado").rjust(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3)
        else:
            os.system('clear') or None
            print(erro.center(41, "="))
            print("\n" + ("Valor invalido para saque").center(41, " ") + "\n")
            print(fecha_bloco.center(41, "="))
            time.sleep(3)
    elif opcao == "3":
        os.system('clear') or None
        print((" EXTRATO ").center(41, "="))
        print((f"Saldo: R$ {saldo:.2f}").rjust(41, " "))
        print("\nSem movimentacoes\n" if not extrato else extrato)
        print(fecha_bloco.center(41, "="))
        time.sleep(5)
    elif opcao == "4":
        os.system('clear') or None
        print(cabecalho_menu)
        print((" OBRIGADO PELA PREFERENCIA, ATE LOGO ").rjust(41, " "))
        print("\n    " + (fecha_bloco.center(37, "=")))
        time.sleep(3)
        os.system('clear') or None
        break
    else:
        os.system('clear') or None
        print(erro.center(41, "="))
        print("\n" + ("Digite apenas os numeros do menu").center(41, " ") + "\n")
        print(fecha_bloco.center(41, "="))
        time.sleep(3)
