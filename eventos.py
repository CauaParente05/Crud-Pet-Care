ARQUIVOS_EVENTOS = "eventos.txt"
import sys
import funcoes
import os
import time
#date.time
def dataFormatada(data):
    return data.replace("/", "")
def menu_cuidados():
    print("-="*12,)
    print('MENU CUIDADOS COM O PET')
    print("-="*12,)
    print('1. Adicionar eventos (Vacina/Consulta/Rémedio)')
    print('2. Visualizar eventos (Vacina/Consulta/Rémedio)')
    print('3. Editar eventos (Vacina/Consulta/Rémedio)')
    print('4. Excluir eventos (Vacina/Consulta/Rémedio)')
    print('5. Volta para o Menu Principal')
    print('6. Encerra o programa')
    print("-="*12,)
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

def escolhas_menu_eventos():
    while True:
        menu_cuidados()
        time.sleep(1)
        try:
            opcao = int(input("Digite o número da opção escolhida: "))
        except ValueError:
            print("Opção inválida! Digite apenas números.")
            continue

        if opcao == 1:
            addEventos()
        elif opcao == 2:
            eventosNaSemana() #Apenas placeHolder
        elif opcao == 3:
            editaEventos() #Apenas placeHolder
        elif opcao == 4:
            editaEventos() #Apenas placeHolder
        elif opcao == 5:
            funcoes.escolhas_menu()
            time.sleep(1)
        elif opcao == 6:
            print("PROGRAMA ENCERRADO")
            sys.exit()   
        else:
            print("Opção inválida! Digite o número de uma das opções exibida")