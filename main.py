#importing libraries
import random
import sys
import os

#pictures for showing mistakes
draw_pics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

#making random word
def word():
    words = ['sahand','sabet','hello','donkey','cow','python']
    random_word = random.randint(0,len(words)-1)
    return words[random_word]

#drawing output
def draw(wrong,word):
    wrong = int(wrong)
    if wrong < 6:
        print(draw_pics[wrong] , "\n\n **",word,"**\n")
    else:
        print(draw_pics[6] , "\n\n ** You Lost! **\n")
        input(" ** Press a key to exit ** ")
        sys.exit()

#check if user won
def check_win(guess,check):
    if guess == check:
        print(" ** You Won! ** ")
        input(" ** Press a key to exit ** ")
        sys.exit()

#clean the console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#main part
check = word()
len_word = int(len(check))
guess = ('-' * len_word)
guess_list = []
wrong = 0
while True:
    draw(wrong,guess)
    check_win(guess,check)
    ip = input(" ** Enter the letter : ")
    ip = ip[0]
    if ip not in guess_list:
        guess_list.append(ip)
    else:
        cls()
        print(" ** You entered this letter before! ** ")
        continue
    if ip in check:
        for i in range(len_word):
            if check[i] == ip :
                list1 = list(guess)
                list1[i] = ip
                guess = ''.join(list1)
    else :
        wrong +=1
    cls()

#Made By SahandS (https://github.com/sahand1385)