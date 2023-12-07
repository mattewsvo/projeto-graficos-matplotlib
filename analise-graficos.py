import sqlite3
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from faker import Faker

# Inicialização do Faker para gerar dados fictícios
fake = Faker()

# Função para gerar um número de CPF fictício
def generate_cpf():
    return f'{random.randint(100, 999):03}.{random.randint(100, 999):03}.{random.randint(100, 999):03}-{random.randint(10, 99):02}'

# Função para criar a tabela no banco de dados SQLite
def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS integracao_cliente_carro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cliente TEXT,
            cpf TEXT,
            carro_comprado TEXT,
            valor_carro INTEGER,
            data DATE
        )
    ''')

# Função para gerar dados aleatórios e inserir no banco de dados
def generate_random_data(cursor):
    # Lista de carros com nomes e valores aleatórios
    carros = [
        {"nome": "Toyota Corolla", "valor": random.randint(20000, 25000)},
        {"nome": "Honda Civic", "valor": random.randint(22000, 30000)},
        {"nome": "Ford Mustang", "valor": random.randint(55000, 60000)},
        {"nome": "Chevrolet Malibu", "valor": random.randint(30000, 40000)},
        {"nome": "Volkswagen Golf", "valor": random.randint(45000, 50000)},
        {"nome": "BMW 3 Series", "valor": random.randint(55000, 60000)},
        {"nome": "Mercedes-Benz C-Class", "valor": random.randint(60000, 65000)},
        {"nome": "Nissan Altima", "valor": random.randint(38000, 40000)},
        {"nome": "Hyundai Sonata", "valor": random.randint(22000, 22000)},
        {"nome": "Audi A4", "valor": random.randint(20000, 500000)},
    ]

    # Data inicial para gerar vendas ao longo do tempo
    data_inicial = datetime(2023, 1, 1)

    for carro in carros:
        # Total de vendas por mes, em um intervalo de 6 meses, agora varia entre 50 e 200
        total_vendas = random.randint(50, 200)

        for _ in range(6):
            # Formato da data para inserção no banco de dados
            data = data_inicial.strftime('%d-%m-%y')
            # Distribuição aproximada de vendas ao longo do tempo
            quantidade_vendas = total_vendas // 6
            cpf = generate_cpf()
            nome_cliente = fake.name()

            # Ajuste nas vendas para cada modelo
            quantidade_vendas_modelo = random.randint(quantidade_vendas - 20, quantidade_vendas + 20)

            # Inserção dos dados na tabela
            cursor.execute('''
                INSERT INTO integracao_cliente_carro (nome_cliente, cpf, carro_comprado, valor_carro, data)
                VALUES (?, ?, ?, ?, ?)
            ''', (nome_cliente, cpf, carro["nome"], carro["valor"], data))

            # Avança 30 dias para o próximo período de vendas
            data_inicial += timedelta(days=30)

# Função para obter todos os dados da tabela integrada
def get_integrated_table(cursor):
    cursor.execute('SELECT * FROM integracao_cliente_carro')
    return cursor.fetchall()

# Função para calcular a média de gastos por cliente
def analyze_average_spending_per_customer(tabela_integrada):
    valores_por_cliente = {}
    for linha in tabela_integrada:
        nome_cliente = linha[1]
        valor_carro = linha[4]
        if nome_cliente in valores_por_cliente:
            valores_por_cliente[nome_cliente] += valor_carro
        else:
            valores_por_cliente[nome_cliente] = valor_carro

    media_gastos = sum(valores_por_cliente.values()) / len(valores_por_cliente)
    return media_gastos

# Função para analisar a distribuição de carros comprados por modelo
def analyze_distribution_by_model(cursor):
    cursor.execute('SELECT carro_comprado, COUNT(*) FROM integracao_cliente_carro GROUP BY carro_comprado')
    dados_modelos = cursor.fetchall()
    nomes_modelos, _ = zip(*dados_modelos)

    # Gere valores aleatórios para a distribuição de carros por modelo
    valores_modelos = [random.randint(20, 100) for _ in nomes_modelos]

    return nomes_modelos, valores_modelos

# Função para analisar o total de vendas ao longo do tempo
def analyze_total_sales_over_time(cursor):
    cursor.execute('SELECT data, SUM(valor_carro) FROM integracao_cliente_carro GROUP BY data')
    dados_evolucao_vendas = cursor.fetchall()
    datas, valores_totais = zip(*dados_evolucao_vendas)
    return datas, valores_totais

# Função para analisar a distribuição de carros comprados por valor
def analyze_car_distribution_by_value(cursor):
    cursor.execute('SELECT valor_carro, COUNT(*) FROM integracao_cliente_carro GROUP BY valor_carro')
    dados_valores = cursor.fetchall()
    valores, contagens = zip(*dados_valores)
    return valores, contagens

# Função para analisar o total de vendas por modelo
def analyze_total_sales_by_model(cursor):
    cursor.execute('SELECT carro_comprado, SUM(valor_carro) FROM integracao_cliente_carro GROUP BY carro_comprado')
    dados_vendas_modelos = cursor.fetchall()
    nomes_modelos, valores_modelos = zip(*dados_vendas_modelos)
    return nomes_modelos, valores_modelos

# Função para visualizar a tabela no formato de texto
def visualizar_tabela(cursor):
    cursor.execute('SELECT * FROM integracao_cliente_carro')
    tabela_db = cursor.fetchall()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    table = ax.table(cellText=tabela_db, colLabels=["ID", "Nome do Cliente", "CPF", "Carro Comprado", "Valor do Carro", "Data"], loc='center')
    plt.show()

# Função para visualizar a análise 1
def visualizar_analise_1(media_gastos):
    print(f'Análise 1: Valor médio gasto por cliente em carros: R$ {media_gastos:.2f}')

# Função para visualizar a análise 2
def visualizar_analise_2(nomes_modelos, valores_modelos):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(valores_modelos, labels=nomes_modelos, autopct='%1.1f%%', startangle=90)
    ax.set_title('Distribuição de Carros Comprados por Modelo')
    plt.show()
    print("Análise 2: Distribuição percentual de carros comprados por modelo.")

# Função para visualizar a análise 3
def visualizar_analise_3(datas, valores_totais):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(datas, valores_totais, marker='o', label='Valor Total')
    ax.bar(datas, valores_totais, alpha=0.7, label='Barras Empilhadas', color='orange')
    ax.set_xlabel('Data')
    ax.set_ylabel('Valor Total de Vendas')
    ax.set_title('Evolução das Vendas ao Longo do Tempo')
    ax.legend()
    plt.xticks(rotation=45, ha='right')
    plt.show()
    print("Análise 3: Evolução das vendas ao longo do tempo com gráfico de linha e barras empilhadas.")

# Função para visualizar a análise 4
def visualizar_analise_4(valores_carros, contagens_carros):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(valores_carros, contagens_carros, alpha=0.7)
    ax.set_xlabel('Valor do Carro (R$)')
    ax.set_ylabel('Quantidade de Vendas')
    ax.set_title('Distribuição de Carros Comprados por Valor')
    plt.show()
    print("Análise 4: Distribuição de carros comprados em relação ao valor com gráfico de dispersão.")

# Função para visualizar a análise 5
def visualizar_analise_5(nomes_modelos, valores_modelos):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(nomes_modelos, valores_modelos, color='green')
    ax.set_xlabel('Modelos de Carro')
    ax.set_ylabel('Valor Total de Vendas (R$)')
    ax.set_title('Valor Total de Vendas por Modelo')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    print("Análise 5: Valor total de vendas por modelo com gráfico de barras.")

# Verificação se o script está sendo executado como principal
if __name__ == "__main__":
    # Conexão ao banco de dados SQLite em memória
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Criação da tabela e geração de dados aleatórios
    create_table(cursor)
    generate_random_data(cursor)
    tabela_integrada = get_integrated_table(cursor)

    # Visualização da tabela e análises
    visualizar_tabela(cursor)
    visualizar_analise_1(analyze_average_spending_per_customer(tabela_integrada))
    visualizar_analise_2(*analyze_distribution_by_model(cursor))
    visualizar_analise_3(*analyze_total_sales_over_time(cursor))
    visualizar_analise_4(*analyze_car_distribution_by_value(cursor))
    visualizar_analise_5(*analyze_total_sales_by_model(cursor))

    # Fechamento da conexão com o banco de dados
    conn.close()