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

        #USUÁRIOS

        if opc == "1":
            while True:
                u = menu_usuario()

                if u == "1":
                    nome = input("Nome: ")
                    email = input("Email: ")
                    sexo = input("Sexo (M/F/O): ")
                    idade = input("Idade (somente números): ")
                    cpf = input("CPF (somente números): ")

                    ok, msg = criar_usuario(nome, email, sexo, idade, cpf)
                    print(msg)

                elif u == "2":
                    usuarios = listar_usuarios()
                    if not usuarios:
                        print("Nenhum usuário cadastrado.")
                    else:
                        for usr in usuarios:
                            print(usr)

                elif u == "3":
                    termo = input("Buscar por: ")
                    tipo = input("Tipo (nome/email): ")
                    encontrados = buscar_usuarios(termo, tipo)

                    if not encontrados:
                        print("Nenhum usuário encontrado.")
                    else:
                        for usr in encontrados:
                            print(usr)

                elif u == "4":
                    ident = input("Nome ou email do usuário: ")

                    novo_nome = input("Novo nome (enter p/ manter): ") or None
                    novo_email = input("Novo email (enter p/ manter): ") or None
                    novo_sexo = input("Novo sexo (enter p/ manter): ") or None
                    nova_idade = input("Nova idade (enter p/ manter): ") or None
                    novo_cpf = input("Novo CPF (enter p/ manter): ") or None

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


        #PROJETOS
        elif opc == "2":
            while True:
                p = menu_projetos()

                if p == "1":
                    nome = input("Nome do projeto: ")
                    desc = input("Descrição: ")
                    inicio = input("Data de início (DD/MM/YYYY): ")
                    fim = input("Data final (DD/MM/YYYY): ")

                    ok, msg = criar_projeto(nome, desc, inicio, fim)
                    print(msg)

                elif p == "2":
                    projetos = listar_projetos()
                    if not projetos:
                        print("\nNenhum projeto cadastrado.")
                    else:
                        for proj in projetos:
                            print(proj)

                elif p == "3":
                    termo = input("Buscar projeto: ")
                    encontrados = buscar_projetos(termo)

                    if not encontrados:
                        print("Nenhum projeto encontrado.")
                    else:
                        for proj in encontrados:
                            print(proj)

                elif p == "4":
                    nome_velho = input("Nome atual do projeto: ")

                    novo_nome = input("Novo nome (Enter p/ manter): ") or None
                    nova_desc = input("Nova descrição (Enter p/ manter): ") or None
                    novo_inicio = input("Nova data de início (DD/MM/YYYY ou Enter): ") or None
                    novo_fim = input("Nova data final (DD/MM/YYYY ou Enter): ") or None

                    ok, msg = atualizar_projeto(
                        nome_velho,
                        novo_nome,
                        nova_desc,
                        novo_inicio,
                        novo_fim
                    )
                    print(msg)

                elif p == "5":
                    nome = input("Nome do projeto: ")
                    ok, msg = remover_projeto(nome)
                    print(msg)

                elif p == "6":
                    break

                else:
                    print("Opção inválida!")


        #TAREFAS

        elif opc == "3":
            while True:
                t = menu_tarefas()

                if t == "1":
                    titulo = input("Título da tarefa: ")
                    projeto = input("Projeto vinculado: ")
                    responsavel = input("Responsável: ")
                    status = input("Status (pendente/andamento/concluída): ")
                    prazo = input("Prazo (AAAA-MM-DD): ")

                    ok, msg = criar_tarefa(titulo, projeto, responsavel, status, prazo)
                    print(msg)

                elif t == "2":
                    tarefas = listar_todas()
                    if not tarefas:
                        print("Nenhuma tarefa cadastrada.")
                    else:
                        for tar in tarefas:
                            print(tar)

                elif t == "3":
                    ident = input("Título da tarefa: ")

                    novo_titulo = input("Novo título (Enter p/ manter): ") or None
                    novo_projeto = input("Novo projeto (Enter p/ manter): ") or None
                    novo_resp = input("Novo responsável (Enter p/ manter): ") or None
                    novo_status = input("Novo status (Enter p/ manter): ") or None
                    novo_prazo = input("Novo prazo (AAAA-MM-DD ou Enter): ") or None

                    ok, msg = atualizar_tarefa(
                        ident,
                        novo_titulo,
                        novo_projeto,
                        novo_resp,
                        novo_status,
                        novo_prazo
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


        #RELATÓRIOS

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
