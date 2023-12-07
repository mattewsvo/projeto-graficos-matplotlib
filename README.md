Introdução: 

O tema do projeto foi proposto pela faculdade como forma de avaliação individual dos conhecimentos da disciplina de Python. 
Este projeto desafiador visa consolidar e aplicar os conceitos e habilidades adquiridos ao longo da matéria, proporcionando uma oportunidade única para avaliar a nossa proficiência na linguagem de programação Python. Ao abordar aspectos práticos e desafiadores, o projeto não apenas testa a nossa capacidade técnica, mas também estimula criatividade e resolução de problemas. 

Essa abordagem de avaliação contribuiu significativamente para um crescimento holístico das minhas habilidades, capacitando-me a enfrentar problemas do mundo real por meio da aplicação prática de meus conhecimentos em Python.


Definição :

O programa tem como finalidade simular uma integração entre dados de clientes e vendas, armazenando essas informações em uma tabela de um banco de dados SQLite. A simulação envolve a geração de dados fictícios, como nomes de clientes, CPFs, modelos de carros (produto em questão), valores e datas de compra. 

Esses dados são inseridos na tabela, e o programa oferece funcionalidades para análise estatística dessas informações. As análises incluem a média de gastos por cliente, a distribuição de carros comprados por modelo, a evolução das vendas ao longo do tempo, a distribuição de carros comprados por valor e o total de vendas por modelo. 

Além disso, o programa fornece uma visualização tabular dos dados da tabela do banco de dados e gráficos para ilustrar as análises realizadas.


Aprendizados :

esse programa abrange várias áreas e conceitos relacionados à programação em Python, manipulação de dados, análise estatística e visualização gráfica.

Manipulação de Banco de Dados SQLite:

Como criar uma tabela em um banco de dados SQLite.
Como inserir dados aleatórios em um banco de dados.
Geração de Dados Fictícios:

Utilização da biblioteca Faker para gerar dados fictícios, como nomes de clientes.
Manipulação de Datas e Horas:

Trabalho com datas usando a biblioteca datetime.
Análise Estatística:

Cálculo da média de gastos por cliente.
Análise da distribuição de carros comprados por modelo.
Análise do total de vendas ao longo do tempo.
Análise da distribuição de carros comprados por valor.
Análise do total de vendas por modelo.
Visualização Gráfica:

Geração de gráficos de pizza, linha, barras e dispersão usando a biblioteca matplotlib.pyplot.

Organização do código em funções.
Utilização de estruturas de controle como loops e condicionais.
Uso de Estruturas de Dados:

Manipulação de listas para armazenar e processar dados.

Como adicionar comentários explicativos ao código para melhor compreensão.

Como verificar se o script está sendo executado como principal usando __name__.
Ao trabalhar com este programa,podemos ganhar experiência prática em uma variedade de conceitos e técnicas essenciais para o desenvolvimento de software em Python.


Métodos Utilizados :

O programa utiliza várias funções e bibliotecas para realizar suas tarefas. Aqui estão os principais métodos e bibliotecas utilizados:

Funções:

generate_cpf(): Gera um número de CPF fictício.
create_table(cursor): Cria a tabela no banco de dados SQLite.
generate_random_data(cursor): Gera dados aleatórios e os insere no banco de dados.
get_integrated_table(cursor): Obtém todos os dados da tabela integrada.
analyze_average_spending_per_customer(tabela_integrada): Calcula a média de gastos por cliente.
analyze_distribution_by_model(cursor): Analisa a distribuição de carros comprados por modelo.
analyze_total_sales_over_time(cursor): Analisa o total de vendas ao longo do tempo.
analyze_car_distribution_by_value(cursor): Analisa a distribuição de carros comprados por valor.
analyze_total_sales_by_model(cursor): Analisa o total de vendas por modelo.
visualizar_tabela(cursor): Visualiza a tabela no formato de texto.
visualizar_analise_1(media_gastos): Visualiza a análise 1 (média de gastos por cliente).
visualizar_analise_2(nomes_modelos, valores_modelos): Visualiza a análise 2 (distribuição de carros por modelo).
visualizar_analise_3(datas, valores_totais): Visualiza a análise 3 (evolução das vendas ao longo do tempo).
visualizar_analise_4(valores_carros, contagens_carros): Visualiza a análise 4 (distribuição de carros por valor).
visualizar_analise_5(nomes_modelos, valores_modelos): Visualiza a análise 5 (total de vendas por modelo).

Bibliotecas:

sqlite3: Para interação com o banco de dados SQLite.
random: Geração de números aleatórios.
datetime: Manipulação de datas e horas.
matplotlib.pyplot: Geração de gráficos.
Faker: Geração de dados fictícios, como nomes de pessoas.
Essas funções e bibliotecas são combinadas para criar uma simulação de dados de vendas de carros, armazenar esses dados em um banco de dados e realizar análises estatísticas sobre esses dados.


Documentação das funções : 

Função generate_cpf (Ponto 1):

Objetivo:
Gera um número de CPF fictício no formato XXX.XXX.XXX-YY.

Parâmetros:
Não tem parâmetros.

Retorno:
Uma string representando o CPF fictício.



Função create_table (Ponto 2):

Objetivo:
Cria a tabela integracao_cliente_carro no banco de dados SQLite, caso ela não exista.

Parâmetros:
cursor: Um objeto de cursor usado para interagir com o banco de dados SQLite.

Retorno:
Não há retorno explícito.



Função generate_random_data (Ponto 3):

Objetivo:
Gera dados aleatórios e os insere na tabela do banco de dados.

Parâmetros:
cursor: Um objeto de cursor usado para interagir com o banco de dados SQLite.

Retorno:
Não há retorno explícito.



Função get_integrated_table (Ponto 4):

Objetivo:
Obtém todos os dados da tabela integracao_cliente_carro.

Parâmetros:
cursor: Um objeto de cursor usado para interagir com o banco de dados SQLite.

Retorno:
Uma lista de tuplas, onde cada tupla representa uma linha da tabela.



Função analyze_average_spending_per_customer (Ponto 5):

Objetivo:
Calcula a média de gastos por cliente.

Parâmetros:
tabela_integrada: A lista de tuplas obtida pela função get_integrated_table.

Retorno:
Um valor float representando a média de gastos.



Função analyze_distribution_by_model (Ponto 6):

Objetivo:
Analisa a distribuição de carros comprados por modelo.

Parâmetros:
cursor: Um objeto de cursor usado para interagir com o banco de dados SQLite.

Retorno:
Duas listas, uma contendo os nomes dos modelos e outra contendo valores aleatórios representando a distribuição.



Função analyze_total_sales_over_time (Ponto 7):

Objetivo:
Analisa o total de vendas ao longo do tempo.

Parâmetros:
cursor: Um objeto de cursor usado para interagir com o banco de dados SQLite.

Retorno:
Duas listas, uma contendo datas e outra contendo valores totais de vendas.



Função analyze_car_distribution_by_value (Ponto 8):

Objetivo:
Analisa a distribuição de carros comprados por valor.

Parâmetros:
cursor: Um objeto de cursor usado para interagir com o banco de dados SQLite.

Retorno:
Duas listas, uma contendo valores dos carros e outra contendo contagens correspondentes.



Função analyze_total_sales_by_model (Ponto 9):

Objetivo:
Analisa o total de vendas por modelo.

Parâmetros:
cursor: Um objeto de cursor usado para interagir com o banco de dados SQLite.

Retorno:
Duas listas, uma contendo nomes dos modelos e outra contendo valores totais de vendas.



Função visualizar_tabela (Ponto 10):

Objetivo:
Visualiza a tabela no formato de texto.

Parâmetros:
cursor: Um objeto de cursor usado para interagir com o banco de dados SQLite.

Retorno:
Não há retorno explícito.



Funções visualizar_analise_1 a visualizar_analise_5 (Pontos 11 a 15):

Objetivo:
Visualiza resultados específicos das análises.

Parâmetros:
Diferentes parâmetros dependendo da análise.

Retorno:
Não há retorno explícito.
Parte Principal do Script (Ponto 16):

Objetivo:
Conecta-se ao banco de dados SQLite, cria a tabela, gera dados aleatórios, realiza análises e visualiza os resultados.

Parâmetros:
Não há.

Retorno:
Não há retorno explícito.