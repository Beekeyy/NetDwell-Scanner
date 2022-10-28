from tkinter import *
from tkinter import ttk
#from vulnerability_scanner import *

def link_input():
    target_url = str(ent.get())

window = Tk()
window.title('Vulnerability Scanner by Network Dwellers')
window.geometry('960x540')
window.resizable(False, False)

mainmenu = Menu(window)
window.config(menu = mainmenu)

mainmenu.add_command(label = 'Справка')

#Label(text = 'Enter scanning link:').place(x = 20, y = 50)

c = Canvas(window, width = 960, height = 540, bg = 'grey')
c.pack()

c.create_rectangle(10, 10, 950, 530, fill = 'lightgrey')

c.create_line(9, 60, 951, 60, fill = 'black', width = 2)
c.create_line(9, 9, 951, 9, fill = 'black', width = 2)
c.create_line(137, 9, 137, 59, fill = 'black', width = 2)
c.create_line(265, 9, 265, 59, fill = 'black', width = 2)
c.create_line(823, 9, 823, 59, fill = 'black', width = 2)
c.create_line(9, 8, 9, 531, fill = 'black', width = 2)
c.create_line(951, 8, 951, 531, fill = 'black', width = 2)
c.create_line(8, 529, 951, 529, fill = 'black', width = 2)

ent = Entry()
ent.place(x = 266, y = 11, width = 556, height = 48)

btn = Button(text = 'Start scanning', command = link_input)
btn.place(x = 139, y = 11, width = 125, height = 48)

stat_btn = Button(text = 'Statistics')
stat_btn.place(x = 825, y = 11, width = 125, height = 48)

cbox = ttk.Combobox(state = 'readonly', values = ['Select vulnerability', 'XSS-vulnerability', 'SQL injection', 'PHP injection'])
cbox.place(x = 11, y = 11, width = 124, height = 48)
cbox.current('0')

window.mainloop()