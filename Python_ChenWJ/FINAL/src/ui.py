#图形用户界面
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from logic import CROSS, EASY, HARD, MEDIUM, X, create, custom, flip, off
root = None
plate = []
button = []
board_frame = None
size_combo = None
rule_combo = None
level_combo = None
radio_classic = None
radio_custom = None
grid_size = None
M = None
R = None
D = None
move_text = None
time_text = None
moves = 0
used_time = 0.0
start_time = 0.0
playing = False
current_rule = CROSS

def change_control():   #按钮禁用
    size_combo.configure(state="disabled" if playing else "readonly")
    rule_combo.configure(state="disabled" if (playing or not M.get()) else "readonly")
    level_combo.configure(state="disabled" if (playing or not M.get()) else "readonly")
    radio_state = "disabled" if playing else "normal"
    radio_classic.configure(state=radio_state)
    radio_custom.configure(state=radio_state)

def change_mode():   #游戏模式
    if playing:
        change_control()
    else:
        reset()

def reset():   #重新开始
    global plate, moves, used_time, current_rule, playing, start_time
    playing = False
    start_time = 0.0
    moves = 0
    used_time = 0.0
    size = int(grid_size.get())
    grid(size)
    if not M.get():
        plate = create(size)
        current_rule = CROSS
    else:
        current_rule = R.get()
        plate = custom(size, current_rule, D.get())
    change_info()
    refresh()
    change_control()

def start_timer():   #开始计时
    global playing, start_time
    playing = True
    start_time = time.time()
    change_control()

def format_time(sec):   #格式化时间
    i = int(sec)
    min = i // 60
    s = i % 60
    ms = round((sec % 1) * 1000)
    return f"{min:02d}:{s:02d}.{ms:03d}"

def change_info():   #更新信息
    move_text.set("操作次数："+str(moves))
    time_text.set("游戏时长："+format_time(used_time))

def change_light(x, y, on):   #开关灯
    btn = button[x][y]
    if on:
        btn.configure(bg="#4169E1", activebackground="#4169E1") #这个宝蓝色挺好看的
    else:
        btn.configure(bg="#333333", activebackground="#333333")

def refresh():   #刷新灯
    for x, y in enumerate(plate):
        for _, on in enumerate(y):
            change_light(x, _, on)

def grid(size):   #创建棋盘
    global button
    for child in board_frame.winfo_children():
        child.destroy()
    button = []
    for x in range(size):
        bx = []
        for y in range(size):
            by = Button(
                board_frame,
                width=8,
                height=3,   #大概是正方形
                relief="flat",
                command=lambda x=x, y=y: click(x, y),
            )
            by.grid(row=x, column=y, padx=2, pady=2)
            bx.append(by)
        button.append(bx)

def add_combo(parent, label, variable, values, column):   #添加下拉菜单
    frame = ttk.Frame(parent)
    frame.grid(row=0, column=column, padx=8, sticky=N)
    ttk.Label(frame, text=label).pack(anchor=W)
    display_values = [text for _, text in values]
    combo = ttk.Combobox(frame, values=display_values, state="readonly", width=16)
    combo.pack(pady=(2, 0))
    combo.current(0)
    variable.set(values[0][0])
    choice = {text: value for value, text in values}
    def on_select(_event=None):
        selected = combo.get()
        variable.set(choice[selected])
        change_mode()
    combo.bind("<<ComboboxSelected>>", on_select)
    return combo

def win():   #游戏胜利
    global used_time
    used_time = time.time() - start_time
    t = format_time(used_time)
    messagebox.showinfo(
        "游戏胜利",
        f"恭喜通关！\n\n操作次数：{moves}\n游戏时长：{t}",
    )
    reset()

def timerloop():   #计时循环
    global used_time
    while playing:
        used_time = time.time() - start_time
        change_info()
        root.update()
        time.sleep(0.1)

def click(x, y):   #点击方块
    global moves
    started = False
    if not playing:
        if not plate or off(plate):
            reset()
        start_timer()
        started = True
    size = len(plate)
    if not (0 <= x < size and 0 <= y < size):
        return
    flip(plate, x, y, current_rule)
    moves += 1
    refresh()
    change_info()
    if off(plate):
        win()
        return
    if started:
        timerloop()

def ui():   #创建界面
    global root, board_frame
    global size_combo, rule_combo, level_combo, radio_classic, radio_custom
    global grid_size, M, R, D, move_text, time_text
    root = Tk()
    root.title("关灯游戏")
    root.resizable(False, False)
    root.configure(bg="#F6F6F6")
    grid_size = IntVar(value=3)
    M = IntVar(value=0)
    R = IntVar(value=CROSS)
    D = IntVar(value=EASY)
    move_text = StringVar(value="操作次数：0")
    time_text = StringVar(value="游戏时长：00:00.000")
    title = ttk.Label(root, text="关 灯 游 戏", font=("Microsoft YaHei UI", 22, "bold"))
    title.pack(pady=16)
    settings = ttk.Frame(root)
    settings.pack(padx=16, pady=4)
    mode_panel = Frame(settings, borderwidth=5, bg="#F6F6F6")
    mode_panel.grid(row=0, column=0, padx=8, pady=4, sticky=N)
    ttk.Label(mode_panel, text="游戏模式").grid(row=0, column=0, columnspan=2, padx=6, pady=(4, 0))
    radio_classic = ttk.Radiobutton(
        mode_panel,
        text="经典",
        variable=M,
        value=0,
        command=change_mode,
    )
    radio_classic.grid(row=1, column=0, padx=4, pady=4, sticky=W)
    radio_custom = ttk.Radiobutton(
        mode_panel,
        text="自定义关卡",
        variable=M,
        value=1,
        command=change_mode,
    )
    radio_custom.grid(row=1, column=1, padx=4, pady=4, sticky=W)
    size_combo = add_combo(
        settings,
        "棋盘大小",
        grid_size,
        [(3, "3 × 3"), (5, "5 × 5"), (7, "7 × 7")],
        1,
    )
    rule_combo = add_combo(
        settings,
        "翻转规则",
        R,
        [(CROSS, "十字翻转"), (X, "X 形翻转")],
        2,
    )
    level_combo = add_combo(
        settings,
        "难度",
        D,
        [(EASY, "简单（1 步）"), (MEDIUM, "中等（2-3 步）"), (HARD, "困难（≥4 步）")],
        3,
    )
    info = Frame(root, bg="#FFFFFF", bd=5)
    info.pack(padx=20, pady=(4, 0), fill="x")
    ttk.Label(info, textvariable=move_text, font=("Microsoft YaHei UI", 12)).pack(
        side="left", padx=16, pady=4
    )
    ttk.Label(info, textvariable=time_text, font=("Microsoft YaHei UI", 12)).pack(
        side="right", padx=16, pady=4
    )
    board_frame = Frame(root, bg="#F6F6F6")
    board_frame.pack(pady=30)
    restart = ttk.Frame(root)
    restart.pack(pady=(0, 8))
    ttk.Button(restart, text="重新开始", width=12, command=reset).pack()
    ttk.Label(
        root,
        text="点击方块开始游戏",
        font=("Microsoft YaHei UI", 9),
    ).pack(pady=(0, 8))
    change_mode()

def app():
    ui()
    root.mainloop()