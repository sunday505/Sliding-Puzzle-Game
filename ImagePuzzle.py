import tkinter as tk
import random
import os
from playsound import playsound

class application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Slide Image Puzzle')
        self.geometry('723x770+600+150')

        self.buttonWidth = 200
        self.buttonHeight = 200
        self.counting = 0
        self.endGame = False

        current_path = os.getcwd()
        self.pic_path = os.path.join(current_path, "SlidePuzzlePic/Lulu")
        self.sound_path = os.path.join(current_path, "SlidePuzzleSoundEffect")


        self.image1 = tk.PhotoImage(file=os.path.join(self.pic_path, 'row-1-column-1.png'))
        self.image2 = tk.PhotoImage(file=os.path.join(self.pic_path, 'row-1-column-2.png'))
        self.image3 = tk.PhotoImage(file=os.path.join(self.pic_path, 'row-1-column-3.png'))
        self.image4 = tk.PhotoImage(file=os.path.join(self.pic_path, 'row-2-column-1.png'))
        self.image5 = tk.PhotoImage(file=os.path.join(self.pic_path, 'row-2-column-2.png'))
        self.image6 = tk.PhotoImage(file=os.path.join(self.pic_path, 'row-2-column-3.png'))
        self.image7 = tk.PhotoImage(file=os.path.join(self.pic_path, 'row-3-column-1.png'))
        self.image8 = tk.PhotoImage(file=os.path.join(self.pic_path, 'row-3-column-2.png'))

        self.button1 = tk.Button(self, image=self.image1, borderwidth = 0, command = lambda : self.move(0))
        self.button2 = tk.Button(self, image=self.image2, borderwidth = 0, command = lambda : self.move(1))
        self.button3 = tk.Button(self, image=self.image3, borderwidth = 0, command = lambda : self.move(2))
        self.button4 = tk.Button(self, image=self.image4, borderwidth = 0, command = lambda : self.move(3))
        self.button5 = tk.Button(self, image=self.image5, borderwidth = 0, command = lambda : self.move(4))
        self.button6 = tk.Button(self, image=self.image6, borderwidth = 0, command = lambda : self.move(5))
        self.button7 = tk.Button(self, image=self.image7, borderwidth = 0, command = lambda : self.move(6))
        self.button8 = tk.Button(self, image=self.image8, borderwidth = 0, command = lambda : self.move(7))
        self.button_Again = tk.Button(self, text="Again", font="Thaisarabun 18", command=self.repeat)
        self.Show_time = tk.Label(self, text="", font="Thaisarabun 18")
        self.Show_Win = tk.Label(self, text="You Win XDDD", font="Thaisarabun 25")

        self.button_Again.grid(row=4, column=2)
        self.Show_time.grid(row=4, column=1)

        self.random_ImagePosition()

        self.timing()

    def random_ImagePosition(self):
        self.Show_time.config(text="0 Seconds")
        self.game_Table = [
            ["X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X"],
            ["X", " ", " ", " ", "X"],
            ["X", " ", " ", " ", "X"],
            ["X", "X", "X", "X", "X"]
        ]
        self.buttonList = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8]
        self.buttonPosition = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
        tempNum = [int(i) for i in range(9)]

        for i in range(100):
            while(True):
                x1, x2 = random.sample(tempNum, 2)
                if (x1 - x2) % 2 == 0 or (x2 - x1) % 2 == 0 : break
            self.buttonPosition[x1], self.buttonPosition[x2] = self.buttonPosition[x2], self.buttonPosition[x1]

        for index, buttons in enumerate(self.buttonList):
            x_Posi, y_Posi = self.buttonPosition[index]
            buttons.grid(row = x_Posi, column = y_Posi)
            self.game_Table[x_Posi][y_Posi] = index + 1

    def check_Move(self, whichButton):
        x_Posi = self.buttonPosition[whichButton][0]
        y_Posi = self.buttonPosition[whichButton][1]
        # Up
        if self.game_Table[x_Posi - 1][y_Posi] == " ":
            return True
        # Down
        if self.game_Table[x_Posi + 1][y_Posi] == " ":
            return True
        # Left
        if self.game_Table[x_Posi][y_Posi - 1] == " ":
            return True
        # Right
        if self.game_Table[x_Posi][y_Posi + 1] == " ":
            return True
        return False

    def move(self, whichButton):
        if self.check_Move(whichButton):
            playsound(os.path.join(self.sound_path, "click_sound_2.wav"), block=True)
            self.buttonPosition[whichButton], self.buttonPosition[-1] = self.buttonPosition[-1], self.buttonPosition[whichButton]
            x1, y1 = self.buttonPosition[whichButton]
            x2, y2 = self.buttonPosition[-1]
            self.game_Table[x1][y1], self.game_Table[x2][y2] = self.game_Table[x2][y2], self.game_Table[x1][y1]
            x_Posi, y_Posi = self.buttonPosition[whichButton]
            self.buttonList[whichButton].grid(row = x_Posi, column = y_Posi)
            self.check_Win()

    def check_Win(self):
        if self.game_Table == [["X", "X", "X", "X", "X"], ["X", 1, 2, 3, "X"], ["X", 4, 5, 6, "X"], ["X", 7, 8, " ", "X"], ["X", "X", "X", "X", "X"]]:
            self.endGame = True
            self.Show_Win.grid(row=4, column=3)
            playsound(os.path.join(self.sound_path, "win_sound_2.wav"), block=True)

    def repeat(self):
            self.endGame = False
            self.random_ImagePosition()
            self.Show_Win.destroy()
            self.counting = 0
            self.Show_Win = tk.Label(self, text="You Win XDDD", font="Thaisarabun 25")

    def timing(self):
        if not self.endGame:
            self.counting += 1
            self.Show_time.config(text=f"{self.counting} Seconds")
        self.after(1000, self.timing)
            
if __name__ == "__main__":
    app = application()
    app.mainloop()