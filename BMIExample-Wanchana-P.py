from tkinter import *
import math

def calculate(event):
    print(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    lableResultShow.configure(text=result)
    if result >= 30 :
        lableBMICategoriseShow.configure(text="Very Obese")
    elif 25 <= result <= 29.9 :
        lableBMICategoriseShow.configure(text="Obese")
    elif 23 <= result <= 24.9 :
        lableBMICategoriseShow.configure(text="Over Weight")
    elif 18.6 <= result <= 22.9 :
        lableBMICategoriseShow.configure(text="Normal Weight")
    elif result < 18.5 :
        lableBMICategoriseShow.configure(text="Under Weight")

MainWindow = Tk()
lableHeight = Label(MainWindow,text="Heigth (cm.)")
lableHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
lableWeight = Label(MainWindow,text="Weight (Kg.)")
lableWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="Calculate")
calculateButton.bind("<Button-1>",calculate)
calculateButton.grid(row=4,column=0)
lableResult = Label(MainWindow,text="Result")
lableResult.grid(row=2,column=0)
lableResultShow = Label(MainWindow)
lableResultShow.grid(row=2,column=1)
lableBMICategories = Label(MainWindow,text="BMI Categorise")
lableBMICategories.grid(row=3,column=0)
lableBMICategoriseShow = Label(MainWindow)
lableBMICategoriseShow.grid(row=3,column=1)
MainWindow.mainloop()
