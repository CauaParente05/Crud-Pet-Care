animal = input("Qual o seu animal? ")
nome = input("Digite o nome do seu animal: ")
tipo = input("Digite o tipo de porte do seu pet (pequeno/médio/grande porte): ")
idade = int(input("Digite a idade do seu pet: "))

if animal == "cachorro" or animal == "gato":
    if idade <= 1:
        idade = 'filhote'
    elif idade > 1 and idade <= 7:
        idade = 'adulto'
    else:
        idade = 'idoso'

if animal == "ave":
    if idade <= 1:
        idade = 'filhote'
    elif idade > 1 and idade <= 5:
        idade = 'adulto'
    else:
        idade = 'idoso'

# config personalizadas cachorros-
if animal == 'cachorro':
    if tipo == 'pequeno porte':
        if idade == 'filhote':
            print("Alimentação rica em proteínas e DHA, socialização precoce, vacinas, vermifugação, espaço seguro.")

if animal == 'cachorro':
    if tipo == 'pequeno porte':
        if idade == 'adulto':
            print("Exercícios moderados (passeios diários), escovação dental, tosa, controle de pulgas e carrapatos.")

if animal == 'cachorro':
    if tipo == 'pequeno porte':
        if idade == 'idoso':
            print("Alimentação com baixo teor de gordura, suplementos articulares, exames periódicos, rampas de acesso.")

if animal == 'cachorro':
    if tipo == 'médio porte':
        if idade == 'filhote':
            print(
                "Treinamento básico, alimentação balanceada para crescimento, socialização com outros animais.")

if animal == 'cachorro':
    if tipo == 'médio porte':
        if idade == 'adulto':
            print(
                "Atividades físicas diárias, cuidados com unhas e ouvidos, vacinação em dia, controle de peso.")

if animal == 'cachorro':
    if tipo == 'médio porte':
        if idade == 'idoso':
            print(
                "Cama ortopédica, dieta rica em fibras, checagem de artrite, check-up semestral.")

if animal == 'cachorro':
    if tipo == 'grande porte':
        if idade == 'filhote':
            print("Alimentação para crescimento lento (prevenir displasia), socialização intensa, reforço positivo.")

if animal == 'cachorro':
    if tipo == 'grande porte':
        if idade == 'adulto':
            print("Exercício intenso (correr, nadar), controle rigoroso de peso, atenção ao quadril e articulações.")

if animal == 'cachorro':
    if tipo == 'grande porte':
        if idade == 'idoso':
            print("Suplementação com condroitina e glucosamina, fisioterapia, suporte ergonômico, monitoramento cardíaco.")

# config personalizadas gatos-
if animal == 'gato':
    if tipo == 'pequeno porte':
        if idade == 'filhote':
            print("Brinquedos para estímulo mental, caixa de areia limpa, alimentação úmida e seca própria para filhotes.")

if animal == 'gato':
    if tipo == 'pequeno porte':
        if idade == 'adulto':
            print("Escovação regular (especialmente peludos), arranhadores, controle de bolas de pelo, enriquecimento.")

if animal == 'gato':
    if tipo == 'pequeno porte':
        if idade == 'idoso':
            print("Areia de fácil acesso, dieta renal/amolecida, visitas frequentes ao veterinário, aquecimento extra.")

if animal == 'gato':
    if tipo == 'médio porte':
        if idade == 'filhote':
            print("Socialização com humanos e outros animais, alimentação específica para crescimento controlado, escovação precoce (pelagem densa).")

if animal == 'gato':
    if tipo == 'médio porte':
        if idade == 'adulto':
            print("Brinquedos interativos, dieta balanceada (controle de peso), escovação semanal (pelagem longa), espaço vertical.")

if animal == 'gato':
    if tipo == 'médio porte':
        if idade == 'idoso':
            print("Monitoramento renal e cardíaco, mobilidade facilitada com rampas, dieta sênior rica em taurina e baixa em fósforo.")

if animal == 'gato':
    if tipo == 'grande porte':
        if idade == 'filhote':
            print("Crescimento mais lento → usar ração de filhote por mais tempo, manipulação para acostumar ao manuseio, atenção à escovação precoce.")

if animal == 'gato':
    if tipo == 'grande porte':
        if idade == 'adulto':
            print("Exercícios leves (por causa do peso), dieta com baixa caloria para evitar sobrepeso, escovação frequente, caixa de areia ampla")

if animal == 'gato':
    if tipo == 'grande porte':
        if idade == 'idoso':
            print("Atenção especial às articulações (peso extra → risco de artrose), cama ortopédica, enriquecimento ambiental calmo, monitoramento do coração.")

# config personalizadas aves-
if animal == 'ave':
    if tipo == 'pequeno porte':
        if idade == 'filhote':
            print(
                "Alimentação com papa específica, aquecimento controlado, manipulação suave e frequente.")

if animal == 'ave':
    if tipo == 'pequeno porte':
        if idade == 'adulto':
            print(
                "Gaiola ampla, dieta variada (sementes + frutas/verduras), socialização, banhos regulares.")

if animal == 'ave':
    if tipo == 'pequeno porte':
        if idade == 'idoso':
            print("Poleiros confortáveis, suplementação vitamínica, temperatura ambiente constante, monitoramento de penas.")

if animal == 'ave':
    if tipo == 'médio porte':
        if idade == 'filhote':
            print(
                "Cuidado com a alimentação manual, controle de calor, socialização para evitar agressividade.")

if animal == 'ave':
    if tipo == 'médio porte':
        if idade == 'adulto':
            print(
                "Interação diária, brinquedos para bico, dieta equilibrada com pellets, visitas veterinárias.")

if animal == 'ave':
    if tipo == 'médio porte':
        if idade == 'idoso':
            print("Gaiola adaptada, voos supervisionados, ajustes na alimentação (menos sementes), cuidados respiratórios.")

if animal == 'ave':
    if tipo == 'grande porte':
        if idade == 'filhote':
            print(
                "Alimentação assistida, vinculação com tutor, introdução a brinquedos e comandos simples.")

if animal == 'ave':
    if tipo == 'grande porte':
        if idade == 'adulto':
            print("Estímulo constante, alimentação variada e rica em nutrientes, interação social, exercícios diários.")

if animal == 'ave':
    if tipo == 'grande porte':
        if idade == 'idoso':
            print("Check-ups regulares, adaptação de poleiros, dieta monitorada, estímulo cognitivo para prevenir tédio.")
else:
    print("O seu animal não possui configurações personalizadas disponíveis.")
