def argumento(a):
    if a > 0:
        return 'P'
    elif a <0:
        return 'N'
    else:
        return '0'

n1 = int(input("Digite um umero: "))

print(f"O numero digitado é: {argumento(n1)}")