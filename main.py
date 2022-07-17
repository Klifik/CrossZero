from tkinter import *
import random



class CrossZero():
    def __init__(self, win, spWIn):
        self.win = win
        self.Buttons = [Button(win, width=6, height=3, fg='black',
                      bg='white', command=lambda digit = i: self.pressButtonPlayer(digit)) for i in range(9)]
        self.logs = [None] * 9
        self.logs2 = list(range(9))
        self.spWin = spWIn
        self.turn = 0
        self.fhod = 0


    def placeButton(self):

        row = 1
        column = 0
        for i in range(9):
            self.Buttons[i].grid(row = row, column = column)
            column +=1
            if column == 3:
                row +=1
                column = 0

        menuBar = Menu(self.win)
        self.win.config(menu=menuBar)

        settingsMenu = Menu(menuBar, tearoff=0)
        settingsMenu.add_command(label='Играть Заново', command=lambda: self.reload())
        settingsMenu.add_command(label='Выход', command=self.win.destroy)
        menuBar.add_cascade(label='Файл', menu=settingsMenu)

    def pressButtonPlayer(self, digit):
        global count
        if count%2==0:
            self.Buttons[digit].config(text = '╳', bg='black', fg='white', state = 'disabled')
            count+=1
            self.logs[digit] = 1
        else:
            self.Buttons[digit].config(text='◯', bg='purple', fg='black', state='disabled')
            count += 1
            self.logs[digit] = 2


        self.winWork()

    def reload(self):
        for i in range(9):
            self.Buttons[i].destroy()
        self.__init__(self.win, self.spWin)
        self.placeButton()




    def winWork(self):
        for i in range(8):
            x = i
            spWin2 = self.spWin[x]
            if self.logs[spWin2[0]] == 1 and self.logs[spWin2[1]] == 1 and self.logs[spWin2[2]] == 1:
                Label(win, text='X выиграл', bg='black', fg='white').grid(row=0, column=0, columnspan=4, rowspan=4,
                                                                          stick='wens')
            if self.logs[spWin2[0]] == 2 and self.logs[spWin2[1]] == 2 and self.logs[spWin2[2]] == 2:
                Label(win, text='0 выиграл', bg='black', fg='white').grid(row=0, column=0, columnspan=4, rowspan=4,
                                                                          stick='wens')
            elif count == 9:
                Label(win, text='Ничья', bg='black', fg='white').grid(row=0, column=0, columnspan=4, rowspan=4,
                                                                      stick='wens')












win = Tk()
win.geometry('137x147')
win.title('Крестики нолики')
win.config(bg='orange')
win.resizable(False, False)
count = 0

spWIn = [[0, 4, 8], [2, 4 , 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]


window = CrossZero(win, spWIn)
window.placeButton()

win.mainloop()


#def pressButtonBot(self, digit):
#    sp1 = [[0, 1], [3, 4], [6, 7], [1, 2], [4, 5], [7, 8], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8],
#           [0, 4], [2, 4], [6, 4], [8, 4]]
#    sp3 = [2, 5, 8, 0, 3, 6, 6, 7, 8, 0, 1, 2, 8, 6, 2, 0]
#    sp5 = [[0, 2], [2, 8], [6, 8], [0, 6]]
#    sp7 = [1, 5, 7, 3]
#    c = 0
#
#    if digit == 4 and self.turn == 0:
#        self.pressPlayer(digit)
#        t = random.choice(self.logs2)
#        self.pressBot(t)
#
#        self.turn = 1
#        self.fhod = 1
#
#    elif digit != 4 and self.turn == 0:
#        t = 4
#        self.pressPlayer(digit)
#        self.pressBot(t)
#        self.turn = 1
#        self.fhod = 2
#
#    elif self.turn == 1:
#        self.pressPlayer(digit)
#        self.turn = 2
#        proverk = 0
#        for i in range(4):
#            sp6 = sp5[i]
#            if self.logs[sp6[0]] == 1 and self.logs[sp6[1]]:
#                self.pressBot(sp7[i])
#                proverk = 1
#
#        for i in range(9):
#            sp2 = sp1[i]
#
#            if self.logs[sp2[0]] == 1 and self.logs[sp2[1]] == 1:
#                self.pressBot(sp3[i])
#            elif self.logs[0] != 1 and self.logs[0] != 2 and self.turn == 2:
#                self.pressBot(0)
#                proverk = 1
#            elif self.logs[2] != 1 and self.logs[2] != 2 and self.turn == 2 and proverk == 0:
#                self.pressBot(2)
#
#    self.winWork()

#def pressPlayer(self, digit):
#    self.Buttons[digit].config(text='╳', bg='black', fg='white', state='disabled')
#    self.logs[digit] = 1
#
#
#def pressBot(self, t):
#    self.Buttons[t].config(text='◯', bg='purple', fg='white', state='disabled')
#    self.logs[t] = 2