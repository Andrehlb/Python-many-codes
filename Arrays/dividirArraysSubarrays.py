# 🧠 Resumo objetivo:
# Dividir nums em n / 3 subarrays de tamanho 3
# Em cada subarray, max - min ≤ k
# 🧪 Exemplo 1 fornecido no problema
# 📘 Enunciado original
# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation: The difference between any two elements in each array is less than or equal to 2.  
# Pseudo Código
# funçãqo divideArray(nums, k):
    # ordenar nums em ordem crescente

    # lista grupos <- lista vazia

    # para i de 0 até tamanho(nums) com passo (subdivide o array) 3:
    # grupo <- subarray de nums do índice i até i+3 ou seja grupo <- [nums[i], nums[i+1], nums[i+2]]
    # se (max(ggrupo) - min(grupo) <= k):
        #adicionar grupo à lista grupos
    # senão:
        # retornar lista vazia

    # retornar grupos

def divideArray(nums, k):
    if len(nums) % 3 !=0:
        return []
    
    nums.sort()  # Ordena o array
    result = []  # Lista para armazenar os subarrays
    for i in range(0, len(nums), 3):
        group = nums[i:i+3]
        if max(group) - min(group) <= k:
            result.append(group)
        else:
            return []
    return result

# Testando a função com o exemplo fornecido
nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k = 2
print(divideArray(nums, k))  # Saída esperada: [[1, 1, 3], [3, 4, 5], [7, 8, 9]]