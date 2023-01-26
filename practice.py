

def temax_scale():

 global temax_value
 temax_value = str(temp_max.get())

def temin_scale():

 global temin_value
 temin_value = str(temp_min.get())

def humax_scale():

  global humax_value
  humax_value = str(humi_max.get())

def humin_scale():

  global humin_value
  humin_value = str(humi_min.get())

def btn_cmd():
    temax_scale()
    temin_scale()
    humax_scale()
    humin_scale()
    print("최고온도" + temax_value,
    "최저온도" + temin_value,
    "최고습도" +humax_value,
    "최저습도" +humin_value)



import tkinter as tk
from tkinter import *
temp = tk.Tk()
temp.title("온습도 측정기")
temp.geometry("600x500")

l1 = Label(temp, text="전송 시간 간격")
l2 = Label(temp, text="온도설정  ")
l3 = Label(temp, text ="MAX")
l4 = Label(temp, text ="MIN")
l5 = Label(temp, text="습도설정")
l6 = Label(temp, text ="MAX")
l7 = Label(temp, text ="MIN")

l1.grid(row = 0 , column=0)
l2.grid(row=0, column=3)
l3.grid(row=1, column=3)
l4.grid(row=3, column=3)
l5.grid(row=0, column=4)
l6.grid(row=1, column=4)
l7.grid(row=3, column=4)


temp_max = Scale(temp, from_=-15, to=50)
temp_max.grid(row=2,column=3)
temp_min = Scale(temp, from_=-20, to=45)
temp_min.grid(row=4,column=3)

humi_max = Scale(temp, from_=0, to=100)
humi_max.grid(row=2,column=4)
humi_min = Scale(temp, from_=0, to=100)
humi_min.grid(row=4,column=4)
hour_var =tk.IntVar()
button_hour1 = tk.Radiobutton(temp, text="5분", value=1,
variable=hour_var)
button_hour1.grid(row=1, column=0)
button_hour2 = tk.Radiobutton(temp, text="10분", value=2,
variable=hour_var)
button_hour2.grid(row=2, column=0)
button_hour3 = tk.Radiobutton(temp, text="1시간", value=3,
variable=hour_var)
button_hour3.grid(row=3, column=0)





btn =Button(temp, text ="데이터 전송",command=btn_cmd)

btn.grid(row =4, column=2)
temp.mainloop()

