import os  

restaurantes = [
    {'nome': 'Praça', 'categoria':'Japonesa', 'ativo':False}, 
    {'nome': 'Pizzaria', 'categoria': 'Italiana', 'ativo':True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo':False}
]

def exibir_nome_programa():
    print("""
        🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢
        """) #aspas triplas servem para pular linha tambem """


def exibir_opcoes():
    print('1.  Cadastrar Restaurante')
    print('2.  Listar Restaurantes')
    print('3.  Ativar Restaurante')
    print('4.  Finalizar o app\n')


def finalizar_app():
    exibir_subtitulo('Finalizar App')
    print()


def voltar_menu_principal():
    input('\nDigite uma tecla para volar ao menu ')
    main()


def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()
 
 
    
def opcao_invalida():
    print('Opção Invalida! \n')
    voltar_menu_principal()



def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    restaurantes.append(nome_restaurante) #passando o nome do restaurante para a lista
    print (f' O restaurante {nome_restaurante} foi cadastrado com sucesso.')
    
    voltar_menu_principal()



def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes')
    
    for restaurante in restaurantes: #restaurante é a variavel nova #restaurantes é a lista
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' {nome_restaurante}')
        
    voltar_menu_principal()

# def listar_restaurantes():
#     exibir_subtitulo('Listar Restaurantes')
    
#     for restaurante in restaurantes: #restaurante é a variavel nova #restaurantes é a lista
#         print(f' -{restaurante}')
        
#     voltar_menu_principal()
        
    
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            print('Finalizar app')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()
    
    


