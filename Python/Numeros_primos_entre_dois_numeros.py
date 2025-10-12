num1 = int(input("Digite um Número..:" ))
num2 = int(input("Digite outro Número..:" ))
i = 1
num = 1
div = 0

ehPrimo = 0

print("Numero primos entre {} e {}:".format(num1, num2))
for num in range(num1, num2+1):
    if (num > 1) :
        div = 0
    for i in range(1, num+1):
        if (num%i==0):
            div += 1
    if (div == 2):
        print(num)
    