def cal_imc(a, b):
    a = float (a)
    b= float(b)
    imc = b/(a**2)
    return imc

altura = (input("Ingresse sua altura em (metros): ")).replace('m','')
kg = (input("Ingresse seu peso en (Kilo Gramas): ")).replace("kg", "")


print(f'Seu IMC é de: {cal_imc(altura, kg):.2f}')