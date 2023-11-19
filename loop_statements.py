

# For Loop

# Aqui criamos um loop que irá mostrar na tela todos os números que tem no range(5), no caso, ele irá printar na tela a sequência de número de 0 a 4 pois na programação, começamos a contar a partir de 0
for number in range(5):
    print(number)

# While Loop
# Neste exemplo, o código mostrará na tela o valor da variável count até que ela seja 5. O código irá se repetir 5 vezes até que pare em 5 < 5.
count = 0
while count < 5:
    print(count)
    count += 1

# While Loop Infinito
# Neste caso passamos a condição "True", tornando o loop infinito. Para que seja parado, o usuário precisa digitar manualmente 'sair' para que o programa encerre o loop com a instrução 'break'. É muito perigoso esse tipo de loop, podendo travar seu programa para sempre.
while True:
    resposta = input("Digite 'sair' para encerrar o loop: ")
    if resposta.lower() == 'sair':
        print("Loop encerrado.")
        break
    else:
        print("Você digitou algo diferente de 'sair'. Continuando o loop.")

