# De 3 números, verifique quanto deles são positivos.

numero1 = float(input("Escreva o primeiro número:"))
numero2 = float(input("Escreva o segundo número:"))
numero3 = float(input("Escreva o terceiro número:"))

if numero1 < 0 and numero2 >= 0 and numero3 >= 0:
    print("Apenas 1 número é negativo.")

elif numero1 < 0 and numero2 < 0 and numero3 >= 0:
    print("Apenas 2 números são negativos.")

elif numero1 < 0 and numero2 < 0 and numero3 < 0:
    print("Os 3 números são negativos.")

elif numero1 > 0 and numero2 < 0 and numero3 < 0:
    print("Apenas 1 número é negativos.")

elif numero1 > 0 and numero2 > 0 and numero3 < 0:
    print("Apenas 2 números são negativos.")

elif numero1 > 0 and numero2 > 0 and numero3 > 0:
    print("Os 3 números são negativos.")

else:
    print("Não há números positivos ou negativos.")
