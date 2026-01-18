# 📊 Pipeline ETL com Python

Este projeto é um desafio prático de **Engenharia de Dados** focado na construção de um fluxo ETL (Extract, Transform, Load).

O objetivo foi extrair uma base de dados de clientes, aplicar regras de negócio baseadas no **status da conta** e no **saldo**, e gerar mensagens de marketing personalizadas.

## ⚙️ O que o projeto faz?

1.  **Extract (Extração):** Lê um arquivo CSV (`SDW2023.csv`) contendo informações financeiras dos clientes.
2.  **Transform (Transformação):** Aplica lógica condicional em Python para segmentar as mensagens:
    * **Clientes Inativos:** Recebem mensagem de reativação ("Estamos com saudades").
    * **Clientes com Saldo > 2000:** Recebem convite para investimentos.
    * **Clientes Padrão ou Negativados:** Recebem oferta de cartão de crédito.
3.  **Load (Carregamento):** Salva os dados enriquecidos em um novo arquivo CSV.

## 🛠 Estrutura do CSV

O arquivo de entrada deve conter as colunas: `UserID`, `Nome`, `Idade`, `Saldo`, `Status`.

## 🚀 Como executar

1. Clone o repositório.
2. Instale o Pandas: `pip install pandas`
3. Execute o script: `python app.py`

---
*Projeto desenvolvido para fins educacionais.*