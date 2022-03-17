def tabela():
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab']
    print("+" + "-"*15 + ("+" + "-"*10)*6 + "+")
    print("|" + " "*15 + "|", end="")
    for i in range(6):
        print(" " + dias[i] + " "*6 + "|", end="")
    print("")
    print("+" + "-" * 15 + ("+" + "-" * 10) * 6 + "+")
    for j in range(quantidadeLinhas()):
        print("|" + " " + str(grade[j][1]) + " "*(14 - len(str(grade[j][1]))) + ("|" + " "*10)*6 + "|")
        print("+" + "-" * 15 + ("+" + "-" * 10) * 6 + "+")


def erro(mensagem):
    print("!(" + mensagem + ")")


def detectaTurno(horario):
    listaDias = []
    posicao = -1
    for i in range(3):
        posicao = horario.find(tiposTurno[i])
        if posicao != -1:
            for j in range(posicao):
                listaDias.append(int(horario[j]))
            listaDias.append(tiposTurno[i])
            listaDias.append(posicao)
            return listaDias
            #return tiposTurno[i] + str(posicao)
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


def excluiDisciplina(pDisciplina, pHorario):
    for i in range(len(grade)):
        if grade[i][0] == pDisciplina and grade[i][1] == pHorario:
            grade[i][0] = 0
            grade[i][1] = 0
            atualizaDisciplina()


def atualizaDisciplina():
    for i in range(len(grade) - 1):
        j = i + 1
        if grade[i][0] == 0 and grade[i][1] == 0 and grade[j][0] != 0 and grade[j][1] != 0:
            grade[i][0], grade[i][1] = grade[j][0], grade[j][1]
            grade[j][0] = 0
            grade[j][1] = 0


def quantidadeLinhas():
    cont = 0
    for i in range(len(grade)):
        if grade[i][0] != 0 and grade[i][1] != 0:
            cont += 1
    return cont


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
            tabela()
        else:
            operacao, disciplina, horario = entrada.split(" ", 2)
            #print(operacao)
            #print(disciplina)
            #print(horario)
            turnos = horario.split()
            print("----------------")
            if operacao == "+":
                for i in range(len(turnos)):
                    incluiDisciplina(disciplina, turnos[i], ctRegistro)
                    ctRegistro += 1
            elif operacao == "-":
                excluiDisciplina(disciplina, horario)
            for i in range(len(turnos)):
                print(turnos[i], " ", detectaTurno(turnos[i]))

        entrada = input()
