from tkinter import *
from tkinter import messagebox
from readwholefile import *

hiddenWord = words[randomNum]
wordle = Tk(className="Wordle!")

GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
WHITE = "#FFFFFF"
PURPLE = "#C3B1E1"

guessnum = 1
wordle.geometry("800x600")
wordle.config(bg=PURPLE)

wordInput = Entry(wordle)
wordInput.grid(row=999,column=0,padx=10,pady=10,columnspan=3)

def getGuess():
    global hiddenWord
    guess = wordInput.get()
    
    global guessnum
    guessnum += 1
    
    if guessnum <= 5:
        if len(guess) == 5:
            if hiddenWord == guess:
                messagebox.showinfo("Correct!",f"Correct! The word was {hiddenWord.title()}")
            else:
                for i,letter in enumerate(guess):
                    label = Label(wordle,text=letter.upper())
                    label.grid(row=guessnum,column=i,padx=10,pady=10)
                    
                    if letter == words[i]: #if the user gets the letter right :D
                        label.config(bg=GREEN,fg=BLACK)
                    
                    if letter in hiddenWord and not letter == hiddenWord[i]:
                        label.config(bg=YELLOW, fg=BLACK)
                    
                    if letter not in hiddenWord:
                        label.config(bg=BLACK, fg=WHITE)
        else:
            messagebox.showerror("Please use 5 characters","Please use 5 characters in your guess")
    else:
        messagebox.showerror("You lose",f"You lose! The word was {hiddenWord}")
                
wordGuessButton = Button(wordle,text="Guess",command=getGuess)
wordGuessButton.grid(row=999,column=3,columnspan=2)

wordle.mainloop()