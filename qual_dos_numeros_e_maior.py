# Escreva um programa que leia 3 números do usuário e indique qual deles é o maior.

print("Descubra qual dos 3 números é maior!")

number1 = float(input("Escreva o primeiro número:"))
number2 = float(input("Escreva o segundo número:"))
number3 = float(input("Escreva o terceiro e último número:"))

if number1 > number2 and number1 > number3:
    print("O primeiro número é maior.")

elif number2 > number1 and number2 > number3:
    print("O segundo número é maior.")

elif number3 > number1 and number3 > number2:
    print("O terceiro número é maior.")

else:
    print("Os números são equivalentes.")

# tá dando errado quando o primeiro
# número é menor que os outros, mas a lógica está correta.

# descobri = só está pegando o primeiro número.

# era a falta do "float/int"