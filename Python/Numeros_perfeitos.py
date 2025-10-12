num1 = int(input("De um numero:"))
num2 = int(input("De outro numero:"))
soma_dos_divisores = 0

print(f"Números perfeitos entre {num1} e {num2}:\n")
for num in range(num1, num2 + 1):
    soma_dos_divisores = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            soma_dos_divisores += divisor
    if soma_dos_divisores == num and num > 0:
        print(num)


