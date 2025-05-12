ARQUIVO_PETS = "pets.txt"

# Função para adicionar um pet ao arquivo
def adicionar_pet(nome, idade, tipo):
    with open(ARQUIVO_PETS, "a", encoding="utf-8") as file:
        file.write(f"{nome},{idade},{tipo}\n")
    print(f"Pet '{nome}' adicionado com sucesso!")

# Função para visualizar todos os pets
def visualizar_pets():
    try:
        with open(ARQUIVO_PETS, "r", encoding="utf-8") as file:
            pets = file.readlines()
        if pets:
            for idx, pet in enumerate(pets, 1):
                dados = pet.strip().split(",")
                print(f"{idx}. Nome: {dados[0]}, Idade: {dados[1]}, Tipo: {dados[2]}")
        else:
            print("Nenhum pet cadastrado.")
    except FileNotFoundError:
        print("Arquivo de registros ainda não existe.")

# Função para editar um pet
def editar_pet(indice, novo_nome, nova_idade, novo_tipo):
    try:
        with open(ARQUIVO_PETS, "r", encoding="utf-8") as file:
            pets = file.readlines()

        if 1 <= indice <= len(pets):
            pets[indice - 1] = f"{novo_nome},{nova_idade},{novo_tipo}\n"

            with open(ARQUIVO_PETS, "w", encoding="utf-8") as file:
                file.writelines(pets)
            print("Pet atualizado com sucesso!")
        else:
            print("Índice inválido.")
    except FileNotFoundError:
        print("Arquivo de registros ainda não existe.")

# Função para excluir um pet
def excluir_pet(indice):
    try:
        with open(ARQUIVO_PETS, "r", encoding="utf-8") as file:
            pets = file.readlines()

        if 1 <= indice <= len(pets):
            pet_removido = pets.pop(indice - 1)

            with open(ARQUIVO_PETS, "w", encoding="utf-8") as file:
                file.writelines(pets)
            print(f"Pet '{pet_removido.strip().split(',')[0]}' removido com sucesso!")
        else:
            print("Índice inválido.")
    except FileNotFoundError:
        print("Arquivo de registros ainda não existe.")

adicionar_pet("Rex", 3, "Cachorro")
adicionar_pet("Mia", 2, "Gato")
visualizar_pets()
editar_pet(1, "Rex", 4, "Cachorro")
excluir_pet(2)
visualizar_pets()
