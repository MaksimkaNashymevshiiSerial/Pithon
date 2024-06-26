from tkinter import *
import random

root = Tk()
root.title('Крестики-нолики')
print("Привет Игрок! Я очень рад тебя видеть! Давай играть в Крестики-нолики! Ты первый!")
game_run = True
field = []
cross_count = 0

def new_game():
	for row in range(3):
		for col in range(3):
			field[row][col]['text'] = ' '
			field[row][col]['background'] = 'lavender'
	global game_run, cross_count
	game_run = True
	cross_count = 0


def click(row,col):
	if game_run and field[row][col]['text'] == ' ':
		field[row][col]['text'] = 'X'
		global cross_count
		cross_count +=1
		check_win('X')
		if game_run and cross_count < 5:
			computer_move()
			check_win('O')

def check_win(smd):
	for n in range(3):
		check_line(field[n][0], field[n][1], field[n][2], smd)
		check_line(field[0][n], field[1][n], field[2][n], smd)
	check_line(field[0][0], field[1][1], field[2][2], smd)
	check_line(field[2][0], field[1][1], field[0][2], smd)

def check_line(a1, a2, a3, smd):
	if a1['text'] == smd and a2['text'] == smd and a3['text'] == smd:
		a1['background'] = a2['background'] = a3['background'] = 'red'
	if a1['text'] == smd and a2['text'] == smd and a3['text'] == smd:
		print(smd, "Победил!")
		global game_run
		game_run = False


def can_win(a1, a2, a3, smd):
	res = False
	if a1['text'] == smd and a2['text'] == smd and a3['text'] == ' ':
		a3['text'] = 'O'
		res = True
	if a1['text'] == smd and a2['text'] == ' ' and a3['text'] == smd:
		a2['text'] = 'O'
		res = True
	if a1['text'] == smd and a2['text'] == smd and a3['text'] == smd:
		a1['text'] = 'O'
		res = True
	return res

def computer_move():
	for n in range(3):
		if can_win(field[n][0], field[n][1], field[n][2], 'O'):
			return
		if can_win(field[0][n], field[1][n], field[2][n], 'O'):
			return
	if can_win(field[0][0], field[1][1], field[2][2], 'O'):
		return
	if can_win(field[2][0], field[1][1], field[0][2], 'O'):
		return

	for n in range(3):
		if can_win(field[n][0], field[n][1], field[n][2], 'X'):
			return
		if can_win(field[0][n], field[1][n], field[2][n], 'X'):
			return
	if can_win(field[0][0], field[1][1], field[2][2], 'X'):
		return
	if can_win(field[2][0], field[1][1], field[0][2], 'X'):
		return

	while True:
		row = random.randint(0,2)
		col = random.randint(0,2)
		if field[row][col]['text'] == ' ':
			field[row][col]['text'] = 'O'
			break

for row in range(3):
	line = []
	for col in range(3):
		button = Button(root, text=' ', width=5, height=2, 
			font=('Verdana', 25, 'bold'), background='lavender',
			command=lambda row=row, col=col: click(row,col))
		button.grid(row=row, column=col, sticky='nsew')
		line.append(button)
	field.append(line)
new_button = Button(root, text='Новая Игра', font=('Verdana', 15, 'bold'), 
	command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()