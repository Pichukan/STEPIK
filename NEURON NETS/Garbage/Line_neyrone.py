# coding: utf-8
# Программа для нейрона с одним входом, обученного предсказывать 
# линейную функцию Y = a * X, с добавлением шума noise:
import numpy as np
import matplotlib.pyplot as plt
#===============================================================
#Функция по изменению веса линейного нейрона

def neuron_lr(x, y, w, i, learn_rate = 0.001): 
    # На вход подаём: X - вектор на входы X_0 - X_n линейного нейрона (по умолч. 2 переменных) 
    # Y - учительский вектор - там правильные ответы, learn_rate - скорость обучения, steps - число , dots_on_plot 
    x = np.array(x[:,i]).reshape(2, 1)
    y = y.flatten()[i]
    #print("x.shape is: ", x.shape, "y.shape is: ", y.shape, "w.shape is: ", w.shape, )
    y_with_hat = w.T.dot(x).flatten()[0]  # Нашли предсказанное нейроном значение функции y = k * x + b
    print('======== ',i,'-й набор данных =============')
    print('x[0] = 1, x[1] = ', x[1, 0], ', y_предсказанное =', y_with_hat, ', y_учительский: ', y)
    print('Относительная погрешность предсказания составила: ',(y_with_hat - y)*100/y,' процентов.')
    print(w)

    # поначалу необученное 
    w[0] = w[0] + (-1) * learn_rate * (y_with_hat - y) * x.flatten()[0] # меняем вес для 
    w[1] = w[1] + (-1) * learn_rate * (y_with_hat - y) * x.flatten()[1] # каждого входа нейрона
    return w # Возвращает один элемент списка w номер i-й 

#===============================================================

#=============КОНСТАНТЫ ДЛЯ РАБОТЫ ПРОГРАММЫ====================

n = 100 # число сэмплов - наборов иксов
m = 1   # число переменных кроме X_0 (там все n раз будет единица)
lr = 0.001  # learning rate - скорость обучения модели (нейрона, точнее)

left_lim = -10  # Левый и ...
right_lim = 10  # правый пределы изменения Х для графика

#=============ЭТИ КОНСТАНТЫ БУДЕМ "УГАДЫВАТЬ"===================
K = -12           # Это коэффициент наклона прямой из уравнения y = k * x + b
B = 50           # Это свободный член из уравнения y = k * x + b
#===============================================================

BB = np.full((m, n), B)  # Это массив из коэффициента B, чтобы плюсануть к массиву K * X

X = np.random.uniform(left_lim, right_lim, (m, n)) # m строк-переменных от X_0 до X_m и n столбцов-наборов данных
NOISE = np.random.uniform(1, 1.1, (m, n))  # степень ШУМА во втором аргументе после 1 (это случ.множитель от 1 и до...)
# Вычисляем неточные (с учётом ШУМА NOISE) значения функции y = k * x + b 
# По этим НЕТОЧНЫМ данным мы будем учить наш линейный нейрон. Это т.н. УЧИТЕЛЬСКИЕ данные :-)
Y = K * X * NOISE + BB       # создан набор иксов (пока без единичек) и набор игреков для обучения
# Проверим на всякий случай размерности и первые пять элементов. Всё ли в порядке? 
# Удалять не буду, интересно ведь. Просто закомментирую. 
#print('X.shape = ',X.shape)
print('Y.shape = ',Y.shape)
#print(X[0][:5])
print(Y[0,:5])
# Теперь добавим строку единиц: 
ones = np.ones((1, n))
X = np.vstack((ones, X))
print('X.shape = ', X.shape)
#print('Y.shape = ', Y.shape)
print(X[0:2,:5])
#print(Y[0][:5])

# Настал черёд последнего массива для весов. При одной постоянной b (соответственно ей W_0 и X_0 = 1) 
# и одной переменной X_1 (двумерный график строим ниже) будет целых ДВА веса: W_0 и W_1. Создадим вектор: 
W = np.random.sample((2, 1))
print(W) 

# попробуем прогнать нашу модель через все 100 наборов данных несколько раз (можно и 1 раз попробовать)
for _ in range(100):
    for i in range(0, n):
        W = neuron_lr(X, Y, W, i) # можно и свои значения задать из констант lr (X, Y, W, 0.001)
        # Скормили нашей модели поочерёдно все пары (X_0, X_1) и к ним УЧИТЕЛЬСКИЙ массив (Y)
        # То есть на двух входах Х_0 и Х_1 нейрона сейчас 1 и 8.2, а учительский ответ при y = 10x + 5 около 84.1234

# После этого безобразия хочется посмотреть на наши веса )))))) 
print("Рассчитанный нейроном коэффициент К равен ", W[0,0], ", а коэффициент В равен ", W[1,0])
# Должно заработать ))))))))