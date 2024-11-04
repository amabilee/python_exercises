def separar_vetores(x):
    vetor_a = [elemento for elemento in x if elemento > 0]
    vetor_b = [elemento for elemento in x if elemento <= 0]
    return vetor_a, vetor_b

vetor_x = [5, -3, 0, 8, -2, 10, -1, 0, 7, -4, 6, -9, 2, 1, -6, 4, -7, 3, 0, -5, 12, -8, 11, -10, 9, -11, 15, 13, -14, 16, -17]

vetor_a, vetor_b = separar_vetores(vetor_x)

print("Vetor A (elementos maiores que zero):", vetor_a)
print("Vetor B (elementos menores ou iguais a zero):", vetor_b)