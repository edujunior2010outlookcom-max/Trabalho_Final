#CADASTRO E OPÇÕES DE USUARIO

from storage import carregar_usuarios, salvar_usuarios
from models import modelo_usuario
from utils import (
    validar_email,
    validar_idade,
    validar_sexo,
    validar_cpf,
    formatar_nome,
    formatar_email
)


def criar_usuario(nome, email, sexo, idade, cpf):
    usuarios = carregar_usuarios()

    if not validar_email(email):
        return False, "E-mail inválido."

    if not validar_idade(idade):
        return False, "Idade inválida."

    if not validar_sexo(sexo):
        return False, "Sexo deve ser M, F ou O."

    if not validar_cpf(cpf):
        return False, "CPF deve ter 11 dígitos numéricos."

    email_formatado = formatar_email(email)

    for u in usuarios:
        if u["email"] == email_formatado:
            return False, "E-mail já cadastrado."

    novo = modelo_usuario(
        formatar_nome(nome),
        email_formatado,
        sexo,
        idade,
        cpf
    )

    usuarios.append(novo)
    salvar_usuarios(usuarios)
    return True, "Usuário cadastrado com sucesso."


def listar_usuarios():
    return carregar_usuarios()


def buscar_usuarios(termo, tipo):
    usuarios = carregar_usuarios()
    termo = termo.lower()

    if tipo == "nome":
        return [u for u in usuarios if termo in u["nome"].lower()]

    if tipo == "email":
        return [u for u in usuarios if termo in u["email"].lower()]

    return []


def atualizar_usuario(identificador, novo_nome=None, novo_email=None,
                      novo_sexo=None, nova_idade=None, novo_cpf=None):

    usuarios = carregar_usuarios()
    identificador = identificador.lower()

    usuario = None
    for u in usuarios:
        if identificador in u["nome"].lower() or identificador == u["email"].lower():
            usuario = u
            break

    if not usuario:
        return False, "Usuário não encontrado."

    if novo_nome:
        usuario["nome"] = formatar_nome(novo_nome)

    if novo_email:
        if not validar_email(novo_email):
            return False, "E-mail inválido."

        novo_email = formatar_email(novo_email)

        for u in usuarios:
            if u is not usuario and u["email"] == novo_email:
                return False, "E-mail já cadastrado por outro usuário."

        usuario["email"] = novo_email

    if novo_sexo:
        if not validar_sexo(novo_sexo):
            return False, "Sexo inválido."
        usuario["sexo"] = novo_sexo.upper()

    if nova_idade:
        if not validar_idade(nova_idade):
            return False, "Idade inválida."
        usuario["idade"] = int(nova_idade)

    if novo_cpf:
        if not validar_cpf(novo_cpf):
            return False, "CPF inválido."
        usuario["cpf"] = novo_cpf

    salvar_usuarios(usuarios)
    return True, "Usuário atualizado com sucesso."


def remover_usuario(identificador):
    usuarios = carregar_usuarios()
    identificador = identificador.lower()

    for u in usuarios:
        if identificador in u["nome"].lower() or identificador == u["email"].lower():
            usuarios.remove(u)
            salvar_usuarios(usuarios)
            return True, "Usuário removido com sucesso."

    return False, "Usuário não encontrado."
