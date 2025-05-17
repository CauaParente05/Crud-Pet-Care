import os
import funcoes
import time
import sys

def dataFormatada(data):
    return data.replace("/", "")
def menu_eventos():
        print("-="*12,)
        print('MENU CUIDADOS COM O PET')
        print("-="*12,)
        print('1. Adicionar eventos (Vacina/Consulta/Rémedio)')
        print('2. Visualizar eventos (Vacina/Consulta/Rémedio)')
        print('3. Editar eventos (Vacina/Consulta/Rémedio)')
        print('4. Excluir eventos (Vacina/Consulta/Rémedio)')
        print('5. Para Menu Principal(adicionar Pets)')
        print('6. Para Finalizar')
        print("-="*12,)

def addEventos():
    nome = funcoes.validar_nome()
    try:
        if os.path.isfile(f"Pet_{nome}.txt"):
            data = input("Digite a data do evento (AAAA/MM/DD): ").strip()
            vacina = input("Digite a vacina do pet: ").strip()
            consulta = input("Digite o tipo de consulta: ").strip()
            data_consulta = input("Digite a data da consulta (AAAA/MM/DD): ").strip()
            nome_arquivo_evento = f"Evento_{nome}_{dataFormatada(data)}.txt"
            with open(nome_arquivo_evento, "w", encoding="UTF-8") as file:
                file.write(f"Nome: {nome}\n")
                file.write(f"Data: {data}\n")
                file.write(f"Vacina: {vacina}")
                file.write(f"Consulta: {consulta}")
                file.write(f"Data próxima Consulta: {dataFormatada(data_consulta)}")
            print(f"Evento {nome_arquivo_evento} foi registrado com sucesso!")
    except FileNotFoundError as e:        
        print(f"Este pet ainda nao foi cadastrado,{e}")


def visualizarEvento():
    nome = funcoes.validar_nome()
    data = input("Digite a data do evento (AAAA/MM/DD): ").strip()  # Solicita a data do evento

    nome_arquivo_evento = f"Evento_{nome}_{dataFormatada(data)}.txt"

    if not os.path.isfile(nome_arquivo_evento):  # verifica a existencia
        print(f"\nErro: O evento '{nome_arquivo_evento}' não foi encontrado! Verifique se digitou o nome correto.")
        return

    try:
        with open(nome_arquivo_evento, "r", encoding="UTF-8") as file:  # abre no modo leitura
            conteudo_Pet = file.read()
            print(f"\n Conteúdo do evento '{nome_arquivo_evento}':\n")
            print(conteudo_Pet)        

    except Exception as erro:  
        print(f"\n Erro ao visualizar o evento: {erro}")


def editarEvento():
    nome = input("Digite o nome do pet do evento: ").strip()
    data_evento = input("Digite a data do evento (AAAA/MM/DD): ").strip()
    nome_arquivo_evento = f"Evento_{nome}_{dataFormatada(data_evento)}.txt"

    if not os.path.isfile(nome_arquivo_evento):
        print(f"Erro: O evento '{nome_arquivo_evento}' não foi encontrado.")
        return

    try:
        with open(nome_arquivo_evento, "r", encoding="UTF-8") as file:
            linhas = file.readlines()

        # Exibir informações atuais; poderia ser um for tb
        print("\nInformações atuais do pet:")
        print(f"1. Nome: {linhas[0].split(':')[1].strip()}")
        print(f"2. Data: {linhas[1].split(':')[1].strip()}")
        print(f"3. Vacina: {linhas[2].split(':')[1].strip()}")
        print(f"4. Consulta: {linhas[3].split(':')[1].strip()}")
        print(f"5. Data próxima consulta: {linhas[4].split(':')[1].strip()}")

        print("\nDigite as novas informações (ou pressione Enter para manter o valor atual):")
        novo_nome = input(f"Nome ({linhas[0].split(': ')[1].strip()}): ").strip() or linhas[0].split(": ")[1].strip()
        nova_data = input(f"Data do evento ({linhas[1].split(': ')[1].strip()}): ").strip() or linhas[1].split(": ")[1].strip()
        nova_vacina = input(f"Vacina ({linhas[2].split(': ')[1].strip()}): ").strip() or linhas[2].split(": ")[1].strip()
        nova_consulta = input(f"Consulta ({linhas[3].split(': ')[1].strip()}): ").strip() or linhas[3].split(": ")[1].strip()
        nova_data_consulta = input(f"Data da consulta ({linhas[4].split(': ')[1].strip()}): ").strip() or linhas[4].split(": ")[1].strip()

        with open(nome_arquivo_evento, "w", encoding="UTF-8") as file:
            file.write(f"Nome: {novo_nome}\n")
            file.write(f"Data do evento: {nova_data}\n")
            file.write(f"Vacina: {nova_vacina}\n")
            file.write(f"Consulta: {nova_consulta}\n")
            file.write(f"Data da consulta: {nova_data_consulta}\n")

        print("\nEvento atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao editar o evento: {e}")

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

def escolhas_menu_eventos():
    while True:
        menu_eventos()
        time.sleep(1)
        try:
            opcao = int(input("Digite o número da opção escolhida: "))
        except ValueError:
            print("Opção inválida! Digite apenas números.")
            continue
        
        if opcao == 1:
            addEventos()
        elif opcao == 2:
            visualizarEvento()
        elif opcao == 3:
            editarEvento()
        elif opcao == 4:
            deleteEventos()
        elif opcao == 5:
            funcoes.menu_principal()
        elif opcao == 6:
            print("PROGRAMA ENCERRADO")
            sys.exit()
        else:
            print("Opção inválida! Digite o número de uma das opções exibida")