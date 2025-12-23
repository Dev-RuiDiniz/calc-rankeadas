# 🎮 Calculadora de Partidas Rankeadas

Projeto desenvolvido para o desafio de lógica de programação, focado em aplicar conceitos básicos como funções, operadores e estruturas de controle.

## 📝 Descrição
O objetivo é calcular o saldo de vitórias de um jogador e determinar em qual nível (Rank) ele se encontra, seguindo a regra de negócio estabelecida.

## 🚀 Tecnologias e Conceitos Utilizados
* **Linguagem:** Python
* **Conceitos:**
    * Variáveis e Tipos de Dados
    * Operadores Aritméticos e de Comparação
    * Estruturas de Decisão (`if`, `elif`, `else`)
    * Laços de Repetição (`while`)
    * Funções com Parâmetros e Retorno

## 📊 Tabela de Classificação

| Vitórias | Nível |
| :--- | :--- |
| Menor que 10 | **Ferro** |
| Entre 11 e 20 | **Bronze** |
| Entre 21 e 50 | **Prata** |
| Entre 51 e 80 | **Ouro** |
| Entre 81 e 90 | **Diamante** |
| Entre 91 e 100 | **Lendário** |
| Maior ou igual a 101 | **Imortal** |

## 💻 Exemplo de Uso

Ao executar o código, o sistema solicitará as vitórias e derrotas:

```python
# Exemplo de entrada:
# Vitórias: 85
# Derrotas: 10

# Saída esperada:
"O Herói tem de saldo de 75 está no nível de Ouro"