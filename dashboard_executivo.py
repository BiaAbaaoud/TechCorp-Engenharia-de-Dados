import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuração de caminhos
pasta_projeto = r'C:\Users\Sucesso\Desktop\TechCorp-Engenharia-de-Dados'
caminho_parquet = os.path.join(pasta_projeto, 'backup_infra_techcorp.parquet')

# 1. Carregar dados do backup Parquet
df = pd.read_parquet(caminho_parquet)

# 2. Processamento dos dados
erros_por_servidor = df[df['status_http'] >= 400]['servidor'].value_counts()
pior_servidor = df.groupby('servidor')['latencia_ms'].mean().idxmax()
total_falhas = erros_por_servidor.sum()

# 3. Configuração do Layout (Aumentamos a largura para caber a caixa ao lado)
plt.rcParams['font.family'] = 'sans-serif'
fig, ax = plt.subplots(figsize=(16, 8), facecolor='#FFFFFF')
plt.subplots_adjust(left=0.05, right=0.6) # Abre espaço na direita para o texto

# Cores Vivas (Rosa, Roxo, Vermelho, Azul)
vivid_colors = ['#FF007F', '#8A2BE2', '#FF4500', '#1E90FF']

# 4. Gráfico de Pizza Clássico
patches, texts, autotexts = ax.pie(
    erros_por_servidor, 
    labels=erros_por_servidor.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=vivid_colors, 
    pctdistance=0.75,
    explode=[0.05] * len(erros_por_servidor), # Pequeno destaque entre fatias
    shadow=False
)

# Estilização das fontes
for t in texts: 
    t.set_fontsize(12)
    t.set_fontweight('bold')
    t.set_color('#333333')

for at in autotexts: 
    at.set_color('white')
    at.set_fontweight('bold')
    at.set_fontsize(11)

# Título do Relatório
plt.title('DISTRIBUIÇÃO DE FALHAS POR REGIÃO DE SERVIDOR\nAnálise de Estabilidade de Infraestrutura', 
          fontsize=18, fontweight='bold', pad=20, color='#1A1A1A', loc='left')

# 5. Caixa de Texto Lateral (Estilo Analista Sênior)
analise_texto = (
    "RELATÓRIO DE INCIDÊNCIAS\n"
    "--------------------------------------------------\n"
    f"DIAGNÓSTICO:\n"
    f"Gargalo crítico identificado no servidor\n[{pior_servidor}].\n"
    f"Incidência total de {total_falhas} falhas na rede.\n\n"
    "PLANO DE CONTENÇÃO:\n"
    "Redirecionamento de tráfego para nós\n"
    "estáveis e auditoria de hardware nos\n"
    "pontos críticos identificados.\n\n"
    "PERSPECTIVA:\n"
    "A otimização deve reduzir a latência\n"
    "e estabilizar o tempo de resposta global."
)

# Posicionando a caixa à direita do gráfico (coordenadas x=0.75, y=0.5)
plt.figtext(0.72, 0.5, analise_texto, ha="left", va="center", fontsize=12, 
            linespacing=1.6, fontweight='medium',
            bbox={"facecolor":"#FFFFFF", "edgecolor":"#FF007F", "boxstyle":"round,pad=1.5", "linewidth": 2})

# 6. Salvamento e Exibição
caminho_final = os.path.join(pasta_projeto, 'analise_viva_techcorp.png')
plt.savefig(caminho_final, dpi=300, bbox_inches='tight')
plt.show()

print(f"✅ Dashboard profissional com cores vivas gerado em: {caminho_final}")