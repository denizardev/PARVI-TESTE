# email_sender.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import os

def send_report(analysis_results):
    """Envia relatório por e-mail com anexo CSV usando configurações do Gmail"""
    
    # Configurações do seu e-mail
    sender_email = "denizard.oliveira@gmail.com"
    sender_password = "oluqosczntfntzzz"  # Senha de app gerada
    recipients = ["denizard.oliveira@gmail.com"]  # Enviando para você mesmo
    
    # Criar mensagem
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = "[DESAFIO RPA] Relatório de Citações - Resultados"
    
    # Corpo do e-mail formatado
    email_body = f"""
    📊 Relatório de Análise - Desafio RPA Python

    Resultados obtidos:
    ==================================
    • Total de citações: {analysis_results['total_quotes']}
    • Autor mais frequente: {analysis_results['top_author']} ({analysis_results['top_author_count']} citações)
    • Tag mais popular: {analysis_results['top_tag']} ({analysis_results['top_tag_count']} ocorrências)

    Anexo: Arquivo CSV com todas as citações coletadas
    ==================================
    
    Att,
    Denizard Oliveira
    """
    
    msg.attach(MIMEText(email_body, 'plain'))
    
    # Anexar arquivo CSV (caminho corrigido para data dentro de src)
    try:
        csv_path = Path(__file__).parent / "data" / "quotes.csv"
        
        with open(csv_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            "attachment; filename=quotes.csv",
        )
        msg.attach(part)
    except FileNotFoundError:
        print(f"❌ ERRO: Arquivo CSV não encontrado em: {csv_path}")
        return False
    except Exception as e:
        print(f"❌ Erro ao processar anexo: {str(e)}")
        return False
    
    # Enviar e-mail
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipients, msg.as_string())
        
        print("✅ E-mail enviado com sucesso!")
        return True
    
    except Exception as e:
        print(f"❌ Falha no envio: {str(e)}")
        print("\nDicas para solução:")
        print("1. Verifique se a senha de app está correta")
        print("2. Confira o acesso a apps menos seguros: https://myaccount.google.com/lesssecureapps")
        print("3. Verifique a conexão com internet")
        return False

# Para teste direto
if __name__ == "__main__":
    # Dados de exemplo para teste
    test_results = {
        "total_quotes": 10,
        "top_author": "Albert Einstein",
        "top_author_count": 3,
        "top_tag": "inspirational",
        "top_tag_count": 2
    }
    
    if send_report(test_results):
        print("🔥 Teste de envio concluído com sucesso!")
    else:
        print("💥 Falha no teste de envio!")