from itertools import chain
tabela=[[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
aaa= list(chain.from_iterable(tabela))
print(aaa)