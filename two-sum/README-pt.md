# Two Sum

**Dificuldade:** Fácil

## Descrição

Dado um array de números inteiros `nums` e um número inteiro `target`, retorne os índices dos dois números de forma que a soma deles seja o `target`.

Você pode assumir que cada entrada terá **exatamente uma solução** e você não pode usar o mesmo elemento duas vezes.

Você pode retornar a resposta em qualquer ordem.

## Exemplos

**Exemplo 1:**

> **Input:** nums = [2,7,11,15], target = 9
> **Output:** [0,1]
> **Explanation:** Como nums[0] + nums[1] == 9, retornamos [0, 1].

**Exemplo 2:**

> **Input:** nums = [3,2,4], target = 6
> **Output:** [1,2]

**Exemplo 3:**

> **Input:** nums = [3,3], target = 6
> **Output:** [0,1]

## Restrições

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Apenas uma resposta válida existe.**
