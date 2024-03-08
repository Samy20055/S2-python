import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

root = tk.Tk() # on initialise la fenetre root 
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100 #c'est le max choisi en entrée - 100
y = CANVAS_HEIGHT / 2 #la ligne est centrée 
canvas.create_line(y,x0, y, x1)
canvas.create_oval( y - 50,x0 + 50, y + 50,x0 - 50 ) #on prend 50 car c'est la moitié de 100 (50 est le rayon du cercle)
canvas.create_oval(y - 50, x1 + 50, y + 50, x1 - 50)
canvas.create_oval(y + 50, (x0 + x1) / 2 - 50, y - 50, (x0 + x1) / 2 + 50)
    # Fin de votre code
#pack ca affiche
#grid ca affiche a une position precise  
canvas.grid() 
root.mainloop()