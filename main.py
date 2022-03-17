def tabela():
    for linha in range(5):
        print("+----+----+----+----+")
        print("| ", end="")
        for coluna in range(4):
            print("c", end="")
            print(coluna, end="")
            print(" | ", end="")
        print("")
    print("+----+----+----+----+")


def erro(mensagem):
    print("!(" + mensagem + ")")


def detectaTurno(horario):
    posicao = -1
    for i in range(3):
        posicao = horario.find(tiposTurno[i])
        if posicao != -1:
            return tiposTurno[i] + str(posicao)
    return "erro"


def detectaDisciplina(entrada):
    operacao, disciplina, horario = entrada.split()


def trataErro(entrada):
    if entrada == "":
        return "erro"
    elif entrada[0] != "+" and entrada[0] != "-" and entrada[0] != "?":
        return "erro"
    elif entrada[0] != "?" and entrada[1] != " ":
        return "erro"
    elif entrada[0] == "?" and len(entrada) > 1:
        return "erro"
    elif entrada[0] == "?":
        return "tabela"
    return


def incluiDisciplina(pDisciplina, pTurnos, pRegistro):
    grade[pRegistro][0] = pDisciplina
    grade[pRegistro][1] = pTurnos


def excluiDisciplina(pDisciplina, pTurnos):
    for i in range(len(grade)):
        if grade[i][0] == pDisciplina and grade[i][1] == pTurnos:
            grade[i][0] = 0
            grade[i][1] = 0


def imprime():
    for i in range(len(grade)):
        if grade[i][0] != 0:
            print(grade[i][0], "-", grade[i][1])


if __name__ == '__main__':

    # coluna 0 - disciplina
    # coluna 1 - turnos
    ctRegistro = 0
    grade = [[0 for _ in range(2)] for _ in range(10)]
    entrada = input()
    tiposTurno = "MTN"

    while entrada != "Hasta la vista, beibe!":

        verificaErro = trataErro(entrada)
        if verificaErro == "erro":
            erro(entrada)
        elif verificaErro == "tabela":
            imprime()
        else:
            operacao, disciplina, horario = entrada.split(" ", 2)
            #print(operacao)
            #print(disciplina)
            #print(horario)
            turnos = horario.split()
            print("----------------")
            if operacao == "+":
                incluiDisciplina(disciplina, turnos, ctRegistro)
                ctRegistro += 1
            elif operacao == "-":
                excluiDisciplina(disciplina, turnos)
            for i in range(len(turnos)):
                print(turnos[i], " ", detectaTurno(turnos[i]))

        entrada = input()

