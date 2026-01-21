import sqlite3
import pandas as pd
import os
import random
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO DE CAMINHOS ---
pasta_projeto = r'C:\Users\Sucesso\Desktop\TechCorp-Engenharia-de-Dados'
caminho_db = os.path.join(pasta_projeto, 'shieldbank_credito.db')
caminho_parquet = os.path.join(pasta_projeto, 'backup_infra_techcorp.parquet')

# Garante que a pasta exista (caso você rode em outro lugar)
if not os.path.exists(pasta_projeto):
    os.makedirs(pasta_projeto)

print(f"🚀 Iniciando operação em: {pasta_projeto}")

# --- PASSO 1: Gerar 1000 logs de infraestrutura ---
print("📊 Gerando 1000 registros sintéticos...")

servidores = ['aws-us-east-1', 'aws-sa-east-1', 'azure-west-us', 'gcp-europe-west']
status_codes = [200, 201, 400, 404, 500]
data_inicial = datetime.now() - timedelta(days=30)

dados = []
for i in range(1000):
    dados.append({
        'log_id': i + 1,
        'timestamp': data_inicial + timedelta(minutes=random.randint(1, 43200)),
        'servidor': random.choice(servidores),
        'api_endpoint': f"/v1/api/{random.choice(['users', 'payments', 'auth', 'data'])}",
        'latencia_ms': random.uniform(10.5, 500.0),
        'status_http': random.choice(status_codes),
        'consumo_cpu_percent': random.uniform(5.0, 95.0)
    })

df_tech = pd.DataFrame(dados)

# --- PASSO 2: Salvar no SQLite (Caminho Específico) ---
try:
    conn = sqlite3.connect(caminho_db)
    df_tech.to_sql('logs_infraestrutura', conn, if_exists='replace', index=False)
    conn.close()
    print(f"✅ Tabela 'logs_infraestrutura' salva com sucesso em: {caminho_db}")
except Exception as e:
    print(f"❌ Erro ao salvar no banco: {e}")

# --- PASSO 3: Migração para Parquet (Otimização) ---
print("🔄 Convertendo dados para formato Parquet...")

try:
    # Lendo de volta para garantir que a migração é real
    conn = sqlite3.connect(caminho_db)
    df_para_backup = pd.read_sql('SELECT * FROM logs_infraestrutura', conn)
    conn.close()

    # Salvando em Parquet
    df_para_backup.to_parquet(caminho_parquet, compression='snappy')
    print(f"✅ Arquivo Parquet gerado: {caminho_parquet}")
except Exception as e:
    print(f"❌ Erro na migração Parquet: {e}")

# --- PASSO 4: Comparação de Eficiência ---
if os.path.exists(caminho_db) and os.path.exists(caminho_parquet):
    tamanho_db = os.path.getsize(caminho_db) / 1024
    tamanho_parquet = os.path.getsize(caminho_parquet) / 1024
    
    print("-" * 40)
    print(f"📈 RESULTADO DA ENGENHARIA:")
    print(f"Tamanho SQLite: {tamanho_db:.2f} KB")
    print(f"Tamanho Parquet: {tamanho_parquet:.2f} KB")
    print(f"Redução de aproximadamente {100 - (tamanho_parquet/tamanho_db*100):.1f}%")
    print("-" * 40)