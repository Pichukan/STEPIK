import numpy as np
import matplotlib
import matplotlib.pyplot as plt
 
if __name__ == "__main__":
 
    # 1.1) "Включение" поддержки кириллицы (при необходимости)
    # matplotlib.rc("font", family="Arial, Ubuntu")
 
    # 2) Формирование данных и построение диаграммы
    x = np.arange(-8, 3, 0.1)  # x - массив np.array
    y = abs(x**2 + 4*x - 5)
 
    # Вызов диаграммы нужного типа
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Мое первое изображение")  # Заголовок окна
 
    ax.grid(True)  # Отображение сетки на координатной плоскости
    ax.plot(x, y, 'r', linewidth=3)  # График красного цвета
 
    # 3) Вывод результата
    plt.savefig("my_image.png")  # Сохранение изображения
    # или
    plt.show()  # Вывод изображения на экран
