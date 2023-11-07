import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from matplotlib.lines import Line2D
import matplotlib.animation as animation
from fractions import Fraction

thet = np.linspace(0, 2 * pi, 500);#создает равномерную последовательность значений от 0 до 2*pi с  500 элементами и сохраняет их в переменную thet.
r = np.ones(500)#создает массив из 500 единиц и сохраняет его в переменную r.
x = r * np.cos(thet)#вычисляет косинусы значений из массива thet, умножает их на элементы из массива r и сохраняет результат в переменную x.
y = r * np.sin(thet)#вычисляет синусы значений из массива thet, умножает их на элементы из массива r и сохраняет результат в переменную y.

dtheta = pi / 25;


R = float(input('Radius:'))

figu = plt.figure()
ax = plt.axes()

figu.set_figheight(7)# устанавливает высоту фигуры figu
figu.set_figwidth(14)#устанавливает ширину фигуры figu

xdata, ydata = [], []
trace = Line2D([], [], color='blue', linewidth=3)
ax.add_line(trace)

rad = Line2D([0, 0], [0, -R], color='red', linewidth=3)
ax.add_line(rad)

line = Line2D(x, y, color='green', linewidth=3)
ax.add_line(line)

ax.axis('equal')#устанавливает соотношение сторон масштабирования осей графика равным 1.
ax.set_aspect('equal', 'box')#устанавливает соотношение сторон масштабирования осей графика так, чтобы график выглядел пропорциональным.
ax.set(xlim=(-1.5, 14), ylim=(-1, 4))#: устанавливает ограничения для осей x и y, чтобы значения на графике были видны в заданных пределах.
ax.grid(color='blue', linewidth=0.5, linestyle='dotted')# добавляет на график сетку синего цвета, толщиной 0.5 и пунктирным стилем.
ax.axhline(y=0, color='k')#добавляет на график горизонтальную линию с y-координатой равной 0.
ax.axvline(x=0, color='k')#добавляет на график вертикальную линию с x-координатой равной 0.
ax.set_title('Cycloid-animation')


def format_func(value, tick_number):#определяет функцию, которая будет форматировать значения на осях графика.
    numer = Fraction(value / pi).numerator #вычисляет числитель дроби, полученной при делении значения на pi.
    denomin = Fraction(value / pi).denominator #вычисляет знаменатель дроби, полученной при делении значения на pi.
    if numer == 0:
        return "0"
    elif numer == 1 and denomin == 1:
        return r"$\pi$"
    elif numer == 1 and denomin != 1:
        return r"$\pi/{0}$".format(denomin)
    elif numer != 1 and denomin == 1:
        return r"${0}\pi$".format(numer)
    else:
        return r"${0}\pi/{1}$".format(numer, denomin)


def trans2d(x, y, tx, ty, phi):
    xx = x * np.cos(phi) - y * np.sin(phi) + tx
    yy = x * np.sin(phi) + y * np.cos(phi) + ty
    return (xx, yy)


def init():
    trace.set_data([], [])
    rad.set_data([0, 0], [0, -R])
    line.set_data([], [])
    return line, rad, trace


def get_pos(theta=0):
    while theta < 4 * pi:
        ax = np.array([0, 0])
        by = np.array([0, -R])
        dx, dy = trans2d(ax, by, theta, 1, -theta)
        yield theta, dx, dy
        theta += dtheta
def animate(pos):
    theta, dx, dy = pos
    line.set_data(x + theta, y + 1)
    rad.set_data(dx, dy)
    xdata.append(dx[1])
    ydata.append(dy[1])
    trace.set_data(xdata, ydata)
    return line, rad, trace


ax.xaxis.set_major_locator(plt.MultipleLocator(pi / 2))#устанавливает основной локатор на оси X, который размещает маркеры на основе заданного интервала, маркеры будут размещены каждые pi / 2 единиц на оси X.
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))#устанавливает форматтер для основных маркеров на оси X. Форматтер принимает функцию format_func, которая определяет собственный формат для меток на оси X


myAnimation = animation.FuncAnimation(figu, animate, get_pos, interval=20, blit=True, repeat=False, init_func=init)

plt.show()