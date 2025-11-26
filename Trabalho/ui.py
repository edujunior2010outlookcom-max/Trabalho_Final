#MENUS GERAIS

def menu_principal():
    print("\n======= MENU PRINCIPAL =======")
    print("[1] - Usuários")
    print("[2] - Projetos")
    print("[3] - Tarefas")
    print("[4] - Relatórios")
    print("[5] - Sair")
    return input("Escolha uma opção: ")


def menu_usuario():
    print("\n======= MENU DE USUÁRIOS =======")
    print("[1] - Cadastrar")
    print("[2] - Listar")
    print("[3] - Buscar (nome/e-mail)")
    print("[4] - Atualizar")
    print("[5] - Remover")
    print("[6] - Voltar")
    return input("Escolha uma opção: ")


def menu_projetos():
    print("\n======= MENU DE PROJETOS =======")
    print("[1] - Cadastrar")
    print("[2] - Listar")
    print("[3] - Buscar")
    print("[4] - Atualizar")
    print("[5] - Remover")
    print("[6] - Voltar")
    return input("Escolha uma opção: ")


def menu_tarefas():
    print("\n======= MENU DE TAREFAS =======")
    print("[1] - Cadastrar")
    print("[2] - Listar todas")
    print("[3] - Atualizar")
    print("[4] - Remover")
    print("[5] - Voltar")
    return input("Escolha uma opção: ")


def menu_relatorios():
    print("\n======= MENU DE RELATÓRIOS =======")
    print("[1] - Usuários cadastrados")
    print("[2] - Projetos e quantidade de tarefas")
    print("[3] - Tarefas detalhadas")
    print("[4] - Voltar")
    return input("Escolha uma opção: ")
