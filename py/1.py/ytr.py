import random
import time

def saudacao():
    print("🌟 Bem-vindos, pais incríveis! 🌟")
    time.sleep(1)
    print("Hoje vocês vão jogar um jogo criado especialmente para vocês! 🎮")
    time.sleep(1)
    print("É um jogo de adivinhação... será que conseguem vencer? 😏\n")
    time.sleep(1)

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("🎯 Eu pensei em um número entre 1 e 100.")
    print("Tente adivinhar! (Digite 'sair' para desistir)\n")

    while True:
        chute = input("🔢 Seu palpite: ")

        if chute.lower() == 'sair':
            print("👋 Tudo bem! O número secreto era", numero_secreto)
            print("Mas valeu a tentativa! 😄")
            break

        if not chute.isdigit():
            print("⚠️ Opa! Isso não parece um número válido.")
            continue

        chute = int(chute)
        tentativas += 1

        if chute < numero_secreto:
            print("🔼 Muito baixo! Tente um número maior.")
        elif chute > numero_secreto:
            print("🔽 Muito alto! Tente um número menor.")
        else:
            print(f"\n🎉 UAU! Parabéns!!! Acertaram o número {numero_secreto} em {tentativas} tentativas! 🏆")
            if tentativas <= 5:
                print("💡 Vocês são gênios! Isso foi rápido demais!")
            elif tentativas <= 10:
                print("👏 Excelente! Boa estratégia!")
            else:
                print("😅 Ufa! Mas o que importa é que conseguiram!")
            break

    print("\n❤️ Obrigado por jogarem! Com amor, do programador da casa. 🧠💻")

if __name__ == "__main__":
    saudacao()
    jogar()
