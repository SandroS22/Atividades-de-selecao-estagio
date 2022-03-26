f = int(input())
num = 1
num2 = 1
soma = 0
for i in range(f):
    print(num, end=' ')  # Printa os valores
    soma = num + num2
    num = num2  # Transforma o número anterior no anterior do atual
    num2 = soma  # Transforma a soma no número atual utilizado para o proximo loop
