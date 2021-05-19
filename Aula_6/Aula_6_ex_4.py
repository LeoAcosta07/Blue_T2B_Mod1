def salario(a, b):
    if a > 40:
        a = (a - 40)
        total = (40*b)+(a*(1.5*b))
        return total
    else:
        total = (a * b)
        return total

total_horas = float(input("Ingresse o total de horas trabalhadas: "))
valor_hora = float(input("Ingresse o por hora a receber: "))


print(f'O valor total a receber é de R$ {salario(total_horas, valor_hora):.2f}')