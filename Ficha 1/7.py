"""
7. Os conjuntos são coleções de elementos, sem repetição (não há elementos
duplicados). Use dois conjuntos para guardar duas frases lidas do teclado.
Depois mostre o seguinte (tire partidos das operações sobre conjuntos):
(a) Todas as letras que aparecem em ambas as frases (se aparecer a mesma
letra mais que uma vez, só deve ser mostrada uma vez).
(b) As letras que aparecem na primeira frase mas não na segunda.
(c) As letras que aparecem simultaneamente em ambas as frases.
(d) As letras que só aparecem na primeira frase ou só aparecem na segunda
frase.
"""

print("Escreva a primeira frase")
frase = input()
frase = set(frase)
print("Escreva a segunda frase")
frase2 = input()
frase2 = set(frase2)

"""
(a)
"""
print("Letras que aparecem em ambas as frases")
print(frase.union(frase2))

"""
(b)
"""
print("Letras que aparecem na primeira frase mas não na segunda")
print(frase.difference(frase2))

"""
(c)
"""
print("letras que aparecem simultaneamente em ambas as frases")
print(frase.intersection(frase2))

"""
(d)
"""
print("letras que só aparecem na primeira frase ou só aparecem na segunda frase.")
print(frase.symmetric_difference(frase2))
