import pandas as pd

# 1. EXTRAÇÃO
try:
    # Lê o arquivo atualizado
    df = pd.read_csv('SDW2023.csv')
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Erro: Arquivo CSV não encontrado.")
    exit()

# 2. TRANSFORMAÇÃO (Nova Lógica com Saldo e Status)
def gerar_mensagem_personalizada(usuario):
    # Pegamos os dados das novas colunas
    nome = usuario['Nome']
    saldo = usuario['Saldo']
    status = usuario['Status']
    
    # Regra 1: Cliente inativo (Prioridade máxima)
    if status == 'Inativo':
        return f"Oi {nome}, estamos com saudade! Reative sua conta e ganhe benefícios."
    
    # Regra 2: Cliente com alto saldo (Investidor)
    elif saldo > 2000:
        return f"{nome}, seu saldo de R$ {saldo:.2f} pode render mais! Conheça nossos investimentos."
    
    # Regra 3: Cliente padrão ou negativo (Crédito)
    else:
        return f"{nome}, que tal um cartão de crédito para facilitar suas compras?"

# Aplica a função linha a linha
df['Mensagem_Marketing'] = df.apply(gerar_mensagem_personalizada, axis=1)

# Mostra uma prévia no terminal
print("\n--- Resultado da Transformação ---")
print(df[['Nome', 'Saldo', 'Status', 'Mensagem_Marketing']].head(10))

# 3. CARREGAMENTO
df.to_csv('SDW2023_enrich_v2.csv', index=False)
print("\nProcesso concluído! Arquivo 'SDW2023_enrich_v2.csv' gerado.")