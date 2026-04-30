# F1-Data-Analytics-Pipeline
Este projeto tem como objetivo o planejamento de um pipeline de engenharia de dados aplicado ao contexto da Formula 1

A proposta consiste em integrar dados históricos e dados em tempo real (simulados), permitindo análise de desempenho de pilotos, equipes e corridas por meio de um fluxo estruturado de dados.

❗ Problema

Os dados da Fórmula 1 estão:

Distribuídos em múltiplas fontes
Em diferentes formatos (JSON, CSV)
Com diferentes frequências (batch e streaming)

Isso dificulta a análise integrada e a geração de insights consistentes.


🎯 Objetivos
Integrar dados batch e streaming
Estruturar e armazenar os dados
Permitir transformação e análise
Disponibilizar dados para dashboards


👥 Stakeholders
Analistas de dados esportivos
Fãs de Fórmula 1
Criadores de conteúdo
Equipes (simulado)


📊 Definição dos Dados
📦 Dados Batch
Resultados de corridas
Classificações
Tempos de volta
Dados de pilotos e equipes

Fontes:

API pública (ex: Ergast)
Arquivos CSV

Formato: JSON / CSV
Latência: Alta


⚡ Dados de Streaming
Velocidade
Posição na pista
Pit stops
Eventos de corrida

Fonte: Simulação (Python)
Formato: JSON
Latência: Baixa


🧩 Domínios e Serviços
Domínios
Corridas
Pilotos
Equipes
Telemetria
Analytics
Serviços
Ingestão de dados batch
Ingestão de streaming
Processamento de dados
Armazenamento
Consumo (dashboards/API)


🏗️ 4.4 Arquitetura — Fluxo de Dados
📌 Visão Geral

A arquitetura proposta para o projeto segue uma abordagem híbrida baseada em:

Arquitetura Lambda (processamento batch + streaming)
Conceito de Data Lake com organização em camadas (Medalhão)

Essa abordagem permite lidar tanto com dados históricos quanto com dados em tempo real, garantindo flexibilidade e escalabilidade.

🔄 Fluxo de Dados (Ponta a Ponta)

flowchart LR

%% FONTES
A[API F1 / CSV] --> B[Ingestão Batch]
C[Streaming Simulado] --> D[Kafka]

%% INGESTÃO
B --> E[Camada Bronze - Raw Data]
D --> E

%% DATA LAKE
E --> F[Camada Silver - Dados Limpos]
F --> G[Camada Gold - Dados Agregados]

%% PROCESSAMENTO
F --> H[Processamento Batch (Python/Spark)]
D --> I[Processamento Streaming]

%% CONSUMO
G --> J[Dashboard (Power BI)]
G --> K[API / Serviços]


🧱 Descrição das Etapas
🔹 Fontes de Dados
APIs e arquivos CSV fornecem dados históricos (batch)
Streaming simulado representa eventos em tempo real
🔹 Ingestão
Dados batch são coletados periodicamente
Dados de streaming são enviados continuamente via Apache Kafka
🔹 Armazenamento (Data Lake)

Os dados são organizados em camadas:

Bronze: dados brutos, sem tratamento
Silver: dados limpos e estruturados
Gold: dados agregados e prontos para análise
🔹 Processamento
Batch: transformação com Python ou Apache Spark
Streaming: processamento em tempo real (conceitual)
🔹 Consumo
Dashboards com Power BI
Possível exposição via APIs


⚖️ Justificativa da Arquitetura

A escolha da arquitetura Lambda combinada com Data Lake se justifica por:

Suporte a dados batch e streaming
Separação entre ingestão, processamento e consumo
Facilidade de expansão futura
Organização eficiente dos dados em camadas


🔄 Trade-offs
✔ Vantagens
Escalabilidade
Flexibilidade
Suporte a múltiplos tipos de dados
Organização clara (Medalhão)


❌ Desvantagens
Maior complexidade arquitetural
Necessidade de gerenciar múltiplos fluxos (batch + streaming)
Dependência de ferramentas mais robustas


🔁 Considerações sobre Escalabilidade e Acoplamento
Baixo acoplamento: cada etapa (ingestão, processamento, consumo) funciona de forma independente
Alta escalabilidade: possível substituir tecnologias sem impactar todo o sistema
Reversibilidade: decisões podem ser ajustadas na Parte 2 (ex: trocar Spark por pandas)

⚙️ Tecnologias
🔹 Ingestão
API REST
Apache Kafka
🔹 Armazenamento
PostgreSQL
Data Lake (arquivos locais)
🔹 Processamento
Python (pandas)
Apache Spark (opcional)
🔹 Orquestração
Apache Airflow
🔹 Visualização
Power BI


🔐 Governança e DataOps
Versionamento com GitHub
Monitoramento por logs
Validação de dados
Controle básico de qualidade


⚠️ Riscos e Limitações
Dependência de APIs externas
Dados de streaming simulados
Limitações de hardware
Complexidade de ferramentas distribuídas


🚀 Próximos Passos
Implementar ingestão de dados
Criar banco de dados PostgreSQL
Desenvolver pipeline em Python
Simular streaming
Criar dashboards no Power BI


📚 Referências
Documentação de APIs de Fórmula 1
Documentação oficial das ferramentas
Conteúdo das aulas da disciplina
