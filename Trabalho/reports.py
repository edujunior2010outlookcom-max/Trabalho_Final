from storage import carregar_usuarios, carregar_projetos, carregar_tarefas


# ----------------------------------------------------
# RELATÓRIO DE USUÁRIOS
# ----------------------------------------------------
def relatorio_usuarios():
    usuarios = carregar_usuarios()

    print("\n====== RELATÓRIO DE USUÁRIOS ======")

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for u in usuarios:
        print(f"Nome: {u['nome']}")
        print(f"Email: {u['email']}")
        print(f"Sexo: {u['sexo']}")
        print(f"Idade: {u['idade']}")
        print(f"CPF: {u['cpf']}")
        print("-" * 40)


# ----------------------------------------------------
# RELATÓRIO DE PROJETOS (+ quantidade de tarefas)
# ----------------------------------------------------
def relatorio_projetos():
    projetos = carregar_projetos()
    tarefas = carregar_tarefas()

    print("\n====== RELATÓRIO DE PROJETOS ======")

    if not projetos:
        print("Nenhum projeto cadastrado.")
        return

    for p in projetos:
        nome = p["nome"]

        # conta tarefas ligadas ao projeto
        qtd = sum(1 for t in tarefas if t["projeto"].lower() == nome.lower())

        print(f"Projeto: {p['nome']}")
        print(f"Descrição: {p['descricao']}")
        print(f"Tarefas vinculadas: {qtd}")
        print("-" * 40)


# ----------------------------------------------------
# RELATÓRIO DE TAREFAS
# ----------------------------------------------------
def relatorio_tarefas():
    tarefas = carregar_tarefas()

    print("\n====== RELATÓRIO DE TAREFAS ======")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for t in tarefas:
        print(f"Título: {t['titulo']}")
        print(f"Projeto: {t['projeto']}")
        print(f"Responsável: {t['responsavel']}")
        print(f"Status: {t['status']}")
        print(f"Prazo: {t['prazo']}")
        print("-" * 40)

