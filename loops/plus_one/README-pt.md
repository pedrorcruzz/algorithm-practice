# Plus One (Mais Um)

**Dificuldade:** Fácil

## Descrição

Você recebe um **inteiro grande** representado como um array de dígitos inteiros `digits`, onde cada `digits[i]` é o i-ésimo dígito do inteiro. Os dígitos estão ordenados do mais significativo para o menos significativo (da esquerda para a direita). O inteiro grande não contém nenhum zero à esquerda (leading zero).

Incremente o inteiro grande em um e retorne o array de dígitos resultante.

## Exemplos

**Exemplo 1:**

> **Input:** digits = [1,2,3]
> **Output:** [1,2,4]
> **Explicação:** O array representa o inteiro 123. Incrementando em um, obtemos 123 + 1 = 124. Portanto, o resultado deve ser [1,2,4].

**Exemplo 2:**

> **Input:** digits = [4,3,2,1]
> **Output:** [4,3,2,2]
> **Explicação:** O array representa o inteiro 4321. Incrementando em um, obtemos 4321 + 1 = 4322.

**Exemplo 3:**

> **Input:** digits = [9]
> **Output:** [1,0]
> **Explicação:** O array representa o inteiro 9. Incrementando em um, obtemos 9 + 1 = 10. Portanto, o resultado deve ser [1,0].

## Restrições

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` não contém zeros à esquerda.
