
from random import randint 

numero = randint(0, 100)

while True:
    valor = int(input("Digite um valor de 0 a 100: "))

    print (numero)
    if valor < numero:
        print (f"o seu numero é menor que {valor}")

    elif valor > numero:
        print (f"o seu numero é maior que {valor}")

    else:
        if {valor} = {numero}: print (f"Você acertou o {numero} é")