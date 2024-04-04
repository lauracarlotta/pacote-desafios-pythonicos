# nome = 'a n a   b a n a n a'
# 		  0 1 2 3 4 5 6 7 8 9

nome = 'ana banana'

print('tamanho de nome: ', len(nome))

# ---------------------------------------
print('--------------------------------')
print('------------- IN ---------------')
print('--------------------------------')
# ---------------------------------------
# ==> 'ana' in nome
# ==> Verifica se uma string está dentro da outra (retornando True or False)
print('ana' in nome) # True
print('y' in nome) # False


# ---------------------------------------
print('--------------------------------')
print('------------ COUNT -------------')
print('--------------------------------')
# ---------------------------------------
# ==> s.count(sub, start, end)
# ==> Quantas vezes apareceu a ocorrência x

print('ocorrencias de "ana" não sobrepostas: ', nome.count('ana')) # 2x (não sobrepostas) 3x sobrepondo
print('ocorrencias de "a": ', nome.count('a')) # 5
print('ocorrencias de "a" a partir do índice "4": ', nome.count('a', 4)) #3
print('ocorrencias de "a" a partir do índice "4" até o índice 9: ', nome.count('a', 4, 9)) #2 - aparecem 2x pois o valor 'end' é contado como x - 1
print('[ERROR] ocorrencias de "x": ', nome.count('x')) # 0 quando não encontrado
print('--------------------------------')



# ---------------------------------------
print('--------------------------------')
print('------------ FIND --------------')
print('--------------------------------')
# ---------------------------------------
# ==> s.find(sub, start, end)
# ==> Qual o primeiro índice de x

print('ocorrencias de "ban": ', nome.find('ban')) # indice 4
print('ocorrencias de "n": ', nome.find('n')) # índice 1
print('ocorrencias de "a" a partir do índice "4": ', nome.find('a', 4)) # índice 5
print('ocorrencias de "n" a partir do índice "4" até o índice 9: ', nome.find('n', 4, 9)) # índice 6
print('[ERROR] - ocorrencias de "x": ', nome.find('x')) # índice -1 quando não encontrado
print('--------------------------------')



# ---------------------------------------
print('--------------------------------')
print('------------ INDEX -------------')
print('--------------------------------')
# ---------------------------------------
# ==> s.index(sub, start, end)
# ==> Qual o primeiro índice de x (com a variante de find, de que quando o valor não é encontrado, estoura o erro 'ValueError')

print('ocorrencias de "ban": ', nome.index('ban')) # indice 4
# print('[ERROR] - ocorrencias de "x": ', nome.index('x')) # ValueError: substring not found
print('--------------------------------')



# ---------------------------------------
print('--------------------------------')
print('----------- JOIN ---------------')
print('--------------------------------')
# ---------------------------------------
# Junta uma lista (retorna uma string - .join() funciona apenas com itens iteraveis.

variable1 = 'O Brasil é um país tropical, o Brasil é o país do futebol, o Brasil é penta campeão.'
list_split = variable1.split(' ')
print(variable1)
print(list_split)
list_split.append('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
list_split_with_join = ' '.join(list_split)
print(list_split_with_join)



# ---------------------------------------
print('--------------------------------')
print('----------- SPLIT --------------')
print('--------------------------------')
# ---------------------------------------
# Divide uma string

variable = 'O Brasil é um país tropical, o Brasil é o país do futebol, o Brasil é penta campeão.'
print('fatiamento da variável strin acima com split:')
items_list_1 = variable.split(' ')
for item in items_list_1:
	print(item)
print(f'items_list_1 tem {len(items_list_1)} elementos.')

# =============================
word = ''
times = 0
for item in items_list_1:
	step = items_list_1.count(item)

	if step > times:
		times = step
		word = item

print(f'A palavra {word} apareceu {times}x')
# =============================
items_list_2 = variable.split(',')
print(items_list_2)
print(f'items_list_2 tem {len(items_list_2)} elementos.')
for item in items_list_2:
	print(item.strip().title())



# ---------------------------------------
print('--------------------------------')
print('--------- ENUMERATE ------------')
print('--------------------------------')
# ---------------------------------------
# Enumera elementos da lista
# Desempacota itens de uma lista

variable2 = 'O Brasil é um país tropical, o Brasil é o país do futebol, o Brasil é penta campeão.'
items_list_3 = variable2.split(' ')
for index, value in enumerate(items_list_3):
	print(index, value)

# =============================

new_list = [
	[1, 2],
	[3, 4],
	[5, 6]
]

for value in new_list:
	print(value)
	print(value[0])
	print(value[1])

for value in new_list:
	for index1 in value:
		print(index1, '-', value)


new_new_list = [
	[30, 'Laura'],
	[59, 'Rubens'],
	[53, 'Lucinha']
]

for age, name in new_new_list:
	print(f'{name} tem {age} anos.')

# Desempacotamento
names = ['helena', 'madalena', 'tereza']
n1, n2, n3 = names
print(n2)
