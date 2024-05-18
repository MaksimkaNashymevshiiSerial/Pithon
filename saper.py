import tkinter as tk
import random

class MyButton(tk.Button):
	def __init__(self, master, x, y, number, *args, **kwargs):
		super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
		self.x = x
		self.y = MyButton
		self.is_mine = False
		self.number = number

	def __repr__(self):
		return f'pole({self.x}, {self.y}, {self.is_mine}, {self.number})'

class MineSweeper:

	ROW = 5
	COLUMN = 7
	MINES = 7
	windows = tk.Tk()

	def __init__(self):
		self.buttons = []
		count = 1
		for i in range(MineSweeper.ROW):
			temp = []
			for j in range(MineSweeper.COLUMN):
				btn = MyButton(MineSweeper.windows, x=i, y=j, number=count)
				btn.config(command=lambda button=btn: self.click(button))
				temp.append(btn)
				count += 1
			self.buttons.append(temp)

	def create_widget(self):
		for i in range(MineSweeper.ROW):
			for j in range(MineSweeper.COLUMN):
				btn = self.buttons[i][j]
				btn.grid(row=i, column=j)

	def get_mine_places(self):
		indexes = list(range(1, MineSweeper.COLUMN + MineSweeper.ROW + 1))
		random.shuffle(indexes)
		return indexes[:MineSweeper.MINES]

	def print_buttons(self):
		for row_btn in self.buttons:
			print(row_btn)

	def insert_mine(self):
		index_mines = self.get_mine_places()
		print(index_mines)
		for row_btn in self.buttons:
			for btn in row_btn:
				if btn.number in index_mines:
					btn.is_mine = True

	def click(self, clicked_button):
		print(clicked_button)
		if clicked_button.is_mine:
			clicked_button.config(text="*", background='red')
		else:
			clicked_button.config(text=clicked_button.number)
		clicked_button.config(state='disabled')

	def start(self):
		game.create_widget()
		game.insert_mine()
		game.print_buttons()
		self.windows.mainloop()

game = MineSweeper()
game.start()
