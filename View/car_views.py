from tkinter import *
import tkinter.ttk as ttk
import  tkinter.messagebox as msg
from Tools.validation import *
from Data_access.database_manager import  save_cars

def save_click():
       try :
              validate_name(name.get())
              validate_model(model.get())
              validate_plate(plate.get())
              save_cars(name.get(),model.get(),plate.get(),color.get())
              msg.showinfo("Save", "Person saved")
       except Exception as e :
              msg.showerror("Error", f"{e}")


window = Tk()
window.title("Parking")
window.geometry("500x400")

# Car Name
name = StringVar()
Label(window, text="Car Name", font = 30 ).place(x=20, y=40)
Entry(window, width = 20, textvariable =name).place(x=120, y=40)
# Model
model = StringVar()
Label(window, text="Model", font = 30 ).place(x=20, y=80)
Entry(window, width = 20, textvariable = model).place(x=120, y=80)
# Plate
plate = StringVar()
Label(window, text="Plate", font = 30 ).place(x=20, y=120)
Entry(window, width = 20, textvariable = plate).place(x=120, y=120)
# Color
color = StringVar(value = "white")
Label(window, text="Color", font = 30 ).place(x=20, y=160)
ttk.Combobox(window ,values=["white","black", "red"] , state = "readonly" ,
             textvariable=color , width=11 , font = 10).place(x = 120, y = 160)

Button(window, text="Save Car", width=15, command=save_click).place(x=70, y=240)

window.mainloop ()
