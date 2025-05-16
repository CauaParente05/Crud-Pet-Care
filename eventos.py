import os
import funcoes
import time
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
    nome = funcoes.validar_nome()
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

def deleteEventos():
    nome = funcoes.validar_nome()
    arquivo = f"Pet{nome}.txt"
    try:
        if os.path.isfile(arquivo):
            os.remove(f"Pet{nome}.txt")
            print(f"Arquivo 'Pet{nome}.txt' foi deletado com sucesso!")
        else:
            print(f"Nome do pet inválido! O arquivo '{arquivo}' não foi encontrado.")
    except FileNotFoundError as erro:
        print(f"Arquivo não encontrado! (Erro: {erro})")

def escolhas_menu():
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
            continue
        elif opcao == 3:
            continue
        elif opcao == 4:
            deleteEventos()
        elif opcao == 5:
            print("PROGRAMA ENCERRADO")
            break
        elif opcao == 6:
            funcoes.menu_principal
        else:
            print("Opção inválida!")