peso = int(input("Entre com o peso dos peixes: "))
excesso = peso - 50

multa = 4 * excesso

print(f"O peso dos peixes é de {peso}kg")
print(f"Peso acima do limite de 50KG. Limite excedido em {excesso}kg")
print(f"A sua multa devido ao peso em excesso será de R${multa:.2f}")

