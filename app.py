
import os

restaurantes = ['Limongi', 'Arabissimo']

def exibir_nome_do_programa():
    print('🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢')

def exibir_opcoes():

    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def finalizar_app():
    exibir_subitulo('Finalizando programa')


def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()
   

def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def exibir_subitulo(texto):
    os.system('cls')
    print(texto)
    print

def cadastrar_restaurantes():
    exibir_subitulo('cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante : -')
    restaurantes.append(nome_do_restaurante)
    print(f' O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    

def listar_restaurantes():
    exibir_subitulo('Listando restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()
    main()


def escolher_opcao():
    try:
        opcao_escolhida =int (input('Escolha uma opção: '))
        #opcao_escolhida = int (opcao_escolhida)

        if opcao_escolhida ==1:
            print('Cadastrar restaurantes')
            cadastrar_restaurantes()
        elif opcao_escolhida ==2:
            print('Listar restaurantes')
            Listar_restaurantes()
        elif opcao_escolhida ==3:
            print('Ativar restaurantes')
        elif opcao_escolhida ==4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


    
if __name__=='__main__':
    main()

    