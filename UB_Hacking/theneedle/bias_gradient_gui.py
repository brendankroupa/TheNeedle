import tkinter as tk
from tkinter import messagebox

class BiasGradientGUI:
    def __init__(self, analyze_function):
        self.analyze_function = analyze_function  # Analysis function
        self.window = tk.Tk()
        self.window.title('Bias Summary')
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg="black")
        self.window.bind("<Escape>", lambda event: self.window.destroy())
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # URL input field
        self.url_entry = tk.Entry(self.window, width=50, font=("Helvetica", 20))
        self.url_entry.pack(pady=20)

        # Analyze button
        self.analyze_button = tk.Button(
            self.window, text="Analyze", command=self.analyze_url, font=("Helvetica", 20)
        )
        self.analyze_button.pack(pady=10)

        # Result label to display analysis outcome
        self.result_label = tk.Label(
            self.window, text="", font=("Helvetica", 24), fg="white", bg="black"
        )
        self.result_label.pack(pady=20)
        '''
    def analyze_url(self):
        """Retrieve the URL, run analysis, and display results."""
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Input Error", "Please enter a URL.")
            return
        
        bias_percentage = self.analyze_function(url)
        
        if bias_percentage is not None:
            self.run(bias_percentage)
        else:
            messagebox.showerror("Analysis Error", "Failed to analyze the URL.")
'''
    def analyze_url(self):
        """Retrieve the URL, run analysis, and display results."""
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Input Error", "Please enter a URL.")
            return
        
        # Call the analysis function
        result_text, bias_percentage = self.analyze_function(url)
        
        # Debugging: Check if the analysis function returns correct values
        print(f"Analysis Result: {result_text}, Bias Percentage: {bias_percentage}")
        
        if bias_percentage is not None:
            self.run(bias_percentage)
        else:
            messagebox.showerror("Analysis Error", "Failed to analyze the URL.")
    '''      
    def setup_frames(self, bias_percentage):
        right_percentage = 100 - bias_percentage
        frame1_width = int(self.screen_width * (bias_percentage / 100))
        frame3_width = self.screen_width - frame1_width

        frame1 = tk.Frame(self.window, width=frame1_width, height=self.screen_height, bd=0, highlightthickness=0)
        frame3 = tk.Frame(self.window, width=frame3_width, height=self.screen_height, bd=0, highlightthickness=0)

        frame1.pack(side="left", fill="y")
        frame3.pack(side="left", fill="y")

        self.apply_gradient(frame1, "#0000ff", "#808080")
        self.apply_gradient(frame3, "#808080", "#ff0000")

        self.add_labels(bias_percentage, right_percentage)
    '''
    def setup_frames(self, bias_percentage):
        # Right bias is the complement of the left bias
        right_percentage = 100 - bias_percentage
        
        # Calculate frame widths based on the screen width and bias percentages
        frame1_width = int(self.screen_width * (bias_percentage / 100))
        frame3_width = self.screen_width - frame1_width

        # Clear any previous frames
        for widget in self.window.winfo_children():
            widget.destroy()
            
        # Create frames for left and right bias
        frame1 = tk.Frame(self.window, width=frame1_width, height=self.screen_height, bd=0, highlightthickness=0)
        frame3 = tk.Frame(self.window, width=frame3_width, height=self.screen_height, bd=0, highlightthickness=0)

        frame1.pack(side="left", fill="y")
        frame3.pack(side="left", fill="y")

        # Apply gradients to frames
        self.apply_gradient(frame1, "#0000ff", "#808080")  # Left bias (blue)
        self.apply_gradient(frame3, "#808080", "#ff0000")  # Right bias (red)

        # Update labels to show bias
        self.add_labels(bias_percentage, right_percentage)


    def apply_gradient(self, frame, color1, color2):
        frame.update_idletasks()
        canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        num_steps = 100
        for i in range(num_steps):
            color = self.interpolate_color(color1, color2, i / num_steps)
            canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                    (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                    outline='', fill=color)

    def interpolate_color(self, color1, color2, factor):
        r1, g1, b1 = self.hex_to_rgb(color1)
        r2, g2, b2 = self.hex_to_rgb(color2)
        r = int(r1 + (r2 - r1) * factor)
        g = int(g1 + (g2 - g1) * factor)
        b = int(b1 + (b2 - b1) * factor)
        return self.rgb_to_hex(r, g, b)
    '''
    def add_labels(self, bias_percentage, right_percentage):
        label_frame = tk.Frame(self.window, bg='black')  
        label_frame.place(relx=0.5, rely=0.5, anchor="center")  

        left_label = tk.Label(
            label_frame, 
            text=f"{bias_percentage}% Left", 
            font=("Helvetica", 30, "bold"), 
            fg="white", 
            bg="black"
        )
        right_label = tk.Label(
            label_frame, 
            text=f"{right_percentage}% Right", 
            font=("Helvetica", 30, "bold"), 
            fg="white", 
            bg="black"
        )

        left_label.pack(side="left", padx=10)
        right_label.pack(side="left", padx=10)
    '''
    def add_labels(self, bias_percentage, right_percentage):
        label_frame = tk.Frame(self.window, bg='black')  
        label_frame.place(relx=0.5, rely=0.5, anchor="center")  

        left_label = tk.Label(
            label_frame, 
            text=f"{bias_percentage}% Left", 
            font=("Helvetica", 30, "bold"), 
            fg="white", 
            bg="black"
        )
        right_label = tk.Label(
            label_frame, 
            text=f"{right_percentage}% Right", 
            font=("Helvetica", 30, "bold"), 
            fg="white", 
            bg="black"
        )

        left_label.pack(side="left", padx=10)
        right_label.pack(side="left", padx=10)
    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    def run(self, bias_percentage):
        self.setup_frames(bias_percentage)
        self.window.mainloop()