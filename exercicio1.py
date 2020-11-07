from modulo1 import converte_para_celsius, converte_para_fahrenheit


def teste1():
    try:
        retorno = converte_para_fahrenheit(0)
        assert retorno == 32.0
        print('Teste 1 Correto')
    except AssertionError:
        print('Teste 1 Errado')


def teste2():
    try:
        retorno = converte_para_fahrenheit(27)
        assert retorno == 80.6
        print('Teste 2 Correto')
    except AssertionError:
        print('Teste 2 Errado')


def teste3():
    try:
        retorno = converte_para_fahrenheit(95)
        assert retorno == 203.0
        print('Teste 3 Correto')
    except AssertionError:
        print('Teste 3 Errado')


def teste4():
    try:
        retorno = converte_para_celsius(32)
        assert retorno == 0
        print('Teste 4 Correto')
    except AssertionError:
        print('Teste 4 Errado')


def teste5():
    try:
        retorno = converte_para_celsius(41)
        assert retorno == 5.0
        print('Teste 5 Correto')
    except AssertionError:
        print('Teste 5 Errado')


def teste6():
    try:
        retorno = converte_para_celsius(95)
        assert retorno == 35.0
        print('Teste 6 Correto')
    except AssertionError:
        print('Teste 6 Errado')


teste1()
teste2()
teste3()
teste4()
teste5()
teste6()
