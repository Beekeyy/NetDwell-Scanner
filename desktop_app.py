from tkinter import *
from tkinter import ttk
import scanner
import output
#from vulnerability_scanner import *

#==============================================
#scanner launching



window = Tk()
window.title('NetDwell Scanner')
window.geometry('960x540')
window.focus_set()
window.resizable(False, False)
#window.iconbitmap('C:/Users/stud/Downloads/wisetree.ico')

mainmenu = Menu(window)
window.config(menu = mainmenu)

mainmenu.add_command(label = 'Справка')

c = Canvas(window, width = 960, height = 540, bg = 'grey')
c.pack()

def selected(event):
    selection = cbox.get()
    if selection != 'Select vulnerability':
        scan_btn['state'] = 'normal'
        if selection == 'XSS-vulnerability':
            pass
        elif selection == 'SQL injection':
            pass
        else:
            pass
    else:
        scan_btn['state'] = 'disabled'

def scan_process():
    #http://localhost/dvwa/
    target_url = web_url 
    links_to_ignore = ["http://localhost/dvwa/logout.php"]
    print(target_url)
    data_dict = {"username": "admin", "password": "password", "Login": "Login"}

    vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
    vuln_scanner.session.post("http://localhost/dvwa/login.php", data = data_dict)

    vuln_scanner.crawl()
    vuln_scanner.run_scanner()


def handle_focus_in(_):
    ent.delete(0, END)
    ent.config(fg = 'black')

def scan_display():
    global web_url
    web_url = str(ent.get()) #defining link
    scan_process()
    global scan_window
    scan_window = Toplevel(window)
    scan_window.title('Scanning')
    scan_window.resizable(False, False)
    current_pos_x = window.geometry()[8:]
    current_pos_y = int(current_pos_x.rpartition('+')[2]) + 111
    current_pos_x = int(current_pos_x.rpartition('+')[0]) + 11
    scan_window.geometry('468x436' + '+' + str(current_pos_x) + '+' + str(current_pos_y))
    scan_window.attributes('-toolwindow', True)
    f = output.f
    res = Text(scan_window, state = 'disabled')
    #res = Label(scan_window, text = f)
    res.insert(1.0,f)
    res.place(x = 0, y = 0)
    scan_window.protocol('WM_DELETE_WINDOW', enabling_scan)
    stat_btn['state'] = 'normal'
    if 'normal' == scan_window.state():
        scan_btn['state'] = 'disabled'
        cbox['state'] = 'disabled'
        ent['state'] = 'disabled'

def stat_display():
    global stat_window
    stat_window = Toplevel(window)
    stat_window.title('Statistics')
    stat_window.resizable(False, False)
    current_pos_x = window.geometry()[8:]
    current_pos_y = int(current_pos_x.rpartition('+')[2]) + 111
    current_pos_x = int(current_pos_x.rpartition('+')[0]) + 481
    stat_window.geometry('468x436' + '+' + str(current_pos_x) + '+' + str(current_pos_y))
    stat_window.attributes('-toolwindow', True)
    stat_window.protocol('WM_DELETE_WINDOW', enabling_stat)
    if 'normal' == stat_window.state():
        stat_btn['state'] = 'disabled'

def enabling_stat():
    stat_btn['state'] = 'normal'
    stat_window.destroy()
def enabling_scan():
    scan_btn['state'] = 'normal'
    stat_btn['state'] = 'disabled'
    cbox['state'] = 'readonly'
    ent['state'] = 'normal'
    scan_window.destroy()
    try:
        stat_window.destroy()
    except:
        pass

def tracking(self):
    try:
        current_pos_x = window.geometry()[8:]
        current_pos_y = int(current_pos_x.rpartition('+')[2]) + 111
        current_pos_x = int(current_pos_x.rpartition('+')[0]) + 481
        stat_window.geometry('468x436' + '+' + str(current_pos_x) + '+' + str(current_pos_y))
    except:
        pass
    try:
        current_pos_x1 = window.geometry()[8:]
        current_pos_y1 = int(current_pos_x1.rpartition('+')[2]) + 111
        current_pos_x1 = int(current_pos_x1.rpartition('+')[0]) + 11
        scan_window.geometry('468x436' + '+' + str(current_pos_x1) + '+' + str(current_pos_y1))
        scan_window.lift()
    except:
        pass

c.create_rectangle(10, 10, 950, 530, fill = 'lightgrey')

c.create_line(9, 60, 951, 60, fill = 'black', width = 2)
c.create_line(9, 9, 951, 9, fill = 'black', width = 2)
c.create_line(147, 9, 147, 59, fill = 'black', width = 2)
c.create_line(686, 9, 686, 59, fill = 'black', width = 2)
c.create_line(823, 9, 823, 59, fill = 'black', width = 2)
c.create_line(9, 8, 9, 531, fill = 'black', width = 2)
c.create_line(951, 8, 951, 531, fill = 'black', width = 2)
c.create_line(8, 529, 951, 529, fill = 'black', width = 2)

ent = Entry(fg = 'grey')
ent.place(x = 148, y = 11, width = 536, height = 48,)
ent.insert(0, 'Enter scanning link...')
ent.bind('<FocusIn>', handle_focus_in)

scan_btn = Button(state = 'disabled', text = 'Start scanning', command = scan_display)
scan_btn.place(x = 688, y = 11, width = 135, height = 48)

stat_btn = Button(state = 'disabled', text = 'Statistics', command = stat_display)
stat_btn.place(x = 825, y = 11, width = 125, height = 48)

cbox = ttk.Combobox(state = 'readonly', values = ['Select vulnerability', 'XSS-vulnerability', 'SQL injection', 'PHP injection'])
cbox.place(x = 11, y = 11, width = 135, height = 48)
cbox.current('0')
cbox.bind('<<ComboboxSelected>>', selected)

window.bind('<Configure>', tracking)

window.mainloop()
