'''
from tkinter import *
import tkinter as tk

# user defined functions
def gradient_background(frame, color1, color2):
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

def gradient_background1(frame, color1, color2):
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

    # Dropdown menu and other widgets
    container = tk.Frame(canvas, bg="", highlightthickness=1, highlightbackground="black")
    container.place(relx=0, rely=0.3, width=300, height=325)

    label = tk.Label(container, text="The Needle\nGale Database\nResearch Tool:",
                     font=("Arial", 14, "bold underline"), wraplength=200, bg="#808080", anchor=tk.CENTER)
    label.place(relx=0.5, y=50, anchor="n")

    text_field = tk.Entry(canvas, font=("Arial", 14), width=30)
    text_field.insert(0, "Enter your URL name")
    text_field.config(fg="#C0C0C0", justify=tk.CENTER)

    def clear_hint(event):
        text_field.delete(0, tk.END)
        text_field.config(fg="#000000")

    def add_hint():
        if text_field.get() == "":
            text_field.insert(0, "Enter your URL name")
            text_field.config(fg="#C0C0C0", justify=tk.CENTER)

    text_field.bind("<FocusIn>", clear_hint)
    text_field.bind("<FocusOut>", add_hint)
    text_field.place(relx=0.49, y=450, anchor="center", width=250)

    button = tk.Button(frame, text="Analyze", font=("Arial", 14, 'bold'), fg="white", bg="green", command=your_function(frame))
    button.place(relx=0.5, y=550, anchor="s")

def your_function(root):
    print("Analyzing URL...")
    root.destroy()
    root.quit()

    

# Helper function to interpolate between two colors
def interpolate_color(color1, color2, factor):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return rgb_to_hex(r, g, b)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def get_url():
    root = Tk()
    root.title("Political Bias Analyzer")
    window_width = 800
    window_height = 500
    root.wm_resizable(0, 0)
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.destroy())
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    frame1_width = int(screen_width * 0.4)
    frame2_width = int(screen_width * 0.2)
    frame3_width = int(screen_width * 0.4)

    frame1 = tk.Frame(root, width=frame1_width, height=screen_height, bd=0, highlightthickness=0, bg="red")
    frame2 = tk.Frame(root, width=frame2_width, height=screen_height, bd=0, highlightthickness=0, bg="grey")
    frame3 = tk.Frame(root, width=frame3_width, height=screen_height, bd=0, highlightthickness=0, bg="blue")

    frame1.pack(side="left", fill="y", padx=0, pady=0)
    frame2.pack(side="left", fill="y", padx=0, pady=0)
    frame3.pack(side="left", fill="y", padx=0, pady=0)

    frame1.after(100, lambda: gradient_background(frame1, "#0000ff", "#808080"))
    frame2.after(100, lambda: gradient_background1(frame2, "#808080", "#808080"))
    frame3.after(100, lambda: gradient_background(frame3, "#808080", "#ff0000"))
    url_entry = StringVar()

    def on_submit():
        root.quit()
        root.destroy()

    Label(root, text="Enter URL:").pack()
    Entry(root, textvariable=url_entry).pack()
    Button(root, text="Submit", command=on_submit).pack()
    root.mainloop()

    return url_entry.get()  # Return the URL entered by the user

# This allows the function to be called directly if needed.
if __name__ == "__main__":
    print(get_url())
   '''
'''
from tkinter import *
import tkinter as tk

# Helper function to interpolate between two colors
def interpolate_color(color1, color2, factor):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return rgb_to_hex(r, g, b)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def gradient_background(frame, color1, color2):
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

def gradient_background1(frame, color1, color2):
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

    # Dropdown menu and other widgets
    container = tk.Frame(canvas, bg="", highlightthickness=1, highlightbackground="black")
    container.place(relx=0, rely=0.3, width=300, height=325)

    label = tk.Label(container, text="The Needle\nGale Database\nResearch Tool:",
                     font=("Arial", 14, "bold underline"), wraplength=200, bg="#808080", anchor=tk.CENTER)
    label.place(relx=0.5, y=50, anchor="n")

    text_field = tk.Entry(canvas, font=("Arial", 14), width=30)
    text_field.insert(0, "Enter your URL name")
    text_field.config(fg="#C0C0C0", justify=tk.CENTER)

    def clear_hint(event):
        text_field.delete(0, tk.END)
        text_field.config(fg="#000000")

    def add_hint():
        if text_field.get() == "":
            text_field.insert(0, "Enter your URL name")
            text_field.config(fg="#C0C0C0", justify=tk.CENTER)

    text_field.bind("<FocusIn>", clear_hint)
    text_field.bind("<FocusOut>", add_hint)
    text_field.place(relx=0.49, y=450, anchor="center", width=250)

    button = tk.Button(frame, text="Analyze", font=("Arial", 14, 'bold'), fg="white", bg="green", command=lambda: your_function(frame))
    button.place(relx=0.5, y=550, anchor="s")

def your_function(root):
    print("Analyzing URL...")
    # root.quit()  # Close the window
    root.destroy()  # Properly destroy the window

def get_url():
    # Ensure this function is only called once, not after "Analyze"
    root = Tk()
    root.title("Political Bias Analyzer")
    window_width = 800
    window_height = 500
    root.wm_resizable(0, 0)
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda event: root.destroy())
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    frame1_width = int(screen_width * 0.4)
    frame2_width = int(screen_width * 0.2)
    frame3_width = int(screen_width * 0.4)

    frame1 = tk.Frame(root, width=frame1_width, height=screen_height, bd=0, highlightthickness=0, bg="red")
    frame2 = tk.Frame(root, width=frame2_width, height=screen_height, bd=0, highlightthickness=0, bg="grey")
    frame3 = tk.Frame(root, width=frame3_width, height=screen_height, bd=0, highlightthickness=0, bg="blue")

    frame1.pack(side="left", fill="y", padx=0, pady=0)
    frame2.pack(side="left", fill="y", padx=0, pady=0)
    frame3.pack(side="left", fill="y", padx=0, pady=0)

    frame1.after(100, lambda: gradient_background(frame1, "#0000ff", "#808080"))
    frame2.after(100, lambda: gradient_background1(frame2, "#808080", "#808080"))
    frame3.after(100, lambda: gradient_background(frame3, "#808080", "#ff0000"))
    url_entry = StringVar()

    def on_submit():
        # root.quit()  # Quit the window after submission
        root.destroy()  # Destroy the root window properly

    Label(root, text="Enter URL:").pack()
    Entry(root, textvariable=url_entry).pack()
    Button(root, text="Submit", command=on_submit).pack()
    root.mainloop()

    return url_entry.get()  # Return the URL entered by the user


# This allows the function to be called directly if needed.
if __name__ == "__main__":
    print(get_url())  # This will print the URL entered by the user
    '''
'''
from tkinter import *
import tkinter as tk
def interpolate_color(color1, color2, factor):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return rgb_to_hex(r, g, b)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def get_url():
    root = Tk()  # Main root window
    root.title("Political Bias Analyzer")
    window_width = 800
    window_height = 500
    root.geometry(f'{window_width}x{window_height}')  # Explicit window size
    root.wm_resizable(0, 0)
    root.attributes('-fullscreen', False)  # Set fullscreen to False for now for testing

    # Create a label
    label = Label(root, text="Enter URL:", font=("Arial", 14))
    label.pack(pady=10)  # Added padding to make it visible

    # Entry field
    url_entry = StringVar()
    entry = Entry(root, textvariable=url_entry, font=("Arial", 14), width=40)
    entry.pack(pady=10)  # Added padding to ensure it’s visible

    # Function to handle the submit button and close window after submission
    def on_submit():
        entered_url = url_entry.get()
        if entered_url:
            print("Submitted URL:", entered_url)  # Print the URL to the console
            root.quit()  # This will stop the main loop and close the window
        else:
            print("No URL entered.")

    # Submit button
    submit_button = Button(root, text="Submit", command=on_submit, font=("Arial", 14, 'bold'), fg="white", bg="green")
    submit_button.pack(pady=20)  # Padding to make sure it's spaced out and visible

    # Run the window’s main loop
    root.mainloop()

    # After the window is closed, return the entered URL
    return url_entry.get()

# Call the function and see if it's working
if __name__ == "__main__":
    print(get_url()) 
    '''
import tkinter as tk
from tkinter import *

# Helper functions for color interpolationimport tkinter as tk
from tkinter import *

# Helper functions for color interpolation
def interpolate_color(color1, color2, factor):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return rgb_to_hex(r, g, b)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# Gradient background function for the frame
def gradient_background(frame, color1, color2):
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

# Function that runs after button click
def on_submit(url_entry, root):
    entered_url = url_entry.get()
    if entered_url:
        print("Submitted URL:", entered_url)  # Print the URL to the console
        root.quit()  # Close the window
    else:
        print("No URL entered.")

# Main function to set up the UI and handle URL input
def get_url():
    root = Tk()
    root.title("Political Bias Analyzer")
    window_width = 800
    window_height = 500
    root.geometry(f'{window_width}x{window_height}')  # Set window size
    root.wm_resizable(0, 0)  # Disable resizing
    root.attributes('-fullscreen', False)  # Disable fullscreen for better control

    # Set up gradient background for the entire window
    gradient_background(root, "#00bfff", "#4b0082")  # Blue to Indigo gradient
    
    # Create a container frame for the form (centered)
    container = tk.Frame(root, bg="white", bd=2, relief="solid", padx=20, pady=20)
    container.place(relx=0.5, rely=0.5, anchor="center")  # Center the container in the window
    
    # Label in the container
    label = tk.Label(container, text="Enter URL for Bias Analysis", font=("Arial", 16, "bold"), bg="white")
    label.pack(pady=10)  # Padding between label and input field

    # URL input field with hint text
    url_entry = StringVar()
    text_field = tk.Entry(container, font=("Arial", 14), textvariable=url_entry, width=30)
    text_field.insert(0, "Enter your URL here")
    text_field.config(fg="#C0C0C0", justify="center")
    
    def clear_hint(event):
        if text_field.get() == "Enter your URL here":
            text_field.delete(0, tk.END)
            text_field.config(fg="black")

    def restore_hint(event):
        if text_field.get() == "":
            text_field.insert(0, "Enter your URL here")
            text_field.config(fg="#C0C0C0")

    text_field.bind("<FocusIn>", clear_hint)
    text_field.bind("<FocusOut>", restore_hint)
    text_field.pack(pady=10)  # Padding between text field and button

    # Submit button
    submit_button = tk.Button(container, text="Submit", font=("Arial", 14, "bold"), fg="white", bg="green", 
                              command=lambda: on_submit(url_entry, root))
    submit_button.pack(pady=20)  # Padding between button and bottom of the container
    
    # Run the main loop
    root.mainloop()

    return url_entry.get()  # Return the URL entered by the user

# Call the function to test
if __name__ == "__main__":
    print(get_url()) 
