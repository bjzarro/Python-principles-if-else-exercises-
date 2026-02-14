# nome, nota final, numero de faltas
# se nota >= 70 e faltas <= 10 então APROVADO
# se nota >= 70 e faltas < 10 então RECUPERAÇÃO
# se nota < 70 e faltas <= 10 então RECUPERAÇÃO
# se nota < 70 e faltas > 10 então RECUPERAÇÃO

nome = input("Informe seu nome:")
nota = int(input("Informe sua nota:"))
faltas = int(input("Informe a quantidade de faltas:"))

if nota >= 70 and faltas <= 10:
    print("Você está aprovado.")

elif nota >= 70 and faltas > 10:
    print("Você está reprovado.")

elif nota < 70 and faltas <= 10:
    print("Você está reprovado.")

else:
    print("Você está reprovado.")

# se eu tivesse colocado if em todas as operações,
# ele iria ler cada bloco obrigatoriamente. Tendo o if e elif, 
# a leitura do script iria acabar na condição onde o input se encontra
# (nesse caso sendo a nota e a falta). (23/08/25)