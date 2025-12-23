def calcular_nivel(vitorias, derrotas):
    # Calcula o saldo
    saldo_vitorias = vitorias - derrotas
    
    # Estrutura de decisão para determinar o nível
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:  # Para vitórias >= 101
        nivel = "Imortal"
    
    return saldo_vitorias, nivel

# Laço de repetição para testar o sistema
while True:
    print("\n--- Calculadora de Partidas Rankeadas ---")
    
    try:
        vits = int(input("Digite a quantidade de vitórias: "))
        ders = int(input("Digite a quantidade de derrotas: "))
        
        # Chamada da função e atribuição do resultado às variáveis
        saldo, rank = calcular_nivel(vits, ders)
        
        # Saída formatada
        print(f"O Herói tem de saldo de **{saldo}** está no nível de **{rank}**")
        
    except ValueError:
        print("Por favor, insira apenas números inteiros.")

    # Opção para sair do laço
    continuar = input("\nDeseja calcular outro jogador? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando programa...")
        break