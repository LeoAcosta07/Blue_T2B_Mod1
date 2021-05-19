import os
def menor_num(num1, num2):
    if num1 < num2:
        return num1
    elif num1 == num2:
        return 0
    else:
        return num2


os.system("cls")
print("Diguite dois numeros\n")
num1 =  int(input("Diguite o primeiro numero:"))
num2 =  int(input("Diguite o segundo numero:"))
os.system("cls")

if menor_num(num1,num2)==0:
  print("Os dois numeros sao iguais")
else:
  print(f"O numero {menor_num(num1,num2)} é o menor")