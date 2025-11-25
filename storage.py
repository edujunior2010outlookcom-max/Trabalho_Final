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


