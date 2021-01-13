from random import randrange


def jogar():
    print("********** Jokenpô **********")

    valores = ["PEDRA", "PAPEL", "TESOURA"]

    nome = str(input("Digite o seu nome: ")).strip()

    ganhou = False
    perdeu = False
    pontuacao_maquina = 0
    pontuacao_usuario = 0

    while not ganhou and not perdeu:

        numero = randrange(0, len(valores))
        escolha_maquina = valores[numero]

        print(f"{nome} {pontuacao_usuario} X {pontuacao_maquina} Máquina")
        print("[ 0 ] PEDRA")
        print("[ 1 ] PAPEL")
        print("[ 2 ] TESOURA")

        escolha_valor = int(input("Digite a sua escolha: "))
        escolha_usuario = None

        if escolha_valor not in range(0, 3):
            print("Escolha Inválida!\n")

        else:
            for _ in valores:
                escolha_usuario = valores[escolha_valor]

            if escolha_valor == numero:
                print(f"Máquina escolheu {escolha_maquina}")
                print(f"{nome} escolheu {escolha_usuario}")
                print("Empate!\n")

            elif escolha_valor == 0 and numero == 1:
                print(f"Máquina escolheu {escolha_maquina}")
                print(f"{nome} escolheu {escolha_usuario}")
                print("Ponto para máquina!\n")
                pontuacao_maquina += 1

            elif escolha_valor == 0 and numero == 2:
                print(f"Máquina escolheu {escolha_maquina}")
                print(f"{nome} escolheu {escolha_usuario}")
                print(f"Ponto para {nome}!\n")
                pontuacao_usuario += 1

            elif escolha_valor == 1 and numero == 0:
                print(f"Máquina escolheu {escolha_maquina}")
                print(f"{nome} escolheu {escolha_usuario}")
                print(f"Ponto para {nome}!\n")
                pontuacao_usuario += 1

            elif escolha_valor == 1 and numero == 2:
                print(f"Máquina escolheu {escolha_maquina}")
                print(f"{nome} escolheu {escolha_usuario}")
                print("Ponto para máquina!\n")
                pontuacao_maquina += 1

            elif escolha_valor == 2 and numero == 0:
                print(f"Máquina escolheu {escolha_maquina}")
                print(f"{nome} escolheu {escolha_usuario}")
                print("Ponto para máquina!\n")
                pontuacao_maquina += 1

            elif escolha_valor == 2 and numero == 1:
                print(f"Máquina escolheu {escolha_maquina}")
                print(f"{nome} escolheu {escolha_usuario}")
                print(f"Ponto para {nome}!\n")
                pontuacao_usuario += 1

        ganhou = pontuacao_usuario == 10
        perdeu = pontuacao_maquina == 10

    if ganhou:
        print("Você venceu!")
        print("Placar final:")
        print(f"{nome} {pontuacao_usuario} X {pontuacao_maquina} Máquina")
    else:
        print("Você perdeu!")
        print("Placar final:")
        print(f"{nome} {pontuacao_usuario} X {pontuacao_maquina} Máquina")


if __name__ == "__main__":
    jogar()
