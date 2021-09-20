# BOUNCE - GAME FOR TIME PASS!

# modules needed
from tkinter import *
import random
import time
from functools import partial


# Main code
class Ball(object):
    def __init__(self, canvas, paddle):
        self.canvas = canvas
        self.paddle = paddle
        # self.myimage = PhotoImage(file='img1.gif')
        # self.a = canvas.create_image(100,100, image=self.myimage)
        self.id = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.id, 245, 100)
        # self.canvas.move(self.a,245,100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        global PLAYER_SCORE
        global PLAYER_LEVEL
        global HIGH_SCORE
        global SPEED
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # posi = self.canvas.coords(self.a)
        if pos[0] <= 0: self.x = 4 + SPEED
        if pos[1] <= 0: self.y = 4 + SPEED
        if pos[2] >= self.canvas_width: self.x = -4 - SPEED
        if pos[3] >= self.canvas_height: self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -4 - SPEED
            self.x += self.paddle.x + SPEED * 0.5
            PLAYER_SCORE += 1
            canvas.create_text(1315, 35, fill='white', font='Times 11', text='SCORE : ' + str(PLAYER_SCORE - 1))
            canvas.create_text(1315, 35, fill='white', font='Times 11', text='SCORE : ' + str(PLAYER_SCORE - 1))
            canvas.create_text(1315, 35, fill='white', font='Times 11', text='SCORE : ' + str(PLAYER_SCORE - 1))
            canvas.create_text(1315, 35, fill='white', font='Times 11', text='SCORE : ' + str(PLAYER_SCORE - 1))
            canvas.create_text(1315, 35, fill='white', font='Times 11', text='SCORE : ' + str(PLAYER_SCORE - 1))
            canvas.create_text(1315, 35, fill='white', font='Times 11', text='SCORE : ' + str(PLAYER_SCORE - 1))
            canvas.create_text(1315, 35, fill='black', font='Times 11', text='SCORE : ' + str(PLAYER_SCORE))
            if PLAYER_SCORE % 5 == 0:
                PLAYER_LEVEL += 1
                canvas.create_text(35, 35, fill='white', font='Times 11', text='LEVEL : ' + str(PLAYER_LEVEL - 1))
                canvas.create_text(35, 35, fill='white', font='Times 11', text='LEVEL : ' + str(PLAYER_LEVEL - 1))
                canvas.create_text(35, 35, fill='white', font='Times 11', text='LEVEL : ' + str(PLAYER_LEVEL - 1))
                canvas.create_text(35, 35, fill='white', font='Times 11', text='LEVEL : ' + str(PLAYER_LEVEL - 1))
                canvas.create_text(35, 35, fill='black', font='Times 11', text='LEVEL : ' + str(PLAYER_LEVEL))
                SPEED += 0.5
            if PLAYER_SCORE > HIGH_SCORE:
                HIGH_SCORE = PLAYER_SCORE
                # Set New high score

    def hit_paddle(self, pos):
        ppos = self.canvas.coords(self.paddle.id)
        return pos[2] >= ppos[0] and pos[0] <= ppos[2] and pos[3] >= ppos[1] and pos[3] <= ppos[3]


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 250, 15, fill=color)
        self.canvas.move(self.id, 650, 600)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -5 - SPEED * 1.2

    def turn_right(self, evt):
        self.x = 5 + SPEED * 1.2

    def start_game(self, evt):
        self.started = True


# Essence Code
def game(U):
    tk = Tk()
    log.withdraw()
    file = open('C:\Games\Game.txt', 'w+')
    PLAYER_NAME = U.get()
    string = 'PLAYER NAME : ' + PLAYER_NAME + '\n' + 'PLAYER LEVEL : ' + '0' + '\n' + 'HIGH SCORE : ' + '0' + '\n' + 'PLAYER SCORE : ' + '0'
    file.write(string)
    tk.update_idletasks()
    tk.update()

try:
    file = open('C:\Games\Game.txt', 'r')
    lines = file.read().split('\n')
    data = []
    for line in lines:
        data.append(line.split(' : ')[1])
    PLAYER_NAME = data[0]
    PLAYER_LEVEL = 0
    HIGH_SCORE = int(data[2])
    PLAYER_SCORE = 0


except Exception as e:
    log = Tk()
    log.geometry('600x300')
    log.title('GAME!')
    log.resizable(height=False, width=False)
    log.configure(background="white")
    canvas = Canvas(bg='white', relief=GROOVE, height=1, width=150)
    canvas.create_line(0, 2, 200, 2)
    canvas.place(x=250, y=168)
    Label(log, text=' WELCOME TO BOUNCE!', font=('Helvetica', 20), relief=FLAT, bg='White').place(x=140, y=30)
    Label(log, text=' Player Name : ', relief=FLAT, font=('Helvetica', 10), bg='white').place(x=150, y=152)
    username = StringVar()
    uent = Entry(log, textvariable=username, relief=FLAT, font=('Helvetica', 10), width=26, bg='white')
    uent.place(x=250, y=150)
    game = partial(game, username)
    Button(log, text='     Let\'s Go!     ', font=('Helvetica', 10), border='1', command=game, bg='white').place(x=260,
                                                                                                                 y=200)
    log.mainloop()

# upper code
tk = Tk()
tk.title('Bounce!')
tk.wm_attributes("-topmost", 1)
tk.state('zoomed')
tk.resizable(0, 0)
w, h = tk.winfo_screenwidth(), tk.winfo_screenheight()
canvas = Canvas(tk, bg='white', width=w - 10, height=h - 25, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle)
canvas.create_text(60, 20, fill='black', font='Times 11', text='NAME : ' + PLAYER_NAME)
canvas.create_text(35, 35, fill='black', font='Times 11', text='LEVEL : ' + str(PLAYER_LEVEL))
canvas.create_text(1300, 20, fill='black', font='Times 11', text='HIGH SCORE : ' + str(HIGH_SCORE))
SPEED = 0
game_over_text = canvas.create_text(650, 350, fill='darkblue', font='Times 60  italic bold', text='GAME OVER!',
                                    state='hidden')
c = 1
while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        font = 'Times ' + str(c) + '  italic bold'
        file = open('C:\Games\Game.txt', 'w+')
        string = 'PLAYER NAME : ' + PLAYER_NAME + '\n' + 'PLAYER LEVEL : ' + str(
            PLAYER_LEVEL) + '\n' + 'HIGH SCORE : ' + str(HIGH_SCORE) + '\n' + 'PLAYER SCORE : ' + '0'
        file.write(string)
        canvas.itemconfig(game_over_text, state='normal', font=font)
        c += 1
        if c >= 150:
            break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

