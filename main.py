def triplo(numero1):    
    return numero1 * 3
def quadrado(numero2):
    return numero2 ** 2 

while True:
    print('========MENU========')
    print('1 - calcular o triplo')
    print('2 - calcular o quadrado')
    print('3 - somar o triplo + quadrado')
    print('0 - sair')
    opcao = input('BEM VINDO AO MEU PROGRAMA, ESCOLHA UMA DAS OPCÕES ACIMA:')

    try:
        if opcao == '1':
            num = int(input('digite um número:'))
            print('o resultado é', triplo(num))

        elif opcao == '2':
            num = int(input('digite um número:'))
            print('o resultado é', quadrado(num))

        elif opcao == '3':
        
            numero1 = int(input('digite o numero que vai ser triplicado:'))
            numero2 = int(input('digite o numero que vai ser elevado ao quadrado:'))

            resultado = triplo(numero1) + quadrado(numero2)
            print('o resultado é', resultado)

        elif opcao == '0':
            print('saindo do programa, aguarde.....')
            print('fim do programa')
            break
        
        else:
            print('você não digitou uma das opções, tente novamente')

    except ValueError:
        print('você não digitou um número inteiro, tente novamente')