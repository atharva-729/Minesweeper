from tkinter import *
from cell import Cell
import settings
import utils

difficulty_window = Tk()
difficulty_window.title("Choose Difficulty")
difficulty_window.geometry("350x450")
difficulty_window.config(bg="lightgreen")

def choose_easy():
    difficulty_window.destroy()
    settings.WIDTH = 360
    settings.HEIGHT = 480
    settings.GRID_ROWS = 9
    settings.GRID_COL = 9
    settings.CELL_COUNT = 9*9
    settings.MINES_COUNT = (9*9)//4

def choose_medium():
    difficulty_window.destroy()
    settings.WIDTH = 690
    settings.HEIGHT = 560
    settings.GRID_ROWS = 10
    settings.GRID_COL = 20
    settings.CELL_COUNT = 10*20
    settings.MINES_COUNT = (10*20)//4

def choose_hard():
    difficulty_window.destroy()
    settings.WIDTH = 1920
    settings.HEIGHT = 1080
    settings.GRID_ROWS = 16
    settings.GRID_COL = 40
    settings.CELL_COUNT = 16*40
    settings.MINES_COUNT = (16*40)//4

font1=("Arial", 14, "bold")
easy_button = Button(difficulty_window, text="not so easy", command=choose_easy, bg="white", font=font1)
medium_button = Button(difficulty_window, text="kinda hard", command=choose_medium, bg="skyblue", font=font1)
hard_button = Button(difficulty_window, text="PRESS TO DIE", command=choose_hard, bg="red", font=font1)

easy_button.grid(row=0, column=0, padx=100, pady=50)
medium_button.grid(row=1, column=0, padx=100, pady=50)
hard_button.grid(row=2, column=0, padx=100, pady=50)

difficulty_window.mainloop()

root = Tk()
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper")

# Make frames
top_frame = Frame(
    root,
    bg="paleturquoise",
    width=utils.width_per(100),
    height=utils.height_per(10)
)
top_frame.place(x=0,y=0)

center_frame = Frame(
    root,
    bg="azure",
    width=utils.width_per(100),
    height=utils.height_per(75)
)
center_frame.place(
    x=utils.width_per(10), 
    y=utils.height_per(10)
    )

for x in range(settings.GRID_ROWS):
    for y in range(settings.GRID_COL):
        c = Cell(x, y)
        c.create_btn_obj(center_frame)
        c.btn_obj.grid(
            row=x, column=y
        )

Cell.cell_count_label(top_frame)
Cell.cell_count_label_obj.place(
    x=0, y=0
)

Cell.mine_count_label(top_frame)
Cell.mine_count_label_obj.place(
    x=settings.WIDTH/2, y=0
)

Cell.where_mines()

# Run window
root.mainloop()