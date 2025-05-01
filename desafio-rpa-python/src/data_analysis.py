import pandas as pd
from pathlib import Path

def analyze_quotes():
    """Analisa o arquivo CSV e retorna estatísticas importantes"""
    try:
        # Caminho dinâmico para o arquivo CSV
        base_dir = Path(__file__).resolve().parent
        csv_path = base_dir / "data" / "quotes.csv"

        df = pd.read_csv(csv_path)
        
        # Análises solicitadas
        num_quotes = len(df)
        top_author = df['author'].mode()[0]
        top_author_count = df['author'].value_counts()[top_author]
        
        # Processamento das tags
        all_tags = []
        for tags in df['tags'].dropna():
            all_tags.extend(tags.split(", "))
        
        tag_series = pd.Series(all_tags)
        top_tag = tag_series.mode()[0]
        top_tag_count = tag_series.value_counts()[top_tag]
        
        # Exibição dos resultados
        print("\n📊 Análise das Citações:")
        print(f"• Total de citações: {num_quotes}")
        print(f"• Autor mais frequente: {top_author} ({top_author_count} citações)")
        print(f"• Tag mais popular: {top_tag} ({top_tag_count} ocorrências)")
        
        return {
            "total_quotes": num_quotes,
            "top_author": top_author,
            "top_author_count": top_author_count,
            "top_tag": top_tag,
            "top_tag_count": top_tag_count
        }
    except Exception as e:
        print(f"❌ Erro na análise: {e}")
        return None

if __name__ == "__main__":
    analyze_quotes()
