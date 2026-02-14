# Conversão de Celsius para Fahrenheit

print("Converta a temperatura!")

print("Escolha a unidade que deseja converter:")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

escolha = input(":")
if escolha == ("1"):
    celsius_fahrenheit = float(input("Escreva a temperatura em Celsius:"))
    print("Temperatura em Fahrenheit =", (celsius_fahrenheit * 1.8) + 32)

elif escolha == ("2"):
    fahrenheit_celsius = float(input("Escreva a temperatura em Fahrenheit:"))
    print("Temperatura em Celsius =", 5/9 * (fahrenheit_celsius - 32))

else:
    print("Opção inválida")

# 26/08