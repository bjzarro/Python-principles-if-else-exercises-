# Escreva um programa que classifique triângulos.
# Equilátero, isósceles ou escaleno.

print("Saiba a classificação de um triângulo!")

lado1 = float(input("Escreva o primeiro lado:"))
lado2 = float(input("Escreva o segundo lado:"))
lado3 = float(input("Escreva o terceiro lado:"))

if lado1 == lado2 == lado3:
    print("Esse triângulo é equilátero (todos os lados são iguais).")

elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
    print("Esse triângulo é isósceles (dois lados são iguais).")

elif lado1 != lado2 != lado3:
    print("Esse triângulo é escaleno (todos os lados são diferentes).")

else:
    print("Triângulo inválido.")
