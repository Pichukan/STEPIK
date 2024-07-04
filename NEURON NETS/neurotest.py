import numpy as np
k=0
"""
a = np.array([[1,2,3], [4,5,6]])  # создаём массив

print(a)  # смотрим на массивimport numpy as np
print('----------')
print(np.eye(5,3,k=0))  #k сдвиг по диагонали 0 для основной диагонали
print('----------')
b=np.zeros([4,4])
print(b)
print('----------')
print(np.ones([2,5,3]))
print('xxxxxxxxxxx')
"""
"""
a=np.array([3,4])
b=np.array([3,4])
d=np.array([3,4])
a=np.eye(3,4,k=0)
#print(a)
b=np.eye(3,4,k=1)
#print(b)
d=a*2+b
print(d)
#print(type(d))
""" """
import random
w=np.array(random.sample(range(1000),12))
print (w)
""" 
"""
import random
#w=np.array([3,4])
w=np.array([random.sample(range(1000),4),random.sample(range(1000),4)])
print (w)
b=np.zeros([4,4])
print(b)
"""
"""
a=np.array([3,4])
b=np.array([3,4])
d=np.array([3,4])
a=np.eye(3,4,k=0)
#print(a)
b=np.eye(3,4,k=1)
#print(b)
d=a*2+b
print(d)
#print(type(d))
d=d.reshape(12,1)
print(d)
"""
"""
v=np.arange(12) #метод библиотеки nympy
print(v)
v=v.reshape(3,4)
print(v)
print(v.mean(axis=0)) #вдоль столбцов
print(v.mean(axis=1))  #вдоль строк
print(v.mean(axis=None))  #вдоль всего массива
"""
"""
x_shape = tuple(map(int, input().split()))

X = np.fromiter(map(int, input().split()), int).reshape(x_shape)

y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), int).reshape(y_shape)
#print(x_shape)
#print(X)
#print("умножение",X*Y)
Y=Y.T
#print(Y)
if x_shape[1]==y_shape[1]:
	C=X.dot(Y)    #умножение матриц
	print(C)
else:
	print("matrix shapes do not match")
"""


#sbux = np.loadtxt("sbux.csv", usecols=(0,1,4), skiprows=1, delimiter=",", 
#                      dtype={'names': ('date', 'open', 'close'),
#                             'formats': ('datetime64[D]', 'f4', 'f4')})

#print(sbux[0:4])


"""
#Cчитывание матрицы из файла инета по ссылке 
from urllib.request import urlopen


filename = input()
f = urlopen(filename)
#print(type(f))
sbux = np.loadtxt(f, skiprows=1, delimiter=",")
#shape=sbux.shape
#print(shape)
#print(sbux)
print(sbux.mean(axis=0))
"""
"""
a = np.array([[10,60], [7,50], [12,75]])
x = np.ones((3,2))
y = np.zeros((3,1))
print(x)
print(y)
for i in range(3):
	#print(a[i,0])
	x[i,1]=a[i,1]
	y[i,0]=a[i,0]

print(x)
print(y)

step1 =	x.T.dot(x)
print(step1)
step2 = np.linalg.inv(step1)
print(step2)
step3 = step2.dot(x.T)
print(step3)
b = step3.dot(y)
print(b)
"""


"""
from urllib.request import urlopen
#fff='https://stepik.org/media/attachments/lesson/16462/boston_houses.csv'
#filename=fff
filename = input()

f = urlopen(filename)
print(f)
print(type(f))
sbux = np.loadtxt(f, skiprows=1, delimiter=",")
#print(sbux)
#print(type(sbux.shape))   
#print(sbux.shape[1])
#x = np.ones_like(sbux)
#print(x)
x=sbux.copy()
#print(x)
y=np.zeros((sbux.shape[0],1))
#print(y.shape)
for i in range(sbux.shape[0]):
	x[i,0]=1
	y[i,0]=sbux[i,0]
#print(x)
#print(y)	

step1 =	x.T.dot(x)
#print(step1)
step2 = np.linalg.inv(step1)
#print(step2)
step3 = step2.dot(x.T)
#print(step3)
b = step3.dot(y)
#print(b)
b1=np.hstack(b)
#print(b1)
s=" ".join(map(str,b1))
print(s)
"""


"""
import numpy as np

x = np.array([[1, 1, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]])
y = np.array([1, 1, 0])
w = np.array([0, 0, 0])
for _ in range(len(x)):
  p = int(w.T @ x[_] > 0)  
  if p != y[_]:
    w = w - x[_] if p else w + x[_]
print(*w.round(2), sep=',')
"""


'''
import numpy as np
Y = np.array([1,1,0]) #реальные ответы
X = np.array([[1, 1, 0.3, 0],
              [1, 0.4, 0.5, 0],
              [1, 0.7, 0.8, 0]]) #массив значений
X[:,3] = Y.transpose() #подтягиваем ответы в массив значений
w = np.array([0,0,0]) #массив весов
def Predict(X):
    E = X.dot(w.transpose()) #сумматор
    p = 1 if E > 0 else 0 #активатор
    return p
perfect = False
while perfect == False:
    perfect = True
    for ex in X:
        #сравниваем предсказание с реальным ответом
        if Predict(ex[0:3]) != ex[3]:
            perfect = False
            #если ответ не совпадает, правим веса
            w = w + (ex[3] - Predict(ex[0:3]))*ex[0:3]
            print(w)
print(w)
'''




