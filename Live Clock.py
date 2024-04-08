import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_clock)  # Update time every 1000 milliseconds (1 second)

# Create the Tkinter window
root = tk.Tk()
root.title("Live Clock")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(padx=20, pady=20)

# Update the clock initially
update_clock()

# Run the Tkinter event loop
root.mainloop()
