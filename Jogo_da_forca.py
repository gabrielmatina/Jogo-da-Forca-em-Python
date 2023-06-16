# Projeto 1 - Desenvolvimento do Jogo Forca em Python - Versão 1
# Importações
import random
from os import system, name


# Função para limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
        # Mac ou Linux
    else:
        _ = system('clear')


# Função Game
def game():

    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n!")

    # Lista de palavras
    palavras = ["abacaxi", "manga", "morango", "laranja", "melancia", "melao",
                "banana", "uva", "goiaba", "caju", "cereja", "pessego",
                "abacate", "acerola", "amora", "cacau", "caqui", "carambola",
                "cereja", "figo", "framboesa", "jabuticaba", "kiwi", "limao",
                "mamao", "maracuja", "mirtilo", "nectarina", "pera", "pitanga",
                "pitaya", "romã", "tamarindo", "tangerina", "umbu", "uvaia"]

    # Escolha aleatória da palavra
    palavra = random.choice(palavras)

    # List comprehension para criar uma lista com os caracteres da palavra
    letras_descobertas = ["_" for letra in palavra]

    # Número de chances
    chances = 6

    # lista para as letras erradas
    letras_erradas = []

    # Loop do jogo
    while chances > 0:
        # print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ".lower())

        # Condicional que verifica se a letra digitada está na palavra
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        # Condicional que verifica se o jogador ganhou
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    # Condicional que verifica se o jogador perdeu
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)


# Função Main
if __name__ == "__main__":
    game()
    print("\nFim de jogo!")
