# Projeto Finance - Gestão Financeira

Projeto desenvolvido para a disciplina de Python da Infnet, contendo duas partes principais: gerenciamento de carteira de ações e análise de dados de funcionários.

## Estrutura do Projeto

```
finance/
├── data/                           # Dados para análise
│   └── Dados_para_TP2_2025.csv    # Base de dados de funcionários
├── app.py                          # Sistema de carteira de ações
├── carteira.py                     # Funções de gerenciamento
├── consultas.py                    # Análise de dados com Pandas (TP2)
├── requirements.txt                # Dependências do projeto
└── README.md                       # Documentação
```

---

## Parte 1: Gerenciador de Carteira de Ações

Sistema simples para gerenciamento de carteira de investimentos em ações.

### Funcionalidades

#### 1. Visualizar Carteira
Exibe todas as ações presentes na carteira com informações detalhadas:
- Código da ação
- Quantidade atual
- Meta definida (se houver)
- Status da posição
- Progresso percentual em relação à meta

#### 2. Comprar Ação
Permite adicionar ações à carteira:
- Escolha entre as ações disponíveis
- Define a quantidade desejada
- Atualiza automaticamente posições existentes
- Calcula novo status após a compra

#### 3. Vender Ação
Remove ações da carteira parcial ou totalmente:
- Venda de quantidade específica
- Remoção automática se quantidade chegar a zero
- Atualização do status após venda

#### 4. Definir Meta
Estabelece objetivos de investimento:
- Define meta de quantidade para qualquer ação
- Atualiza metas existentes
- Adiciona ações com quantidade zero à lista de objetivos

### Status das Posições

O sistema classifica automaticamente cada posição:
- **Sem meta**: Ação sem objetivo definido
- **Posição comprada**: Quantidade abaixo da meta estabelecida
- **Posição neutra**: Meta atingida exatamente
- **Posição de venda**: Quantidade acima da meta estabelecida

### Como Executar a Carteira

```bash
python app.py
```

---

##  Parte 2: Análise de Dados de Funcionários (TP2)

Análise de dados de funcionários utilizando **Pandas**, com 15 consultas baseadas em operações SQL.

### Consultas Implementadas

1. **Funcionários do departamento de TI**
2. **Funcionários com salário maior que 5.000,00**
3. **Funcionários contratados após 01/01/2022**
4. **Salário médio por departamento**
5. **Funcionários com "da Silva" no nome**
6. **Funcionários com cargos de confiança**
7. **Analistas (nome e departamento)**
8. **Funcionários ordenados por salário (decrescente)**
9. **Funcionários contratados em 2023**
10. **Funcionários do Jurídico com salário ≤ 3.000,00**
11. **Gerentes ou Diretores**
12. **Funcionários e anos de experiência (considerando 2025)**
13. **Funcionários ordenados alfabeticamente**
14. **Funcionários cujo nome começa com 'João'**
15. **Quantidade de funcionários por departamento**

### Como Executar as Consultas

```bash
python consultas.py
```

---

##  Instalação e Configuração

### Pré-requisitos

- Python 3.x instalado

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/matheuszilli/pb-financial.git
cd finance
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Execute o programa desejado**
```bash
# Para a carteira de ações
python app.py

# Para as consultas de funcionários
python consultas.py
```

---

##  Dependências

- **pandas**: Manipulação e análise de dados

Para instalar manualmente:
```bash
pip install pandas
```

---