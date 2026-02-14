# e leia a idade de uma pessoa e classifique-a como 
# criança, adolescente, adulto ou idoso.

print("Descubra se você é criança, adolescente, adulto ou idoso!")

age = int(input("Escreva sua idade:"))

if 0 <= age <= 12:
    print("Você é uma criança.")

elif 13 <= age <= 17:
    print("Você é um adolescente.")

elif 18 <= age <= 64:
    print("Você é adulto.")

elif 65 <= age <= 150:
    print("Você é idoso.")

elif age < 0:
    print("Idade negativa? Essa é nova...")

else:
    print("Parabéns, vc já virou um fóssil.")
