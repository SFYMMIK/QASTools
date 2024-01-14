import tkinter as tk
from time import strftime, gmtime

class QASDW24H(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Digital Watch (24-hour)")
        self.master.attributes("-topmost", True)  # Keep the window on top
        self.pack()
        self.create_widgets()
        self.update_time()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=200, height=60, bg='black')
        self.canvas.pack()

        # Create seven segments for hours and minutes
        self.segments = []
        for i in range(4):
            segment = self.canvas.create_text(i * 40 + 20, 30, text='', font=('Courier', 20), fill='red')
            self.segments.append(segment)

        # Update time every second
        self.after(1000, self.update_time)

    def display_time(self, current_time):
        for i in range(4):
            self.canvas.itemconfig(self.segments[i], text=current_time[i])

    def update_time(self):
        current_time = strftime("%H:%M:%S", gmtime())
        self.display_time(current_time)
        self.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x60+800+500")  # Set the initial position
    app = QASDW24H(master=root)
    app.mainloop()
