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
print('[ERROR] - ocorrencias de "x": ', nome.index('x')) # ValueError: substring not found
print('--------------------------------')
