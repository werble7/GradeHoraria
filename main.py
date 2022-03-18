def tabela():
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab']
    dia = ""
    print("+" + "-"*15 + ("+" + "-"*10)*6 + "+")
    print("|" + " "*15 + "|", end="")
    for dsemana in range(6):
        print(" " + dias[dsemana] + " "*6 + "|", end="")
    print("")
    print("+" + "-" * 15 + ("+" + "-" * 10) * 6 + "+")
    for i in range(quantidadeLinhas()):
        # listaSiglas = ['M1', 'M2', 'M3', 'M4', 'M5', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'N1', 'N2', 'N3', 'N4']
        # organizaGrade()
        print("|" + " " + formatarHorarioSigla(str(grade[i][1])[1:3]) + " ", end="")
        if str(grade[i][1])[0] == "2":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = " "
        if str(grade[i][1])[0] == "3":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[i][1])[0] == "4":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[i][1])[0] == "5":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[i][1])[0] == "6":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[i][1])[0] == "7":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)) + "|")
        dia = ""
        print("+" + "-" * 15 + ("+" + "-" * 10) * 6 + "+")


def erro(mensagem):
    print("!(" + mensagem + ")")


def transformaHorario(horario):
    turnos = horario.split()
    listaDias = []
    posicao = -1

    if len(turnos) == 1:
        x = str(turnos[0])[0]
        if not(str(turnos[0])[0].isnumeric()) or x == '1' or x == '8' or x == '9' or x == '0':
            return "erro"
        elif len(str(turnos[0])) == 3:
            x = str(turnos[0])[2]
            if x == '7' or x == '8' or x == '9' or x == '0':
                return "erro"
            return turnos
        else:
            for i2 in range(3):
                posicao = str(turnos[0]).find(tiposTurno[i2])
                if posicao != -1:
                    for i3 in range(posicao):
                        for i4 in range(posicao + 1, len(str(turnos[0]))):
                            listaDias.append(str(str(turnos[0])[i3]) + str((turnos[0])[posicao]) + str(turnos[0])[i4])
                            x = str(turnos[0])[i4]
                            if x == '7' or x == '8' or x == '9' or x == '0':
                                return "erro"
                    return listaDias
    else:
        x = []
        for i5 in range(len(turnos)):
            x = transformaHorario(turnos[i5])
            for i6 in range(len(x)):
                listaDias.append(str(x[i6]))
        return listaDias
    return "erro"


def formatarHorarioNumero(turno):
    if turno[0] == "M":
        horario = int(turno[1])
    elif turno[0] == "T":
        horario = int(turno[1]) + 5
    else:
        horario = int(turno[1]) + 11
    return horario


def formatarHorarioSigla(turno):
    horario = formatarHorarioNumero(turno)

    if horario == 1:
        return "08:00 - 08:55"
    elif horario == 2:
        return "08:55 - 09:00"
    elif horario == 3:
        return "10:00 - 10:55"
    elif horario == 4:
        return "10:55 - 11:50"
    elif horario == 5:
        return "12:00 - 12:55"
    elif horario == 6:
        return "12:55 - 13:50"
    elif horario == 7:
        return "14:00 - 14:55"
    elif horario == 8:
        return "14:55 - 15:50"
    elif horario == 9:
        return "16:00 - 16:55"
    elif horario == 10:
        return "16:55 - 17:50"
    elif horario == 11:
        return "18:00 - 18:55"
    elif horario == 12:
        return "19:00 - 19:50"
    elif horario == 13:
        return "19:50 - 20:40"
    elif horario == 14:
        return "20:50 - 21:40"
    elif horario == 15:
        return "21:40 - 22:30"
    else:
        return "erro"


def atualizaRegistro(registro):
    if registro >= len(grade):
        for i7 in range(len(grade)):
            if grade[i7][0] == 0 and grade[i7][1] == 0:
                return i7
    else:
        return registro - 1


def trataEntrada(entradaerro):
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
    for i8 in range(len(grade)):
        if grade[i8][1] == pTurnos:
            return "erro"
    grade[pRegistro][0] = pDisciplina
    grade[pRegistro][1] = pTurnos


def excluiDisciplina(pDisciplina, pHorario):
    for i9 in range(len(grade)):
        if grade[i9][0] == pDisciplina and grade[i9][1] == pHorario:
            grade[i9][0] = 0
            grade[i9][1] = 0
            atualizaDisciplina()
            return
    return "erro"


def atualizaDisciplina():
    for i10 in range(len(grade) - 1):
        j = i10 + 1
        if grade[i10][0] == 0 and grade[i10][1] == 0 and grade[j][0] != 0 and grade[j][1] != 0:
            grade[i10][0], grade[i10][1] = grade[j][0], grade[j][1]
            grade[j][0] = 0
            grade[j][1] = 0


def quantidadeLinhas():
    cont = 0
    for i11 in range(len(grade)):
        if grade[i11][0] != 0 and grade[i11][1] != 0:
            cont += 1
    return cont


def imprime():
    for i12 in range(len(grade)):
        if grade[i12][0] != 0:
            print(grade[i12][0], "-", grade[i12][1])


if __name__ == '__main__':

    ctRegistro = 0                                                  # coluna 0 - disciplina coluna 1 - turnos
    grade = [[0 for _ in range(2)] for _ in range(108)]
    entrada = input()
    tiposTurno = "MNT"

    while entrada != "Hasta la vista, beibe!":

        verificaErro = trataEntrada(entrada)
        if verificaErro == "erro":
            erro(entrada)
        elif verificaErro == "tabela":
            tabela()
        else:
            operacao, disciplina, horario = entrada.split(" ", 2)

            if len(disciplina) > 8:
                erro(entrada)
            if transformaHorario(horario) == "erro":
                erro(entrada)
            turnos = transformaHorario(horario)
            print("----------------")

            if operacao == "+" and transformaHorario(horario) != "erro" and len(disciplina) < 9:
                for i13 in range(len(turnos)):
                    if incluiDisciplina(disciplina, turnos[i13], ctRegistro) == "erro":
                        erro(entrada)
                    else:
                        ctRegistro += 1
            elif operacao == "-":
                if excluiDisciplina(disciplina, horario) == "erro":
                    erro(entrada)
                else:
                    ctRegistro = atualizaRegistro(ctRegistro)

            print(ctRegistro)
            print("-----------------")
            for i14 in range(len(grade)):
                print(grade[i14][0] + grade[i14][1])

        entrada = input()
