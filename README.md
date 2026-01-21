# TechCorp: Engenharia de Dados e Resiliência de Infraestrutura

Este projeto simula um ecossistema de monitoramento de infraestrutura focado em resiliência de dados (DRP) e eficiência de armazenamento. Implementamos um pipeline ETL para migração de logs críticos de um banco relacional para um formato colunar otimizado.

### 🎯 Objetivo
Reduzir custos de armazenamento e processamento através da migração de dados de um banco relacional (SQLite) para o formato Parquet, garantindo uma estratégia de **Disaster Recovery** e visualização executiva para suporte à decisão rápida.

### 🛠️ O Que Foi Feito (Passo a Passo)
1.  **Ingestão & Simulação:** Geração de 1.000 logs sintéticos contendo latência, status HTTP (200, 4xx, 500) e consumo de CPU.
2.  **Armazenamento Inicial:** Persistência dos dados brutos em banco de dados SQLite (`shieldbank_credito.db`).
3.  **Processo de ETL & Otimização:** Migração dos dados para o formato `.parquet` com compressão *snappy*, alcançando uma redução significativa no tamanho do arquivo.
4.  **Auditoria Técnica:** Script de análise para identificar gargalos de latência e ranking de instabilidade por servidor.
5.  **Plano de Recuperação (DRP):** Implementação de rotina de restauração automática do banco de dados a partir do backup comprimido caso ocorra um `DROP TABLE`.
6.  **Data Viz:** Dashboard executivo profissional com gráfico de pizza e análise de plano de contenção.

### 📂 Estrutura de Documentos
| Arquivo | Descrição |
| :--- | :--- |
| `migracao_dados_parquet.py` | Script de geração de dados e conversão SQL -> Parquet. |
| `auditoria_infra.py` | Analisador de logs focado em latência e erros críticos. |
| `restaurar_dados.py` | Mecanismo de Disaster Recovery (Restaura o DB via Parquet). |
| `dashboard_executivo.py` | Gera o relatório visual `analise_viva_techcorp.png`. |
| `shieldbank_credito.db` | Banco de dados relacional utilizado na operação. |
| `backup_infra_techcorp.parquet` | Dataset otimizado e comprimido para longa retenção. |

### 🧰 Ferramentas Utilizadas
* **Python 3.x**
* **Pandas** (Data Manipulation)
* **SQLite3** (Relational Database)
* **PyArrow / FastParquet** (Columnar Storage Engine)
* **Matplotlib** (Visualização de Dados)

### ❓ FAQ - Perguntas Frequentes
1.  **Por que migrar de SQLite para Parquet?** O Parquet economiza espaço e é muito mais veloz para ferramentas de Analytics por ser colunar.
2.  **O que acontece se a tabela SQL for deletada?** O script `restaurar_dados.py` reconstrói a tabela original em segundos usando o backup.
3.  **Como a latência é calculada?** Através da média aritmética da latência registrada em milissegundos para cada servidor global.
4.  **Por que as cores do dashboard são vibrantes?** Para facilitar a identificação imediata de incidentes em ambientes de monitoramento (NOC).
5.  **Qual o motor de compressão utilizado?** Utilizamos o *Snappy*, padrão na indústria por ser extremamente rápido e eficiente.
6.  **Como atualizar o banco após novos logs?** Basta rodar o script de migração novamente para atualizar o backup Parquet com os dados mais recentes.

---

### 🚀 Como Executar o Projeto na Prática

Siga esta ordem para ver o fluxo de Engenharia de Dados acontecer:

1. **Geração e Ingestão:**
   Execute o comando abaixo para criar o banco de dados e o backup inicial:
   ```bash
   python migracao_dados_parquet.py
---
**Desenvolvedora:** BiaAbaaoud