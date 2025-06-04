from util import limpar_tela

def ler_opcao(lim_sup):
    # ler a opção ate q seja valida 
    op = input('Escolha uma opção: ')
    
    if 0 <= op <= lim_sup:
        return op
    print('Você não digitou um op válida!')
    return -1


def menu_principal():
    limpar_tela()
    print('-----> MENU <-----')
    print('1 - Cadastrar')
    print('2 - Matricular')
    print('3 - Consultar')
    print('4 - Relatório')
    print('0 - Sair')
    op = ler_opcao(4)



def menu_cadastro():
    limpar_tela()
    print('-----> Menu Cadastrar <-----')
    print('1 - aluno')
    print('2 - professor')
    print('3 - turma')
    print('0 - voltar')
    op = ler_opcao(4)
