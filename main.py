def tabela():
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab']
    dia = ""
    print("+" + "-"*15 + ("+" + "-"*10)*6 + "+")
    print("|" + " "*15 + "|", end="")
    for dsemana in range(6):
        print(" " + dias[dsemana] + " "*6 + "|", end="")
    print("")
    print("+" + "-" * 15 + ("+" + "-" * 10) * 6 + "+")
    for j in range(quantidadeLinhas()):
        #print("|" + " " + str(grade[j][1]) + " "*(14 - len(str(grade[j][1]))) + ("|" + str(grade[j][0]) + " "*(10 - len(str(grade[j][0]))))*6 + "|")
        print("|" + " " + str(grade[j][1]) + " " * (14 - len(str(grade[j][1]))), end="")
        if str(grade[j][1])[0] == "2":
            dia = str(grade[j][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[j][1])[0] == "3":
            dia = str(grade[j][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[j][1])[0] == "4":
            dia = str(grade[j][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[j][1])[0] == "5":
            dia = str(grade[j][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[j][1])[0] == "6":
            dia = str(grade[j][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[j][1])[0] == "7":
            dia = str(grade[j][0])
        print("| " + dia + " " * (9 - len(dia)))
        dia = ""
        print("+" + "-" * 15 + ("+" + "-" * 10) * 6 + "+")


def erro(mensagem):
    print("!(" + mensagem + ")")


def detectaTurno(horario):
    listaDias = []
    posicao = -1
    turnos = horario.split()

    if len(turnos) >= 1:
        for i in range(len(turnos)):
            if not(turnos[i][0].isnumeric()):
                return "erro"
    if not(horario[0].isnumeric()):
        return "erro"
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

def transformaHorario(horario):
    turnos = []
    turnos = horario.split()
    listaDias = []
    posicao = -1

    if len(turnos) == 1:
        if not(str(turnos[0])[0].isnumeric()):
            return "erro"
        elif len(str(turnos[0])) == 3:
            return turnos
        else:
            for i in range(3):
                posicao = str(turnos[0]).find(tiposTurno[i])
                if posicao != -1:
                    for j in range(posicao):
                        # listaDias.append(str(str(turnos[0])[j]) + str((turnos[0])[posicao]) + str(str(turnos[0])[posicao]))
                        for k in range(posicao + 1, len(str(turnos[0]))):
                            listaDias.append(str(str(turnos[0])[j]) + str((turnos[0])[posicao]) + str(str(turnos[0])[k]))
                    return listaDias
                        #listaDias[j] = str(str(turnos[0])[j])
                    #return listaDias

    return "erro"


#def detectaDisciplina(entrada):
    #operacao, disciplina, horario = entrada.split()


def atualizaRegistro(registro):
    if registro >= len(grade):
        for i in range(len(grade)):
            if grade[i][0] == 0 and grade[i][1] == 0:
                return i
    else:
        return registro - 1


def trataErro(entradaerro):
    if entradaerro == "":
        return "erro"
    elif entradaerro[0] != "+" and entradaerro[0] != "-" and entradaerro[0] != "?":
        return "erro"
    elif entradaerro[0] != "?" and entradaerro[1] != " ":
        return "erro"
    elif entradaerro[0] == "?" and len(entradaerro) > 1:
        return "erro"
    elif entradaerro[0] == "?":
        return "tabela"
    return


def incluiDisciplina(pDisciplina, pTurnos, pRegistro):
    for i in range(len(grade)):
        if grade[i][1] == pTurnos:
            return "erro"
    grade[pRegistro][0] = pDisciplina
    grade[pRegistro][1] = pTurnos


def excluiDisciplina(pDisciplina, pHorario):
    for i in range(len(grade)):
        if grade[i][0] == pDisciplina and grade[i][1] == pHorario:
            grade[i][0] = 0
            grade[i][1] = 0
            atualizaDisciplina()
            return
    return "erro"


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
    tiposTurno = "MNT"

    while entrada != "Hasta la vista, beibe!":

        verificaErro = trataErro(entrada)
        if verificaErro == "erro":
            erro(entrada)
        elif verificaErro == "tabela":
            tabela()
        else:
            operacao, disciplina, horario = entrada.split(" ", 2)

            if transformaHorario(horario) == "erro":
                erro(entrada)
            #print(operacao)
            #print(disciplina)
            #print(horario)
            turnos = transformaHorario(horario)
            print("----------------")

            if operacao == "+" and transformaHorario(horario) != "erro":
                for i in range(len(turnos)):
                    if incluiDisciplina(disciplina, turnos[i], ctRegistro) == "erro":
                    # necessita tratativa de disciplina(max.:letras)
                        erro(entrada)
                    else:
                        ctRegistro += 1
            elif operacao == "-":
                if excluiDisciplina(disciplina, horario) == "erro":
                    erro(entrada)
                else:
                    ctRegistro = atualizaRegistro(ctRegistro)

            #for i in range(len(turnos)):
                #print(turnos[i], " ", detectaTurno(turnos[i]))
            print(ctRegistro)
            print("-----------------")
            for j in range(len(grade)):
                print(grade[j][0] + grade[j][1])

        entrada = input()


