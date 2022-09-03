import numpy as np                 #PLANO CARTESIANO
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.widgets import Button
#Puntos en la grafica
xs = [0, 2, -3, -1.5]
ys = [0, 3, 1, -2.5]
colors = ['m', 'g', 'r', 'b']
#Ancho y largo del plano
xmin, xmax, ymin, ymax = -6, 6, -6, 6
f_cuadros = 1
#Grafica
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(xs, ys, c=colors)
#Escalar valores
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
#Mover la grafica a plano cartesiano
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
#Remover los margenes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# X - Y valores en los ejes (nombre, tamaño, x, y , rotacion)
ax.set_xlabel('X', size=15, labelpad=-24, x=1.02)
ax.set_ylabel('Y', size=15, labelpad=-21, y=1.02, rotation=0)
# Crea determinados valores de cuadricula
x_cuadro = np.arange(xmin, xmax+1, f_cuadros)
y_cuadro = np.arange(ymin, ymax+1, f_cuadros)
ax.set_xticks(x_cuadro[x_cuadro != 0])
ax.set_yticks(y_cuadro[y_cuadro != 0])
#Cuadricula
ax.grid()
#Boton --- izquierda, abajo, ancho, altura
ax3= plt.axes((0.44, 0.07 , 0.15, 0.04))
boton = Button(ax3, label="Clasificar")
#Boton evento
class clic:
    def onclick(event):
        print("hecho")
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
#Cambiar titulo de la ventana
plt.get_current_fig_manager().canvas.set_window_title('Funcion de escalon - IA2')
plt.show()