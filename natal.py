#Aluno: Gustavo Donato - Questão: "Desviando de arvores de natal"

#numero de rodadas que o usuario iria jogar
rodadas = int(input("digite a quantidade de rodadas que deseja jogar:"))

#explicação para dar complemento ao codigo
print("0 representa o espaço que pode ser passado e 1 o obstaculo")

#aqui eu difini uma variavel como zero para ir acrecentando os movimentos

mover = 0

#comecei um laço de repetição com while

while rodadas:

    #criei inputs para a entrada das variaveis

    p = int(input("\nlinha da esquerda"))
    c = int(input("\nlinha do centro"))
    r = int(input("\nlinha da direita"))

    #aqui é uma sequencia se ifs e elifs para identificar se ele realiza um movimento ou não
    #para ele fzr um movimento eu setei quando ele faria um movimento, basicamento tadas as vezes em que possuise um obstaculo ele mudaria de lugar, a fim de desviar do obstaculo, caso todos os lugares tivessem obstaculos, seria um "game over"

    if p == 1 and c == 1 and r == 1:
        print("\ntodos os lugares possuem obstaculos, voce perdeu")
        break

    elif p == 0 and c == 0 and r == 0:
        mover += 0

    elif p == 1 and c == 0 and r == 0:
        print("realizou um movimento")
        mover += 1

    elif p == 1 and c == 1 and r == 0:
        print("realizou um movimento")
        mover += 1

    elif p == 1 and c == 0 and r == 1:
        print("realizou um movimento")
        mover += 1

    elif p == 0 and c == 0 and r == 0:
        print("realizou um movimento")
        mover += 1

    elif p == 0 and c == 1 and r == 1:
        print("realizou um movimento")
        mover += 1

    elif p == 0 and c == 1 and r == 0:
        print("realizou um movimento")
        mover += 1

    #aqui é uma variavel para parar o código
    pare = int(input("\ndigite 0 para parar, ou qualquer outra coisa para continuar"))

    if pare == 0:
        break

#aqui mostra a quantidade de movimentos realizados, fiz isso somando todas a vezes os movimentos
print("\nesta é a quantidade de movimentos realizados:", mover)


