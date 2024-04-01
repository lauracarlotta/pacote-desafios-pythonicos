# ✅ usar o slice()
# ✅ fazer o código em uma única linha
# ✅ (Se muito fácil) usar while pra contar as letras na mão

"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""

def both_ends(s):
    # +++ SUA SOLUÇÃO +++
    # SOLUTION 4 - COM WHILE
    # SOLUTION 4 - COM WHILE
    string_received = s
    result = ''
    if len(string_received) < 2:
        result = ''
    else:
        cont = 0
        while cont != 2:
            result += s[cont]
            cont += 1
        cont = 2
        while cont != 0:
            result += s[len(s) - cont]
            cont -= 1
    return result

    # SOLUTION 3
    """return '' if len(s) < 2 else s[slice(2)] + s[slice(-2, len(s))]"""

    # SOLUTION 2
    """string_received = s
    if len(string_received) < 2:
        result = ''
    else:
        initial_string = slice(2)
        final_string = slice(-2, len(string_received))
        result = string_received[initial_string] + string_received[final_string]
    return result"""

    #SOLUTION 1
    """string_received = s
    if len(string_received) < 2:
        result = ''
    else:
        result = f'{string_received[0]}{string_received[1]}{string_received[-2]}{string_received[-1]}'
    return result"""


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(function, input, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    output = function(input)

    if output == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {function.__name__}({input!r}) retornou {output!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')
