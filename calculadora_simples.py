numero_um = float(input("insira um numero"))
numero_dois = float(input("insira um numero"))
operacao = input("insira as operações para calcular os numeros (+ - * /): ")

resultado = ''
if operacao =='+':
    resultado = numero_um + numero_dois

elif operacao == '-':
    resultado = numero_um - numero_dois

elif operacao == '*':
    resultado = numero_um * numero_dois

elif operacao == '/':
    if numero_dois ==0:
        print("Não é possivel dividir por zero")
    else:
        resultado = numero_um / numero_dois
else:
    print("Operação não reconhecida.")

if resultado != '':
        print(f"O resultado é: {resultado}")