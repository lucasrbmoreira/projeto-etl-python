# 📊 Pipeline ETL com Python

Este projeto é um desafio prático de **Engenharia de Dados** focado na construção de um fluxo ETL (Extract, Transform, Load).

O objetivo foi extrair dados de clientes, aplicar uma regra de negócio para gerar mensagens de marketing personalizadas e salvar os dados transformados.

## ⚙️ O que o projeto faz?

1.  **Extract (Extração):** Lê um arquivo CSV (`SDW2023.csv`) contendo IDs e nomes de usuários.
2.  **Transform (Transformação):** Utiliza a biblioteca Pandas e lógica em Python para segmentar os clientes e gerar mensagens automáticas (simulando uma IA Generativa).
3.  **Load (Carregamento):** Salva os dados enriquecidos em um novo arquivo (`SDW2023_novo.csv`).

## 🛠 Tecnologias Utilizadas

* **Python 3**
* **Pandas** (Manipulação de dados)
* **CSV** (Formato de armazenamento)

## 🚀 Como executar

1. Clone o repositório.
2. Instale o Pandas: `pip install pandas`
3. Execute o script: `python app.py`

---
*Projeto desenvolvido com fins educacionais.*