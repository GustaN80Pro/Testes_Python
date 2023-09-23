# Escrever o código para imprimir a tabuada do 2 usando um laço for

tabuada = int(input("Qual tabuada deseja: "))

for numero in range(0, 11):

    print(f'{tabuada} x {numero} = {numero * tabuada}')