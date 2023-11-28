import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('TkAgg')

x = 12.1
def f(a):
    return np.exp(a * x) - 3.45 * a


a_values = np.arange(-5, 12, 1.75)
y_values = f(a_values)
for i in range(len(a_values)):
    print(f"t={a_values[i]},f(t)={y_values[i]}")
max = np.max(y_values)
print("Наибольшее значение массива: ", max)
min = np.min(y_values)
print("Наименьшее значение массива: ", min)
sr = np.mean(y_values)
print("Среднее значение массива: ", sr)
kol_el = len(y_values)
print("Количество элементов массива: ", kol_el)
sort = np.sort(y_values)[::-1]
print("Отсортированный массив: ", sort)

plt.plot(a_values, y_values, label='f(t)')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('График функции f(t)')
plt.grid(True)
plt.show()

sr_line = np.full(len(y_values), sr)
plt.plot(a_values, y_values, label='f(t)')
plt.plot(a_values, sr_line, label='Среднее значение')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('График функции f(t) и прямой со средним значением')
plt.legend()
plt.grid(True)
plt.show()
