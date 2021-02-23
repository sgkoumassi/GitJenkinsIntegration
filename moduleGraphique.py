#coding:utf-8

import tkinter


mainapp = tkinter.Tk()
mainapp.title("First python Ui")

check_widget = tkinter.Checkbutton(mainapp,text ="Publier")
radio_widget = tkinter.Radiobutton(mainapp,text ="Homme",value =1)
radio_widget2 = tkinter.Radiobutton(mainapp,text ="Femme",value=2)

check_widget.pack()
radio_widget.pack()
radio_widget2.pack()
#mainapp.minsize(640,480)
#mainapp.maxsize(1280,720)

#mainapp.sizefrom("user")
#mainapp.resizable(width=True, height=False)

#geometry("XxY+O+0")

# Centrer la fenetre 
screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
window_x = 800
window_y = 600
posX = (screen_x // 2) - (window_x //2)
posY = (screen_y // 2) - (window_y // 2)
geo ="{}x{}+{}+{}".format(window_x,window_y,posX,posY)

mainapp.geometry(geo)

mainapp.mainloop()