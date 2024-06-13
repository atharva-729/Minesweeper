from tkinter import Button, Label, PhotoImage
import random
import settings
import ctypes
import sys
import time

class Cell:
    all = [] # will contain objects
    cell_count_label_obj = None
    cell_count = settings.CELL_COUNT
    mine_count_label_obj = None
    mine_count = settings.MINES_COUNT
    
    def __init__(self, x, y,  is_mine=False):
        self.is_mine = is_mine
        self.btn_obj = None
        self.x = x
        self.y = y
        self.flag = False

        # Append objects to Cell.all list
        Cell.all.append(self)


    def create_btn_obj(self, location):
        image = PhotoImage("./irene.jpg")
        font1=("Arial", 14, "bold")
        btn = Button(
            location,
            text="  ",
            font=font1,
            bg="mistyrose",
            highlightthickness=2
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        # <button-1> is left click and 3 is right click
        
        self.btn_obj = btn

    visited = set()
    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.check()
            Cell.cell_count = settings.CELL_COUNT - len(Cell.visited)
            Cell.cell_count_label_obj.configure(
                text=f"Cells Left: {Cell.cell_count}"
            )
            self.show_cell()
            if Cell.cell_count == settings.MINES_COUNT:
                time.sleep(0.5)
                ctypes.windll.user32.MessageBoxW(
                0, "You Won.",
                "Game Over!!", 0
                )
                sys.exit()
            
    
    def check(self):
        if self in Cell.visited:
            return
        
        Cell.visited.add(self)
        self.show_cell()

        if self.count_mines == 0:
            for neighbor in self.surrounding_cells:
                Cell.check(neighbor)


    
    def show_mine(self):
        self.btn_obj.configure(bg="red")
        self.btn_obj.update()
        time.sleep(0.5)
        ctypes.windll.user32.MessageBoxW(
            0, "That was a mine.",
            "Game Over!!", 0
        )
        sys.exit()

    def show_cell(self):
        mines = self.count_mines
        if mines == 0:
            self.btn_obj.configure(
            text="  ",
            bg="whitesmoke"
            )
        if mines == 1:
            self.btn_obj.configure(
            bg="whitesmoke",
            text=1,
            fg="royalblue"
            )
        if mines == 2:
            self.btn_obj.configure(
            bg="whitesmoke",
            text=2,
            fg="green"
            )
        if mines == 3:
            self.btn_obj.configure(
            bg="whitesmoke",
            text=3,
            fg="red"
            )
        if mines == 4:
            self.btn_obj.configure(
            bg="whitesmoke",
            text=4,
            fg="midnightblue"
            )
        if mines == 5:
            self.btn_obj.configure(
            bg="whitesmoke",
            text=5,
            fg="maroon"
            )
        if mines == 6:
            self.btn_obj.configure(
            bg="whitesmoke",
            text=6,
            fg="mediumturquoise"
            )
        self.btn_obj.update()
        

    def get_cell_by_axis(self, x, y):
        # return cell object based on x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return  cell

    @property
    def surrounding_cells(self):
        cells = []
        for i in [self.x-1, self.x, self.x+1]:
            if i>=0 and i<=settings.GRID_ROWS-1:
                for j in [self.y-1, self.y, self.y+1]:
                    if j>=0 and j<=settings.GRID_COL-1:
                        if self.x == i and self.y == j:
                            continue
                        cells.append(Cell.all[i*(settings.GRID_COL) + j])
        return cells

    @staticmethod
    def cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left:{Cell.cell_count}",
            bg="paleturquoise",
            font=("Arial", 20)
        )
        Cell.cell_count_label_obj = lbl
    
    @staticmethod
    def mine_count_label(location):
        lbl = Label(
            location,
            text=f"Mines Left:{Cell.mine_count}",
            anchor="w",
            bg="paleturquoise",
            font=("Arial", 20)
        )
        Cell.mine_count_label_obj = lbl


    def right_click_action(self, event):
        if self not in Cell.visited:
            if not self.flag:  
                self.btn_obj.configure(bg="limegreen")
                Cell.mine_count -= 1
                Cell.mine_count_label_obj.configure(
                        text=f"Mines Left: {Cell.mine_count}"
                    )
                self.flag = True
            else:
                self.btn_obj.configure(bg="mistyrose")
                Cell.mine_count += 1
                Cell.mine_count_label_obj.configure(
                        text=f"Mines Left: {Cell.mine_count}"
                    )
                self.flag = False

    @property
    def count_mines(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1

        return counter


    @staticmethod
    def where_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"cell ({self.x},{self.y})"