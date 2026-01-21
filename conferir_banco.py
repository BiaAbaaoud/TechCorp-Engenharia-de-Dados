import sqlite3

conn = sqlite3.connect('shieldbank_credito.db')
cursor = conn.cursor()

# Conta quantas linhas tem na tabela nova
cursor.execute("SELECT count(*) FROM logs_infraestrutura")
total = cursor.fetchone()[0]

print(f"✅ Sucesso! Existem {total} registros na tabela 'logs_infraestrutura'.")

# Mostra as 5 primeiras linhas para você ver os dados da TechCorp
cursor.execute("SELECT * FROM logs_infraestrutura LIMIT 5")
linhas = cursor.fetchall()

for linha in linhas:
    print(linha)

conn.close()