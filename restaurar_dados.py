import pandas as pd
import sqlite3
import os

# --- CONFIGURAÇÃO DE CAMINHOS ---
pasta_projeto = r'C:\Users\Sucesso\Desktop\TechCorp-Engenharia-de-Dados'
caminho_db = os.path.join(pasta_projeto, 'shieldbank_credito.db')
caminho_parquet = os.path.join(pasta_projeto, 'backup_infra_techcorp.parquet')

print("🛠️ Iniciando processo de restauração de desastre...")

# 1. Verificar se o backup existe
if os.path.exists(caminho_parquet):
    print("📦 Backup Parquet encontrado! Lendo dados...")
    
    # 2. Ler o arquivo Parquet (o backup)
    df_restaurado = pd.read_parquet(caminho_parquet)
    
    # 3. Conectar ao SQLite e devolver a tabela
    try:
        conn = sqlite3.connect(caminho_db)
        # O 'replace' vai criar a tabela novamente do zero
        df_restaurado.to_sql('logs_infraestrutura', conn, if_exists='replace', index=False)
        conn.close()
        
        print("-" * 40)
        print(f"✅ SUCESSO! A tabela 'logs_infraestrutura' foi restaurada.")
        print(f"🔢 Total de registros recuperados: {len(df_restaurado)}")
        print("-" * 40)
        
    except Exception as e:
        print(f"❌ Erro ao tentar restaurar: {e}")
else:
    print("⚠️ Erro: Arquivo de backup não encontrado. O desastre é real!")