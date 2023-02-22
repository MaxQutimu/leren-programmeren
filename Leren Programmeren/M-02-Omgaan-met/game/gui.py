from tkinter import *
window = Tk()
window.geometry("1920x1080")
window.title("Slayer")

icon = PhotoImage(file='icon.png')


label = Label(window,text="Slayer",font=('Arial',40,'bold'))
lable.pack()

window.iconphoto(True,icon)


window.mainloop()

