# Escreva um programa que leia 2 números e informe se o primeiro número é maior, menor ou igual ao segundo.

print("Saiba se o primeiro número é maior, menor ou igual ao segundo.")

numero1 = float(input("Informe o primeiro número:"))
numero2 = float(input("Informe o segundo número:"))

if numero1 > numero2:
    print("O primeiro número é maior que o segundo.")

elif numero1 == numero2:
    print("Os números são iguais.")

else:
    print("O segundo número é maior que o primeiro.")
    