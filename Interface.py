__author__ = 'Dylana'

from tkinter import *

from Funciones import*


form1 = Tk()
form1.geometry("688x398")  # Size of the Window
form1.title("Battleship")  # Title of thee Window
form1.resizable(0, 0)  # Disables Minimize and Maximize

# ################################# Imagenes used in The start menu ######################################################

imagenfondo = PhotoImage(file="battle-ships-menu.gif")

labelfondo = Label(form1, image=imagenfondo).place(x=0, y=0)  #  Label that puts the image in the start menu
#########################################################################################################################

label1 = Label(form1, text="1-Jugador vs Computador:", fg="black", bg="white").place(x=250, y=180)
label2 = Label(form1, text="2-Multijugador:", fg="black", bg="white").place(x=250, y=215)
label3 = Label(form1, text="Cantidad de barcos:", fg="black", bg="white").place(x=250, y=250)
label4 = Label(form1, text="Profundidad:", fg="black", bg="white").place(x=250,
                                                                         y=285)  # Labels to indicate where to put the nickname,cubes, and select the size of the matriz
label5 = Label(form1, text="Estadisticas:", fg="black", bg="white").place(x=250, y=320)

############################### TEXTBOX   ############################################################################################################

#entryTxt1 = StringVar() #### NICKNAME
#entryTxt1.set(nick)
txtbox1 = Entry(form1, textvariable="", bd=2).place(x=410, y=180)  # Entry txtbox that receives the nickname of the user

#entryTxt1 = StringVar() #### NICKNAME
#entryTxt1.set(nick)
txtbox2 = Entry(form1, textvariable="", bd=2).place(x=350, y=215)

#entryTxt1 = StringVar() #### NICKNAME
#entryTxt1.set(nick)
txtbox3 = Entry(form1, textvariable="", bd=2).place(x=500, y=215)

#entryTxt1 = StringVar() #### NICKNAME
#entryTxt1.set(nick)
txtbox4 = Entry(form1, textvariable="", bd=2).place(x=370, y=250)

#########################################################################################################################

rdBFacil = Radiobutton(form1, text="7x7", value=1).place(x=400, y=285)
rdBMedio = Radiobutton(form1, text="10x10", value=2).place(x=470, y=285)
rdBDificil = Radiobutton(form1, text="13x13", value=3).place(x=550, y=285)

#########################################################################################################################

btnStart = Button(form1, text="START", command=lambda: start(), font=("Agency FB", 16), height=1, width=10).place(x=10,
                                                                                                                  y=350)
btnExit = Button(form1, text="EXIT", command=lambda: exit1(form1), font=("Agency FB", 16), height=1, width=10).place(
    x=600, y=350)
#btnReset = Button(form1,text = "RESET",state=DISABLED,command = lambda : exit1(form2), font = ("Agency FB",16), height = 1, width = 10).place(x = 500, y = 350)


#########################################################################################################################
def start():

    form1.withdraw()       # This hides the start menu window

    def matriz():
        global matrizJue            # This function creates the matriz using the value that the user selects about what size of the matriz he wants.
        global matrizlog            # Also, this function fill the matriz with zeros that represents empty boxes,then, taking the values of quantity of cubes, it
                                                       # fills the matriz with the numbers 1 ,2 ,3.
        matrizJue = []               # The numbers represents each kind of cube
        matrizlog = []

        for i in range(road.size):
                    matrizJue.append([0]*road.size)             # Number 0 Represents the Empty Boxes
                    matrizlog.append([0]*road.size)

        for y in range(len(matrizJue)):
                for x in range(len(matrizJue)):
                    obj = Label(inter, text = " ", image = fondo)        # This is the function that creates the graphic part
                    matrizJue[y][x] = obj                                # Filling that matriJue with the image "fondo" and using grid to ordenate them
                    matrizJue[y][x].grid(column = x, row = y)
                matrizJue[0][0].config(image=hormiga1)
                matrizJue[road.size-1][road.size-1].config(image=hormiguero)



#########################################################################################################################

def exit1(principal):
    principal.withdraw() #     <----- HIDE THE FIRST WINDOW
    ws.PlaySound("SystemExit", ws.SND_ALIAS)




form1.mainloop()