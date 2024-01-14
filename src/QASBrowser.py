import tkinter as tk
import webbrowser

def open_browser():
    query = entry.get()

    if query.startswith(('http://', 'https://')):
        # Remove 'www.' if present in the URL
        query = query.replace('www.', '')
        webbrowser.open(query)
    else:
        search_url = f'https://search.brave.com/search?q={query}'
        webbrowser.open(search_url)

# Create the main window
window = tk.Tk()
window.title("QASBrowser")
window.configure(bg="black")  # Set the background color to black

# Create and pack GUI elements with lime green text
label = tk.Label(window, text="Enter URL starting with https:// or http:// or search query:", fg="lime green", bg="black")
label.pack(pady=10)

entry = tk.Entry(window, width=50, bg="black", fg="lime green", insertbackground="lime green")
entry.pack(pady=10)

button = tk.Button(window, text="Search", command=open_browser, fg="lime green", bg="black", activebackground="black", activeforeground="lime green")
button.pack(pady=10)

# Start the GUI main loop
window.mainloop()
