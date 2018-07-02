'''
A POMODORO timer to maximize productivity! 25 minutes focus followed by 5 minutes rest.
Author: Kris Buote
'''
import time
import tkinter as tk
 
def pomodoro():
    
    lbl.config(bg='green')
    root.attributes('-topmost',1)
    root.focus_force()
    root.attributes('-topmost',0)
    for t in range(25*60, -1, -1):
        minute = str(t//60)
        second = str(t%60)
        lbl["text"] = "POMODORO FOCUS \n \n Time remaining: " + minute + "m " + second +"s"
        time.sleep(1)
        root.update()

    lbl.config(bg = 'cyan')
    root.attributes('-topmost',1)
    root.focus_force()
    root.attributes('-topmost',0)
    for t in range(5*60, -1 ,-1):
        minute = str(t//60)
        second = str(t%60)
        lbl["text"] = "Great job! Take a 5 minute break :) \n \n Time remaining: " + minute + "m " + second +"s"
        time.sleep(1)
        root.update()

root = tk.Tk()
label_font = ('helvetica', 40)
lbl = tk.Label(font=label_font)
lbl.pack(fill='both', expand=1)

lbl.config(bg='green')
lbl["text"] = "Welcome to the Pomodoro! \n \n Get ready to be productive!"
root.update()
time.sleep(3)

while True:
    pomodoro()

    
