# Desafio proposto por: Sr View | djairdj LinkedIn: https://www.linkedin.com/in/djairdj/
# Crie uma função chamada "solution", com um parâmetro do tipo matriz.
# Sua função irá receber uma matriz de números inteiros k, onde -10³ ≤ k ≤ 10³.
# Essa matriz terá duas dimensões e será de ordem qualquer.
# Sua função terá que retorna um array (em ordem crescente) que contenha os números
# que faltam para completar a sequência que vem na matriz, desde o menor até o maior número nela.
# Caso não haja nenhum número faltando no intervalo, retornar um array vazio.
# Exemplo:
# input:
# {
#   {1, 3},
#   {6, 9}
# }
# output:
# {2, 4, 5, 7, 8}
# Código em Python 3.8.2 criado por: André Luiz Barbosa | Andrehlb
# Data: 19/08/2023
def solution(matrix):
    # min(iterable, *[, default=obj, key=func]) -> value min(arg1, arg2, *args, *[, key=func]) -> value
    min_num = min(min(row) for row in matrix)
    max_num = max(max(row) for row in matrix)

    numbers_in_matrix = [num for row in matrix for num in row]

    missing_numbers = [num for num in range(min_num, max_num + 1) if num not in numbers_in_matrix]

    return missing_numbers

matrix = [
    [1, 3],
    [6, 9]
]
print(solution(matrix))