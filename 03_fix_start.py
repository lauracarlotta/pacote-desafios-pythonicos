# ✅ TODO usar o método replace
# ✅ TODO usar outros métodos do python
# ✅ TODO escrever em apenas uma linha

# 1 - substitui e substitui de novo
# 2 - quantas ocorrencias aparecem daquela letra
# 3 - replace a partir do indice 1  <================

# ==> Eliminar repetições, legibilidade, nomear variáveis com nomes semanticos e pequenos
"""
03. fix_start

Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.

Exemplo: 'babble' retorna 'ba**le'

Assuma que a string tem tamanho 1 ou maior.

Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""


def fix_start(s):
    # +++ SUA SOLUÇÃO +++
    # SOLUTION 3

    letter = s[0]
    new_word = ''
    for cont in range(len(s)):
        if s.find(letter, cont) and not cont == 0:
            new_word += s[cont].replace(letter, '*')
        else:
            new_word += s[cont]
        cont += 1
    return new_word


    # SOLUTION 2
    """new_string = ''
    for cont, value in enumerate(s):
        if cont == 0 or value != s[0]:
            new_string += value
        else:
            new_string += value.replace(s[0], '*')

    return new_string"""

    # SOLUTION 1
    return s[0] + s[1:].replace(s[0], '*') if len(s) > 1 else s

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
    test(fix_start, 'babble', 'ba**le')
    test(fix_start, 'aardvark', 'a*rdv*rk')
    test(fix_start, 'google', 'goo*le')
    test(fix_start, 'donut', 'donut')
    # test(fix_start, 'd', 'donut')
