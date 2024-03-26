# Soma de Dois Números em Python para _newbies_

<h4> Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "_Presentation Error_". </h4>

<p> Entrada </p>

A entrada contém 2 valores inteiros.

<p> Saída </p>

Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade, conforme o exemplo abaixo.

<p> Exemplos de Entrada	Exemplos de Saída </p>

![Exemplos de Entrada e Saída](assets\img\somaDeDoisNumeros.png)

From <https://resources.beecrowd.com/repository/UOJ_1001.html> 

Pseudo código

<p> Linguagem Natural Estruturada </p>

```
    1. Inicialize as duas variáveis, A e B
    2. Ler o primeiro valor inteiro e armazenar na variável A
    3. Ler o segundo valor inteiro e armazenar na variável B
    4. Efetuar a soma de A e B e armazenar na variável X
    5. Imprimir "X =", seguido pelo valor da variável X e um fim de linha
```
<p> Pseudo código </p>

```pseudo-código
Inicio
    Declare A, B, X
    Leia A
    Leia B
    X = A + B
    Imprime "X = ", X
Fim
```
<p> em Python será assim: </p>

```py
// Declare A, B, X
A = int(input())     # Leia A
B = int(input())     # Leia B
X = A + B            # X = A + B
print("X = ", X)     # Imprime "X = ", X
```

## Explicação de cada linha:

1. `A = int(input())`
    Esta linha lê o valor inteiro do usuário e o armazena na variável A.
    A Função `input()` lê uma linha de texto da entrada padrão (normalmente o teclado), e `int()` converte esta linha em um numero inteiro.

2. `B = int(input())` idem ao anterior.

3. `X = A + B` esta linha soma os valores de A e B e armazena o resultado na variável X.
4. `print("X = ", X)` 
    Esta linha de código imprime a string `"X = "`, seguida pelo valor da variável X. A função `print()` imprime seus argumentos na saída padrão (normalmente a tela).

👍Obrigado! `:)`