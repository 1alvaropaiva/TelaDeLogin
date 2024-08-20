from tkinter import *

root = Tk ()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
    def tela(self):
        self.root.title("Alvaro")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=700, height=500)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd= 4, bg='red', highlightbackground='white', highlightthickness=2)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='red', highlightbackground='white', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

Application()
