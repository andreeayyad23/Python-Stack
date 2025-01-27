# Import the necessary Tkinter modules
import tkinter as tk
from tkinter import messagebox

# Define a function to display the message when the button is clicked
def show_message():
    messagebox.showinfo("Birthday Message", "Happy Birthday Leen Congrats!")

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Birthday Greetings")

# Set the size of the window (optional)
root.geometry("300x200")

# Create a button widget
# The 'command' parameter links the button to the show_message function
button = tk.Button(root, text="Click Me!", command=show_message)

# Center the button in the window using the pack geometry manager
button.pack(expand=True)

# Run the main event loop to display the window
root.mainloop()