# ETLProject

Este projeto é uma aplicação em Python que realiza um processo ETL (Extract, Transform, Load) para obter dados de preços de Bitcoin da API do Coinbase e armazená-los localmente utilizando o TinyDB.

## Funcionalidades

- **Extração**: Obtém o preço atual do Bitcoin em USD através da API pública do Coinbase.
- **Transformação**: Processa os dados extraídos para extrair informações relevantes, como valor, criptomoeda, moeda e timestamp.
- **Carga**: Armazena os dados transformados em um banco de dados local (`btc.json`) utilizando o TinyDB.

## Requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `tinydb`

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/victorgoveia/ETLProject.git
   cd ETLProject

2. **Crie um ambiente virtual:**

- python -m venv venv

3. **Ative o ambiente virtual:**

- win: venv\Scripts\activate
- macOS/Linux: source venv/bin/activate


4. **Instale as dependências:**

- pip install -r requirements.txt


