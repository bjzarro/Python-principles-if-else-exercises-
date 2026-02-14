# Classificador de Números

print("Classifique o número em positivo/negativo e par/ímpar")

numero = int(input("Escreva o número:"))

if numero > 0 and numero % 2 == 0:
    print("Este número é positivo e par.")

elif numero > 0 and numero % 2 == 1:
    print("Este número é positivo e ímpar.")

elif numero < 0 and numero % 2 == 0:
    print("Este número é negativo e par.")

elif numero < 0 and numero % 2 == 1:
    print("Este número é negativo e ímpar.")

else:
    print("Número zero.")