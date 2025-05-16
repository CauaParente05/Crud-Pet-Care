import os
import time 
import eventos


def menu_principal():
        print("-="*12,)
        print('MENU PRINCIPAL COM O PET')
        print("-="*12,)
        print('1. Adicionar PETS (Cachorro/Gato/Ave)')
        print('2. Visualizar Pet (Cachorro/Gato/Ave)')
        print('3. Editar Pet (Cachorro/Gato/Ave)')
        print('4. Excluir Pet (Cachorro/Gato/Ave)')
        print('5. Para Finalizar')
        print('6. Menu de Eventos Pet')
        print("-="*12,)
        #tirei o input de opção que estava errado aqui e so deixei no main

def validar_nome():
    while True:
        nome = input("Digite o nome do pet: ").capitalize()
        
        if nome.replace(" "," ").isalpha():  # O comando replace serve para que seja possivel colocar 2 nomes ou espaços em branco e o isalpha verifica se a string contém apenas letras  
            return nome
        else:
            print("Erro: O nome do pet deve conter apenas letras! Tente novamente.")

def validar_tipo():
    while True:
        tipo = input("Digite o tipo do pet (Cachorro/Gato/Ave): ").capitalize()
        if tipo in ["Cachorro", "Gato", "Ave"]:
            return tipo
        else:
            print("Tipo inválido! Escolha entre Cachorro, Gato ou Ave.")
            
def validar_novo_tipo(nome, tipo):
    while True:
        try:
            with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
                linhas = file.readlines()
                novo_tipo = input("Novo tipo (pressione Enter caso não deseje trocar): ").strip().capitalize()
                novo_tipo = novo_tipo if novo_tipo else linhas[2].split(":")[1].strip()
                if novo_tipo in ["Cachorro", "Gato", "Ave", tipo]:
                    return novo_tipo
                else:
                    print("Tipo inválido! Escolha entre Cachorro, Gato ou Ave.")
        except FileNotFoundError:
            print(f"Erro: O pet '{nome}' não existe.")
            return None
#adicionar Pet
def addPet():
    nome = validar_nome()
    
    if os.path.isfile(f"Pet{nome}.txt"):
        print(f"Erro: Um pet com o nome '{nome}' já existe! Escolha outro nome.")
        return
    
    try:
        idade = int(input("Digite a idade do pet: "))
        tipo = validar_tipo()
        
    except ValueError as erro: #troquei o nome da variavel e para erro
        print(f"Digite uma idade valida! (Erro: {erro})")#mesma coisa
        return
    
    #função que cria um Arquivo.txt, ID = PET{nome}.txt 
    with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
        file.write(f"Nome: {nome}\n")
        file.write(f"Idade: {idade}\n")
        file.write(f"Tipo: {tipo}\n")

    
def visualizarPet():
    nome = validar_nome()
    
    try:
        with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
            #if os.path.isfile(f"Pet{nome}.txt"):
            #agora conteudo_Pet le o arquivo e depois printa
            conteudo_Pet = file.read()
            print(conteudo_Pet)        
    except FileNotFoundError as erro: #troquei o nome da variavel e para erro
        print(f"(Erro: Pet {nome}) não foi encontrado! verifique se foi digitado o nome certo")

def editarPet():
    nome = validar_nome()
    
    try:
        with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
            linhas = file.readlines()
            
        if len(linhas) < 3 or not all(":" in linha for linha in linhas[:3]):
            print("Erro: O formato do arquivo está incorreto!")
            return
        
        # Exibir informações atuais
        print("\nInformações atuais do pet:")
        print(f"1. Nome: {linhas[0].split(':')[1].strip()}")
        print(f"2. Idade: {linhas[1].split(':')[1].strip()}")
        print(f"3. Tipo: {linhas[2].split(':')[1].strip()}")

        # Pedir novas infos ao usuário
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
            return

        # Atualizar as linhas
        linhas[0] = f"Nome: {novo_nome.strip()}\n"
        linhas[1] = f"Idade: {str(nova_idade).strip()}\n"
        linhas[2] = f"Tipo: {novo_tipo.strip()}\n"
        
        with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
            file.writelines(linhas)
        
        print(f"Arquivo Pet{nome}.txt atualizado com sucesso!")    
    except FileNotFoundError as erro: #troquei o nome da variavel e para erro
        print(f"Digite um nome inválido (Erro: {erro})")    
    except IndexError:
        print(f"Erro: Este pet não existe portanto não pode ser editado!.")

def deletePet():
    nome = validar_nome()
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
        menu_principal()
        time.sleep(1)
        try:
            opcao = int(input("Digite o número da opção escolhida: "))
        except ValueError:
            print("Opção inválida! Digite apenas números.")
            continue

    if opcao == 1:
        addPet()
    elif opcao == 2:
        visualizarPet()
    elif opcao == 3:
        editarPet()
    elif opcao == 4:
        deletePet()   
    elif opcao == 5:
        print("PROGRAMA ENCERRADO")
        break
    elif opcao == 6:
        eventos.menu_cuidados()
    else:
        print("Opção inválida!")