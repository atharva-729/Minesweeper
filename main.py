from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

# Set window settings
root.configure(bg="white")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)

# Make frames
top_frame = Frame(
    root,
    bg="paleturquoise",
    width=utils.width_per(100),
    height=utils.height_per(15)
)
top_frame.place(x=0,y=0)

# I don't need this left frame
# left_frame = Frame(
#     root,
#     bg="lightcyan",
#     width=utils.width_per(20),
#     height=utils.height_per(75) 
# )
# left_frame.place(x=0, y=utils.height_per(25))

center_frame = Frame(
    root,
    bg="azure",
    width=utils.width_per(100),
    height=utils.height_per(75)
)
center_frame.place(
    x=utils.width_per(3.5), 
    y=utils.height_per(15)
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
    x=175, y=0
)

# print((Cell.all))
Cell.where_mines()

# Run window
root.mainloop()