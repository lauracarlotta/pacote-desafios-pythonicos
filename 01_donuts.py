# ✅ bifurcação na execução do código através de condicionais
# ✅ tipos diferentes: começa com número e precisa retornar uma string.
#       (processo de tranformação de número para string).
# ✅ ATENÇÃO com a nomeação de variáveis
# ✅ fazer o exercício com apenas um return
# ✅ É possível simplificar o código? (RENOMEEI OS PARÂMETROS) => sERÁ POSSÍVEL SIMPLIFICÁ-LA MAIS TARDE?

"""
01. donuts

Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""
# todo !r - formatação de string PESQUISAR
# ✅ todo renomear os parametros da função test
# ✅ todo explicar if __name__ == '__main__'
        # =>Esse teste só será executado se esse arquivo for executado

def donuts(count):
    if count > 0 and count < 10:
        message = f'Number of donuts: {count}'

    else:
        message = 'Number of donuts: many'

    return message


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
    test(donuts, 4, 'Number of donuts: 4')
    test(donuts, 9, 'Number of donuts: 9')
    test(donuts, 10, 'Number of donuts: many')
    test(donuts, 99, 'Number of donuts: many')
    # breakpoint()

# -> breakpoint())
#(Pdb) donuts
#<function donuts at 0x7dd945d18900>
#(Pdb) dir(donuts)
#['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
#(Pdb) donuts.__name__
#'donuts'
