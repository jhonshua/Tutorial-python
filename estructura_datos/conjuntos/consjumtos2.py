visitantes_a = ["Juan", "Maria", "Pedro", "Ana"]
visitantes_b = ["Maria", "Luis", "Ana", "Sofia"]

conjunto_a = set(visitantes_a)
conjunto_b = set(visitantes_b)

visitantes_ambas = conjunto_a & conjunto_b
print(visitantes_ambas)  # {'Maria', 'Ana'}