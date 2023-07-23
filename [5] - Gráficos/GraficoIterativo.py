
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import plotly.express as px

# Gráfico com interação no nível de dados - conforme os dados vão mudando, o gráfico vai se "adaptando"
def GraficoInterativoDados():
    x = np.arange(1, 6)

    plt.style.use("ggplot")
    plt.ion()

    for i in range(0, 10):
        dados = np.random.randint(20, 30, 5)
        plt.bar(x, dados)
        plt.pause(3)    # Pausa por 3 segundos
        plt.cla()       # Limpa os eixos

    plt.ioff()

def GraficoInterativoUsuarioLinha():
    df = pd.read_excel("vendas.xlsx")

    fig = px.line(df, x="Dias", y="Vendas", color="Ano")
    fig.show()

def GraficoInterativoUsuarioScatter():
    df = px.data.iris()  # iris is a pandas DataFrame
    fig = px.scatter(df, x="sepal_width", y="sepal_length")
    fig.show()

def GraficoInterativoUsuarioScatter2():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                     size='petal_length')
    fig.show()

def GraficoInterativoUsuarioBarra():
    data = px.data.gapminder().query("country == 'Brazil'")
    fig = px.bar(data, x='year', y='pop')
    fig.show()

def GraficoInterativoUsuarioBarra2():
    long_df = px.data.medals_long()
    fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
    fig.show()

def GraficoInterativoUsuarioPizza():
    df = px.data.gapminder().query("year == 2007").query("continent == 'Americas'")
    fig = px.pie(df, values='pop', names='country',
                 title='População do continente americano',
                 hover_data=['lifeExp'], labels={'lifeExp': 'Espectativa de vida'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.show()

def GraficoInterativoUsuarioSunBurst():
    df = px.data.gapminder().query("year == 2007")
    fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                      color='lifeExp', hover_data=['iso_alpha'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
    fig.show()

def GraficoInterativoUsuarioTreeMap():
    df = px.data.gapminder().query("year == 2007")
    fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                     color='lifeExp', hover_data=['iso_alpha'],
                     color_continuous_scale='RdBu',
                     color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()

def GraficoInterativoUsuarioMapScatter():
    df = px.data.gapminder().query("year == 2007")
    fig = px.scatter_geo(df, locations="iso_alpha",
                         color="continent",  # which column to use to set the color of markers
                         hover_name="country",  # column added to hover information
                         size="pop",  # size of markers
                         projection="natural earth")
    fig.show()

def GraficoInterativoUsuarioPolarChart():
    df = px.data.wind()
    fig = px.line_polar(df, r="frequency", theta="direction", color="strength",
                        color_discrete_sequence=px.colors.sequential.Plasma_r,
                        template="plotly_dark")
    fig.show()

def GraficoIMShow():
    from skimage import io
    img = io.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Crab_Nebula.jpg/240px-Crab_Nebula.jpg')
    fig = px.imshow(img)
    fig.show()


# ###################### Programa Principal ##################### #
opcao = 8         # 1 e 9

if opcao == 1:
    GraficoInterativoDados()
elif opcao == 2:
    GraficoInterativoUsuarioLinha()
elif opcao == 3:
    GraficoInterativoUsuarioScatter()
elif opcao == 4:
    GraficoInterativoUsuarioScatter2()
elif opcao == 5:
    GraficoInterativoUsuarioBarra()
elif opcao == 6:
    GraficoInterativoUsuarioBarra2()
elif opcao == 7:
    GraficoInterativoUsuarioPizza()
elif opcao == 8:
    GraficoInterativoUsuarioSunBurst()
elif opcao == 9:
    GraficoInterativoUsuarioTreeMap()
elif opcao == 10:
    GraficoInterativoUsuarioMapScatter()
elif opcao == 11:
    GraficoInterativoUsuarioPolarChart()
elif opcao == 12:
    GraficoIMShow()





# Acessar https://plotly.com/python/plotly-express/ para outros exemplo
# Acessar https://www.kaggle.com/datasets para datasets



