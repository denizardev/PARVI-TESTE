from src.web_scraping import main as run_scraping
from src.data_analysis import analyze_quotes
from src.email_sender import send_report

def main():
    print("🚀 Iniciando pipeline RPA completo...\n")
    
    # Parte 1: Web Scraping
    print("🔍 Parte 1: Coletando citações...")
    run_scraping()
    
    # Parte 2: Análise de Dados
    print("\n📊 Parte 2: Analisando dados...")
    analysis = analyze_quotes()
    
    # Parte 3: Envio de E-mail (só executa se a análise foi bem sucedida)
    if analysis:
        print("\n✉️ Parte 3: Enviando relatório por e-mail...")
        send_report(analysis)
    
    print("\n✅ Pipeline concluído com sucesso!")

if __name__ == "__main__":
    main()