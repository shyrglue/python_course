# 游戏逻辑模块
# N 表示棋盘大小N*N
# M 表示翻转规则MODE
# D 表示难度DIFFICULTY
import random
CROSS = 0
X = 1
EASY = 0
MEDIUM = 1
HARD = 2

def flip(plate, x, y, M):   #翻转
    N = len(plate)
    click = [(x, y)]
    if M == CROSS:
        for dh, dv in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            h = x + dh
            v = y + dv
            if 0 <= h < N and 0 <= v < N:
                click.append((h, v))
    else:
        for dh, dv in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            h = x + dh
            v = y + dv
            if 0 <= h < N and 0 <= v < N:
                click.append((h, v))
    for x, y in click:
        plate[x][y] = not plate[x][y]

def off(plate): #全关
    return all(not y for x in plate for y in x)

def custom(N, M, D):   #逆向模拟法
    if D == EASY:
        T = 1
    elif D == MEDIUM:
        T = random.randint(2, 3)
    else:
        T = random.randint(4, 9)
    plate = [[False for _ in range(N)] for _ in range(N)]
    click = [(x, y) for x in range(N) for y in range(N)]
    selected = set()
    while len(selected) < T:
        selected.add(random.choice(click))
    for x, y in selected:
        flip(plate, x, y, M)
    return plate

def create(N):   #创建关卡
    return [[True for _ in range(N)] for _ in range(N)]