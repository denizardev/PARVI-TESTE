📋 DESAFIO RPA PYTHON
Automação de Web Scraping, Análise de Dados e Envio de Relatório por E-mail

📌 Visão Geral
Este projeto automatiza a coleta de citações do site Quotes to Scrape, realiza análises estatísticas e envia um relatório por e-mail com os resultados.

🔧 Funcionalidades
✔ Web Scraping com Selenium (coleta de citações, autores e tags)
✔ Análise de Dados com Pandas (total de citações, autor mais frequente, tag mais popular)
✔ Envio Automatizado de E-mail com anexo CSV e resumo dos dados

🚀 Como Executar
📋 Pré-requisitos
Python 3.8+

Navegador Chrome/Chromium instalado

Conta Gmail (para envio de e-mails)

⚙️ Instalação
Clone o repositório:

bash
git clone https://github.com/denizardev/PARVI-TESTE.git
cd desafio-rpa-python
Instale as dependências:

bash
pip install -r requirements.txt
Configure o arquivo .env (na raiz do projeto):

ini
EMAIL_FROM=seu_email@gmail.com
EMAIL_PASS=sua_senha_app # Senha de app do Gmail
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
📂 Estrutura do Projeto
desafio-rpa-python/  
├── src/  
│ ├── data/ # Dados coletados (CSV)  
│ │ └── quotes.csv  
│ ├── web_scraping.py # Raspagem de dados  
│ ├── data_analysis.py # Análise estatística  
│ └── email_sender.py # Envio de relatório  
├── .env # Configurações sensíveis  
├── .gitignore  
├── requirements.txt # Dependências  
└── README.md  
📜 Módulos Principais

1. Web Scraping (web_scraping.py)
   Funções:

setup_driver() → Configura o navegador automatizado.

scrape_quotes() → Extrai citações do site.

save_to_csv() → Salva os dados em data/quotes.csv.

Execução:

bash
python src/web_scraping.py 2. Análise de Dados (data_analysis.py)
Funções:

analyze_quotes() → Gera estatísticas:

Total de citações

Autor mais frequente

Tag mais popular

Saída no Terminal:

📊 Análise das Citações:  
• Total de citações: 10  
• Autor mais frequente: Albert Einstein (3 citações)  
• Tag mais popular: inspirational (2 ocorrências)  
Execução:

bash
python src/data_analysis.py 3. Envio de E-mail (email_sender.py)
Funções:

send_report() → Envia relatório com:

Resumo das estatísticas

Anexo quotes.csv

Configuração:

Os destinatários estão definidos dentro do código (recipients = [...]).

Execução:

bash
python src/email_sender.py
🔁 Fluxo Completo
Para rodar todo o pipeline:

bash
python src/web_scraping.py && python src/data_analysis.py && python src/email_sender.py
📦 Dependências
selenium → Automação do navegador

pandas → Análise de dados

python-dotenv → Gerenciamento de variáveis de ambiente
