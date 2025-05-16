import os
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
    nome = input("Digite o nome do pet que você deseja realizar o evento: ").strip()

    if not os.path.isfile(f"Pet{nome}.txt"):
        print(f"Erro: O pet '{nome}' ainda não foi cadastrado.")
        return

    data = input("Digite a data do evento (DD/MM/AAAA): ").strip()
    vacina = input("Digite a vacina do pet (ou 'Nenhuma' se não aplicável): ").strip()
    consulta = input("Digite o tipo de consulta (ou 'Nenhuma'): ").strip()
    data_consulta = input("Digite a data da consulta (DD/MM/AAAA) (ou 'Nenhuma'): ").strip()

    nome_arquivo_evento = f"Evento_{nome}_{dataFormatada(data)}.txt"
    
    try:
        with open(nome_arquivo_evento, "w", encoding="UTF-8") as file:
            file.write(f"Nome: {nome}\n")
            file.write(f"Data do evento: {data}\n")
            file.write(f"Vacina: {vacina}\n")
            file.write(f"Consulta: {consulta}\n")
            file.write(f"Data da consulta: {dataFormatada(data_consulta)}\n")

        print(f"Evento registrado com sucesso no arquivo: {nome_arquivo_evento}")

    except Exception as e:
        print(f"Erro ao registrar o evento: {e}")

def editarEvento():
    nome = input("Digite o nome do pet do evento: ").strip()
    data_evento = input("Digite a data do evento (DD/MM/AAAA): ").strip()
    nome_arquivo_evento = f"Evento_{nome}_{dataFormatada(data_evento)}.txt"

    if not os.path.isfile(nome_arquivo_evento):
        print(f"Erro: O evento '{nome_arquivo_evento}' não foi encontrado.")
        return

    try:
        with open(nome_arquivo_evento, "r", encoding="UTF-8") as file:
            linhas = file.readlines()

        print("\nInformações atuais do evento:")
        for linha in linhas:
            print(linha.strip())

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

        print("\n✅ Evento atualizado com sucesso!")

    except Exception as e:
        print(f"Erro ao editar o evento: {e}")


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
        editarEvento()
    elif opcao == 4:
        continue   
    elif opcao == 5:
        print("PROGRAMA ENCERRADO")
        break
    else:
        print("Opção inválida!")