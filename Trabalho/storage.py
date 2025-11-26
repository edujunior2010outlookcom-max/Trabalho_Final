import json
import os


CAMINHO_DATA = os.path.join(os.path.dirname(__file__), "data")


os.makedirs(CAMINHO_DATA, exist_ok=True)

CAMINHO_USUARIOS = os.path.join(CAMINHO_DATA, "usuarios.json")


def carregar_usuarios():
    """Lê o arquivo usuarios.json e retorna a lista de usuários.""" 
    try:
        with open(CAMINHO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return [] 


def salvar_usuarios(lista_usuarios):
    """Salva a lista de usuários no arquivo usuarios.json."""
    with open(CAMINHO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(lista_usuarios, f, indent=4, ensure_ascii=False)



CAMINHO_TAREFAS = os.path.join(CAMINHO_DATA, "tarefas.json")


def carregar_tarefas():
    """Lê o arquivo tarefas.json e retorna a lista de tarefas."""
    try:
        with open(CAMINHO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  
    except json.JSONDecodeError:
        return []  


def salvar_tarefas(lista_tarefas):
    """Salva a lista de tarefas no arquivo tarefas.json."""
    with open(CAMINHO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(lista_tarefas, f, indent=4, ensure_ascii=False)




CAMINHO_PROJETOS = os.path.join(CAMINHO_DATA, "projetos.json")


def carregar_projetos():
    """Lê o arquivo projetos.json e retorna a lista de projetos."""
    try:
        with open(CAMINHO_PROJETOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def salvar_projetos(lista_projetos):
    """Salva a lista de projetos no arquivo projetos.json."""
    with open(CAMINHO_PROJETOS, "w", encoding="utf-8") as f:
        json.dump(lista_projetos, f, indent=4, ensure_ascii=False)
