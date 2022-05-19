#!/home/ben/projects/inning_pace/venv/bin/python

import tkinter as tk
from tkinter import messagebox
from pybaseball import standings

def main():
    nl = standings()[3:]
    
    gs = []
    for div in nl:
        div['g'] = div['W'].astype(int) + div['L'].astype(int)
        gs.append(div['g'].mean())

    pace = round(sum(gs)/len(gs) / 162.0 * 1500,2)
    print('Pace for 1500 innings: {}'.format(pace))

    root = tk.Tk(className='MyTkApp')
    root.withdraw()
    messagebox.showinfo('Inning Pace', str('Pace for 1500 innings: {}'.format(str(pace))))

if __name__== '__main__':
    main()
              
