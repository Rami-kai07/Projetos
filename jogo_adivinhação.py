import random
numero_secreto = random.randint (1,10)
contagem_tentativas = 0
print("Bem-vindo ao Jogo da Adivinhação")
print("Tente acertar o número secreto de 1 a 10.")

while tentativas != contagem_tentativas:
    numero = int(input("Digite um número: "))
    contagem_tentativas=contagem_tentativas+1
    if numero == numero_secreto:
        print("Parabéns!!")
        print(f"vc precisou de {contagem_tentativas}")
        break
    elif numero< numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número é menor.")