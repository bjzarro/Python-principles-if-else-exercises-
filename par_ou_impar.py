# se numero for divisível por 2, é par.
# se numero não for divisível por 2, é ímpar.

numero = int(input("Informe um número:"))

if numero % 2 == 0:
    print("Este é um número PAR.")

else:
    print("Este é um número ÍMPAR.")

# Todo número par quando dividido por 2, tem resto 0.
# Logo, o que não tem resto 0, não é par, mas sim ímpar.
# (24/08/25)