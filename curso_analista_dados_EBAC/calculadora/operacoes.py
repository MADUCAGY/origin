def soma():
    soma = 0
    print('\n\n')
    print('----------SOMA----------')
    print('\n\n')
    numeros = int(input('Quantos números deseja somar? '))
    for i in range(1,numeros+1):
        num = float(input(f'Digite o número {i}° que deseja somar: '))
        print('\n\n')
        soma = soma + num
    print('\n\n')
    print(f'Sua soma é {soma}.')
    sair()

def subtracao():
    subtracao = 0
    print('\n\n')
    print('----------SUBTRACAO----------')
    print('\n\n')
    numeros = int(input('Quantos números deseja subtrair? '))
    print('\n\n')
    for i in range(1,numeros+1):
        num = float(input(f'Digite o número {i}° que deseja subtrair: '))
        subtracao = subtracao - num
    print('\n\n')
    print(f'Seu resultado foi:{subtracao}')
    sair()

def multiplicacao():
    multiplicacao = 1
    print('\n\n')
    print('----------MULTIPLICACAO----------')
    print('\n\n')
    numeros = int(input('Quantos números deseja multiplicar? '))
    print('\n\n')
    for i in range(1,numeros+1):
        num = float(input(f'Digite o número {i}° que deseja multiplicar: '))
        multiplicacao = multiplicacao * num
    print('\n\n')
    print(f'Seu resultado foi:{multiplicacao}')
    sair()

def divisao():
    divisao = 1
    print('\n\n')
    print('----------DIVISAO----------') 
    print('\n\n')   
    numeros = int(input('Quantos números deseja dividir? '))
    for i in range(1,numeros+1):
        num = float(input(f'Digite o número {i}° que deseja dividir: '))
        divisao = divisao / num
    print('\n\n')
    print(f'Seu resultado foi:{divisao}')
    sair()

def sair():
    print('\n\n')
    print('----------SAIR----------')
    print('\n\n')
    sair = int(input('Deseja realizar outra operacao? \n1 - Sim \n2 - Não: '))
    if sair == 1: 
        main()
    else:
        print('\n\n')
        print('Obrigado por utilizar a calculadora!')
        return 0

  
def main():
    print('\n\n')
    print('-------Calculadora de operacoes básicas-------')
    print('---------Escolha uma das opcoes abaixo--------')
    print('\n\n')
    print('1 - Soma; \n2 - Subtracao; \n3 - Multiplicacao; \n4 - Divisão')
    print('\n\n')
    opcao = int(input(('Digite o número da opcao desejada: ')))
    

    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    else:
        print('Desculpe, só consigo reconhecer uma das opcoes anteriores.')
        sair()


        
