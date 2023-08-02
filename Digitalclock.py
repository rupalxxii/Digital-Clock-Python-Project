from tkinter import *
import datetime

# print(datetime.datetime.now())
def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am_pm =time.strftime("%p")
    date = time.strftime("%d")
    month =time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")


    Hour.config(text=hr)
    Min.config(text=min)
    Sec.config(text=sec)
    AM_PM.config(text=am_pm)
    Date.config(text=date)
    Month.config(text=month)
    Year.config(text=year)
    Day.config(text=day)

    Hour.after(200,date_time)
    Date.after(200,date_time)




clock = Tk()
clock.title("Digital_Clock")
clock.geometry("550x300")
clock.config(bg="#003566")
Hour = Label(clock,text="00",font=("Arial",40,"bold"),bg = "#ffc300",fg="#000814")
Hour.place(x=50,y=20,height=50,width=100)
Hour_txt= Label(clock,text="Hour",font=("calibri",20,"bold"),bg="#ffc300",fg="#000814")
Hour_txt.place(x=50,y=90,height=30,width=100)

Min = Label(clock,text="00",font=("Arial",40,"bold"),bg = "#ffc300",fg="#000814")
Min.place(x=160,y=20,height=50,width=100)
Min_txt= Label(clock,text="Min",font=("calibri",20,"bold"),bg="#ffc300",fg="#000814")
Min_txt.place(x=160,y=90,height=30,width=100)

Sec = Label(clock,text="00",font=("Arial",40,"bold"),bg = "#ffc300",fg="#000814")
Sec.place(x=270,y=20,height=50,width=100)
Sec_txt= Label(clock,text="Sec",font=("calibri",20,"bold"),bg="#ffc300",fg="#000814")
Sec_txt.place(x=270,y=90,height=30,width=100)

AM_PM = Label(clock,text="00",font=("Arial",30,"bold"),bg = "#ffc300",fg="#000814")
AM_PM.place(x=380,y=20,height=50,width=100)
AM_PM_txt= Label(clock,text="AM/PM",font=("calibri",20,"bold"),bg="#ffc300",fg="#000814")
AM_PM_txt.place(x=380,y=90,height=30,width=100)


Date = Label(clock,text="00",font=("Arial",40,"bold"),bg = "#ffc300",fg="#000814")
Date.place(x=50,y=140,height=50,width=100)
Date_txt= Label(clock,text="Date",font=("calibri",20,"bold"),bg="#ffc300",fg="#000814")
Date_txt.place(x=50,y=210,height=30,width=100)

Month = Label(clock,text="00",font=("Arial",40,"bold"),bg = "#ffc300",fg="#000814")
Month.place(x=160,y=140,height=50,width=100)
Month_txt= Label(clock,text="Month",font=("calibri",20,"bold"),bg="#ffc300",fg="#000814")
Month_txt.place(x=160,y=210,height=30,width=100)


Year = Label(clock,text="00",font=("Arial",40,"bold"),bg = "#ffc300",fg="#000814")
Year .place(x=270,y=140,height=50,width=100)
Year_txt= Label(clock,text="Year",font=("calibri",20,"bold"),bg="#ffc300",fg="#000814")
Year_txt.place(x=270,y=210,height=30,width=100)


Day = Label(clock,text="00",font=("Arial",30,"bold"),bg = "#ffc300",fg="#000814")
Day.place(x=380,y=140,height=50,width=100)
Day_txt= Label(clock,text="Day",font=("calibri",20,"bold"),bg="#ffc300",fg="#000814")
Day_txt.place(x=380,y=210,height=30,width=100)



date_time()
clock.mainloop()