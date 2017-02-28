import os, shutil
from tkinter import *
from tkinter import ttk, filedialog

def updateText(*args):
    bracketFile = open('bracket.txt', 'w')
    bracketFile.write(bracket.get())
    bracketFile.close()

    player1File = open('player1.txt', 'w')
    player1File.write(player1.get())
    player1File.close()

    score1File = open('score1.txt', 'w')
    score1File.write(score1.get())
    score1File.close()

    player2File = open('player2.txt', 'w')
    player2File.write(player2.get())
    player2File.close()

    score2File = open('score2.txt', 'w')
    score2File.write(score2.get())
    score2File.close()

def swapText(*args):
    newPlayer1 = player2.get()
    newScore1 = score2.get()
    newPlayer2 = player1.get()
    newScore2 = score1.get()

    replaceText(player1_entry, newPlayer1)
    replaceText(player2_entry, newPlayer2)
    replaceText(score1_entry, newScore1)
    replaceText(score2_entry, newScore2)

def clearText(*args):
    newPlayer1 = ''
    newScore1 = '0'
    newPlayer2 = ''
    newScore2 = '0'

    replaceText(player1_entry, newPlayer1)
    replaceText(player2_entry, newPlayer2)
    replaceText(score1_entry, newScore1)
    replaceText(score2_entry, newScore2)
    clearPic()

def replaceText(entry, newText):
    entry.delete(0, END)
    entry.insert(0, newText)

def loadCharPic(btn):
    filename = filedialog.askopenfilename(filetypes = (('Character Portraits','*.png'),))

    if btn == 'PlayerPic1':
        PlayerPic1 = filename
        PlayerPic1File = open('PlayerPic1File.png','w')
        PlayerPic1File.close()
        shutil.copyfile(PlayerPic1, 'PlayerPic1File.png')
    else:
        PlayerPic2 = filename
        PlayerPic2File = open('PlayerPic2File.png','w')
        PlayerPic2File.close()
        shutil.copyfile(PlayerPic2, 'PlayerPic2File.png')

def clearPic():
    shutil.copyfile('png/clearPic.png', 'PlayerPic1File.png')
    shutil.copyfile('png/clearPic.png', 'PlayerPic2File.png')


root = Tk()
root.title('BCM Stream Input')

mainframe = ttk.Frame(root, padding = '12')
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

bracket = StringVar()
player1 = StringVar()
score1 = StringVar()
player2 = StringVar()
score2 = StringVar()

ttk.Label(mainframe, text = 'Bracket:').grid(column = 1, row = 1, sticky = E)
bracket_entry = ttk.Entry(mainframe, width = 16, textvariable = bracket)
bracket_entry.grid(column = 2, row = 1, columnspan = 2, sticky = W)

ttk.Label(mainframe, text = 'Player 1:').grid(column = 1, row = 2, sticky = E)
player1_entry = ttk.Entry(mainframe, width = 16, textvariable = player1)
player1_entry.grid(column = 2, row = 2, columnspan = 2, sticky = W)

ttk.Label(mainframe, text = 'Score:').grid(column = 4, row = 2, sticky = W)
score1_entry = ttk.Entry(mainframe, width = 2, textvariable = score1)
score1_entry.grid(column = 5, row = 2, sticky = W)

ttk.Label(mainframe, text = 'Player 2:').grid(column = 1, row = 3, sticky = E)
player2_entry = ttk.Entry(mainframe, width = 16, textvariable = player2)
player2_entry.grid(column = 2, row = 3, columnspan = 2, sticky = W)

ttk.Label(mainframe, text = 'Score:').grid(column = 4, row = 3, sticky = W)
score2_entry = ttk.Entry(mainframe, width = 2, textvariable = score2)
score2_entry.grid(column = 5, row = 3, sticky = W)

ttk.Button(mainframe, text = 'Update', command = updateText).grid(column = 1, row = 4)
ttk.Button(mainframe, text = 'Clear All', command = clearText).grid(column = 4, row = 4)
ttk.Button(mainframe, text = 'Swap', command = swapText).grid(column = 2, row = 4)
ttk.Button(mainframe, text = 'Clear Pic', command = clearPic).grid(column = 3 , row = 4)

ttk.Button(mainframe, text = 'P1 Pic', command = lambda: loadCharPic('PlayerPic1')).grid(column = 3, row = 2)
ttk.Button(mainframe, text = 'P2 Pic', command = lambda: loadCharPic('PlayerPic2')).grid(column = 3, row = 3)



for child in mainframe.winfo_children(): child.grid_configure(padx = 15, pady = 5)

bracket_entry.focus()

root.mainloop()
