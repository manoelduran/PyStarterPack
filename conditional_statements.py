
# if - else

age = 25

# Aqui temos uma simples verificação. Se a variável age for menor que 18, o programa irá executar o bloco de código dentro do if, que neste caso, seria: "Você é menor de idade.", mas como age é 25, a condição será falsa, fazendo com que o programa execute: "Você é maior de idade."
if age < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

# if - elif - else

age = 30

# Neste caso temos múltiplas verificações. O resultado será: "Você é um jovem adulto." pois ele cai no range de idade entre maior ou igual a 18 e menor ou igual a 30.

if age < 18:
    print("Você é menor de idade.")
elif 18 <= age <= 30:
    print("Você é um jovem adulto.")
elif 31 <= age <= 50:
    print("Você é um adulto de meia-idade.")
else:
    print("Você é um adulto mais velho.")
