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
    


def modelo_tarefa(titulo, projeto, responsavel, status, prazo):
    """
    Estrutura base de uma tarefa.
    """
    return {
        "titulo": titulo,
        "projeto": projeto,           
        "responsavel": responsavel,   
        "status": status,             
        "prazo": prazo                
    }


def modelo_projeto(nome, descricao, inicio, fim):
    """
    Estrutura base de um projeto.
    """
    return {
        "nome": nome,
        "descricao": descricao,
        "inicio": inicio,   
        "fim": fim
    }
