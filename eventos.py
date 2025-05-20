import os
import menu_principal
import cuidados
import time
import sys
import datetime


def data_formatada(data):
    return data.replace("/", "")

def validar_vacina():
    while True:
        vacina = input("Digite a vacina do pet: ").strip()

        if vacina.isalpha():  # isalpha verifica se a string contém apenas letras
            return vacina
        else:
            print("Erro: O campo de vacina deve conter apenas letras! Tente novamente.")

def validar_consulta():
    while True:
        consulta = input("Digite o tipo de consulta: ").strip()

        if consulta.isalpha():  # isalpha verifica se a string contém apenas letras
            return consulta
        else:
            print("Erro: O campo de consulta deve conter apenas letras! Tente novamente.")

def formatar_data_para_visualizacao(data):
    return f"{data[:4]}/{data[4:6]}/{data[6:]}"

def valida_data(data):
    try:
        # Verifica se a data está correta
        datetime.datetime.strptime(data, "%Y/%m/%d")
        return True
    except ValueError:
        return False


def solicitar_data():
    while True:
        data = input("Digite a data do evento (AAAA/MM/DD): ").strip()
        if valida_data(data):
            return data
        else:
            print(
                "Formato de data inválido! Tente novamente no formato correto (AAAA/MM/DD).")
            
def solicitar_data_consulta():
    while True:
        data = input("Digite a data da próxima consulta (AAAA/MM/DD): ").strip()
        if valida_data(data):
            return data
        else:
            print(
                "Formato de data inválido! Tente novamente no formato correto (AAAA/MM/DD).")

def menu_eventos():
    print("-="*20,)
    print('MENU CUIDADOS COM O PET')
    print("-="*20,)
    print('1. Adicionar eventos (Vacina/Consulta/Rémedio)')
    print('2. Visualizar eventos (Vacina/Consulta/Rémedio)')
    print('3. Editar eventos (Vacina/Consulta/Rémedio)')
    print('4. Excluir eventos (Vacina/Consulta/Rémedio)')
    print('5. Para Menu Principal')
    print('6. Para Menu de Cuidados')
    print('7. Para Finalizar')
    print("-="*20,)


def add_eventos():
    nome = menu_principal.validar_nome()
    try:
        if os.path.isfile(f"Pet{nome}.txt"):
            data = solicitar_data()
            vacina = validar_vacina()
            consulta = validar_consulta()
            data_consulta = solicitar_data_consulta()
            nome_arquivo_evento = f"Evento_{nome}_{data_formatada(data)}.txt"
            with open(nome_arquivo_evento, "w", encoding="UTF-8") as file:
                file.write(f"Nome: {nome}\n")
                file.write(f"Data: {data_formatada(data)}\n")
                file.write(f"Vacina: {vacina}\n")
                file.write(f"Consulta: {consulta}\n")
                file.write( f"Data para a próxima Consulta: {data_formatada(data_consulta)}\n")

        print(f"Evento {nome_arquivo_evento} foi registrado com sucesso!")
    except FileNotFoundError as e:
        print(f"Este pet ainda nao foi cadastrado,{e}")


def visualizar_evento():
    nome = menu_principal.validar_nome()
    data = solicitar_data()  # Solicita a data do evento
    if not data:
        return

    nome_arquivo_evento = f"Evento_{nome}_{data_formatada(data)}.txt"

    if not os.path.isfile(nome_arquivo_evento):  # verifica a existencia
        print(
            f"\nErro: O evento '{nome_arquivo_evento}' não foi encontrado! Verifique se digitou o nome correto.")
        return

    try:
        with open(nome_arquivo_evento, "r", encoding="UTF-8") as file:  # abre no modo leitura
            linhas = file.readlines()

        print(f"\nConteúdo do evento '{nome_arquivo_evento}':\n")
        print(f"1. Nome: {linhas[0].split(':')[1].strip()}")
        print(
            f"2. Data: {formatar_data_para_visualizacao(linhas[1].split(':')[1].strip())}")
        print(f"3. Vacina: {linhas[2].split(':')[1].strip()}")
        print(f"4. Consulta: {linhas[3].split(':')[1].strip()}")
        print(
            f"5. Data próxima consulta: {formatar_data_para_visualizacao(linhas[4].split(':')[1].strip())}")

    except Exception as erro:
        print(f"\n Erro ao visualizar o evento: {erro}")


def editar_evento():
    nome = input("Digite o nome do pet do evento: ").strip()
    data_evento = solicitar_data()
    if not data_evento:
        return
    nome_arquivo_evento = f"Evento_{nome}_{data_formatada(data_evento)}.txt"

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

        print(
            "\nDigite as novas informações (ou pressione Enter para manter o valor atual):")
        novo_nome = input(f"Nome ({linhas[0].split(': ')[1].strip()}): ").strip(
        ) or linhas[0].split(": ")[1].strip()
        nova_data = input(f"Data do evento ({linhas[1].split(': ')[1].strip()}): ").strip(
        ) or linhas[1].split(": ")[1].strip()
        nova_vacina = input(f"Vacina ({linhas[2].split(': ')[1].strip()}): ").strip(
        ) or linhas[2].split(": ")[1].strip()
        nova_consulta = input(f"Consulta ({linhas[3].split(': ')[1].strip()}): ").strip(
        ) or linhas[3].split(": ")[1].strip()
        nova_data_consulta = input(f"Data da consulta ({linhas[4].split(': ')[1].strip()}): ").strip(
        ) or linhas[4].split(": ")[1].strip()

        with open(nome_arquivo_evento, "w", encoding="UTF-8") as file:
            file.write(f"Nome: {novo_nome}\n")
            file.write(f"Data do evento: {nova_data}\n")
            file.write(f"Vacina: {nova_vacina}\n")
            file.write(f"Consulta: {nova_consulta}\n")
            file.write(f"Data da consulta: {nova_data_consulta}\n")

        print("\nEvento atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao editar o evento: {e}")


def delete_eventos():
    nome = menu_principal.validar_nome()
    data_evento = solicitar_data()
    if not data_evento:
        return

    nome_arquivo_evento = f"Evento_{nome}_{data_formatada(data_evento)}.txt"

    if not os.path.isfile(nome_arquivo_evento):
        print(f"Erro: O evento '{nome_arquivo_evento}' não foi encontrado.")
        return

    try:
        os.remove(nome_arquivo_evento)
        print(f"Evento '{nome_arquivo_evento}' foi deletado com sucesso!")
    except FileNotFoundError as erro:
        print(f"Erro ao excluir evento: {erro}")


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
            add_eventos()
        elif opcao == 2:
            visualizar_evento()
        elif opcao == 3:
            editar_evento()
        elif opcao == 4:
            delete_eventos()
        elif opcao == 5:
            menu_principal.escolhas_menu()
        elif opcao == 6:
            cuidados.escolhas_menu_cuidados()
        elif opcao == 7:
            print("PROGRAMA ENCERRADO")
            sys.exit()
        else:
            print("Opção inválida! Digite o número de uma das opções exibida")
