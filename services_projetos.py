from storage import carregar_projetos, salvar_projetos
from models import modelo_projeto
from utils import (
    validar_nome_projeto,
    validar_data,
    comparar_datas
)

def criar_projeto(nome, descricao, inicio, fim):
    projetos = carregar_projetos()

    #  Validações.
    if not validar_nome_projeto(nome):
        return False, "Nome do projeto inválido."
    print('Nome do projeto válido!')

    if not validar_data(inicio):
        return False, "Data de início inválida. Use DD/MM/YYYY."
    print('Data de ínicio válida!')

    if not validar_data(fim):
        return False, "Data final inválida. Use DD/MM/YYYY."
    print('Data final válida!')

    if not comparar_datas(inicio, fim):
        return False, "A data final deve ser igual ou posterior à inicial."
    print('A data final e inicial são válidas e foram salvas!')

    # Verifica duplicidade
    for p in projetos:
        if p["nome"].lower() == nome.lower():
            return False, "Já existe um projeto com esse nome."

    #Criar usando o MODELOS
    if descricao:
        descricao_final = descricao
    else:
        descricao_final = ""
        print("Não existe uma descrição de projeto!")

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
    return carregar_projetos()


def buscar_projetos(termo):
    termo = termo.lower()
    projetos = carregar_projetos()
    return [p for p in projetos if termo in p["nome"].lower()]


def atualizar_projeto(nome_antigo, novo_nome=None, nova_descricao=None,
                      novo_inicio=None, novo_fim=None):

    projetos = carregar_projetos()
    nome_antigo = nome_antigo.lower()

    projeto = None
    for p in projetos:
        if p["nome"].lower() == nome_antigo:
            projeto = p
            break

    if not projeto:
        return False, "Projeto não encontrado."

    # ---- Atualizações com validação ----
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
    projetos = carregar_projetos()
    nome = nome.lower()

    for p in projetos:
        if p["nome"].lower() == nome:
            projetos.remove(p)
            salvar_projetos(projetos)
            return True, "Projeto removido com sucesso."

    return False, "Projeto não encontrado."
