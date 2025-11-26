#SEVIÇOS DE TAREFA. BASE DAS FUNÇÕES DE TAREFAS

from storage import carregar_tarefas, salvar_tarefas
from models import modelo_tarefa
from utils import (
    validar_titulo_tarefa,
    validar_status_tarefa,
    validar_prazo
)

def listar_todas():
    return carregar_tarefas()

def criar_tarefa(titulo, projeto, responsavel, status, prazo):
    tarefas = carregar_tarefas()

    if not validar_titulo_tarefa(titulo):
        return False, "O título não pode ser vazio."

    if not validar_status_tarefa(status):
        return False, "Status inválido. Use: pendente, andamento ou concluída."

    if not validar_prazo(prazo):
        return False, "O prazo deve estar no formato YYYY-MM-DD."

    for t in tarefas:
        if t["titulo"].lower() == titulo.lower():
            return False, "Já existe uma tarefa com esse título."

    nova = modelo_tarefa(
        titulo=titulo,
        projeto=projeto,
        responsavel=responsavel,
        status=status.lower(),
        prazo=prazo
    )

    tarefas.append(nova)
    salvar_tarefas(tarefas)
    return True, "Tarefa cadastrada com sucesso."


def listar_tarefas():
    return carregar_tarefas()


def listar_por_projeto(nome_projeto):
    tarefas = carregar_tarefas()
    return [t for t in tarefas if t["projeto"].lower() == nome_projeto.lower()]


def listar_por_responsavel(nome_responsavel):
    tarefas = carregar_tarefas()
    return [t for t in tarefas if t["responsavel"].lower() == nome_responsavel.lower()]


def listar_por_status(status):
    tarefas = carregar_tarefas()
    return [t for t in tarefas if t["status"].lower() == status.lower()]


def atualizar_tarefa(titulo, novo_titulo=None, novo_projeto=None,
                     novo_responsavel=None, novo_status=None, novo_prazo=None):

    tarefas = carregar_tarefas()
    titulo_lower = titulo.lower()

    tarefa = None
    for t in tarefas:
        if t["titulo"].lower() == titulo_lower:
            tarefa = t
            break

    if not tarefa:
        return False, "Tarefa não encontrada."


    if novo_titulo:
        if not validar_titulo_tarefa(novo_titulo):
            return False, "Título inválido."
        tarefa["titulo"] = novo_titulo

    if novo_projeto:
        tarefa["projeto"] = novo_projeto

    if novo_responsavel:
        tarefa["responsavel"] = novo_responsavel

    if novo_status:
        if not validar_status_tarefa(novo_status):
            return False, "Status inválido."
        tarefa["status"] = novo_status.lower()

    if novo_prazo:
        if not validar_prazo(novo_prazo):
            return False, "O prazo deve estar no formato YYYY-MM-DD."
        tarefa["prazo"] = novo_prazo

    salvar_tarefas(tarefas)
    return True, "Tarefa atualizada com sucesso."


def concluir_tarefa(titulo):
    return atualizar_tarefa(titulo, novo_status="concluída")


def reabrir_tarefa(titulo):
    return atualizar_tarefa(titulo, novo_status="pendente")



def remover_tarefa(titulo):
    tarefas = carregar_tarefas()
    titulo_lower = titulo.lower()

    for t in tarefas:
        if t["titulo"].lower() == titulo_lower:
            tarefas.remove(t)
            salvar_tarefas(tarefas)
            return True, "Tarefa removida com sucesso."

    return False, "Tarefa não encontrada."
