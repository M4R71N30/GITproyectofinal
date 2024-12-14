from tkinter import*
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import Image
import pygame
import webbrowser
from tkinter import PhotoImage


ventana=tk.Tk()
ventana.title("Que vas a jugar hoy?")
ventana.geometry("800x500")
ventana.config(bg="red")
ventana.iconbitmap("Imagenes.ico/4854246.ico")
barra_menu= tk.Menu(ventana)
ventana.config(menu=barra_menu)
imagen=PhotoImage(file=r"C:\Users\gjm30\OneDrive\Documentos\ProyectoFinal\Imagenes.png\Sin título.png")
fondo=Label(image=imagen).place(x=0,y=0)

def acerca_de():
    messagebox.showinfo("Acerca de","Desarrollado por Martin Romero")

def abrir_pagina1():
    webbrowser.open("https://vandal.elespanol.com")

def abrir_pagina2(): 
    webbrowser.open("https://www.metacritic.com/game/")

def abrir_pagina3():   
    webbrowser.open("https://howlongtobeat.com/?q=")

def mostrar_imagen():
    webbrowser.open(r"https://cdn.discordapp.com/attachments/1143918881866526851/1317374001068114021/depositphotos_607148484-stock-photo-woman-touching-fresh-grass-green.jpg?ex=675e73a5&is=675d2225&hm=522ade0d19703ceadc0a1d6859536d7da89b035d8bb705bfd4ea25445902f21f&")

def mostrar_lista():
    Lista.pack()

Lista = tk.Listbox(ventana)
Lista.insert(1, "God of war")
Lista.insert(2, "Call of duty")
Lista.insert(3, "Assasins creed")
Lista.insert(4,"Transfromers foc")
Lista.pack_forget()  

def agregar_elemento():
    nuevo_elemento = simpledialog.askstring("Nuevo juego", "Ingresa un nuevo juego:")
    
    if nuevo_elemento: 
        Lista.append(nuevo_elemento) 
        actualizar_lista()

    def actualizar_lista():
        Lista.delete(0, tk.END)
        for item in Lista: 
           Lista.insert(tk.END, item)


menu_ayuda=tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Info", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)


menu_url=tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Paginas de juegos", menu=menu_url)
menu_url.add_command(label="Vandal",command=abrir_pagina1)
menu_url.add_command(label="metacritic",command=abrir_pagina2)
menu_url.add_command(label="Cuanto dura...?",command=abrir_pagina3)

menu_imagen=tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Otro juego", menu=menu_imagen)
menu_imagen.add_command(label="tambien puedes jugar a",command=mostrar_imagen)

menu_lista=tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Lista de juegos", menu=menu_lista)
menu_lista.add_command(label="Juegos",command=mostrar_lista)

menu_opciones=tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones de juegos", menu=menu_opciones)
menu_opciones.add_command(label="Agregar",command=agregar_elemento)


from pygame import mixer
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("musica.mp3\【GhostFinal】One Hit Kill 「Girls_ Frontline 2_ Exilium」【ドールズフロントライン2_エクシリウム】Official(MP3_160K).mp3")
pygame.mixer.music.play(-1)
 
ventana.mainloop()



