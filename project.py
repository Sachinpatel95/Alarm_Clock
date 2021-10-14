from playsound import playsound
from tkinter import *
from win10toast import ToastNotifier
import datetime
import time

def alarm(set_alarm):
    toast = ToastNotifier()
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("Alarm Clock")
            toast.show_toast("Alarm Clock",duration=1)
            playsound("alarm.mp3")

def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

root = Tk()
root.geometry("190x130")
info = Label(root,text = "(24) Hour   Min   Sec").place(x = 60, y=10)
set_time = Label(root,text = "Set Time",relief = "solid",font=("Cambria",10,"bold")).place(x=10,y=35)

# Entry Variables
hour = StringVar()
min = StringVar()
sec = StringVar()

# Entry Widget
hour_E = Entry(root,textvariable = hour,bg = "grey",width = 4).place(x=85,y=35)
min_E = Entry(root,textvariable = min,bg = "grey",width = 4).place(x=118,y=35)
sec_E = Entry(root,textvariable = sec,bg = "grey",width = 4).place(x=150,y=35)

submit = Button(root,text = "Set Alarm",width = 10,command = getvalue).place(x =60,y=70)

root.mainloop()