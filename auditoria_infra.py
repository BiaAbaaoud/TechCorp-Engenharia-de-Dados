import pandas as pd

# 1. Lendo o arquivo otimizado (Big Data Style)
df = pd.read_parquet('backup_infra_techcorp.parquet')

print("📊 RELATÓRIO DE AUDITORIA - TECHCORP")
print("-" * 40)

# 2. Qual servidor está mais lento? (Média de latência)
latencia_media = df.groupby('servidor')['latencia_ms'].mean().sort_values(ascending=False)
print("\n🐢 Servidores por Latência Média (ms):")
print(latencia_media)

# 3. Onde estão os erros críticos? (Status 500)
erros_500 = df[df['status_http'] == 500].shape[0]
print(f"\n🚨 Total de Erros Críticos (500): {erros_500}")

# 4. Servidor com mais instabilidade (Contagem de erros por servidor)
ranking_erros = df[df['status_http'] >= 400]['servidor'].value_counts()
print("\n🏆 Ranking de Instabilidade (Erros 400 e 500):")
print(ranking_erros)

# 5. Insight de Negócio
servidor_ruim = latencia_media.index[0]
print(f"\n💡 RECOMENDAÇÃO: Verificar o servidor '{servidor_ruim}', ele está com a maior lentidão.")