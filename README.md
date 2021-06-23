# Direction_Field
Calculus direction Filed

Calculate and Draw direction Filed by using python numpy and matplotlib


## Getting Started
### Prerequisites
python3 에서 프로그램이 실행되고 아래의 모듈이 설치되어 있어야 합니다.
* numpy
* matplotlib


### Installing

github repository를 clone하고 원하는 종류에 따라서 Drawing_DirectionFiled_f(x,y).py 또는 Drawing_DirectionFiled_parameter.py 파일을 엽니다.

```
git clone https://github.com/jiwon79/Direction_Field
```


## How to use

### 1. Drawing_DirectionFiled_f(x,y).py

y' = f(x,y)의 꼴로 주어졌을 때 x,y-axis direction field를 그려줍니다.

1. input functionn
```
def diff(x,y):
    return cos(x*y)*sin(x*y)
```
return 뒤에 그리고 싶은 함수식을 입력합니다

2. grid configuration
```
x_min, x_max, x_num = -5, 5, 30
y_min, y_max, y_num = -10, 10, 30
x_init, y_init = 0,1
gridSetting = True
```
x,y-axis의 범위, 초기값을 설정합니다.

gridSetting은 True이면 격자점이 보이고, False이면 보이지 않습니다.


<img src="https://user-images.githubusercontent.com/59159410/122944989-36630d80-d3b3-11eb-8d92-d00cece199fa.png" width="500">

위 예제의 direction field와 초기값을 설정한 graph입니다.


### 2. Drawing_DirectionFiled_parameter.py

x' = f(x,y) / y' = g(x,y) 의 꼴로 주어졌을 때 direction field와 x,y-t axis의 graph를 그려줍니다.

1. input function
```
def diff_x(x,y):
    return 0.08*x-0.001*x*y
def diff_y(x,y):
    return -0.02*y+0.00002*x*y
```
diff_x, diff_y의 return값에 x', y'의 함수값들을 입력해줍니다.


2. grid configuration

```
x_min, x_max, x_num = 0, 3000, 30
y_min, y_max, y_num = 0, 150, 30
time_start, time_finish, time_interval = -10, 300, 0.1
x_init, y_init, time_init = 1000, 40, 0

gridSet_DirectionField = False
gridSet_population = False
```
x,y-axis의 범위, 초기값을 설정합니다.

time_start, time_finish, time_interval로 시작시간, 끝나는 시간, 시간의 단위를 설정합니다.

gridSet_DirectionField, girdSet_population은 Direction field, population graph의 격자점의 유무를 의미합니다.

<img src="https://user-images.githubusercontent.com/59159410/122949600-c22a6900-d3b6-11eb-81bb-03bb2d290513.png" width="800">

왼쪽은 direction Filed와 초기값으로 설정한 graph, 오른쪽은 시간에 따른 population graph입니다.

