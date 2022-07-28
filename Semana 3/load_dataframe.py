#Ejemplo para prototipar una UI con TKinter en Pyhton
#       1. Permitir seleccionar el csv al usuario desde el sistema de 
#          archivos
#       2. Cargar el dataframe
#       3. Graficar para las columnas de datos seleccionadas
#       
from ctypes import alignment
from tkinter import *
from tkinter import filedialog
from pandas import *
from matplotlib import *

new_df = DataFrame()
#Definición de la función para selección de archivo:
def select_file():
    global new_df
    my_filename = filedialog.askopenfilename(
                    initialdir="C:/Users/ASUS/Downloads",
                    title="Seleccione el CSV...",
                    filetypes=( ("DAT files","*.dat"), ("CSV Files","*.csv"), ("TXT files","*.txt")  )
    )  
    
    new_df = read_csv(my_filename, encoding="latin-1", sep=";")
    #print(new_df.info)
    
#Por definir: 
def plot_dataframe():
   
    print(new_df)

#mostrar la ventana:
if __name__ == "__main__":

    #Creación de la ventana
    my_window = Tk()
    my_window.title("DataFrame Test and Plot")
    my_window.geometry("800x600")

    top_frame = Frame(my_window)
    top_frame.pack(side="top")
    label_title = Label(top_frame,
                        text="Cargar y graficar dataframe",
                        
                        fg="red",
                        
    )

    middle_frame = Frame(my_window)
    middle_frame.pack(side="left")

    bottom_frame = Frame(my_window)
    bottom_frame.pack(side="bottom")

    
    button_selectfile = Button(
                            bottom_frame,
                            text="Abrir CSV...",
                            command=select_file
    )

    button_plot = Button(
                        bottom_frame,
                        text="Graficar Dataframe" ,
                        command=plot_dataframe
    )

    

    label_filename = Label(middle_frame, text="", fg="blue")
    label_info = Label(middle_frame, text="", fg="blue")

    #ubicar botones de acuerdo a la diagramación:
    button_selectfile.grid(column=1, row=2) #Ubicar en dos columnas

    button_plot.grid(column=2, row=2)
    label_title.grid(column=1, row=0)
    label_filename.grid(column=2, row=3, columnspan=3)

    
    print("Salida:"+new_df)

    my_window.mainloop()




