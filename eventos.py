ARQUIVO_PETS = "pets.txt"
ARQUIVOS_EVENTOS = "eventos.txt"
import os
#date.time
def dataFormatada(data):
    return data.replace("/", "")
def menu_cuidados():
    while True:
        print("-="*12,)
        print('MENU CUIDADOS COM O PET')
        print("-="*12,)
        print('1. Adicionar eventos (Vacina/Consulta/Rémedio)')
        print('2. Visualizar eventos (Vacina/Consulta/Rémedio)')
        print('3. Editar eventos (Vacina/Consulta/Rémedio)')
        print('4. Excluir eventos (Vacina/Consulta/Rémedio)')
        print('5. Para Menu Principal(adicionar Pets)')
def addEventos():
    nome = input("Digite o nome do pet que você deseja realizar o evento: ")

    if os.path.isfile(f"Pet{nome}.txt"):
        data = input("Digite a data do evento: ")
        vacina = input("Digite a vacina do pet: ")
        with open(f"Evento{nome}{dataFormatada(data)}.txt", "w", encoding="UTF-8") as file:
            file.write(f"Nome: {nome}\n")
            file.write(f"data: {data}\n")
            file.write(f"vacina: {vacina}")
    else:
        print("Este pet ainda nao foi cadastrado")