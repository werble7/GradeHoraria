def tabela():
    dias = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab']
    dia = ""
    print("+" + "-"*15 + ("+" + "-"*10)*6 + "+")
    print("|" + " "*15 + "|", end="")
    for dsemana in range(6):
        print(" " + dias[dsemana] + " "*6 + "|", end="")
    print("")
    print("+" + "-" * 15 + ("+" + "-" * 10) * 6 + "+")
    for i in range(15):
        if grade[i][1] == 0 and grade[i+15][1] == 0 and grade[i+30][1] == 0 and grade[i+45][1] == 0 and grade[i+60][1] == 0 and grade[i+75][1] == 0:
            continue
        print("|" + " " + formatarHorarioSigla(str(grade[i][1])[1:3]) + " ", end="")
        if str(grade[i][1])[0] == "2":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = " "
        if str(grade[i+15][1])[0] == "3":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[i+30][1])[0] == "4":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[i+45][1])[0] == "5":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[i+60][1])[0] == "6":
            dia = str(grade[i][0])
        print("| " + dia + " " * (9 - len(dia)), end="")
        dia = ""
        if str(grade[i+75][1])[0] == "7":
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
            letra = str(turnos[0])[1]
            if letra == "M":
                hora = str(turnos[0])[2]
                if hora == '6' or hora == '7' or hora == '8' or hora == '9' or hora == '0':
                    return "erro"
            elif letra == "T":
                hora = str(turnos[0])[2]
                if hora == '7' or hora == '8' or hora == '9' or hora == '0':
                    return "erro"
            elif letra == "N":
                hora = str(turnos[0])[2]
                if hora == '5' or hora == '6' or hora == '7' or hora == '8' or hora == '9' or hora == '0':
                    return "erro"
            else:
                return "erro"
            return turnos
        else:
            for i2 in range(3):
                posicao = str(turnos[0]).find(tiposTurno[i2])
                if posicao != -1:
                    for i3 in range(posicao):
                        for i4 in range(posicao + 1, len(str(turnos[0]))):
                            x = str(str(turnos[0])[i3]) + str((turnos[0])[posicao]) + str(turnos[0])[i4]
                            if transformaHorario(x) != "erro":
                                listaDias.append(x)
                            else:
                                return "erro"
                    return listaDias
    else:
        x = []
        for i5 in range(len(turnos)):
            x = transformaHorario(turnos[i5])
            if x == "erro":
                return "erro"
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


def defineRegistro(pturnos):
    x = 0
    if str(pturnos)[0] == "3":
        x = 15
    elif str(pturnos)[0] == "4":
        x = 30
    elif str(pturnos)[0] == "5":
        x = 45
    elif str(pturnos)[0] == "6":
        x = 60
    elif str(pturnos)[0] == "7":
        x = 75
    if str(pturnos)[1] == "M":
        x += 0
    elif str(pturnos)[1] == "T":
        x += 5
    elif str(pturnos)[1] == "N":
        x += 11
    if str(pturnos)[2] == "1":
        x += 0
    if str(pturnos)[2] == "2":
        x += 1
    if str(pturnos)[2] == "3":
        x += 2
    if str(pturnos)[2] == "4":
        x += 3
    if str(pturnos)[2] == "5":
        x += 4
    if str(pturnos)[2] == "6":
        x += 5
    return x


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
            return
    return "erro"


'''
def imprime():
    for i12 in range(len(grade)):
        if grade[i12][0] != 0:
            print(grade[i12][0], "-", grade[i12][1])
'''


if __name__ == '__main__':

    ctRegistro = 0                                                  # coluna 0 - disciplina;coluna 1 - turnos
    grade = [[0 for _ in range(2)] for _ in range(90)]
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

            if operacao == "+" and turnos != "erro" and len(disciplina) < 9:
                for i13 in range(len(turnos)):
                    registro = defineRegistro(turnos[i13])
                    if incluiDisciplina(disciplina, turnos[i13], registro) == "erro":
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
                print(str(grade[i14][0]) + str(grade[i14][1]))

        entrada = input()
