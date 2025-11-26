from storage import carregar_projetos, salvar_projetos
from models import modelo_projeto
from utils import (
    validar_nome_projeto,
    validar_data,
    comparar_datas
)


def criar_projeto(nome, descricao, inicio, fim):
    projetos = carregar_projetos()

    #Validações 
    if not validar_nome_projeto(nome):
        return False, "Nome do projeto inválido."

    if not validar_data(inicio):
        return False, "Data de início inválida. Use DD/MM/YYYY."

    if not validar_data(fim):
        return False, "Data final inválida. Use DD/MM/YYYY."

    if not comparar_datas(inicio, fim):
        return False, "A data final deve ser igual ou posterior à inicial."

    # Verifica duplicidade
    for p in projetos:
        if p["nome"].lower() == nome.lower():
            return False, "Já existe um projeto com esse nome."

    #Criar usando o MODELO 
    if not descricao:
        descricao_final = ""
        print("Descrição vazia (permitido).")
    else:
        descricao_final = descricao

    novo = modelo_projeto(
        nome=nome,
        descricao=descricao_final,
        inicio=inicio,
        fim=fim
    )

    projetos.append(novo)
    salvar_projetos(projetos)
    return True, "Projeto criado com sucesso."


def listar_projetos():
    projetos = carregar_projetos()

    if not projetos:
        return False, "Nenhum projeto cadastrado."

    return True, projetos


def buscar_projetos(termo):
    termo = termo.lower().strip()

    if not termo:
        return False, "Digite algo para buscar."

    projetos = carregar_projetos()

    if not projetos:
        return False, "Nenhum projeto cadastrado."

    encontrados = []

    for p in projetos:
        nome_proj = str(p.get("nome", "")).lower()
        if termo in nome_proj:
            encontrados.append(p)

    if not encontrados:
        return False, "Nenhum projeto encontrado para esse termo."

    return True, encontrados


def atualizar_projeto(nome_antigo, novo_nome=None, nova_descricao=None,
                      novo_inicio=None, novo_fim=None):

    projetos = carregar_projetos()
    nome_antigo = nome_antigo.lower().strip()

    if not nome_antigo:
        return False, "O nome antigo não pode ser vazio."

    # Localizar o projeto
    projeto = None
    for p in projetos:
        if p["nome"].lower() == nome_antigo:
            projeto = p
            break

    if not projeto:
        return False, "Projeto não encontrado."

    #Atualizações com validação
    if novo_nome:
        if not validar_nome_projeto(novo_nome):
            return False, "Nome inválido."

        # Verifica duplicidade
        for p in projetos:
            if p is not projeto and p["nome"].lower() == novo_nome.lower():
                return False, "Já existe outro projeto com esse nome."

        projeto["nome"] = novo_nome

    if nova_descricao is not None:
        projeto["descricao"] = nova_descricao

    if novo_inicio:
        if not validar_data(novo_inicio):
            return False, "Data inicial inválida."
        projeto["inicio"] = novo_inicio

    if novo_fim:
        if not validar_data(novo_fim):
            return False, "Data final inválida."

        # Confere coerência das datas
        inicio_valida = projeto["inicio"]
        if not comparar_datas(inicio_valida, novo_fim):
            return False, "Data final não pode ser antes da inicial."

        projeto["fim"] = novo_fim

    salvar_projetos(projetos)
    return True, "Projeto atualizado com sucesso."


def remover_projeto(nome):
    if not validar_nome_projeto(nome):
        return False, "Nome inválido."

    projetos = carregar_projetos()

    if not projetos:
        return False, "Nenhum projeto cadastrado."

    nome = nome.lower()
    removido = False
    nova_lista = []


    for p in projetos:
        if p["nome"].lower() == nome:
            removido = True
        else:
            nova_lista.append(p)

    if not removido:
        return False, "Projeto não encontrado."

    salvar_projetos(nova_lista)
    return True, "Projeto removido com sucesso."
