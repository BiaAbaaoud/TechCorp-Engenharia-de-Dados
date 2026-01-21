# TechCorp: Engenharia de Dados e Resiliência de Infraestrutura

Este projeto simula um ecossistema de monitoramento de infraestrutura focado em resiliência de dados (DRP) e eficiência de armazenamento. Implementamos um pipeline ETL para migração de logs críticos de um banco relacional para um formato colunar otimizado.

### 🎯 Objetivo
Reduzir custos de armazenamento e processamento através da migração de dados de um banco relacional (SQLite) para o formato Parquet, garantindo uma estratégia de **Disaster Recovery** e visualização executiva para suporte à decisão rápida.

### 🛠️ O Que Foi Feito
1. **Ingestão & Simulação:** Geração de logs sintéticos contendo latência e status HTTP.
2. **Armazenamento:** Persistência inicial em SQLite.
3. **Otimização:** Migração para `.parquet` com compressão *snappy*.
4. **Resiliência:** Implementação de rotina de restauração automática (Data Recovery).

### 📂 Estrutura de Documentos
* `migracao_dados_parquet.py`: Script de geração e conversão SQL -> Parquet.
* `auditoria_infra.py`: Analisador de logs e latência.
* `restaurar_dados.py`: Mecanismo de Disaster Recovery.
* `dashboard_executivo.py`: Gera o relatório visual `analise_viva_techcorp.png`.
* `shieldbank_credito.db`: Banco de dados relacional.
* `backup_infra_techcorp.parquet`: Dataset otimizado.

### 🧰 Ferramentas Utilizadas
* **Python 3.x**
* **Pandas** (Manipulação de dados)
* **SQLite3** (Banco Relacional)
* **PyArrow** (Motor para Parquet)
* **Matplotlib/Seaborn** (Visualização)

### 🚀 Como Executar o Projeto
1. **Geração:** `python migracao_dados_parquet.py`
2. **Auditoria:** `python auditoria_infra.py`
3. **Dashboard:** `python dashboard_executivo.py`
4. **Restauração:** `python restaurar_dados.py`

### ❓ FAQ - Perguntas Frequentes

**1. Por que migrar de SQLite para Parquet?**
O Parquet utiliza armazenamento colunar e compressão Snappy, o que reduz o espaço em disco em mais de 60% e acelera drasticamente consultas para análise de Big Data.

**2. Qual a principal métrica de performance monitorada?**
A Latência Média (ms). O sistema identifica gargalos em servidores específicos (como AWS, Azure ou GCP) para sugerir o rebalanceamento de carga imediato.

**3. Como o projeto lida com erros críticos?**
O monitoramento foca nos Status HTTP 4xx (erro do cliente) e 5xx (erro de servidor). O dashboard visual categoriza essas falhas para que a equipe de SRE possa atuar na região correta.

**4. O projeto é escalável?**
Sim. A estrutura de scripts e o formato Parquet são os padrões utilizados em grandes clusters de dados, permitindo que este mesmo pipeline processe milhões de registros com alta eficiência.

**5. Quais bibliotecas são necessárias para rodar o projeto?**
Para executar todos os scripts e gerar os gráficos, utilize: `pip install pandas pyarrow matplotlib seaborn`.

**6. Como o Disaster Recovery é testado?**
Ao executar `python restaurar_dados.py`, o sistema busca o backup imutável em Parquet e reconstrói o banco de dados SQL do zero, simulando a recuperação após uma perda total da tabela original.

---
**Desenvolvedora:** [BiaAbaaoud](https://github.com/BiaAbaaoud)