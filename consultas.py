import pandas as pd

df = pd.read_csv('data/Dados_para_TP2_2025.csv', encoding='utf-8', sep=';')

df['Salário'] = df['Salário'].str.replace('.', '').str.replace(',', '.').astype(float)
df['Data da Contratação'] = pd.to_datetime(df['Data da Contratação'], format='%d/%m/%Y')

print("="*60)
print("CONSULTAS SQL - TP2")
print("="*60)

# Busca 01
print("\n1. Funcionários do TI:")
funcionarios_ti = df[df['Departamento'] == 'TI']
print(funcionarios_ti)

# Busca 02
print("\n2. Funcionários com salário maior que 5 mil:")
funcionario_salario_maior_5k = df[df['Salário'] > 5000][['Nome']]
print(funcionario_salario_maior_5k)

# Busca 03
print("\n3. Funcionários contratados após 01/01/2022:")
funcionarios_contratados_apos_2022 = df[df['Data da Contratação'] > '2022-01-01'][['Nome', 'Data da Contratação']]
print(funcionarios_contratados_apos_2022)

# Busca 04
print("\n4. Salário médio por departamento:")
salario_medio_por_departamento = df.groupby('Departamento')['Salário'].mean().reset_index()
salario_medio_por_departamento.columns = ['Departamento', 'Salário Médio']
salario_medio_por_departamento['Salário Médio'] = salario_medio_por_departamento['Salário Médio'].round(2)
print(salario_medio_por_departamento)

# Busca 05
print("\n5. Funcionários com 'da Silva' no nome:")
funcionarios_da_silva = df[df['Nome'].str.contains("da Silva", case=False, na=False)][['Nome', 'Cargo']]
print(funcionarios_da_silva)

# Busca 06
print("\n6. Funcionários com cargo de confiança:")
funcionarios_cargo_confianca = df[df['Cargo Confiança'] == 1]
print(funcionarios_cargo_confianca)

# Busca 07
print("\n7. Analistas:")
funcionarios_analistas = df[df['Cargo'] == 'Analista'][['Nome', 'Departamento']]
print(funcionarios_analistas)

#Busca 08
print("\n8. Funcionários ordenados por salário (decrescente):")
funcionarios_ordenados_salario = df[['Nome', 'Salário']].sort_values(by='Salário', ascending=False)
print(funcionarios_ordenados_salario)

#Busca 09
print("\n9. Funcionários contratados em 2023:")
funcionarios_contratados_2023 = df[df['Data da Contratação'].dt.year == 2023][['Nome', 'ID Funcionario']]
print(funcionarios_contratados_2023)

#Busca 10
print("\n10. Funcionários do Jurídico com salário <= 3.000:")
funcionarios_juridico_salario_menor_3000 = df[(df['Departamento'] == 'Jurídico') & (df['Salário'] <= 3000.0)][['Nome']]
print(funcionarios_juridico_salario_menor_3000)

#Busca 11
print("\n11. Funcionários Gerentes ou Diretores:")
funcionarios_gerentes_diretores = df[df['Cargo'].isin(['Gerente', 'Diretor'])][['Nome']]
print(funcionarios_gerentes_diretores)

# Busca 12
print("\n12. Funcionários e anos de experiência:")
df['Anos de Experiência'] = 2025 - df['Data da Contratação'].dt.year
funcionarios_anos_experiencia = df[['Nome', 'Anos de Experiência']]
print(funcionarios_anos_experiencia)

# Busca 13
print("\n13. Funcionários ordenados alfabeticamente:")
funcionarios_ordenados_alfabeticamente = df[['Nome', 'Departamento']].sort_values(by='Nome')
print(funcionarios_ordenados_alfabeticamente)

# Busca 14
print("\n14. Funcionários com nome começando com 'João':")
funcionarios_nome_joao = df[df['Nome'].str.startswith('João', na=False)][['Nome', 'Cargo']]
print(funcionarios_nome_joao)

# Busca 15
print("\n15. Quantidade de funcionários por departamento:")
quantidade_funcionarios_por_departamento = df.groupby('Departamento').size().reset_index(name='Quantidade')
print(quantidade_funcionarios_por_departamento)