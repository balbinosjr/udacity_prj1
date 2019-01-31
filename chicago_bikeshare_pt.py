# coding: utf-8

#Aluno: Balbino S. Junior

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.

print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
#Balbino: A primeira linha (indice 0) foi descartada por ser o header
for indlin in range(1,21):
    print(data_list[indlin])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for indlin in range(0,20):
    print(data_list[indlin][6])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")

# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
      column_to_list: Função responsável por retornar uma nova lista com base em outra 
                      lista e no indice passados como parâmetro. Os itens da nova lista
                      deverá possuir a mesma ordenação da lista passada por parâmetro.
      Argumentos:
       data: Lista que contendo a coluna que será adicionada na nova lista.
       index: Indice que aponta para a coluna da lista de origem (data).
      Retorna:
       column_list: Lista contendo todos os itens de uma determinada coluna da lista (data)
                    passada como parâmetro.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line in range(len(data)):
        column_list.append(data[line][index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")

# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for colval in column_to_list(data_list, -2):
    if colval == "Male":
        male += 1
    elif colval == "Female":
        female += 1


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
      count_gender: Função responsável por contar a quantidade de ocorrências de 
                    cada um dos gêneros ("Male" ou "Female") em uma lista. A função
                    deverá retornar uma lista contendo dois itens (inteiros) com a
                    contabilização dos gêneros ("Male" e "Female") respectivamente.
      Argumentos:
       data_list: Lista contendo os gêneros a serem contabilizados.
      Retorna:
       Lista contendo a contabilização dos gêneros: "Male" e "Female".
    """
    male   = 0
    female = 0
    for colval in column_to_list(data_list, -2):
        if colval == "Male":
            male += 1
        elif colval == "Female":
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

def most_popular_gender(data_list):
    """
      most_popular_gender: Função responsável por verificar (na lista passada por parâmetro) qual o 
                           gênero mais popular ("Male" ou "Female") e retorná-lo através de uma string.
                           Caso não haja um gênero mais popular, a função deverá devolver a string "Equal".
      Argumentos:
       data_list: Lista contendo os gêneros a serem contabilizados.
      Retorna:
       answer: String que deverá conter uma das seguintes alternativas: "Male", "Female" ou "Equal".
       
    """
    answer = ""
    [n_male, n_female] = count_gender(data_list)
    if n_male > n_female:
        answer = "Male"
    elif n_male < n_female:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
quantity = []
types_client = []
column_list = column_to_list(data_list, -3)
#Utilizando a função set() para iterar sobre uma lista com itens não duplicados
for type_client in set(column_list):
    types_client.append(type_client)
    #Contando o numero de ocorrência de um determinado item na lista
    count_type_client = 0
    for type_client2 in column_list:
        if type_client2 == type_client:
           count_type_client += 1
    #Adicionando a quantidade de ocorrências do Tipo do Cliente em questão
    quantity.append(count_type_client)

y_pos = list(range(len(types_client)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Cliente')
plt.xticks(y_pos, types_client)
plt.title('Quantidade por Tipo de Cliente')
plt.show(block=True)

print("\nTAREFA 7: Verifique o gráfico!")


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque em muitas linhas do data_list um dos gêneros: 'Male' ou 'Female' não é informado."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

def calculaDuracaoMedia(data_list):
    """
      calculaDuracaoMedia: Função responsável por calcular a duração média com base em uma lista.
      Argumentos:
       data_list: Lista contendo as durações para o cálculo da média.
      Retorna:
       duracaoMedia: Variável contendo o valor da duração média calculada".
    """
    sum_trip = 0.
    duracaoMedia = 0.
    #Somando as durações das viagens sem a utilização de função
    for index in range(len(data_list)):
        sum_trip += float(data_list[index])
        
    duracaoMedia = sum_trip/len(data_list)
    
    return duracaoMedia

def calculaMediana(data_list):
    """
      calculaMediana: Função responsável por calcular a mediana com base em uma lista.
      Argumentos:
       data_list: Lista contendo as durações para o cálculo da mediana.
      Retorna:
       mediana: Variável contendo o valor da Mediana calculada".
    """
    mediana = 0.
    #Para calcular a mediana, é preciso que a lista esteja ordenada em ordem crescente de valor
    data_list.sort(key=float)
    # Se a quantidade de itens da lista for par, a mediana é a soma dos itens que estão nas 
    # posições: (tamanho da lista//2) - 1 e (tamanho da lista//2) dividido por 2.
    if len(data_list) % 2 == 0:
        index = len(data_list) // 2
        mediana = (float(data_list[index-1]) + float(data_list[index]))/2
    # Se a quantidade de itens da lista for impar, a mediana é o item da lista
    # que está na posição (tamanho da lista//2)
    else:
        index = len(data_list) // 2
        mediana = float(data_list[index])
    
    return mediana

    
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

#Calculando a duração média das viagens
mean_trip = calculaDuracaoMedia(trip_duration_list)
#Reordenando a lista de forma crescente
trip_duration_list.sort(key=float)
#Ao reordenar a lista o menor item encontra-se no indice zero(0) da lista
min_trip = float(trip_duration_list[0])
#Ao reordenar a lista o maior item encontra-se no ultimo item indice (-1) da lista
max_trip = float(trip_duration_list[-1])
#Calcula mediana
median_trip = calculaMediana(trip_duration_list)



print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
  Função de exemplo com anotações.
  Argumentos:
  param1: O primeiro parâmetro.
  param2: O segundo parâmetro.
  Retorna:
  Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
      count_items: Função responsável por contabilizar a quantidade de vezes que cada um
                   dos diferentes itens aparecem na lista passada como parâmetro.
      Argumentos:
       column_list: Lista contendo os itens a serem contabilizados.
      Retorna:
       item_types : Lista contendo a descrição de cada um dos itens da lista passada como parâmetro. 
       count_items: Lista contendo as quantidades associadas a cada um dos itens descritos em item_types.
       
    """
    item_types = []
    count_items = []
    #A utilização da função set() agrupa os itens evitando duplicidade
    for items in set(column_list):
     item_types.append(items)
     count_items.append(column_list.count(items))

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
