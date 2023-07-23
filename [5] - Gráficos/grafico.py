import matplotlib.pyplot as plt


# Um gráfico de linhas fornece a representação gráfica mais clara das variáveis dependentes do tempo.
# É também o modo preferido de representação de tendências ou variáveis ao longo de um período de tempo.
def GraficoLinhasSimples():
    Eixo_x = [1, 2, 3, 4, 5]
    Eixo_y = [2, 4, 1, 6, 2]
    plt.plot(Eixo_x, Eixo_y)
    plt.show()


def GraficoLinhas():
    Eixo_x1 = [1, 2, 3, 4, 5]
    Eixo_y1 = [2, 4, 1, 6, 2]
    plt.plot(Eixo_x1, Eixo_y1, label="Série A")

    Eixo_x2 = [1, 2, 3, 4, 5]
    Eixo_y2 = [3, 1, 1, 4, 3]
    plt.plot(Eixo_x2, Eixo_y2, label="Série B")

    plt.legend()  # Plota a legenda (labels)
    plt.xlabel("Dias")
    plt.ylabel("Pessoas")
    plt.title("Frequência")
    plt.show()

# Um gráfico de barras é uma boa forma de representar dados qualitativos.
def GraficoBarras():
    Eixo_x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
    Eixo_y1 = [50, 40, 70, 80, 20]
    plt.bar(Eixo_x1, Eixo_y1, label="BMW", width=.5)

    Eixo_x2 = [.75, 1.75, 2.75, 3.75, 4.75]
    Eixo_y2 = [80, 20, 20, 50, 60]
    plt.bar(Eixo_x2, Eixo_y2, label="Audi", color='r', width=.5)

    plt.legend()
    plt.xlabel("Dias")
    plt.ylabel("Distância(km)")
    plt.title("Informação")
    plt.show()

def GraficoBarrasHorizontal():
    Eixo_x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
    Eixo_y1 = [50, 40, 70, 80, 20]
    plt.barh(Eixo_x1, Eixo_y1, label="BMW", height=.5)

    Eixo_x2 = [.75, 1.75, 2.75, 3.75, 4.75]
    Eixo_y2 = [80, 20, 20, 50, 60]
    plt.barh(Eixo_x2, Eixo_y2, label="Audi", color='r', height=.5)

    plt.legend()
    plt.ylabel("Dias")
    plt.xlabel("Distância(km)")
    plt.title("Informação")
    plt.show()


# Os gráficos de pizza são usados para visualizar partes de um todo; suas “fatias” devem sempre somar 100%.
def GraficoPizza():
    # Analisando 5 dias de atividades

    Dormindo = [7, 8, 6, 11, 7]
    Comendo = [2, 3, 4, 3, 2]
    Trabalhando = [7, 8, 7, 2, 2]
    Jogando = [8, 5, 7, 8, 13]

    Atividades = ["Dormir", "Comer", "Trabalhar", "Jogar"]
    Tot_atividades = [sum(Dormindo), sum(Comendo), sum(Trabalhando), sum(Jogando)]
    Total = 24 * 5  # 5 dias de análise

    slices = [x / Total for x in Tot_atividades]
    Cores = ["c", "m", "r", "b"]

    plt.pie(slices, labels=Atividades, colors=Cores, startangle=90)
    plt.title("Gráfico de Pizza")
    plt.show()

def GraficoPizzaDetalhe():
    # Analisando 5 dias de atividades

    Dormindo = [7, 8, 6, 11, 7]
    Comendo = [2, 3, 4, 3, 2]
    Trabalhando = [7, 8, 7, 2, 2]
    Jogando = [8, 5, 7, 8, 13]

    Atividades = ["Dormir", "Comer", "Trabalhar", "Jogar"]
    Tot_atividades = [sum(Dormindo), sum(Comendo), sum(Trabalhando), sum(Jogando)]
    Total = 24 * 5  # 5 dias de análise

    slices = [x / Total for x in Tot_atividades]
    Cores = ["c", "m", "r", "b"]

    plt.pie(slices, labels=Atividades, colors=Cores, startangle=90, shadow=True, explode=(0, 0.1, 0, 0),
            autopct="%1.1f%%")
    plt.title("Gráfico de Pizza")
    plt.show()

# O gráfico de dispersão é um tipo de gráfico utilizado para representar a relação entre duas variáveis quantitativas.
# Ele é construído plotando os valores de uma variável no eixo horizontal e os valores da outra variável no eixo
# vertical. Cada par de valores é representado por um ponto no gráfico.
def GraficoDispersao():
    x1 = [1, 1.5, 2, 2.5, 3, 3.5, 3.6]
    y1 = [7.5, 8, 8.5, 9, 9.5, 10, 10.5]

    x2 = [8, 8.5, 9, 9.5, 10, 10.5, 11]
    y2 = [3, 3.5, 3.7, 4, 4.5, 5, 5.2]

    plt.scatter(x1, y1, label="Alta renda, baixa economia", color="r")
    plt.scatter(x2, y2, label="Baixa renda, alta economia", color="b")

    plt.xlabel("Economia*100")
    plt.ylabel("Renda*1000")
    plt.title("Gráfico de dispersão")
    plt.legend()
    plt.show()

# Um histograma é uma espécie de gráfico de barras que demonstra uma distribuição de frequências.
# No histograma, a base de cada uma das barras representa uma classe e a altura representa a quantidade
# ou frequência absoluta com que o valor de cada classe ocorre.
def GraficoHistograma():
    populacao_idades = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 2, 102, 95, 85, 55, 110, 120, 70, 65, 55, 111, 115, 80,
                        75, 65, 54, 44, 43, 42, 48]

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    plt.hist(populacao_idades, bins, histtype="bar", rwidth=0.4)
    # plt.hist(populacao_idades, bins, histtype="step", rwidth=0.4)
    # plt.hist(populacao_idades, bins, histtype="stepfilled", rwidth=0.4)

    plt.xlabel("Grupos etários")
    plt.ylabel("Número de pessoas")
    plt.title("Histograma")

    plt.show()

def GraficoHistogramaDetalhe():
    populacao_idades1 = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 2, 102, 95, 85, 55, 110, 120, 70, 65, 55, 111, 115, 80,
                        75, 65, 54, 44, 43, 42, 48]

    populacao_idades2 = [52, 55, 62, 45, 41, 22, 34, 42, 42, 40, 42, 72, 65, 65, 55, 50, 60, 70, 65, 55, 61, 75, 50,
                         75, 65, 54, 44, 43, 42, 48]

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


    plt.hist(populacao_idades1, bins, histtype="barstacked", rwidth=0.8)
    plt.hist(populacao_idades2, bins, histtype="barstacked", rwidth=0.4)

    plt.xlabel("Grupos etários")
    plt.ylabel("Número de pessoas")
    plt.title("Histograma")


# ####################### PRINCIPAL ######################## #
opcao = 7         # 2 e 4

if opcao == 1:
    GraficoLinhasSimples()
elif opcao == 2:
    GraficoLinhas()
elif opcao == 3:
    GraficoBarras()
elif opcao == 4:
    GraficoBarrasHorizontal()
elif opcao == 5:
    GraficoPizza()
elif opcao == 6:
    GraficoPizzaDetalhe()
elif opcao == 7:
    GraficoDispersao()
elif opcao == 8:
    GraficoHistograma()
elif opcao == 9:
    GraficoHistogramaDetalhe()
