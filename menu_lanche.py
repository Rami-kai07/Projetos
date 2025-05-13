opçao = 0
while opçao != 5:
    print("====MENU====")
    print("1-Hamburguer")
    print("2-Pizza")
    print("3-Refrigerante")
    print("4-Salada")
    print("5-Sair")
    opçao= int(input("Escolha uma opção: "))
    if opçao==1:
        print("Você escolheu Hamburguer.")
    elif opçao==2:
        print("Você escolheu Pizza.")
    elif opçao==3:
        print("Você escolheu Refrigerante.")
    elif opçao==4:
        print("Você escolheu Salada.")
    elif opçao==5:
        print("Finalizou o pedido.")
        break