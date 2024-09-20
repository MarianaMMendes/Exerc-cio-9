# 1 - biblioteca, framework e referencias externas


import pytest #framework de teste de unidade

# referenciar as funções que são testadas
from Area.Area import area_do_quadrado, area_do_retangulo, area_do_triangulo

from utils.utils import ler_csv # função de leitura de arquivos csv
# 2- Testes

def test_area_do_quadrado():

    # Padrão / Starndard AAA (se diz Triple A) = Arrange, Act, Assert
    
    # Arrange / Prepara / Configura
    # Dados de entrada e saída
    lado =2

    resultado_esperado = 4

    # Act / Executa
    resultado_obtido = area_do_quadrado(lado) 
    
    #Assert / Valida

    assert resultado_esperado == resultado_obtido

def test_area_do_retangulo():

    # Prepara
    base = 12
    altura = 10
    resultado_esperado = 120

    # Excecuta
    resultado_obtido = area_do_retangulo(base, altura)

    # Valida

    assert resultado_esperado == resultado_obtido

def test_area_do_triangulo():

    # Prepara
    base = 12
    altura = 10
    resultado_esperado = 60

    # Excecuta
    resultado_obtido = area_do_triangulo(base,altura)

    # Valida

    assert resultado_esperado == resultado_obtido

# Dados em uma lista


@pytest.mark.parametrize('lado, resultado_esperado',
                         [ # array / matriz
                            (50, 2500), # tupla / registro 
                            (40, 1600),
                            (20, 400),
                            (100, 10000)
                         ]
                         )
def test_area_do_quadrado_lista(lado, resultado_esperado):
    
    # Arrange / Prepara / Configura
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista

    # Act / Executa
    resultado_obtido = area_do_quadrado(lado)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido


# Dados em um arquivo

@pytest.mark.parametrize('base, altura, resultado_esperado',
                           ler_csv('./fixtures/massa_area_do_retangulo.csv')
                         )

def test_area_doretangulo_csv(base, altura, resultado_esperado):
    
    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert

    # Arrange / Prepara / Configura
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista

    # Act / Executa
    resultado_obtido = area_do_retangulo(float(base), float(altura))

    # Assert / Valida
    assert float(resultado_esperado) == resultado_obtido