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


O script extrairá os dados da API, transformará as informações necessárias e as armazenará no arquivo btc.json.


## Estrutura do Projeto
- main.py: Script principal que executa o processo ETL.
- btc.json: Banco de dados local onde os dados transformados são armazenados.
- requirements.txt: Arquivo contendo as dependências necessárias para o projeto.
- .gitignore: Arquivo que especifica quais arquivos ou pastas devem ser ignorados pelo Git.


## Observações
Certifique-se de que sua máquina esteja conectada à internet para que o script possa acessar a API do Coinbase.
O arquivo btc.json será criado automaticamente no diretório raiz do projeto após a primeira execução do script.


## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.


