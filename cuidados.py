import menu_principal
import eventos
import os
import time
import sys

def menu_cuidados():
    print("-="*12,)
    print('MENU DE CUIDADOS COM O PET')
    print("-="*12,)
    print('1. Visualizar Cuidados do Pet')
    print('2. Editar Cuidados do Pet')
    print('3. Excluir Cuidados do Pet')
    print('4. Para Menu Principal')
    print('5. Para Menu de Eventos de Pet')
    print('6. Para Finalizar')
    print("-="*12,)
    
def salvar_cuidados(nome, tipo, porte, idade):
    idade_categoria = categorizar_idade(tipo, idade)
    
    if idade_categoria is None:
        print(f"Erro: Tipo de animal '{tipo}' não possui configuração disponível.")
        return
    
    cuidados = obter_cuidados(tipo.lower(), porte, idade_categoria)
    
    if os.path.isfile(f"Cuidados_{nome}.txt"):
        print(f"Erro: Um plano de cuidados com '{nome}' já existe! Escolha outro nome.")
        return

    with open(f"Cuidados_{nome}.txt", "w", encoding="UTF-8") as file:
        file.write(f"Nome: {nome}\n")
        file.write(f"Tipo: {tipo}\n")
        file.write(f"Porte: {porte}\n")
        file.write(f"Idade: {idade} anos ({idade_categoria})\n")
        file.write(f"Cuidados recomendados:\n{cuidados}\n")

    print(f"Arquivo 'Cuidados_{nome}.txt' criado com sucesso!")

def visualizar_cuidados(nome):
    try:
        with open(f"Cuidados_{nome}.txt", "r", encoding="UTF-8") as file:
            conteudo = file.read()
            print("\nInformações sobre cuidados do pet:")
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: Nenhum arquivo de cuidados encontrado para o pet '{nome}'.")

def editar_cuidados(nome):
    try:
        with open(f"Cuidados_{nome}.txt", "r", encoding="UTF-8") as file:
            linhas = file.readlines()

        nova_idade = int(input("Digite a nova idade do pet: "))
        tipo = menu_principal.validar_tipo()
        porte = menu_principal.validar_porte()
        
        idade_categoria = categorizar_idade(tipo.lower(), nova_idade)
        cuidados = obter_cuidados(tipo.lower(), porte, idade_categoria)

        linhas[3] = f"Idade: {nova_idade} anos ({idade_categoria})\n"
        linhas[4] = f"Cuidados recomendados:\n{cuidados}\n"

        with open(f"Cuidados_{nome}.txt", "w", encoding="UTF-8") as file:
            file.writelines(linhas)

        print(f"Arquivo 'Cuidados_{nome}.txt' atualizado com sucesso!")
    except FileNotFoundError:
        print(f"Erro: O arquivo de cuidados do pet '{nome}' não existe.")

def delete_cuidados():
    nome = menu_principal.validar_nome()
    arquivo = f"Cuidados_{nome}.txt"
    
    try:
        if os.path.isfile(arquivo):
            os.remove(arquivo)
            print(f"Arquivo '{arquivo}' foi deletado com sucesso!")
        else:
            print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado!")


def categorizar_idade(tipo, idade):
    limites_idade = {
        "Cachorro": [1, 7],
        "Gato": [1, 5],
        "Ave": [1, 5]
    }
    
    tipo = tipo.capitalize().strip()
    
    if tipo in limites_idade:
        if idade <= limites_idade[tipo][0]:
            return 'filhote'
        elif idade <= limites_idade[tipo][1]:
            return 'adulto'
        else:
            return 'idoso'
    else:
        return "A configuração para este animal não está disponível"

def cuidados_pet(tipo, porte, idade):
    idade_categoria = categorizar_idade(tipo, idade)
    return obter_cuidados(tipo, porte, idade_categoria)

def obter_cuidados(tipo, porte, idade):
    cuidados = {
        "Cachorro": {
        ('Pequeno', 'filhote'): "Alimentação rica em proteínas e DHA, socialização precoce, vacinas, vermifugação, espaço seguro.",
        ('Pequeno', 'adulto'): "Exercícios moderados (passeios diários), escovação dental, tosa, controle de pulgas e carrapatos.",
        ('Pequeno', 'idoso'): "Alimentação com baixo teor de gordura, suplementos articulares, exames periódicos, rampas de acesso.",
        ('Médio', 'filhote'): "Treinamento básico, alimentação balanceada para crescimento, socialização com outros animais.",
        ('Médio', 'adulto'): "Atividades físicas diárias, cuidados com unhas e ouvidos, vacinação em dia, controle de peso.",
        ('Médio', 'idoso'): "Cama ortopédica, dieta rica em fibras, checagem de artrite, check-up semestral.",
        ('Grande porte', 'filhote'): "Alimentação para crescimento lento (prevenir displasia), socialização intensa, reforço positivo.",
        ('Grande porte', 'adulto'): "Exercício intenso (correr, nadar), controle rigoroso de peso, atenção ao quadril e articulações.",
        ('Grande porte', 'idoso'): "Suplementação com condroitina e glucosamina, fisioterapia, suporte ergonômico, monitoramento cardíaco."
    },
        "Gato": {
        ('Pequeno', 'filhote'): "Brinquedos para estímulo mental, caixa de areia limpa, alimentação úmida e seca própria para filhotes.",
        ('Pequeno', 'adulto'): "Escovação regular (especialmente peludos), arranhadores, controle de bolas de pelo, enriquecimento.",
        ('Pequeno', 'idoso'): "Areia de fácil acesso, dieta renal/amolecida, visitas frequentes ao veterinário, aquecimento extra.",
        ('Médio', 'filhote'): "Socialização com humanos e outros animais, alimentação específica para crescimento controlado, escovação precoce (pelagem densa).",
        ('Médio', 'adulto'): "Brinquedos interativos, dieta balanceada (controle de peso), escovação semanal (pelagem longa), espaço vertical.",
        ('Médio', 'idoso'): "Monitoramento renal e cardíaco, mobilidade facilitada com rampas, dieta sênior rica em taurina e baixa em fósforo.",
        ('Grande porte', 'filhote'): "Crescimento mais lento → usar ração de filhote por mais tempo, manipulação para acostumar ao manuseio, atenção à escovação precoce.",
        ('Grande porte', 'adulto'): "Exercícios leves (por causa do peso), dieta com baixa caloria para evitar sobrepeso, escovação frequente, caixa de areia ampla.",
        ('Grande porte', 'idoso'): "Atenção especial às articulações (peso extra → risco de artrose), cama ortopédica, enriquecimento ambiental calmo, monitoramento do coração."
        },
        
        "Ave": {
        ('Pequeno', 'filhote'): "Alimentação com papa específica, aquecimento controlado, manipulação suave e frequente.",
        ('Pequeno', 'adulto'): "Gaiola ampla, dieta variada (sementes + frutas/verduras), socialização, banhos regulares.",
        ('Pequeno', 'idoso'): "Poleiros confortáveis, suplementação vitamínica, temperatura ambiente constante, monitoramento de penas.",
        ('Médio', 'filhote'): "Cuidado com a alimentação manual, controle de calor, socialização para evitar agressividade.",
        ('Médio', 'adulto'): "Interação diária, brinquedos para bico, dieta equilibrada com pellets, visitas veterinárias.",
        ('Médio', 'idoso'): "Gaiola adaptada, voos supervisionados, ajustes na alimentação (menos sementes), cuidados respiratórios.",
        ('Grande porte', 'filhote'): "Alimentação assistida, vinculação com tutor, introdução a brinquedos e comandos simples.",
        ('Grande porte', 'adulto'): "Estímulo constante, alimentação variada e rica em nutrientes, interação social, exercícios diários.",
        ('Grande porte', 'idoso'): "Check-ups regulares, adaptação de poleiros, dieta monitorada, estímulo cognitivo para prevenir tédio."
        }
    }
    return cuidados.get(tipo.capitalize(), {}).get((porte, idade), "Cuidados não disponíveis para essa categoria.")

def escolhas_menu_cuidados():
    while True:
        menu_cuidados()
        time.sleep(1)
        try:
            opcao = int(input("Digite o número da opção escolhida: "))
        except ValueError:
            print("Opção inválida! Digite apenas números.")
            continue
            
        if opcao == 1:
            nome = menu_principal.validar_nome()
            visualizar_cuidados(nome)
        elif opcao == 2:
            nome = menu_principal.validar_nome()
            editar_cuidados(nome)
        elif opcao == 3:
            delete_cuidados()
        elif opcao == 4:
            menu_principal.escolhas_menu()
        elif opcao == 5:
            eventos.escolhas_menu_eventos()
        elif opcao == 6:
            print("PROGRAMA ENCERRADO")
            sys.exit()