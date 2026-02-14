# Veja se a data é correta.

print("Veja se a data é válida!")

dia = int(input("Escreva o dia do mês:"))
mes = int(input("Escreva o mês (1,2,4,8):"))
ano = int(input("Escreva o ano:"))

if 1 <= dia <= 31 and 1 <= mes <= 12 and 1990 <= ano <= 2100:
    print("Essa data é válida.")

else:
    print("Essa data é inválida.")
