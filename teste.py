from modulo1 import somar, calcular_fatorial


def test_soma1():
    try:
        resultado = somar(10, 20)
        assert type(resultado) == int, 'O resultado não é inteiro'
        assert resultado % 2 == 0, 'O resultado não é par'
        assert resultado == 30, 'O resultado está errado'
        print('Correto')
    except AssertionError as x:
        print('Erro:', x)


def test_soma2():
    try:
        resultado = somar(-5, -10)
        assert resultado == -15
        print('Correto')
    except AssertionError:
        print('Erro')


def test_fatorial_5():
    try:
        resultado = calcular_fatorial(5)
        assert resultado == 120
        print('Fatorial correto')
    except AssertionError:
        print('Erro no fatorial')


test_soma1()
test_soma2()
test_fatorial_5()
