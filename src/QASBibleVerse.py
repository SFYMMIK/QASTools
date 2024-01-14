import requests
import tkinter as tk

class QASBible:
    def __init__(self, root):
        self.root = root
        self.root.title("QASBibleVerse")
        self.root.configure(bg="black")  # Set background color to black

        self.verse_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Arial", 12), fg="lime green", bg="black")
        self.verse_label.pack(pady=20)

        self.get_verse_button = tk.Button(root, text="Get Verse", command=self.get_daily_verse, fg="lime green", bg="black")
        self.get_verse_button.pack(pady=10)

    def get_daily_verse(self):
        try:
            verse_text = self.fetch_verse()
            self.verse_label.config(text=verse_text)
        except Exception as e:
            print(f"Error: {e}")
            self.verse_label.config(text="Failed to retrieve the verse. Please try again later.")

    def fetch_verse(self):
        # labs.bible.org endpoint for the "Verse of the Day"
        url = "https://labs.bible.org/api/?passage=random&type=json"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON response to get the verse text
            verse_data = response.json()
            verse_text = f"{verse_data[0]['bookname']} {verse_data[0]['chapter']}:{verse_data[0]['verse']} - {verse_data[0]['text']}"
            return verse_text
        else:
            raise Exception(f"Failed to fetch the verse. Status code: {response.status_code}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QASBible(root)
    root.mainloop()
