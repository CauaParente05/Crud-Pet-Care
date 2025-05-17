import os
# RASCUNHO MONITORIA


def add_pet():
    nome = input("Digite o nome do pet: ")
    try:
        idade = int(input("Digite a idade do pet: "))
    except ValueError as e:
        print(f"Digite uma idade valida! (Erro: {e})")

    with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
        file.write(f"Nome: {nome}\n")
        file.write(f"Idade: {idade}")


def data_formatada(data):
    return data.replace("/", "")


def add_eventos():
    nome = input("Digite o nome do pet que você deseja realizar o evento: ")

    if os.path.isfile(f"Pet{nome}.txt"):
        data = input("Digite a data do evento: ")
        vacina = input("Digite a vacina do pet: ")
        with open(f"Evento{nome}{data_formatada(data)}.txt", "w", encoding="UTF-8") as file:
            file.write(f"Nome: {nome}\n")
            file.write(f"data: {data}\n")
            file.write(f"vacina: {vacina}")
    else:
        print("Este pet ainda nao foi cadastrado")


# add_pet()
add_eventos()
