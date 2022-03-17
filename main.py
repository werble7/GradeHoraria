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


if __name__ == '__main__':

    disciplinas = []
    entrada = input()
    tiposTurno = "MTN"

    while entrada != "Hasta la vista, beibe!":

        verificaErro = trataErro(entrada)
        if verificaErro == "erro":
            erro(entrada)
        elif verificaErro == "tabela":
            tabela()
        else:
            operacao, disciplina, horario = entrada.split(" ", 3)
            print(operacao)
            print(disciplina)
            print(horario)

            turno = detectaTurno(horario)
            print(turno)

        entrada = input()
