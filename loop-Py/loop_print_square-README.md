Claro, esse título é apropriado e descreve bem o exercício. Aqui está o README atualizado:

---

# Exercício de Loop e Potência em Python

## Descrição

Este é um exercício de programação em Python que envolve a impressão de quadrados de números inteiros não-negativos usando loops e operações de potência.

## Problema

O problema pede para ler um número inteiro `n` e para cada número inteiro não-negativo `i` menor que `n`, imprimir o quadrado de `i`.

## Restrições

- `n` é um número inteiro.
- 1 ≤ `n` ≤ 20.

## Formato de Entrada

A entrada consiste em um único número inteiro `n`.

## Formato de Saída

A saída deve consistir em `n` linhas, cada uma contendo o quadrado de um número inteiro `i` (0 ≤ `i` < `n`).

## Exemplo

### Entrada de Exemplo

```
5
```

### Saída de Exemplo

```
0
1
4
9
16
```

Neste exemplo, `n` é 5. Portanto, o programa imprime o quadrado de cada número inteiro de 0 a 4.

## Solução

A solução para este problema envolve a leitura da entrada do usuário, a verificação se a entrada está dentro das restrições especificadas e, em seguida, a execução de um loop para calcular e imprimir os quadrados dos números.

Aqui está o código da solução em Python:

```python
if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 20:
        for i in range(n):
            print(i**2)
```

---

</br>

:) Obrigado 😊