import pandas as pd
import random

# 1. EXTRAÇÃO
try:
    df = pd.read_csv('SDW2023.csv')
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
    exit()

# 2. TRANSFORMAÇÃO (IA Simulada)
def gerar_mensagem(usuario):
    nome = usuario['Nome']
    if usuario['Segmento'] == 'Investidor':
        return f"Olá {nome}, invista melhor conosco!"
    elif usuario['Segmento'] == 'Crédito':
        return f"{nome}, temos crédito aprovado para você."
    else:
        return f"{nome}, obrigado por ser nosso cliente."

df['Mensagem'] = df.apply(gerar_mensagem, axis=1)

# 3. CARREGAMENTO
df.to_csv('SDW2023_novo.csv', index=False)
print("Processo concluído! Arquivo 'SDW2023_novo.csv' criado.")