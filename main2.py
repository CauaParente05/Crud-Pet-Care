#adicionar Pet
#função que cria um Arquivo.txt, ID = PET{nome}.txt 
import os

def menu_principal(opcao):
  
        print("-="*12,)
        print('MENU PRINCIPAL COM O PET')
        print("-="*12,)
        print('1. Adicionar PETS (Cachorro/Gato/Ave)')
        print('2. Visualizar Pet (Cachorro/Gato/Ave)')
        print('3. Editar Pet (Cachorro/Gato/Ave)')
        print('4. Excluir Pet (Cachorro/Gato/Ave)')
        print('5. Para Finalizar')
        opcao = input("Digite o número da opção escolha: ")
def addPet():
    nome = input("Digite o nome do pet: ")
    try:
        idade = int(input("Digite a idade do pet: "))
    except ValueError as e:
        print(f"Digite uma idade valida! (Erro: {e})")

    with open(f"Pet{nome}.txt", "w", encoding="UTF-8") as file:
        file.write(f"Nome: {nome}\n")
        file.write(f"Idade: {idade}")
    
def visualizarPet():
    nome = input("Digite o nome do pet: ")
    try:
        with open(f"Pet{nome}.txt", "r", encoding="UTF-8") as file:
            #if os.path.isfile(f"Pet{nome}.txt"):
            conteudo_Pet = (f"Pet{nome}.txt".read())
            print(conteudo_Pet)
    except FileNotFoundError as e:
        print(f"Digite uma idade valida! (Erro: {e})")


def deletePet():
    nome = input("Digite o nome do pet: ")
    arquivo_nome = f"Pet{nome}.txt"
    try:
        # Verifica se o arquivo existe antes de tentar remover
        os.remove(arquivo_nome)
        print(f"Arquivo {arquivo_nome} foi deletado com sucesso!")
    except FileNotFoundError as erro:
        print(f"Arquivo não encontrado! (Erro: {erro})")

