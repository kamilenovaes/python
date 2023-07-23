
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

def PlotarPlano():
    fig = plt.figure()
    eixos = plt.axes(projection="3d")
    plt.show()

def GraficoBarras3D():
    fig = plt.figure()
    eixos = plt.axes(projection="3d")
    for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):  # Para cada par (cor,número)
        xs = np.arange(20)  # Gera uma lista [0, 1, 2, ..., 19]
        ys = np.random.rand(20)  # Gera 20 valores entre 0 e 1

        cs = [c] * len(xs)  # Gera uma lista com 20 posições da cor descrita em c

        eixos.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.6)  # alpha indica a transparência

    eixos.set_xlabel('X')
    eixos.set_ylabel('Y')
    eixos.set_zlabel('Z')

    plt.show()

def GraficoLinha3D():
    fig = plt.figure()
    eixos = plt.axes(projection="3d")

    z_line = np.linspace(0, 15, 1000)  # Gera 1000 pontos, bem distribuídos, entre 0 e 15
    x_line = np.cos(z_line)
    y_line = np.sin(z_line)
    eixos.plot3D(x_line, y_line, z_line, 'red')
    plt.show()

def GraficoLinha3DMelhorado():
    fig = plt.figure()
    eixos = plt.axes(projection="3d")

    z_line = np.linspace(0, 15, 1000)
    x_line = np.cos(z_line)
    y_line = np.sin(z_line)
    eixos.plot3D(x_line, y_line, z_line, 'gray')

    pontos_z = 15 * np.random.random(100)  # Gera 100 pontos aleatórios entre 0 e 1 - Depois multiplica por 15
    pontos_x = np.cos(pontos_z) + 0.1 * np.random.randn(100)
    pontos_y = np.sin(pontos_z) + 0.1 * np.random.randn(100)
    #eixos.scatter3D(pontos_x, pontos_y, pontos_z, c=pontos_z, cmap='viridis')  # cmap usa um mapa de cores (variação em 'c')

    mapa_cores = eixos.scatter3D(pontos_x, pontos_y, pontos_z, c=pontos_z, cmap='Purples')
    plt.colorbar(mapa_cores)

    plt.show()

def Cubo():
    fig = plt.figure()
    eixos = plt.axes(projection="3d")

    sides = np.array([3, 3, 3])
    # Cria uma matriz 3D, 3X3X3, preenchida com 1's
    data = np.ones(sides)
    # Plota o grid ('voxel') representado por data
    eixos.voxels(data, facecolors="blue")
    plt.show()

def Esfera():
    fig = plt.figure()
    eixos = plt.axes(projection="3d")

    # Make data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = 10 * np.outer(np.cos(u), np.sin(v))  # outer - realiza o produto (outer) de dois vetores, gerando uma matriz
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the surface
    eixos.plot_surface(x, y, z, color='b')

    plt.show()


# ################### Programa Principal #################### #
opcao = 4              # 2 e 4

if opcao == 1:
    PlotarPlano()
elif opcao == 2:
    GraficoBarras3D()
elif opcao == 3:
    GraficoLinha3D()
elif opcao == 4:
    GraficoLinha3DMelhorado()
elif opcao == 5:
    Cubo()
elif opcao == 6:
    Esfera()
