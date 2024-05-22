while True:
    # usuario informa os numeros
    x = str(input('informe o primeiro número: ')).replace(',', '.')
    y =str(input('informe o segundo núemro: ')).replace(',','.')

    # converte para numeros decimais
    x = float(x)
    y = float(y)

    print('operações disponíveis:\n')
    print('"+" para somar. ')
    print('"-" para subtrair. ')
    print('"*" para multiplcar. ')
    print('"/" para dividir. ')
    print('"%" para encontrar o resto da divisão. ')
    
    op = input('Operação desejada: ')

    match op:
        case'+':
            print(f'A soma é: {x + y}.')
        case'-':
            print(f'A subtração é: {x - y}.')
        case'*':
            print(f'A multiplicação é: {x * y}.')
        case'/':
            print(f'A divisão é: {x / y}.')
        case'%':
            print(f'O resto da divisão é: {x % y}.')
        case _:
            print('operação inválida')
            continue

# pergunta para o usuario se deseja continuar ou encerrar
    continuar =input('Deseja continuar (s/n)? ')

    # verifica a opção usuario
    if continuar == 's':
        continue
    elif continuar == 'n':
        break
    else:
        print('opção inválida')



