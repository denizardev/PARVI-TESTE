import os
from pathlib import Path

# Estrutura de pastas e arquivos
structure = {
    "desafio-rpa-python": {
        "src": {
            "web_scraping.py": "# Parte 1 - Código de web scraping\n\nimport requests\nfrom bs4 import BeautifulSoup\nimport pandas as pd\n\n# Seu código de web scraping aqui\n\n# Exemplo básico:\n# response = requests.get('https://example.com/quotes')\n# soup = BeautifulSoup(response.text, 'html.parser')\n# quotes = [quote.text for quote in soup.select('.quote')]\n# pd.DataFrame(quotes, columns=['quote']).to_csv('../data/quotes.csv', index=False)",
            "data_analysis.py": "# Parte 2 - Código de análise com Pandas\n\nimport pandas as pd\n\n# Seu código de análise aqui\n\n# Exemplo básico:\n# df = pd.read_csv('../data/quotes.csv')\n# print(df.describe())\n# print(df.head())",
            "email_sender.py": "# Parte 3 - Código de envio de e-mail\n\nimport smtplib\nfrom email.mime.text import MIMEText\nfrom email.mime.multipart import MIMEMultipart\nimport os\nfrom dotenv import load_dotenv\n\n# Seu código de envio de e-mail aqui\n\n# Exemplo básico:\n# load_dotenv()\n# msg = MIMEMultipart()\n# msg['From'] = os.getenv('EMAIL_FROM')\n# msg['To'] = os.getenv('EMAIL_TO')\n# msg['Subject'] = 'Resultados do Web Scraping'\n# msg.attach(MIMEText('Segue em anexo os resultados...', 'plain'))\n# with smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT')) as server:\n#     server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))\n#     server.send_message(msg)"
        },
        "data": {
            "quotes.csv": "quote,author\n\"A vida é o que acontece enquanto você está ocupado fazendo outros planos.\",John Lennon\n\"A simplicidade é o último grau de sofisticação.\",Leonardo da Vinci"
        },
        "docs": {
            "instructions.pdf": ""
        },
        ".env": "EMAIL_FROM=seu_email@example.com\nEMAIL_TO=destinatario@example.com\nSMTP_SERVER=smtp.example.com\nSMTP_PORT=587\nEMAIL_USER=seu_usuario\nEMAIL_PASS=sua_senha",
        ".gitignore": "__pycache__/\n*.py[cod]\n*$py.class\n.env\nvenv/\nenv/\n*.log\n*.sqlite3\n.DS_Store\n.idea/\n.vscode/",
        "requirements.txt": "requests==2.31.0\nbeautifulsoup4==4.12.2\npandas==2.1.0\npython-dotenv==1.0.0",
        "README.md": "# Desafio RPA com Python\n\nProjeto de automação com Python contendo:\n\n1. Web Scraping\n2. Análise de dados\n3. Envio de e-mail\n\n## Como executar\n\n1. Instale as dependências:\n```\npip install -r requirements.txt\n```\n\n2. Configure as variáveis de ambiente no arquivo `.env`\n\n3. Execute os scripts na ordem:\n```\npython src/web_scraping.py\npython src/data_analysis.py\npython src/email_sender.py\n```\n\nOu execute o script principal:\n```\npython main.py\n```",
        "main.py": "# Script principal\n\nfrom src.web_scraping import *\nfrom src.data_analysis import *\nfrom src.email_sender import *\n\nif __name__ == '__main__':\n    print('Executando o pipeline RPA completo...')\n    # Adicione a lógica para chamar as funções principais de cada módulo\n"
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = base_path / name
        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Arquivo criado: {path}")

# Ponto de entrada
if __name__ == "__main__":
    base_dir = Path.cwd() / "desafio-rpa-python"
    create_structure(base_dir, structure["desafio-rpa-python"])
    print("\nEstrutura de pastas criada com sucesso!")