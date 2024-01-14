import os
import tkinter as tk
from tkinter import filedialog
import pygame
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3
import random

class QASMusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("QASMusic Player")
        self.master.geometry("750x400")
        self.master.configure(bg="#000")  # Set overall background color to black

        self.playlist = []
        self.current_song = 0
        self.paused = False
        self.random_mode = False

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create GUI components
        self.create_gui()

    def create_gui(self):
        # Song listbox
        self.song_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, width=60, height=15, bg="#222", fg="#32CD32")
        self.song_listbox.pack(pady=10)

        # Song information display
        self.song_info_label = tk.Label(self.master, text="", bg="#000", fg="#32CD32")
        self.song_info_label.pack()

        # Next song label
        self.next_song_label = tk.Label(self.master, text="Next Song: None", bg="#000", fg="#32CD32")
        self.next_song_label.pack()

        # Buttons
        button_color = "#000"  # Change button color to black
        text_color = "#00FF00"  # Lime green text color
        self.play_button = tk.Button(self.master, text="Play", command=self.play_music, bg=button_color, fg=text_color)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_music, bg=button_color, fg=text_color)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music, bg=button_color, fg=text_color)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_music, bg=button_color, fg=text_color)
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.unpause_button = tk.Button(self.master, text="Unpause", command=self.unpause_music, bg=button_color, fg=text_color)
        self.unpause_button.pack(side=tk.LEFT, padx=10)

        self.prev_button = tk.Button(self.master, text="Previous", command=self.prev_music, bg=button_color, fg=text_color)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.random_button = tk.Button(self.master, text="Toggle Random", command=self.toggle_random, bg=button_color, fg=text_color)
        self.random_button.pack(side=tk.RIGHT, padx=10)

        self.add_button = tk.Button(self.master, text="Open Folder", command=self.open_folder, bg=button_color, fg=text_color)
        self.add_button.pack(side=tk.RIGHT, padx=10)

    def open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = self.get_supported_files(folder_path)
            self.current_song = 0
            self.update_listbox()
            self.update_song_info()

    def get_supported_files(self, folder_path):
        supported_extensions = (".mp3", ".flac", ".wav", ".wma")
        files = []
        for root, dirs, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.lower().endswith(supported_extensions):
                    files.append(os.path.join(root, filename))
        return files

    def play_music(self):
        if not self.playlist:
            return

        if pygame.mixer.music.get_busy():
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.stop()
                self.current_song = self.choose_next_song()
                self.play_music()
        else:
            file_path = self.playlist[self.current_song]
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.update_song_info()
            self.update_next_song_label()

    def choose_next_song(self):
        if self.random_mode:
            return random.randint(0, len(self.playlist) - 1)
        else:
            return (self.current_song + 1) % len(self.playlist)

    def pause_music(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_music(self):
        if not self.playlist:
            return

        self.current_song = self.choose_next_song()
        self.play_music()

    def unpause_music(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def prev_music(self):
        if not self.playlist:
            return

        # Go back two songs to effectively play the previous song
        self.current_song = (self.current_song - 2) % len(self.playlist)
        self.play_music()

    def toggle_random(self):
        self.random_mode = not self.random_mode
        mode = "ON" if self.random_mode else "OFF"
        self.random_button.config(text=f"Random Mode: {mode}")

    def update_listbox(self):
        self.song_listbox.delete(0, tk.END)
        for song in self.playlist:
            self.song_listbox.insert(tk.END, os.path.basename(song))

    def update_song_info(self):
        if not self.playlist:
            return

        file_path = self.playlist[self.current_song]
        audio = None

        if file_path.lower().endswith(".mp3"):
            audio = ID3(file_path)
        elif file_path.lower().endswith((".flac", ".wav", ".wma")):
            audio = FLAC(file_path)

        title = audio.get("title", [None])[0] or os.path.basename(file_path)
        author = audio.get("artist", [None])[0] or "Unknown Artist"

        self.song_info_label.config(text=f"Now Playing: {title} - {author}")

    def update_next_song_label(self):
        if not self.playlist:
            return

        next_song = self.choose_next_song()
        next_song_title = os.path.basename(self.playlist[next_song])
        self.next_song_label.config(text=f"Next Song: {next_song_title}")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#000")  # Set overall background color to black
    app = QASMusicPlayer(root)
    root.mainloop()
