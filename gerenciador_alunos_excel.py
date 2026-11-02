import openpyxl
from openpyxl import load_workbook

def adicionar_aluno(planilha):
    print("\n--- Adicionar Novo Aluno ---")
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso: ")
    area = input("Digite a área: ")

    while True:
        try:
            semestre = int(input("Digite o semestre(apenas números): "))
            break
        except ValueError:
            print("Erro: Por Favor, digite um número válido para o semestre.")
    nova_linha = [nome, curso, area, semestre]
    planilha.append(nova_linha)
    print(f"\n Aluno(a) {nome} adicionado com sucesso!")

def editar_celula(planilha):
    print(f"\n---Editar Aluno---")
    nome_aluno = input("Digite o nome do aluno que deseja editar: ")

    linha_aluno = None
    for i in range(2, planilha.max_row + 1):
        if planilha.cell(row=i, column=1).value == nome_aluno:
            linha_aluno = i
            break
    if not linha_aluno:
        print(f"Aluno(a) '{nome_aluno}' não encontrado(a).")
        return

    print("\nQual informação você quer editar?")
    print("1 - Nome")
    print("2 - Curso")
    print("3 - Área")
    print("4 - Semestre")

    while True:
        try:
            coluna = int(input("Escolha o número da coluna para editar:"))
            if 1 <= coluna <= 4:
                break
            else:
                print("Opção inválida. Escolha um número entre 1 e 4.")
        except ValueError:
            print("Por favor, digite um número.")

    novo_valor = input('Digite o novo valor: ')

    if coluna == 4:
        try:
            novo_valor = int(novo_valor)
        except ValueError:
            print('Semestre deve ser um número. A alteração falha')
            return

    planilha.cell(row=linha_aluno, column=coluna).value = novo_valor
    print(f'\nDados de {nome_aluno} atualizado com sucesso!')

def apagar_aluno(planilha):
    print("\n--- Apagar Aluno ---")
    nome_aluno = input("Digite o nome do aluno que deseja apagar: ")

    linha_aluno = None
    for i in range(1, planilha.max_row + 1):
        if planilha.cell(row=i, column=1).value == nome_aluno:
            linha_aluno = i
            break
    if linha_aluno:
        planilha.delete_rows(linha_aluno)
        print(f'\nAluno(a) {nome_aluno} excluído(a) com sucesso!')
    else:
        print(f"\n Aluno(a) {nome_aluno} não encontrado para apagar")

def listar_alunos(planilha):
    print("\n" + "=" * 70)
    print("\n---LISTA DE ALUNO OFICIAL---")

    cabecalho = [str(celula.value or "") for celula in planilha[1]]
    print(f"{cabecalho[0]:<20} | {cabecalho[1]:<20} | {cabecalho[2]:<15} | {cabecalho[3]}")
    print("-" * 70)
    for linha in planilha.iter_rows(min_row=2, values_only=True):
        nome = str(linha[0] or "-")
        curso = str(linha[1] or "-")
        area = str(linha[2] or "-")
        semestre = str(linha[3] or "N/A")

        print(f"{nome:<20} | {curso:<20} | {area:<15} | {semestre} ")
    print("=" * 70 + "\n")

def menu_principal():
    caminho = "curso.xlsx"
    try:
        pasta_cursos = load_workbook(caminho)
        planilha = pasta_cursos.active
        print(f"Arquivo {caminho} carregado com sucesso.")
    except FileNotFoundError:
        print(f"ERRO: Arquivo {caminho} não encontrado. Execute a célula de upload (Passo 1) primeiro")
        return
    while True:
        print("\n---MENU DE OPÇÕES---")
        print("1- Listar todos os alunos")
        print("2- Adicionar um novo aluno")
        print("3- Editar um aluno")
        print("4- Apagar um aluno")
        print("5- Salvar e sair")

        escolha = input("Digite o número da sua escolha: ")
        if escolha == '1':
            listar_alunos(planilha)
        elif escolha == '2':
            adicionar_aluno(planilha)
        elif escolha == '3':
            editar_celula(planilha)
        elif escolha == '4':
            apagar_aluno(planilha)
        elif escolha == '5':
            caminho_salvar = "cursos_modificado.xlsx"
            pasta_cursos.save(caminho_salvar)
            print(f"\n Alterações salvas com sucesso no arquivo: {caminho_salvar}")
            print("Saindo do programa. Execute o Passo 3 para fazer o download.")
            break
        else:
            print("\n Opção inválida! Por favor, escolha um número de 1 a 5")

menu_principal()
