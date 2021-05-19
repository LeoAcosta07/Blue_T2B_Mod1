def soma_imposto(a, b):
    b = float(b)/100
    total = a + (a*b)
    return  total


custo = float(input("Ingresse o valor da venda R$: "))
taxa_imposto = input("Ingresse o porcentual do imposto: ").replace('%','')

print(f"O valor total da vanda com os impostos é: {soma_imposto(custo, taxa_imposto)}")