from tkinter import *
from tkinter import ttk
#from vulnerability_scanner import *

def link_input():
    target_url = str(ent.get())

window = Tk()
window.title('Vulnerability Scanner by Network Dwellers')
window.geometry('540x368')
window.resizable(False, False)

mainmenu = Menu(window)
window.config(menu = mainmenu)

mainmenu.add_command(label = 'Справка')

Label(text = 'Enter scanning link:').place(x = 20, y = 50)

ent = Entry()
ent.place(x = 130, y = 50)

btn = Button(text = 'Start scanning', command = link_input)
btn.place(x = 145, y = 75)

cbox = ttk.Combobox(state = 'readonly', values = ['XSS-vulnerability', 'SQL injection', 'PHP injection'])
cbox.place(x = 300, y = 50)
cbox.current(0)

window.mainloop()