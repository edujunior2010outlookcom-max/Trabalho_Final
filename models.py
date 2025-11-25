## -------------USUARIO-------------
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


