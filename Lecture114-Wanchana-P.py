####โปรแกรมเช็คผลกำไรขาดทุนย้อนหลัง โดยคิดเป็น % (API ใหม่มีปัญหาในการดึงข้อมูลแบบวันที่ ไม่สามารถดึงข้อมูลบางวันได้)####
from datetime import date
from currency_converter import CurrencyConverter
from tkinter import *

"""" กำหนดตัวแปร """
c = CurrencyConverter()
input_day = 0 #วันที่ผู้ใช้งานต้องการเช็ค
input_month = 0 #เดือนที่ผู้ใช้งานต้องการเช็ค
input_year = 0 #ปีที่ผู้ใช้งานต้องการเช็ค
input_investment = 0 #จำนวนเงินที่ผู้ใช้งานลงทุน

def Calculate(event):
    investment = c.convert(int(textbox_input_investment.get()), 'THB', 'EUR')
    price_now = c.convert(int(investment), 'EUR', 'USD')
    price_check = c.convert(investment, 'EUR', 'USD',
                            date=date(int(textbox_input_year.get()),
                                      int(textbox_input_month.get()),
                                      int(textbox_input_day.get())))
    delta_price = price_now - price_check
    if delta_price > 0:
        percent_profit = int((delta_price * 100) / investment)
        delta_price = int(c.convert(delta_price, 'USD', 'THB'))
        label_investment_results_show_percent.configure(text=("ผลการลงทุน","+", percent_profit,"%"),fg="GREEN")
        label_investment_results_show_delta.configure(text=(delta_price,"บาท"),fg="GREEN")
    elif delta_price < 0:
        percent_lost = int((delta_price * 100) / investment)
        delta_price = int(c.convert(delta_price, 'USD', 'THB'))
        label_investment_results_show_percent.configure(text=("ผลการลงทุน",percent_lost,"%"),fg="RED")
        label_investment_results_show_delta.configure(text=(delta_price,"บาท"),fg="RED")
    else:
        label_investment_results_show_percent.configure(text=("ผลการลงทุน", "+", "0.00 %","% "),fg="BULE")



""" GUI """
mainwindows = Tk()
mainwindows.geometry('350x150')
mainwindows.configure(bg = "PINK")
mainwindows.title("ผลกำไร การลงทุน")
####รับจำนวนเงินที่ลงทุน####
lable_input_investment = Label(mainwindows,text = "ใส่จำนวนเงินที่ลงทุน(บาท) = ")
lable_input_investment.grid(row=0,column=0)
lable_input_investment.configure(bg = "PINK")
textbox_input_investment = Entry(mainwindows)
textbox_input_investment.grid(row=0,column=1)
####รับวันที่####
lable_input_day = Label(mainwindows,text = "ใส่วันที่ใส่วันที่ต้องการเช็ค = ")
lable_input_day.grid(row=1,column=0)
lable_input_day.configure(bg = "PINK")
textbox_input_day = Entry(mainwindows)
textbox_input_day.grid(row=1,column=1)
####รับเดือน####
lable_input_month = Label(mainwindows,text="ใส่เดือนที่ต้องการเช็ค = ")
lable_input_month.grid(row=2,column=0)
lable_input_month.configure(bg = "PINK")
textbox_input_month = Entry(mainwindows)
textbox_input_month.grid(row=2,column=1)
####รับปี####
lable_input_year = Label(mainwindows,text="ใส่ปีที่ต้องการเช็ค = ")
lable_input_year.grid(row=3,column=0)
lable_input_year.configure(bg = "PINK")
textbox_input_year = Entry(mainwindows)
textbox_input_year.grid(row=3,column=1)
####หน้าแสดงผล####
lable_investment_results = Label(mainwindows,text="ผลการลงทุน % และ บาท")
lable_investment_results.grid(row=4,column=0)
lable_investment_results.configure(bg="PINK")
label_investment_results_show_percent = Label(mainwindows)
label_investment_results_show_percent.grid(row=4,column=1)
label_investment_results_show_percent.configure(bg="PINK")
label_investment_results_show_delta = Label(mainwindows)
label_investment_results_show_delta.grid(row=5,column=1)
label_investment_results_show_delta.configure(bg="PINK")

###ปุ่มคำนวณ###
button_calculate = Button(mainwindows,text="Calculate",fg="GREEN")
button_calculate.bind("<Button-1>",Calculate)
button_calculate.grid(row=5,column=0)

mainwindows.mainloop()

