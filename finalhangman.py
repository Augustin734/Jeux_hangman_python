## HANG MAN ##

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

penalty = 0

letter_tried = []

word_tried = []

import time

# To choose and print a random file from the word.txt,
# then get it hidden.
import random

with open("words.txt") as file:
	words = file.read().splitlines()

x = random.choice(words)

print (x)

answer=["_"]*len(x)

# Ask for an input and execute func depending on the input
def gamebase(n):
	uinput=input("Pls choose a letter, or give me a full answer : ")
	if len(uinput) > 1:
		wordp(uinput)
		word_tried.append(uinput)
	else:
		letterp(uinput)
		letter_tried.append(uinput)

# For input as a word
def wordp(n):
	global penalty
	global answer
	if list(n) == list(x):
		answer = list(x)
	else:
		penalty += 5
		print ("Nop but nt, u have", 12-penalty, "tries left, ")

# For input as a letter
def letterp(n):
	global penalty
	global uinput
	global answer
	if n in alphabet:
		if n in x :
			for i, y in enumerate(x):
				if y == n:
					answer[i]=n
			print (*answer)
		else:
			penalty += 1
			print ("Nop, but nt, u have", 12-penalty, "tries left,")
	else :
		penalty += 1
		print ("U think i'm stupid or smth ?! +1 penalty for ur recklessness ")

# To make the func run until u get it right (with helps printed)
def hangman(n):
	while "_" in answer:
		print ("The random word contains : ", len(x), "letters")
		print ("U actually have : ", penalty, "penalties")
		print ("U have already gave me : ", ", ".join(letter_tried))
		print ("U already tried : ", ", ".join(word_tried))
		gamebase(n)
		if penalty >= 12:
			print ("U loose !!!!")
			break

		if answer == list(x):
			print ("Wp 2 u, u find the good word !! Wich was : ", "".join(x))
			break

# Create a time score, if it's lower than last best, print success text and save it in the file
def p_score(n):
	with open("scores.txt", "r+") as scores_file:
		b_score = float(scores_file.read())
		if n <= b_score:
			print ("WOW !! U just made a new best score !!")
			print ("U find the good answer in", n)
			scores_file.seek(0)
			scores_file.write(str(n))
			scores_file.truncate()
		else:
			print ("Nt but the best score remains : ", b_score)

# Treat the player answer, and create a timer if yes/y
def p_wanna_p(n):
	if "yes" in n or n == "y":
		return True
		start = time.time()
		hangman(answer)
		player_time = round((time.time()- start), 2)
		p_score(player_time)
	else:
		return False
		print("See ya !!")

# Ask the player if they wanna play, and use the score.py file
p_input = input("Do u wanna play ? (yes/no answer) : ").lower()
p_wanna_p(p_input)



## PY GAME ##
import pygame
from sys import exit

# La taile de la fenetre
game_width = 1200
game_height = 800

# Le nom de la fenêtre
nom_fenetre = "Hangman Game"

# Initialisation du jeu
pygame.init()
window = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption(nom_fenetre)
clock = pygame.time.Clock()

# L'image en fond
fond = pygame.image.load("pirate_background.png").convert()
fond = pygame.transform.scale(fond, (game_width, game_height))



# Boucle qui fait tourner le jeu
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		p_input = input("Do u wanna play ? (yes/no answer) : ").lower

	window.blit(fond, (0,0))
	pygame.display.update()
	clock.tick(90)
