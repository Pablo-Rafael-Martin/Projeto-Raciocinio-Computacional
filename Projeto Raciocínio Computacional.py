# Feito por: Pablo Rafael Caramori Fontes Martin. Em andamento

menuPrincipal = ['Estudantes', 'Disciplinas', 'Professores', 'Turmas', 'Matrículas']
menuDeOperacoes = ['Incluir', 'Listar', 'Atualizar', 'Excluir']

listaEstudantes = []
listaDisciplinas = []
listaProfessores = []
listaTurmas = []
listaMatriculas = []

def mostrarMenuPrincipal():
    # printar o menu
    print('----- MENU PRINCIPAL ----- \n ')
    for i in range(0, len(menuPrincipal)):
        print(f'{i+1}. {menuPrincipal[i]}')
    print('6. Sair \n')

def mostrarMenuDeOperacoes(menuEscolhido):
    # printar o menu de operações
    print(f'***** [{menuEscolhido.upper}] MENU DE OPERAÇÕES ***** \n')
    for i in range(0, len(menuDeOperacoes)):
        print(f'{i+1}. {menuDeOperacoes[i]}')
    print('5. Voltar \n')
    gerenciarMenuDeOperacoes(menuEscolhido)

def acaoDoMenuPrincipal(inputDoUsuario):
    if ((inputDoUsuario == 6) or (inputDoUsuario == 'sair')):
        print('Saindo do programa')
        return 1

    elif ((inputDoUsuario == 1) or (inputDoUsuario == 'estudantes')):
        mostrarMenuDeOperacoes(listaEstudantes)
    
    elif ((inputDoUsuario == 2) or (inputDoUsuario == 'disciplinas')):
        mostrarMenuDeOperacoes(listaDisciplinas)
    
    elif ((inputDoUsuario == 3) or (inputDoUsuario == 'professores')):
        mostrarMenuDeOperacoes(listaProfessores)
    
    elif ((inputDoUsuario == 4) or (inputDoUsuario == 'matrículas')):
        mostrarMenuDeOperacoes(listaMatriculas) 
    
    elif ((inputDoUsuario == 5) or (inputDoUsuario == 'turmas')):
        mostrarMenuDeOperacoes(listaTurmas)
    
    else:
        print('Comando desconhecido, por favor digite novamente!')
        acaoDoMenuPrincipal(inputDoUsuario)
            
def gerenciarMenuDeOperacoes(menuEscolhido):
    #todo: incluir
    #todo: listar
    #todo: atualizar
    #todo: excluir
    #todo: voltar ao menu principal
    print('hello world')



while True:
    mostrarMenuPrincipal()
    # ação do usuário
    inputDoUsuario = input('O que deseja fazer? ')
    try:
        inputDoUsuario = int(inputDoUsuario)
    except:
        inputDoUsuario = inputDoUsuario.lower()        

    # realizar a ação
    if acaoDoMenuPrincipal(inputDoUsuario) == 1:
        break

# Ao rodar, puxa a função mostrarMenuPrincipal, que exibe o menu principal. As escolhas do usuário são gerenciada pela função acaoDoMenuPrincipal. Se a escolha do usuário for válida, ela puxa a função
# mostrarMenuDeOperacoes, que puxa a função gerenciarMenuDeOperacoes e passa para ela o menu escolhido pelo usuário. 