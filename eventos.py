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
    try:
        if os.path.isfile(f"Pet{nome}.txt"):
            data = input("Digite a data do evento: ")
            vacina = input("Digite a vacina do pet: ")
            consulta = input("Digite o tipo de consulta: ")
            data_consulta = input("Digite a data da consulta: ")
            with open(f"Evento{nome}{dataFormatada(data)}.txt", "w", encoding="UTF-8") as file:
                file.write(f"Nome: {nome}\n")
                file.write(f"data: {data}\n")
                file.write(f"vacina: {vacina}")
                file.write(f"consulta: {consulta}")
                file.write(f"Data Formada: {dataFormatada(data_consulta)}")
    except FileNotFoundError as e:        
        print(f"Este pet ainda nao foi cadastrado,{e}")
def editaEventos():
    nome = input("Digite o nome do pet que você deseja editar o evento: ")
def data_para_numero(data):
    partes = data.split("/")
    return int(partes[2] + partes[1] + partes[0])   
def eventosNaSemana():
    hoje = input("Digite a data de hoje (DD/MM/AAAA): ")
    hoje_num = data_para_numero(hoje)
    semana_futura_num = hoje_num + 7 
    eventos_encontrados = []
    for arquivo in os.listdir():
        if arquivo.startswith("Evento") and arquivo.endswith(".txt"):
            partes = arquivo.replace("Evento", "").replace(".txt", "").split("_")
            if len(partes) == 2:
                nome, data_evento = partes
                data_evento_num = int(data_evento)
                if hoje_num <= data_evento_num <= semana_futura_num:
                    eventos_encontrados.append((nome, data_evento))
    if eventos_encontrados:
        print("Eventos para esta semana:")
        for pet, data in eventos_encontrados:
            print(f"Pet: {pet} - Data do evento: {str(data[:2])}/{str(data[2:4])}/{str(data[4:])}")
    else:
        print("Nenhum evento programado para esta semana.")
