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


