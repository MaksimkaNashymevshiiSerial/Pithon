import tkinter as tk
import random
from tkinter.messagebox import showinfo

colors = {
	1: 'blue',
	2: 'green',
	3: '#10e0d9',
	4: '#830acf',
	5: '#630848',
	6: '#eb6010',
	7: '#738f72',
	8: '#0d0d0d'
}

class MyButton(tk.Button):
	def __init__(self, master, x, y, number, *args, **kwargs):
		super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
		self.x = x
		self.y = MyButton
		self.is_mine = False
		self.number = number
		self.count_bomb = 0
		self.is_open = False



	def __repr__(self):
		return f'pole({self.x}, {self.y}, {self.is_mine}, {self.number})'

class MineSweeper:

	ROW = 10
	COLUMN = 10
	MINES = 20
	IS_GAME_OVER = False
	IS_FIRST_CLICK = True
	windows = tk.Tk()

	def __init__(self):
		self.buttons = []

		for i in range(MineSweeper.ROW + 2):
			temp = []
			for j in range(MineSweeper.COLUMN + 2):
				btn = MyButton(MineSweeper.windows, x=i, y=j, number=0)
				btn.config(command=lambda button=btn: self.click(button))
				temp.append(btn)

			self.buttons.append(temp)

	def create_widget(self):
		menubar = tk.Menu(self.windows, tearoff=0)
		self.window.config(menu=menubar)
		settings_menu = tk.Menu(menubar)
		settings_menu.add_command(label='Играть')
		settings_menu.add_command(label='Настойки')
		settings_menu.add_command(label='Выход', command=self.window.destroy)
		menubar.add_cascade(label='Файл', menu=settings_menu)

		count = 1
		for i in range(1, MineSweeper.ROW + 1):
			for j in range(1, MineSweeper.COLUMN + 1):
				btn = self.buttons[i][j]
				btn.number = count
				btn.grid(row=i, column=j)
				count += 1

	def open_all_button(self):
		for i in range(MineSweeper.ROW + 2):
			for j in range(MineSweeper.COLUMN + 2):
				btn = self.buttons[i][j]
				if btn.is_mine:
					btn.config(text='*', background='red', disabledforeground='black')
				elif btn.count_bomb in colors:
					color = colors.get(btn.count_bomb, 'black')
					btn.config(text=btn.count_bomb, fg=color)

	def get_mine_places(exclude_number:int):
		indexes = list(range(1, MineSweeper.COLUMN * MineSweeper.ROW + 1))
		indexes.remove(exclude_number)
		random.shuffle(indexes)
		return indexes[:MineSweeper.MINES]

	def print_buttons(self):
		for i in range(1, MineSweeper.ROW + 1):
			for j in range(1, MineSweeper.COLUMN + 1):
				btn = self.buttons[i][j]
				if btn.is_mine:
					print('B', end="")
				else:
					print(btn.count_bomb, end='')
			print()

	def insert_mine(self, number:int):
		index_mines = self.get_mine_places(self, number)
		print(index_mines)
		for i in range(1, MineSweeper.ROW + 1):
			for j in range(1, MineSweeper.COLUMN + 1):
				btn = self.buttons[i][j]
				if btn.number in index_mines:
					btn.is_mine = True
				#count += 1

	def click(self, clicked_button:MyButton):
		if MineSweeper.IS_GAME_OVER:
			return None

		if MineSweeper.IS_FIRST_CLICK:
			self.insert_mine(clicked_button.number)
			self.count_mines_in_buttons()
			self.print_buttons()
			MineSweeper.IS_FIRST_CLICK = False
		clicked_button.is_open = True
		if clicked_button.is_mine:
			clicked_button.config(text="*", background='red', disabledforeground='black')
			MineSweeper.IS_GAME_OVER = True
			showinfo('Game Over', 'Ты проиграл!')
			for i in range(1, MineSweeper.ROW + 1):
				for j in range(1, MineSweeper.COLUMN + 1):
					btn = self.buttons[i][j]
					if btn.is_mine:
						btn['text'] = '*'
		else:
			color = colors.get(clicked_button.count_bomb, 'black')
			if clicked_button.count_bomb:
				clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
			else:
				clicked_button.config(text='', disabledforeground=color)
				self.breadth_first_search(clicked_button)
		clicked_button.config(state='disabled')
		clicked_button.config(relief=tk.SUNKEN)

	def start(self):
		self.create_widget()
		#self.open_all_button()
		self.windows.mainloop()

	def count_mines_in_buttons(self):
		for i in range(1, MineSweeper.ROW + 1):
			for j in range(1, MineSweeper.COLUMN + 1):
				btn = self.buttons[i][j]
				count_bomb = 0
				if not btn.is_mine:
					for row_dx in [-1, 0, 1]:
						for col_dx in [-1, 0, 1]:
							neighbour = self.buttons[i + row_dx][j + col_dx]
							if neighbour.is_mine:
								count_bomb += 1
				btn.count_bomb = count_bomb


	def breadth_first_search(self, btn:MyButton):
		quere = [btn]
		while quere:
			cur_btn = quere.pop()
			color = colors.get(cur_btn.count_bomb, 'black')
			if cur_btn.count_bomb:
				cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
			else:
				cur_btn.config(text='', disabledforeground=color)
			cur_btn.config(state='disabled')
			cur_btn.config(relief=tk.SUNKEN)
			cur_btn.is_open = True
			if cur_btn.count_bomb == 0:
				x, y = cur_btn.x, cur_btn.y
				for dx in [-1, 0, 1]:
					for dy in [-1, 0, 1]:
						if not abs(dx - dy) == 1:
							continue
						next_btn = self.buttons[x + dx][y + dy]
						if not next_btn.is_open and 1 <= next_btn.x < MineSweeper.ROW and \
								1 <= next_btn.x < MineSweeper.COLUMN and next_btn not in quere:
							quere.append(next_btn)




game = MineSweeper()
game.start()
