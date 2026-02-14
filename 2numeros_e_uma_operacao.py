# Escreva um programa que leia 2 números e uma operação matemática ( + , ‑ , * , / ).
# O programa deve executar a operação correspondente e imprimir o resultado.

print("Faça operações de 2 números!")

number1 = float(input("Informe o primeiro número:"))
number2 = float(input("Informe o segundo número:"))
operation = (input("Informe o tipo de operação (+,-,*,/):"))

if operation == ("+"):
    print(" O resultado é:", number1 + number2)

elif operation == ("-"):
    print(" O resultado é:", number1 - number2)

elif operation == ("*"):
    print(" O resultado é:", number1 * number2)

elif operation == ("/"):
    print(" O resultado é:", number1 / number2)

else:
    print("Tipo de operação não suportado.")