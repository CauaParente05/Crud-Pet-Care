#adicionar Pet
#função que cria um Arquivo.txt, ID = PET{nome}.txt 
import os
import time 
# colocar um delay entre menu e as funções
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
        time.sleep(2)
def addPet():
    nome = input("Digite o nome do pet: ")
    try:
        if os.path.isfile(f"Pet{nome}.txt"):
            idade = int(input("Digite a idade do pet: "))
            tipo = str(input("Digite o tipo do seu pet(Cachorro/Gato/Ave):"))
    except ValueError as erro: #troquei o nome da variavel e para erro
        print(f"Digite uma idade valida! (Erro: {erro})")#mesma coisa
    

    with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
        file.write(f"Nome: {nome}\n")
        file.write(f"Idade: {idade}\n")
        file.write(f"Tipo: {tipo}\n")
        return

    
def visualizarPet():
    nome = input("Digite o nome do pet: ")
    try:
        with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
            #if os.path.isfile(f"Pet{nome}.txt"):
            #agora conteudo_Pet le o arquivo e depois printa
            conteudo_Pet = file.read()
            print(conteudo_Pet)
            
    except FileNotFoundError as erro: #troquei o nome da variavel e para erro
        print(f"Digite nome inválido (Erro: {erro})")

def editarPet():#nao to conseguindo ainda
    nome = input("Digite o nome do pet: ")
    # Abrir o arquivo original para leitura
    try:
        with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
            linhas = file.readlines()
        # Modificar a linha desejada (por exemplo, a linha 2)
        linhas[1] = 'Esta é a nova linha 2\n'
        # Escrever de volta no arquivo
        with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
            file.writelines(linhas)
    except FileNotFoundError as erro: #troquei o nome da variavel e para erro
        print(f"Digite nome inválido (Erro: {erro})")

def deletePet(): 
    nome = input("Digite o nome do pet: ")
    try:
            os.remove(f"Pet{nome}.txt")
            print(f"Arquivo {f"Pet{nome}.txt"} foi deletado com sucesso!")
    except FileNotFoundError as erro:
        print(f"Arquivo não encontrado! (Erro: {erro})")

while True:
    menu_principal()
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
        continue   #vou criar a função editar pet, o continue e apenas para rodar os testes
        # editar_pet()
    elif opcao == 4:
        deletePet()   
        
    elif opcao == 5:
        print("PROGRAMA ENCERRADO")
        break
    else:
        print("Opção inválida!, Escolha as opções oferecidas.")