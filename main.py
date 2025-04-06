import tkinter

window = tkinter.Tk()
text = tkinter.Label(text="this button does nothing", anchor='center')
text.place(relx=0.5, rely=0.1)
button = tkinter.Button(text="press me!", anchor='center')
button.place(relx=0.5, rely=0.5)

tkinter.mainloop()
