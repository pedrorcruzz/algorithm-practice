# Binary Search (Busca Binária)

**Dificuldade:** Fácil

## Descrição

Dado um array de inteiros `nums` ordenado em ordem **crescente** e um inteiro `target`, escreva uma função para procurar o `target` em `nums`. Se o `target` existir, retorne o seu índice. Caso contrário, retorne `-1`.

Você deve escrever um algoritmo com complexidade de tempo de execução **O(log n)**.

## Exemplos

**Exemplo 1:**

> **Input:** nums = [-1,0,3,5,9,12], target = 9
> **Output:** 4
> **Explicação:** 9 existe em nums e seu índice é 4.

**Exemplo 2:**

> **Input:** nums = [-1,0,3,5,9,12], target = 2
> **Output:** -1
> **Explicação:** 2 não existe em nums, então retorna -1.

## Restrições

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- Todos os inteiros em `nums` são **únicos**.
- `nums` está ordenado em ordem crescente.
