# 🧠 Resumo objetivo:
# Dividir nums em n / 3 gera subarrays de tamanho 3
# Em cada subarray, max - min ≤ k
# 🧪📘 Enunciado original
# Input: nums = [2,4,2,2,5,2], k = 2
# Output: []
# Explanation: Difference ways to nums into 2 arrays of size 3 are:
# [2,2,2], [2,4,5] (and its permutations)
# [2,2,4], [2,2,5] (and its permutations)
# Because there are four 2s there will be an array with the elementds 2 and 5 no matter how we divide it. 
# Since 5 - 2 = 3 > k, the condition is not satisfied and so there is no valid division.
# Isto significa que 5-2 = 3 > k, logo não é possível dividir o array em dois subarrays de tamanho 3,
# ou ainda, nenhum agrupamento possível satisfaz, atende a condição de max - min ≤ k.
# 🧠 Resumo objetivo do problema:  A partir de array de tamanho 6, obter 2 arrays de tamanho 3

# Pseudo Código
# função divideArray(nums, k):
#    se tamanho(nums) % 3 != 0:
#         retornar lista vazia
#    ordenar nums em ordem crescente

#    lista grupos <- lista vazia

#    para i de 0 até tamanho(nums) com passo (subdivide o array) 3:
#       (grupo <- subarray de nums do índice i até i+3 ou seja )
#       grupo <- [nums[i], nums[i+1], nums[i+2]]
#       se (max(grupo) - min(grupo) <= k):
#           adicionar grupo à lista grupos
#       senão:
#           retornar lista vazia

#    retornar grupos