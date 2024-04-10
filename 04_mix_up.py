"""
04. mix_up

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Assuma que a e b tem tamanho 2 ou maior.
"""
# ✅ TODO utilizando o método replace()
# ✅ TODO utilizando o método slice()
# ✅ TODO juntar as strings com concatenação ou método join()   JOIN
# ✅ TODO fazer tudo numa só linha
# ✅ TODO validação tendo dois caracteres ou mais

def mix_up(a, b):
    # +++ SUA SOLUÇÃO +++

    # NOVA SOLUÇÃO LAURA
    # SOLUÇÃO 5

    if len(a) <= 2 and len(b) <= 2:
        return f'{a} {b}'

    two_letters_a = a[0:2]
    two_letters_b = b[0:2]
    completed_letters_a = two_letters_a + b[2:]
    completed_letters_b = two_letters_b + a[2:]
    result =  f'{completed_letters_b} {completed_letters_a}'
    # breakpoint()

    return result


    """# SOLUÇÃO WELL
    if len(one) <= 2 or len(two) <=2:
        return f"{one} {two}"

    first_word_letter = one[0:2]
    second_word_letter = two[0:2]

    first_word = f"{second_word_letter + one[2:]}"
    second_word = f"{first_word_letter + two[2:]}"
    # breakpoint()
    result = f"{first_word} {second_word}"

    return result"""


    # SOLUÇÃO 4
    """if len(a) > 2 and len(b) > 2:
        list_names = [b, a]

        for cont in range(len(list_names)):
            letter_0 = b
            letter_1 = a

            for cont in range(2):
                list_names[cont] = list_names[cont].replace(letter_0[0], letter_1[0])
                list_names[cont] = list_names[cont].replace(letter_0[1], letter_1[1])

                letter_0 = a
                letter_1 = b

        list_names.reverse()
        result = ' '.join(list_names)
    else:
        result = f'{a} {b}'
    return result"""


    # SOLUÇÃO 3
    """
    return f'{b[0] + b[1] + a[2:]} {a[0] + a[1] + b[2:]}' if len(a) > 2 or len(b) > 2 else f'{a} {b}'
    """

    # SOLUÇÃO 2
    """string_a = ''
    string_b = ''
    if len(a) > 2 and len(b) > 2:
        for cont in range(2):
            string_a += a[cont].replace(a[cont], b[cont])
            string_b += b[cont].replace(b[cont], a[cont])
        indice_a = slice(2, len(a))
        string_a += a[indice_a]
        indice_b = slice(2, len(b))
        string_b += b[indice_b]
        completed_sentence = f'{string_a} {string_b}'
    else:
        completed_sentence = f'{a} {b}'
    return completed_sentence"""

    # SOLUÇÃO 1
    """string_a = ''
    string_b = ''
    if len(a) > 2 and len(b) > 2:
        for cont in range(2):
            string_a += b[cont]
            string_b += a[cont]
        string_a += a[2:]
        string_b += b[2:]
        new_string = f'{string_a} {string_b}'
        # print(f'{string_a} {string_b}')
    else:
        new_string = f'{a} {b}'
    return new_string"""


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(function, input, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    output = function(*input)

    if output == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {function.__name__}{input!r} retornou {output!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
    test(mix_up, ('dj', 'fi'), 'dj fi')
