
def start():
    form1.withdraw()       # This hides the start menu window


    def matriz():
        global matrizJue            # This function creates the matriz using the value that the user selects about what size of the matriz he wants.
        global matrizlog            # Also, this function fill the matriz with zeros that represents empty boxes,then, taking the values of quantity of cubes, it
                                                       # fills the matriz with the numbers 1 ,2 ,3.
        matrizJue = []               # The numbers represents each kind of cube
        matrizlog = []

        for y in range(len(matrizJue)):
                for x in range(len(matrizJue)):
                    obj = Label(inter, text = " ", image = fondo)        # This is the function that creates the graphic part
                    matrizJue[y][x] = obj                                # Filling that matriJue with the image "fondo" and using grid to ordenate them
                    matrizJue[y][x].grid(column = x, row = y)
                matrizJue[0][0].config(image=hormiga1)
                matrizJue[road.size-1][road.size-1].config(image=hormiguero)


