import os
import sys
import csv
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    """Configura o driver do Chrome com opções adequadas"""
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # descomente se quiser rodar sem abrir o navegador
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_page_load_timeout(30)
        return driver
    except Exception as e:
        print(f"❌ Falha ao configurar o driver: {e}")
        raise

def scrape_quotes(driver):
    """Extrai citações, autores e tags do site"""
    url = "https://quotes.toscrape.com/js-delayed/"
    
    try:
        print("🌐 Acessando o site...")
        driver.get(url)
        
        print("⏳ Aguardando carregamento do conteúdo...")
        WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.CLASS_NAME, "quote"))
        )
        
        start_time = time.time()
        while time.time() - start_time < 10:
            quotes = driver.find_elements(By.CLASS_NAME, "quote")
            if len(quotes) >= 10:
                break
            time.sleep(0.5)
        else:
            print("⚠️ Poucas citações encontradas - continuando mesmo assim")

        print(f"🔍 Extraindo {len(quotes)} citações...")
        results = []
        
        for quote in quotes:
            try:
                text = quote.find_element(By.CLASS_NAME, "text").get_attribute("textContent").strip('"')
                author = quote.find_element(By.CLASS_NAME, "author").text
                tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]
                
                results.append({
                    "quote": text,
                    "author": author,
                    "tags": ", ".join(tags) if tags else "Sem tags"
                })
            except Exception as e:
                print(f"⚠️ Erro ao processar uma citação: {e}")
                continue
        
        return results

    except Exception as e:
        print(f"❌ Erro durante o scraping: {e}")
        raise

def save_to_csv(data, filename="data/quotes.csv"):
    """Salva os dados em um arquivo CSV no mesmo diretório do script"""
    try:
        script_dir = Path(__file__).parent.resolve() if '__file__' in globals() else Path.cwd()
        full_path = script_dir / filename

        if not data:
            print("⚠️ Nenhum dado para salvar")
            return False

        os.makedirs(full_path.parent, exist_ok=True)

        with open(full_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
            writer.writeheader()
            writer.writerows(data)

        print(f"💾 Dados salvos com sucesso em {full_path}")
        return True

    except Exception as e:
        print(f"❌ Falha ao salvar arquivo CSV: {e}")
        return False

def main():
    """Função principal para execução do script"""
    driver = None
    try:
        driver = setup_driver()
        quotes_data = scrape_quotes(driver)
        
        if not quotes_data:
            print("❌ Nenhum dado foi coletado")
            return False
        
        if not save_to_csv(quotes_data):
            return False
            
        return True

    except Exception as e:
        print(f"❌ Erro fatal: {e}")
        return False

    finally:
        if driver:
            print("🛑 Encerrando driver...")
            driver.quit()

if __name__ == "__main__":
    success = main()
    if not success:
        print("❌ O script terminou com erros")
        sys.exit(1)
    print("✅ Script executado com sucesso")
    sys.exit(0)
