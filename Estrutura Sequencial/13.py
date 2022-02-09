h = float(input("Entre com a altura da pessoa: "))

pH = (72.7 * h) - 58
pM = (62.1 * h) - 44.7

print(f"O peso ideal de uma pessoa de {h}m é {pH:.0f}kg se for homem e {pM:.0f}kg se for mulher")