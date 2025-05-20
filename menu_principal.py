import os
import time
import eventos
import sys
import cuidados

def menu_principal():
    print("-="*20,)
    print('MENU PRINCIPAL COM O PET')
    print("-="*20,)
    print('1. Adicionar PETS (Cachorro/Gato/Ave)')
    print('2. Visualizar Pet (Cachorro/Gato/Ave)')
    print('3. Editar Pet (Cachorro/Gato/Ave)')
    print('4. Excluir Pet (Cachorro/Gato/Ave)')
    print('5. Menu de Eventos Pet')
    print('6. Menu de Cuidados com Pet')
    print('7. Para Finalizar')
    print("-="*20,)

# Verificações:---------------------------------------|

def validar_nome():
    while True:
        nome = input("Digite o nome do pet: ").capitalize()

        # O comando replace serve para que seja possivel colocar 2 nomes ou espaços em branco e o isalpha verifica se a string contém apenas letras
        if nome.replace(" ", " ").isalpha():
            return nome
        else:
            print("Erro: O nome do pet deve conter apenas letras! Tente novamente.")


def validar_tipo():
    while True:
        tipo = input("Digite o tipo do pet (Cachorro/Gato/Ave): ").strip().capitalize()
        if tipo in ["Cachorro", "Gato", "Ave"]:
            return tipo
        else:
            print("Tipo inválido! Escolha entre Cachorro, Gato ou Ave.")

def validar_porte():
    while True:
        porte = input("Digite o tipo de porte do seu pet (Pequeno/Médio/Grande porte): ").strip().capitalize()
        
        if porte == "Medio":
            porte = "Médio"
        elif porte == "Grande":
            porte = "Grande porte"
        
        if porte in ["Pequeno", "Médio", "Grande porte"]:
            return porte
        else:
            print("Porte inválido! Escolha entre (Pequeno/Médio/Grande porte).")

def validar_novo_porte(nome, porte):
    while True:
        try:
            with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
                linhas = file.readlines()
                novo_porte = input("Novo porte (Pequeno/Médio/Grande porte) ou (pressione Enter caso não deseje trocar): ").strip().capitalize()
                novo_porte = novo_porte if novo_porte else linhas[3].split(":")[1].strip()
                if novo_porte == "Medio":
                    novo_porte = "Médio"
                elif novo_porte == "Grande":
                    novo_porte = "Grande porte"
                if novo_porte in ["Pequeno", "Médio", "Grande porte", porte]:
                    return novo_porte
                else:
                    print("Porte inválido! Escolha entre (Pequeno/Médio/Grande porte).")
        except FileNotFoundError:
            print(f"Erro: O pet '{nome}' não existe.")
            return None

def validar_novo_tipo(nome, tipo):
    while True:
        try:
            with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
                linhas = file.readlines()
                novo_tipo = input("Novo tipo (Cachorro/Gato/Ave) ou (pressione Enter caso não deseje trocar): ").strip().capitalize()
                novo_tipo = novo_tipo if novo_tipo else linhas[2].split(":")[1].strip()
                if novo_tipo in ["Cachorro", "Gato", "Ave", tipo]:
                    return novo_tipo
                else:
                    print("Tipo inválido! Escolha entre Cachorro, Gato ou Ave.")
        except FileNotFoundError:
            print(f"Erro: O pet '{nome}' não existe.")
            return None
        
# Verificações---------------------------------------|

# Manipulação de arquivos---------------------------------------|
def add_pet():
    nome = validar_nome()

    if os.path.isfile(f"Pet{nome}.txt"):
        print(
            f"Erro: Um pet com o nome '{nome}' já existe! Escolha outro nome.")
        return

    try:
        idade = int(input("Digite a idade do pet: "))
        tipo = validar_tipo()
        porte = validar_porte()

    except ValueError as erro:
        print(f"Digite uma idade valida! (Erro: {erro})")
        return

    with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
        file.write(f"Nome: {nome}\n")
        file.write(f"Idade: {idade}\n")
        file.write(f"Tipo: {tipo}\n")
        file.write(f"Porte: {porte}\n")
    
    cuidados.salvar_cuidados(nome, tipo, porte, idade)

def visualizar_pet():
    nome = validar_nome()

    try:
        with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
            conteudo_pet = file.read()
            print(conteudo_pet)
    except FileNotFoundError as erro:
        print(
            f"(Erro: Pet {nome}) não foi encontrado! verifique se foi digitado o nome certo")


def editar_pet():
    nome = validar_nome()
    nome_arquivo_pet_anterior = f"Pet{nome}.txt"
    try:
        with open(nome_arquivo_pet_anterior, "r", encoding="UTF-8") as file:
            linhas = file.readlines()

        if len(linhas) < 3 or not all(":" in linha for linha in linhas[:3]):
            print("Erro: O formato do arquivo está incorreto!")
            return

        print("\nInformações atuais do pet:")
        print(f"1. Nome: {linhas[0].split(':')[1].strip()}")
        print(f"2. Idade: {linhas[1].split(':')[1].strip()}")
        print(f"3. Tipo: {linhas[2].split(':')[1].strip()}")
        print(f"4. Porte: {linhas[3].split(':')[1].strip()}")

        novo_nome = input("Novo nome (pressione Enter caso não deseje trocar): ").strip().capitalize()
        novo_nome = novo_nome if novo_nome else linhas[0].split(":")[1].strip()

        nova_idade = input("Nova idade (pressione Enter caso não deseje trocar): ").strip()
        try:
            nova_idade = int(nova_idade) if nova_idade else int(linhas[1].strip().split(":")[1].strip())
        except ValueError:
            print("Erro: Idade inválida! Deve ser um número.")
            return

        novo_tipo = validar_novo_tipo(nome, linhas[2])
        if novo_tipo is None:
            return None
        
        novo_porte = validar_novo_porte(nome, linhas[3])
        if novo_porte is None:
            return None

        linhas[0] = f"Nome: {novo_nome.strip()}\n"
        linhas[1] = f"Idade: {str(nova_idade).strip()}\n"
        linhas[2] = f"Tipo: {novo_tipo.strip()}\n"
        linhas[3] = f"Porte: {novo_porte.strip()}\n"
        
        nome_arquivo_pet = f"Pet{novo_nome}.txt"
        
        os.remove(nome_arquivo_pet_anterior)

        with open(nome_arquivo_pet, "w", encoding="UTF-8") as file:
            file.writelines(linhas)

        print(f"Arquivo Pet{nome}.txt atualizado com sucesso!")
    except FileNotFoundError as erro:
        print(f"Digite um nome inválido (Erro: {erro})")
    except IndexError:
        print(f"Erro: Este pet não existe portanto não pode ser editado!.")


def delete_pet():
    nome = validar_nome()
    arquivo = f"Pet{nome}.txt"
    try:
        if os.path.isfile(arquivo):
            os.remove(f"Pet{nome}.txt")
            print(f"Arquivo 'Pet{nome}.txt' foi deletado com sucesso!")
        else:
            print(
                f"Nome do pet inválido! O arquivo '{arquivo}' não foi encontrado.")
    except FileNotFoundError as erro:
        print(f"Arquivo não encontrado! (Erro: {erro})")
        
# Manipulação de arquivos---------------------------------------|

# Menu---------------------------------------|
def escolhas_menu():
    while True:
        menu_principal()
        time.sleep(1)
        try:
            opcao = int(input("Digite o número da opção escolhida: "))
        except ValueError:
            print("Opção inválida! Digite apenas números.")
            continue
        
        if opcao == 1:
            add_pet()
        elif opcao == 2:
            visualizar_pet()
        elif opcao == 3:
            editar_pet()
        elif opcao == 4:
            delete_pet()
        elif opcao == 5:
            eventos.escolhas_menu_eventos()
        elif opcao == 6:
            cuidados.escolhas_menu_cuidados()
        elif opcao == 7:
            print("PROGRAMA ENCERRADO")
            sys.exit()
        else:
            print("Opção inválida! Digite o número de uma das opções exibida")
           
# Menu---------------------------------------|