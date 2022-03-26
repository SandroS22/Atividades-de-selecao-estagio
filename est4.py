def fatorial(n):
    total = 1
    y = 2
    while y <= n:
        total *= y  # Multiplica o total da multiplicação anterior com o próximo número
        y += 1
    return total


print(fatorial(6))
