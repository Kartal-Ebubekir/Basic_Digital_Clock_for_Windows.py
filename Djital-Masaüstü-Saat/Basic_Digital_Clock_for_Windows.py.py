from tkinter import Label,Tk
import time
def digital_clock():
  time_live = time.strftime("%H:%M:%S")
  clock_label.config(text=time_live)
  date_info = time.strftime("%d %B %Y")
  date_label.config(text=date_info)
  clock_label.after(200,digital_clock) # Her 200 milisaniyede bir yenileniyor.

window  = Tk()
window.iconbitmap("icon.ico")
window.title("Digital Clock for Windows")
window.geometry("250x100")
window.resizable(0,0) # Ekran boy ve genişliğinin değiştirilmemesi için
window.configure(bg="black")

# clock label
clock_label = Label(window,font="times 20",bg="black",fg="white")
clock_label.pack()

# calander label 
date_label = Label(window,font="times 20",bg="black",fg="white")
date_label.pack()

digital_clock()
window.mainloop()

