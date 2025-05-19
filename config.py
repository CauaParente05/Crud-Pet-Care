def cuidados_pet(animal, tipo, idade):

    idade_categoria = categorizar_idade(animal, idade)
    
    if animal == "cachorro":
        return cuidados_cachorro(tipo, idade_categoria)
    elif animal == "gato":
        return cuidados_gato(tipo, idade_categoria)
    elif animal == "ave":
        return cuidados_ave(tipo, idade_categoria)
    else:
        return print("O seu animal não possui configurações personalizadas disponíveis.")
    
def categorizar_idade(animal, idade):
    if animal == "cachorro":
        if idade <= 1:
            return 'filhote'
        elif idade <= 7:
            return 'adulto'
        else:
            return 'idoso'
    elif animal == "gato":
        if idade <= 1:
            return 'filhote'
        elif idade <= 5:
            return 'adulto'
        else:
            return 'idoso'
    elif animal == "ave":
        if idade <= 1:
            return 'filhote'
        elif idade <= 5:
            return 'adulto'
        else:
            return 'idoso'
    else:
        return print ("a configuração para este animal não está disponível")
    
def cuidados_cachorro(tipo, idade):

    cuidados = {
        ('pequeno porte', 'filhote'): "Alimentação rica em proteínas e DHA, socialização precoce, vacinas, vermifugação, espaço seguro.",
        ('pequeno porte', 'adulto'): "Exercícios moderados (passeios diários), escovação dental, tosa, controle de pulgas e carrapatos.",
        ('pequeno porte', 'idoso'): "Alimentação com baixo teor de gordura, suplementos articulares, exames periódicos, rampas de acesso.",
        ('médio porte', 'filhote'): "Treinamento básico, alimentação balanceada para crescimento, socialização com outros animais.",
        ('médio porte', 'adulto'): "Atividades físicas diárias, cuidados com unhas e ouvidos, vacinação em dia, controle de peso.",
        ('médio porte', 'idoso'): "Cama ortopédica, dieta rica em fibras, checagem de artrite, check-up semestral.",
        ('grande porte', 'filhote'): "Alimentação para crescimento lento (prevenir displasia), socialização intensa, reforço positivo.",
        ('grande porte', 'adulto'): "Exercício intenso (correr, nadar), controle rigoroso de peso, atenção ao quadril e articulações.",
        ('grande porte', 'idoso'): "Suplementação com condroitina e glucosamina, fisioterapia, suporte ergonômico, monitoramento cardíaco."
    }
    return cuidados.get(tipo, idade)

def cuidados_gato(tipo, idade):
    cuidados = {
        ('pequeno porte', 'filhote'): "Brinquedos para estímulo mental, caixa de areia limpa, alimentação úmida e seca própria para filhotes.",
        ('pequeno porte', 'adulto'): "Escovação regular (especialmente peludos), arranhadores, controle de bolas de pelo, enriquecimento.",
        ('pequeno porte', 'idoso'): "Areia de fácil acesso, dieta renal/amolecida, visitas frequentes ao veterinário, aquecimento extra.",
        ('médio porte', 'filhote'): "Socialização com humanos e outros animais, alimentação específica para crescimento controlado, escovação precoce (pelagem densa).",
        ('médio porte', 'adulto'): "Brinquedos interativos, dieta balanceada (controle de peso), escovação semanal (pelagem longa), espaço vertical.",
        ('médio porte', 'idoso'): "Monitoramento renal e cardíaco, mobilidade facilitada com rampas, dieta sênior rica em taurina e baixa em fósforo.",
        ('grande porte', 'filhote'): "Crescimento mais lento → usar ração de filhote por mais tempo, manipulação para acostumar ao manuseio, atenção à escovação precoce.",
        ('grande porte', 'adulto'): "Exercícios leves (por causa do peso), dieta com baixa caloria para evitar sobrepeso, escovação frequente, caixa de areia ampla.",
        ('grande porte', 'idoso'): "Atenção especial às articulações (peso extra → risco de artrose), cama ortopédica, enriquecimento ambiental calmo, monitoramento do coração."
    }
    return cuidados.get(tipo, idade)

def cuidados_ave(tipo, idade):

    cuidados = {
        ('pequeno porte', 'filhote'): "Alimentação com papa específica, aquecimento controlado, manipulação suave e frequente.",
        ('pequeno porte', 'adulto'): "Gaiola ampla, dieta variada (sementes + frutas/verduras), socialização, banhos regulares.",
        ('pequeno porte', 'idoso'): "Poleiros confortáveis, suplementação vitamínica, temperatura ambiente constante, monitoramento de penas.",
        ('médio porte', 'filhote'): "Cuidado com a alimentação manual, controle de calor, socialização para evitar agressividade.",
        ('médio porte', 'adulto'): "Interação diária, brinquedos para bico, dieta equilibrada com pellets, visitas veterinárias.",
        ('médio porte', 'idoso'): "Gaiola adaptada, voos supervisionados, ajustes na alimentação (menos sementes), cuidados respiratórios.",
        ('grande porte', 'filhote'): "Alimentação assistida, vinculação com tutor, introdução a brinquedos e comandos simples.",
        ('grande porte', 'adulto'): "Estímulo constante, alimentação variada e rica em nutrientes, interação social, exercícios diários.",
        ('grande porte', 'idoso'): "Check-ups regulares, adaptação de poleiros, dieta monitorada, estímulo cognitivo para prevenir tédio."
    } 
    return cuidados.get(tipo, idade)

animal=input("Qual o seu animal? ").lower()
nome=input("Digite o nome do seu animal: ")
tipo=input("Digite o tipo de porte do seu pet (pequeno/médio/grande porte): ").lower()
idade=int(input("Digite a idade do seu pet: "))

