# Entrada
nome_vendedor = input("Nome do vendedor: ")
salario_fixo = float(input("Salário fixo: "))
total_vendas = float(input("Total de vendas: "))

# Fórmula
a_receber = (total_vendas * 0.15) + salario_fixo

# Resposta
print(f"{nome_vendedor} deve receber R$ {a_receber:.2f}")