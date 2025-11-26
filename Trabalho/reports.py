from storage import carregar_usuarios, carregar_projetos, carregar_tarefas


# RELATÓRIO DE USUÁRIOS

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



# RELATÓRIO DE PROJETOS

def relatorio_projetos():
    projetos = carregar_projetos()
    tarefas = carregar_tarefas()

    print("\n====== RELATÓRIO DE PROJETOS ======")

    if not projetos:
        print("Nenhum projeto cadastrado.")
        return

    for p in projetos:
        nome = p["nome"]

        # buscar tarefas do projeto
        relacionadas = [t for t in tarefas if t["projeto"].lower() == nome.lower()]
        total = len(relacionadas)
        concluidas = sum(1 for t in relacionadas if t["status"].lower() == "concluída")

        # evitar divisão por zero
        porcentagem = (concluidas / total * 100) if total > 0 else 0

        print(f"Projeto: {p['nome']}")
        print(f"Descrição: {p['descricao']}")
        print(f"Tarefas vinculadas: {total}")
        print(f"Tarefas concluídas: {concluidas} ({porcentagem:.1f}%)")
        print("-" * 40)



# RELATÓRIO DE TAREFAS

def relatorio_tarefas():
    tarefas = carregar_tarefas()

    print("\n====== RELATÓRIO DE TAREFAS ======")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    # separar por status
    pendentes = [t for t in tarefas if t["status"].lower() == "pendente"]
    andamento = [t for t in tarefas if t["status"].lower() == "andamento"]
    concluidas = [t for t in tarefas if t["status"].lower() == "concluída"]

    grupos = [
        ("PENDENTES", pendentes),
        ("EM ANDAMENTO", andamento),
        ("CONCLUÍDAS", concluidas)
    ]

    for status_nome, grupo in grupos:
        print(f"\nSTATUS: {status_nome} ({len(grupo)} tarefas)")
        print("-" * 40)

        if not grupo:
            print("Nenhuma tarefa neste status.")
            print("-" * 40)
            continue

        for t in grupo:
            print(f"Título: {t['titulo']}")
            print(f"Projeto: {t['projeto']}")
            print(f"Responsável: {t['responsavel']}")
            print(f"Prazo: {t['prazo']}")
            print("-" * 40)
