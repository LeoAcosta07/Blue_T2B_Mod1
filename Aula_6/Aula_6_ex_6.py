import os
def conceito(nota):
    if nota < 6.0:
        letra = "F"
    elif nota >= 6.0 and nota < 7.0:
        letra = "D"
    elif nota >= 7.0 and nota < 8.0:
        letra = "C"
    elif nota >= 8.0 and nota < 9.0:
        letra = "B"
    else:
        letra = "A"

    return letra

os.system("cls")
nota = float(input("Digite a nota do aluno:"))
os.system("cls")
print(f'O conceito do estudante é: {conceito(nota)}')