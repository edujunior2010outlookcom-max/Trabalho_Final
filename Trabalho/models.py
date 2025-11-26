def modelo_usuario(nome, email, sexo, idade, cpf):
    """
    Estrutura base de um usuário.
    Nenhuma validação ocorre aqui.
    """
    return {
        "nome": nome,
        "email": email.lower(),
        "sexo": sexo.upper(),
        "idade": int(idade),
        "cpf": cpf
    }
    

# TAREFAS
def modelo_tarefa(titulo, projeto, responsavel, status, prazo):
    """
    Estrutura base de uma tarefa.
    """
    return {
        "titulo": titulo,
        "projeto": projeto,           # nome do projeto ao qual pertence
        "responsavel": responsavel,   # e-mail ou nome do usuário
        "status": status,             # pendente / andamento / concluída
        "prazo": prazo                # YYYY-MM-DD (string)
    }


#  PROJETOS 
def modelo_projeto(nome, descricao, inicio, fim):
    """
    Estrutura base de um projeto.
    """
    return {
        "nome": nome,
        "descricao": descricao,
        "inicio": inicio,   # datas no formato YYYY-MM-DD ou DD/MM/YYYY
        "fim": fim
    }
