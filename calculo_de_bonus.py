
salario = float(input("insira seu salário: "))
tempo_servico = float(input("insira seu tempo de serviço: "))

total = 0
if tempo_servico > 5:

    total = salario * 1.05
else:
    total = salario

if (total > salario):
    print(f"Seu novo salário é de {total}")
else:
    print(f"Seu salário permanece o mesmo") 





