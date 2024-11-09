from tkinter import *
import os

# Window info
window=Tk()
window.title('App Title')
window_width = 800
window_height = 500
window.iconbitmap('C:\\Users\\shoem\\Desktop\\UB_Hacking\\pngStore\\favicon.ico')

#Window Controls
window.wm_resizable(0,0)
window.wm_overrideredirect(False)
window.wm_iconwindow()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")



# Boot GUI Startup 
window.mainloop()