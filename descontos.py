# leia o preço original de um produto e o tipo de cliente
# ( regular , silver , gold ), aplique descontos diferentes
# (ex.: 0 %, 5%, 10%). Mostre o preço final.

print("Descubra o valor do seu desconto!")

preco_original = float(input("Escreva o preço original do produto:"))
plano = str(input("Escreva seu plano (regular, silver, gold):"))

if preco_original > 500:
    print("Seu desconto é 25%!")
    print("VALOR TOTAL:", 75/100 * preco_original)

elif plano == ("regular"):
    print("Seu desconto é de 5%!")
    print("VALOR TOTAL:", 95/100 * preco_original)

elif plano == ("silver"):
    print("Seu desconto é de 12%!")
    print("VALOR TOTAL:", 88/100 * preco_original)

elif plano == ("gold"):
    print("Seu desconto é de 20%!")
    print("VALOR TOTAL:", 80/100 * preco_original)

else:
    print("Plano incorreto.")
