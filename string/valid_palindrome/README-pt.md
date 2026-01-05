# Valid Palindrome (Palíndromo Válido)

**Dificuldade:** Fácil

## Descrição

Uma frase é um **palíndromo** se, após converter todas as letras maiúsculas em minúsculas e remover todos os caracteres não alfanuméricos, ela for lida da mesma forma da esquerda para a direita e vice-versa. Caracteres alfanuméricos incluem letras e números.

Dada uma string `s`, retorne `true` se for um palíndromo, ou `false` caso contrário.

## Exemplos

**Exemplo 1:**

> **Input:** s = "A man, a plan, a canal: Panama"
> **Output:** true
> **Explicação:** "amanaplanacanalpanama" é um palíndromo.

**Exemplo 2:**

> **Input:** s = "race a car"
> **Output:** false
> **Explicação:** "raceacar" não é um palíndromo.

**Exemplo 3:**

> **Input:** s = " "
> **Output:** true
> **Explicação:** s é uma string vazia após remover caracteres não alfanuméricos. Como uma string vazia lê-se igual de trás para frente, é um palíndromo.

## Restrições

- `1 <= s.length <= 2 * 10^5`
- `s` consiste apenas em caracteres ASCII imprimíveis.
