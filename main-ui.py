from tkinter.constants import LEFT
import wikipediaapi
import datetime
import tkinter

window = tkinter.Tk()
window.title("Wooh")

day_now = datetime.datetime.now().day
month_now = datetime.datetime.now().month

if month_now == 1:
    month = 'January'
if month_now == 2:
    month = 'February'
if month_now == 3:
    month = 'March'
if month_now == 4:
    month = 'April'
if month_now == 5:
    month = 'May'
if month_now == 6:
    month = 'June'
if month_now == 7:
    month = 'July'
if month_now == 8:
    month = 'August'
if month_now == 9:
    month = 'September'
if month_now == 10:
    month = 'October'
if month_now == 11:
    month = 'November'
if month_now == 12:
    month = 'December'


day_now = str(day_now)

title_page = str(month+'_'+day_now)

wikipedia = wikipediaapi.Wikipedia('en')
page = wikipedia.page(title_page)
h = page.section_by_title('Holidays and observances')
sm = page.summary[0:60]

tkinter.Label(window, text="Wooh").pack()
tkinter.Label(window, text=sm).pack()
tkinter.Label(window, text=h).pack()

window.mainloop()