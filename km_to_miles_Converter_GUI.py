from Tkinter import *
import tkMessageBox


# create a window
window = Tk()


# give the window a title
window.title("km to miles converter")


# create a function for the km to miles button
def kmB_click():
    try:
        num = float(field.get())
        km_to_miles = float(field.get()) * 0.62
        tkMessageBox.showinfo("result", str(field.get()) + " km is " + str(km_to_miles) + " miles")
    except ValueError:
        return


# create a function for the miles to km button
def milesB_click():
    try:
        num = float(field.get())
        miles_to_km = float(field.get()) / 0.62
        tkMessageBox.showinfo("result", str(field.get()) + " miles is " + str(miles_to_km) + " km")
    except ValueError:
        return


# explain what the program does and put in the window
program_explanation = Label(window, text="This is a simple kilometers to miles converter.\nPut a number in the field and click a button for conversion.\n")
program_explanation.pack()


# create entry field and put it in the window
field = Entry(window)
field.pack()


# create a km to miles button and put it in the window
kmB = Button(window, text="km to miles", command=kmB_click)
kmB.pack()


# create a miles to km button and put it in the window
milesB = Button(window, text="miles to km", command=milesB_click)
milesB.pack()




# keep the window open
window.mainloop()