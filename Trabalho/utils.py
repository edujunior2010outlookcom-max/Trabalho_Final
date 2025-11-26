import datetime
import re


def validar_email(email: str) -> bool:
    """Verifica se o email possui formato válido."""
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(padrao, email))


def validar_idade(idade: str | int) -> bool:
    """Idade deve ser um número inteiro positivo."""
    try:
        idade = int(idade)
        return idade > 0
    except ValueError:
        return False


def validar_sexo(sexo: str) -> bool:
    """Aceita apenas M, F ou O (outro)."""
    if not isinstance(sexo, str):
        return False
    return sexo.upper() in ["M", "F", "O"]


def validar_cpf(cpf: str) -> bool:
    """Validação simples de formato para o trabalho."""
    return cpf.isdigit() and len(cpf) == 11



def validar_nome_projeto(nome: str) -> bool:
    """Nome não pode ser vazio ou apenas espaços."""
    return isinstance(nome, str) and len(nome.strip()) > 0


def validar_data(data_str: str) -> bool:
    """Valida datas no formato DD/MM/YYYY."""
    try:
        datetime.datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def comparar_datas(inicio: str, fim: str) -> bool:
    """Retorna True se a data final for igual ou depois da inicial."""
    try:
        d1 = datetime.datetime.strptime(inicio, "%d/%m/%Y")
        d2 = datetime.datetime.strptime(fim, "%d/%m/%Y")
        return d2 >= d1
    except ValueError:
        return False



STATUS_VALIDOS = ["pendente", "andamento", "concluída"]

def validar_titulo_tarefa(titulo: str) -> bool:
    """Título não pode ser vazio."""
    return isinstance(titulo, str) and len(titulo.strip()) > 0


def validar_status_tarefa(status: str) -> bool:
    """Valida status da tarefa."""
    if not isinstance(status, str):
        return False
    return status.lower() in STATUS_VALIDOS


def validar_prazo(prazo: str) -> bool:
    """Prazo deve estar no formato YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(prazo, "%Y-%m-%d")
        return True
    except ValueError:
        return False



def formatar_nome(nome: str) -> str:
    """Padroniza nome com primeira letra maiúscula."""
    return nome.strip().title()


def formatar_email(email: str) -> str:
    """Email sempre minúsculo."""
    return email.strip().lower()
