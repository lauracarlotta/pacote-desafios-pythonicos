# - usar o slice()
# - fazer o código em uma única linha
# - (Se muito fácil) usar while pra contar as letras na mão

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

function_both_ends = both_ends('hello')
print(function_both_ends)