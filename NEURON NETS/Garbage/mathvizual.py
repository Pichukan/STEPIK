import numpy as np
import matplotlib.pyplot as plt

# Функция, которую минимизируем, минимум в точке (0, 0)
def f(x, y):
    return 1.3 * (x - y) ** 2 + 0.7 * (x + y) ** 2

# Отрисовка траектории и линий уровня функции
def plot_trajectory(func, traj, limit_point=None):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])    
    
    if limit_point:
        ax.plot([limit_point[0]], [limit_point[1]], 'o', color='green')
    #Level contours
    delta = 0.025
    x = np.arange(-2, 2, delta)
    y = np.arange(-2, 2, delta)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i][j] = func(X[i][j], Y[i][j])
    CS = ax.contour(X, Y, Z, [0.5, 1.5, 3], colors=['blue', 'purple', 'red'])
    ax.plot([u[0] for u in traj], [u[1] for u in traj], color='black')
    ax.plot([u[0] for u in traj], [u[1] for u in traj], 'o', color='black')
    
    plt.close(fig)
    return fig

x, y = (1.0, 1.0)
num_iters = 50
trajectory = [(x, y)]
plots = []
# Итерируемся и сохраняем текущий путь на каждом шаге
for i in range(num_iters):
    angle = 2 * np.pi * np.random.rand(1)
    dx, dy = (np.cos(angle) / 2 / (i + 1) ** 0.5, np.sin(angle) / 2 / (i + 1) ** 0.5)
    trajectory.append((x + dx, y + dy))
    plots.append(plot_trajectory(f, trajectory, limit_point=(0, 0)))
    if f(x, y) > f(x + dx, y + dy):
        x = x + dx
        y = y + dy
    else:
        trajectory = trajectory[:-1]

animate_list(plots, play=True, interval=300);