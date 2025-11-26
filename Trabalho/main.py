
from ui import (
    menu_principal,
    menu_usuario,
    menu_projetos,
    menu_tarefas,
    menu_relatorios
)

from services_usuario import (
    criar_usuario,
    listar_usuarios,
    buscar_usuarios,
    atualizar_usuario,
    remover_usuario
)

from services_projetos import (
    criar_projeto,
    listar_projetos,
    buscar_projetos,
    atualizar_projeto,
    remover_projeto
)

from services_tarefas import (
    criar_tarefa,
    listar_todas,
    listar_por_projeto,
    listar_por_responsavel,
    listar_por_status,
    atualizar_tarefa,
    remover_tarefa
)

from reports import (
    relatorio_usuarios,
    relatorio_projetos,
    relatorio_tarefas
)


def main():
    while True:
        opc = menu_principal()

        # ===================== USUÁRIOS ======================
        if opc == "1":
            while True:
                u = menu_usuario()

                if u == "1":
                    nome = input("Nome: ")
                    email = input("Email: ")
                    sexo = input("Sexo (M/F/O): ")
                    idade = input("Idade(Somente números): ")
                    cpf = input("CPF(Somente números): ")
                    ok, msg = criar_usuario(nome, email, sexo, idade, cpf)
                    print(msg)

                elif u == "2":
                    usuarios = listar_usuarios()
                    for usr in usuarios:
                        print(usr)

                elif u == "3":
                    termo = input("Buscar por: ")
                    tipo = input("Tipo (nome/email): ")
                    encontrados = buscar_usuarios(termo, tipo)
                    for usr in encontrados:
                        print(usr)

                elif u == "4":
                    ident = input("Nome ou email do usuário: ")
                    novo_nome = input("Novo nome (ou enter): ") or None
                    novo_email = input("Novo email (ou enter): ") or None
                    novo_sexo = input("Novo sexo (ou enter): ") or None
                    nova_idade = input("Nova idade (ou enter): ") or None
                    novo_cpf = input("Novo CPF (ou enter): ") or None

                    ok, msg = atualizar_usuario(
                        ident, novo_nome, novo_email,
                        novo_sexo, nova_idade, novo_cpf
                    )
                    print(msg)

                elif u == "5":
                    ident = input("Nome ou email do usuário: ")
                    ok, msg = remover_usuario(ident)
                    print(msg)

                elif u == "6":
                    break
                else:
                    print("Opção inválida!")


        # ============== PROJETOS ===============
        elif opc == "2":
            while True:
                p = menu_projetos()

                if p == "1":
                    nome = input("Nome do projeto: ")
                    desc = input("Descrição: ")
                    ok, msg = criar_projeto(nome, desc)
                    print(msg)

                elif p == "2":
                    for proj in listar_projetos():
                        print(proj)

                elif p == "3":
                    termo = input("Buscar projeto: ")
                    encontrados = buscar_projetos(termo)
                    for proj in encontrados:
                        print(proj)

                elif p == "4":
                    nome_velho = input("Nome atual: ")
                    novo_nome = input("Novo nome: ") or None
                    nova_desc = input("Nova descrição: ") or None
                    ok, msg = atualizar_projeto(nome_velho, novo_nome, nova_desc)
                    print(msg)

                elif p == "5":
                    nome = input("Nome do projeto: ")
                    ok, msg = remover_projeto(nome)
                    print(msg)

                elif p == "6":
                    break
                else:
                    print("Opção inválida!")


        # =================== TAREFAS ======================
        elif opc == "3":
            while True:
                t = menu_tarefas()

                if t == "1":
                    titulo = input("Título: ")
                    projeto = input("Projeto: ")
                    responsavel = input("Responsável: ")
                    status = input("Status: ")
                    prazo = input("Prazo (AAAA-MM-DD): ")
                    ok, msg = criar_tarefa(titulo, projeto, responsavel, status, prazo)
                    print(msg)

                elif t == "2":
                    for tar in listar_todas():
                        print(tar)

                elif t == "3":
                    ident = input("Título da tarefa: ")

                    novo_titulo = input("Novo título (ou Enter): ") or None
                    novo_projeto = input("Novo projeto (ou Enter): ") or None
                    novo_resp = input("Novo responsável (ou Enter): ") or None
                    novo_status = input("Novo status (ou Enter): ") or None
                    novo_prazo = input("Novo prazo (AAAA-MM-DD ou Enter): ") or None

                    ok, msg = atualizar_tarefa(
                        ident, novo_titulo, novo_projeto,
                        novo_resp, novo_status, novo_prazo
                    )
                    print(msg)

                elif t == "4":
                    ident = input("Título da tarefa: ")
                    ok, msg = remover_tarefa(ident)
                    print(msg)

                elif t == "5":
                    break
                else:
                    print("Opção inválida!")


        # ===================== RELATÓRIOS ============
        elif opc == "4":
            while True:
                r = menu_relatorios()

                if r == "1":
                    relatorio_usuarios()

                elif r == "2":
                    relatorio_projetos()

                elif r == "3":
                    relatorio_tarefas()

                elif r == "4":
                    break
                else:
                    print("Opção inválida!")


        elif opc == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()

