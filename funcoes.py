import os
import time 

def menu_principal():
        print("-="*12,)
        print('MENU PRINCIPAL COM O PET')
        print("-="*12,)
        print('1. Adicionar PETS (Cachorro/Gato/Ave)')
        print('2. Visualizar Pet (Cachorro/Gato/Ave)')
        print('3. Editar Pet (Cachorro/Gato/Ave)')
        print('4. Excluir Pet (Cachorro/Gato/Ave)')
        print('5. Para Finalizar')
        print("-="*12,)
        #tirei o input de opção que estava errado aqui e so deixei no main

#adicionar Pet
def addPet():
    nome = input("Digite o nome do pet: ").capitalize()
    
    if os.path.isfile(f"Pet{nome}.txt"):
        print(f"Erro: Um pet com o nome '{nome}' já existe! Escolha outro nome.")
        return
    
    try:
        idade = int(input("Digite a idade do pet: "))
        while True:
            tipo = str(input("Digite o tipo do seu pet(Cachorro/Gato/Ave):")).capitalize()
            if tipo in ["Cachorro", "Gato", "Ave"]:
                break
            else:
                print("Tipo inválido! não atendemos esse tipo de animal aqui por favor escolha (Cachorro/Gato/Ave)") 
        
    except ValueError as erro: #troquei o nome da variavel e para erro
        print(f"Digite uma idade valida! (Erro: {erro})")#mesma coisa
        return
    
    #função que cria um Arquivo.txt, ID = PET{nome}.txt 
    with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
        file.write(f"Nome: {nome}\n")
        file.write(f"Idade: {idade}\n")
        file.write(f"Tipo: {tipo}\n")

    
def visualizarPet():
    nome = input("Digite o nome do pet: ").capitalize()
    try:
        with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
            #if os.path.isfile(f"Pet{nome}.txt"):
            #agora conteudo_Pet le o arquivo e depois printa
            conteudo_Pet = file.read()
            print(conteudo_Pet)
            
    except FileNotFoundError as erro: #troquei o nome da variavel e para erro
        print(f"Digite nome inválido (Erro: {erro})")

def editarPet():
    nome = input("Digite o nome do pet: ").capitalize()
    
    try:
        with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
            linhas = file.readlines()
            
        # Exibir informações atuais
        print("\nInformações atuais do pet:")
        print(f"1. Nome: {linhas[0].strip()}")
        print(f"2. Idade: {linhas[1].strip()}")
        print(f"3. Tipo: {linhas[2].strip()}")

        # Pedir novos infos ao usuário
        novo_nome = str(input("Novo nome (pressione Enter caso não deseje trocar): ")).strip().capitalize() or linhas[0].strip()
        nova_idade = input("Nova idade (pressione Enter caso não deseje trocar): ").strip()
        nova_idade = int(nova_idade) if nova_idade else int(linhas[1].strip())
        novo_tipo = str(input("Novo tipo (pressione Enter caso não deseje trocar): ")).strip().capitalize() or linhas[2].strip()

        # Atualizar as linhas
        linhas[0] = f"Nome: {novo_nome}\n"
        linhas[1] = f"Idade: {nova_idade}\n"
        linhas[2] = f"Tipo: {novo_tipo}\n"
        
        with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
            file.writelines(linhas)
        
        print(f"Arquivo Pet{nome}.txt atualizado com sucesso!")
        
    except FileNotFoundError as erro: #troquei o nome da variavel e para erro
        print(f"Digite um nome inválido (Erro: {erro})")    
    except IndexError:
        print(f"Erro: Este pet não existe portanto não pode ser editado!.")

def deletePet(): 
    nome = input("Digite o nome do pet: ").capitalize()
    arquivo = f"Pet{nome}.txt"
    try:
        if os.path.isfile(arquivo):
            os.remove(f"Pet{nome}.txt")
            print(f"Arquivo 'Pet{nome}.txt' foi deletado com sucesso!")
        else:
            print(f"Nome do pet inválido! O arquivo '{arquivo}' não foi encontrado.")
    except FileNotFoundError as erro:
        print(f"Arquivo não encontrado! (Erro: {erro})")

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
        continue  #vou criar a função editar pet, o continue e apenas para rodar os testes
        # editar_pet()
    elif opcao == 4:
        deletePet()   
        
    elif opcao == 5:
        print("PROGRAMA ENCERRADO")
        break
    else:
        print("Opção inválida!")