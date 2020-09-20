import numpy as np
from math import *
from matplotlib import pyplot as plt

# Differential equation
# diff = y'= diff(x,y)
def diff(x,y):
    return sin(x)*sin(y)
print("definition diff function process")

#input
x_min, x_max, x_num = -5, 5, 30
y_min, y_max, y_num = -5, 5, 30
x_init, y_init = -3,2
gridSetting = True
print("input process")

# x,y range
x = np.linspace(x_min, x_max, x_num)
y = np.linspace(y_min, y_max, y_num)

x_dis = (x_max-x_min)/(x_num+1)
y_dis = (y_max-y_min)/(y_num+1)
print("x domain process")

# drawing direction field
for j in x:
    for k in y:
        slope = diff(j,k)
        if abs(slope) <= y_dis/x_dis :
            domain = np.linspace(j-x_dis/2.5,j+x_dis/2.5,2)
        else :
            domain = np.linspace(j-y_dis/slope/2.5,j+y_dis/slope/2.5,2)
        def fun(x1,y1):
            z = slope*(domain-x1)+y1
            return z
        plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')
print("drawing direction field process")

# Error
class outOfRange(Exception) :
    def __init__(self, msg) :
        self.msg = msg
    def __str__(self) :
        return self.msg
print("Error setting process")

# drawing graph by newton method
if not x_min <= x_init <= x_max or not y_min <= y_init <= y_max :
    raise outOfRange('초기값이 범위를 벗어났습니다')
print("Error check process")


# x right
x = x_init
y = y_init
while x_min <= x <= x_max and y_min <= y <= y_max:
    xNext = x+0.1
    yNext = y+diff(x,y)*0.1
    plt.plot([x,xNext], [y,yNext], 'k', linewidth=1)
    x, y = xNext, yNext
print("right drawing graph process")

# x left
x = x_init
y = y_init
while x_min <= x <= x_max and y_min <= y <= y_max:
    xNext = x-0.1
    yNext = y-diff(x,y)*0.1
    plt.plot([x,xNext], [y,yNext], 'k', linewidth=1)
    x, y = xNext, yNext
print("left drawing graph process")

plt.title("Direction Field")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(gridSetting)
plt.show()
    
print("End of the program")