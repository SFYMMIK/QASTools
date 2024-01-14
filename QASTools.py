import tkinter as tk
from tkinter import messagebox
import subprocess

def open_window(title, script_name):
    script_path = os.path.join("src", script_name)
    new_window = tk.Toplevel(root)
    new_window.title(title)

    try:
        # Use subprocess.Popen instead of subprocess.run
        subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception as e:
        error_message = f"Failed to run the script: {script_path}\n\nError: {str(e)}"
        label = tk.Label(new_window, text=error_message)
        label.pack(padx=20, pady=20)

# Main window
root = tk.Tk()
root.title("QASTools")
root.configure(bg="black")  # Set background color to black

# Buttons
button1 = tk.Button(root, text="24-Hour Clock", command=lambda: open_window("", "QAS24hclock.py"), bg="lime green", fg="black")
button1.grid(row=0, column=0, pady=20, padx=20)

button2 = tk.Button(root, text="12-Hour Clock", command=lambda: open_window("", "QAS12hclock.py"), bg="lime green", fg="black")
button2.grid(row=1, column=0, pady=20, padx=20)

button3 = tk.Button(root, text="Calculator", command=lambda: open_window("", "QASCalculator.py"), bg="lime green", fg="black")
button3.grid(row=2, column=0, pady=20, padx=20)

button4 = tk.Button(root, text="Random Bible Verse", command=lambda: open_window("", "QASBibleVerse.py"), bg="lime green", fg="black")
button4.grid(row=0, column=1, pady=20, padx=10)

button5 = tk.Button(root, text="Music Player", command=lambda: open_window("", "QASMusicPlayer.py"), bg="lime green", fg="black")
button5.grid(row=1, column=1, pady=20, padx=10)

button6 = tk.Button(root, text="Quick Search Engine", command=lambda: open_window("", "QASBrowser.py"), bg="lime green", fg="black")
button6.grid(row=2, column=1, pady=20, padx=10)

# Run the application
root.mainloop()
