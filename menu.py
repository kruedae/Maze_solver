import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import *
from tkvideo import tkvideo
import numpy as np
from astar import *
from uniforme import *
from anchura import *
from profundidad import *
from greedy import *

# create the root window
root = tk.Tk()
root.title('Bienvenido al laboratorio de IA')
Label(root,
          text ="Seleccione un laberinto a resolver",font=("Helvetica", 9)).pack()
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Abrir un archivo',
        initialdir='./',
        filetypes=filetypes)
    
    maze = np.genfromtxt(filename, delimiter=',', dtype=str)
    
    def play_video(algorithm, time, memory):
        newWindow2 = Toplevel(newWindow)
        my_label = Label(newWindow2)
        my_label.pack()
        player = tkvideo("./"+algorithm+"_result.mp4", my_label, loop = 0)
        player.play()
        Label(newWindow2,
          text ="Tiempo: "+str(time)+' segundos',font=("Helvetica", 9)).pack()
        Label(newWindow2,
          text ="Espacio: "+str(memory)+ ' MB',font=("Helvetica", 9)).pack()
    
    def charge_astar():
        time, memory = main_astar(maze)
        play_video('astar',time, memory)        

    def charge_uniforme():
        time, memory = main_uniform(maze)
        play_video('uniform',time, memory) 
    
    def charge_anchura():
        time, memory = main_anchura(maze)
        play_video('anchura',time, memory)

    def charge_profundidad():
        time, memory = main_profundidad(filename)
        play_video('profundidad',time, memory)

    def charge_greedy():
        time, memory = main_greedy(filename)
        play_video('greedy',time, memory)
    
    
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("300x300")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="Seleccione un solucionador").pack()
    b1 = Button(newWindow,text = "A*",command = charge_astar,activeforeground = "red",activebackground = "pink",pady=10)  
  
    b2 = Button(newWindow, text = "Búsqueda greedy",command = charge_greedy,activeforeground = "blue",activebackground = "pink",pady=10)  

    b3 = Button(newWindow, text = "Búsqueda de costo uniforme",command = charge_uniforme,activeforeground = "green",activebackground = "pink",pady = 10)  

    b4 = Button(newWindow, text = "Profundidad iterativa",activeforeground = "yellow",activebackground = "pink",pady = 10)
    
    b5 = Button(newWindow, text = "Anchura",command = charge_anchura,activeforeground = "yellow",activebackground = "pink",pady = 10)
    
    b6 = Button(newWindow, text = "Profundidad",command = charge_profundidad,activeforeground = "yellow",activebackground = "pink",pady = 10)

    b1.pack()  

    b2.pack()  

    b3.pack()  

    b4.pack()
    
    b5.pack()  

    b6.pack()
    


# open button
open_button = ttk.Button(
    root,
    text='Abrir un archivo',
    command=select_file
)

open_button.pack(expand=True)

# run the application
root.mainloop()
