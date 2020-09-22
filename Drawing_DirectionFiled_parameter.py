import numpy as np
import math
from matplotlib import pyplot as plt


# ----------- Differential equation ------------
# ----------- diff = y'= diff(x,y) -------------
def diff_x(x,y):
    return 0.08*x-0.001*x*y
def diff_y(x,y):
    return -0.02*y+0.00002*x*y

def diff(x,y) :
    if diff_x(x,y) == 0 :
        return 99
    return diff_y(x,y)/diff_x(x,y)
print("definition diff function process")

# ----------------- input ----------------------
x_min, x_max, x_num = 0, 3000, 30
y_min, y_max, y_num = 0, 150, 30
time_start, time_finish, time_interval = -10, 300, 0.1
x_init, y_init, time_init = 1000, 40, 0

gridSet_DirectionField = False
gridSet_population = False
print("input process")


# ---------------- x,y range -------------------
x = np.linspace(x_min, x_max, x_num)
y = np.linspace(y_min, y_max, y_num)

x_dis = (x_max-x_min)/(x_num+1)
y_dis = (y_max-y_min)/(y_num+1)
print("x domain process")

# ---------- drawing direction field -----------
for j in x:
    for k in y:
        slope = diff(j,k)
        if abs(slope) <= y_dis/x_dis :
            domain = np.linspace(j-x_dis/2.5+0.07,j+x_dis/2.5-0.07,2)
        else :
            domain = np.linspace(j-y_dis/slope/2+0.07,j+y_dis/slope/2-0.07,2)
        def fun(x1,y1):
            z = slope*(domain-x1)+y1
            return z
        plt.figure(1)
        plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')
print("drawing direction field process")

# -------------- Error handling ----------------
class outOfRange(Exception) :
    def __init__(self, msg) :
        self.msg = msg
    def __str__(self) :
        return self.msg
print("Error setting process")

# ------- drawing graph by newton method -------
if not x_min <= x_init <= x_max or not y_min <= y_init <= y_max \
    or not time_start <= time_init <= time_finish:
    raise outOfRange('초기값이 범위를 벗어났습니다')
print("Error check process")

# --------- x right direction drawing ----------
# -------------- init setting ------------------
time = time_init
check = [0]*11
x = x_init
y = y_init

# ---------------- drawing ---------------------
while x_min <= x <= x_max and y_min <= y <= y_max and time <= time_finish:
    xNext = x+time_interval*diff_x(x,y)
    yNext = y+time_interval*diff_y(x,y)

    # Direction Field plot
    plt.figure(1)
    plt.plot([x,xNext], [y,yNext], 'k', linewidth=1)
    # Each population plot
    plt.figure(2)
    timeList = [time, time+time_interval]
    plt.plot(timeList, [x,xNext], 'r')
    plt.plot(timeList, [y,yNext], 'b')
    
    x, y = xNext, yNext
    time += time_interval

    # loading effect
    n = int(10*(time-time_init)/(time_finish-time_init))
    if check[n] == 0 :
        for i in range(n):
            print("■",end='')
        for i in range(20-n):
            print("□",end='')
        print()
        check[n] = 1
print("right drawing graph process")

# --------- x left direction drawing -----------
# -------------- init setting ------------------
x = x_init
y = y_init
time = time_init
check = [0]*11

# ---------------- drawing ---------------------
while x_min <= x <= x_max and y_min <= y <= y_max and time_start < time:
    xNext = x-time_interval*diff_x(x,y)
    yNext = y-time_interval*diff_y(x,y)
    # Direction Field plot
    plt.figure(1)
    plt.plot([x,xNext], [y,yNext], 'k', linewidth=1)
    # Each population plot
    plt.figure(2)
    timeList = [time, time-time_interval]
    plt.plot(timeList, [x,xNext], 'r', label='1')
    plt.plot(timeList, [y,yNext], 'b', label='2')

    x, y = xNext, yNext
    time -= time_interval
    
    
    # loading effect
    n = int(10*(time-time_start)/(time_init-time_start))
    if check[n] == 0 :
        for i in range(20-n):
            print("■",end='')
        for i in range(n):
            print("□",end='')
        print()
        check[n] = 1

print("left drawing graph process")

plt.figure(1)
plt.title("Direction Field")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(gridSet_DirectionField)

plt.figure(2)
plt.title("Each polulation")
plt.xlabel('time')
plt.ylabel('population')
plt.show()
    
print("End of the program")