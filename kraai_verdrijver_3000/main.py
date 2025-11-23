from tkinter import *

import pygame.mixer
from pygame import mixer

class Window(Tk):
    def __init__(self):
        Tk.__init__(self)

        pygame.mixer.init()

        width = 800
        height = width - 200
        x = int((self.winfo_screenwidth() - width) / 2)
        y = int((self.winfo_screenheight() - height) / 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.resizable(False, False)
        self.title('Kraai Verdrijver')

        self.config(bg='deep sky blue')


        title_lbl = Label(self, font=('Andale Mono', 50), text='Kraai Verdrijver 3000', bg='deep sky blue', fg="white")
        title_lbl.pack(pady=10)

        verdrijf_btn = Button(self, font=('Andale Mono', 40), text='Schrik Kraaien', command=self.verdrijf)
        verdrijf_btn.pack(pady=50)

        roof_vogel_btn = Button(self, font=('Andale Mono', 40), text='Havik', command=self.play_roof_vogel)
        roof_vogel_btn.pack(pady=50, ipadx=110)


        self.mainloop()


    def verdrijf(self):
        mixer.init()
        mixer.music.load('kraaiverdrijver.mp3')
        mixer.music.play()

    def play_roof_vogel(self):
        self.roof_vogel()
        self.after(2000, self.roof_vogel)

    def roof_vogel(self):
        mixer.init()
        mixer.music.load('Havik.mp3')
        mixer.music.play()



if __name__ == '__main__':
    Window()