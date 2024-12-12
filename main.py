from tkinter import*
import tkinter as tk
from tkinter import messagebox, simpledialog
import pygame


ventana=tk.Tk()
ventana.title("Que vas a jugar hoy?")

ventana.iconbitmap("Imagenes.ico/4854246.ico")
barra_menu= tk.Menu(ventana)
ventana.config(menu=barra_menu)

def acerca_de():
    messagebox.showinfo("Acerca de","Desarrollado por Martin Romero")

def juegos():
    file=open(r"C:\Users\gjm30\OneDrive\Documentos\ProyectoFinal\Juegos.txt","r")
    file.readlines()
    file.closed()

def Agregarjuego():
    file=open(r"C:\Users\gjm30\OneDrive\Documentos\ProyectoFinal\Juegos.txt","w")
    file.write()
    file.closed()

menu_juegos=tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="lista de Juegos", menu=menu_juegos)
menu_juegos.add_command(label="Juegos", command=juegos)


menu_ayuda=tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Info", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)













from pygame import mixer
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("musica.mp3\【GhostFinal】One Hit Kill 「Girls_ Frontline 2_ Exilium」【ドールズフロントライン2_エクシリウム】Official(MP3_160K).mp3")
pygame.mixer.music.play(-1)
 
































ventana.mainloop()



