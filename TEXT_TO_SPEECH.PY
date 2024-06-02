import tkinter as tk
from tkinter import ttk
import pyttsx3
from gtts import gTTS
import os

class TextToSpeechApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text-to-Speech Application")

        # Text input field
        self.text_label = ttk.Label(self, text="Enter Text:")
        self.text_label.grid(row=0, column=0, padx=10, pady=5)
        self.text_entry = ttk.Entry(self, width=50)
        self.text_entry.grid(row=0, column=1, padx=10, pady=5)

        # Language selection dropdown
        self.language_label = ttk.Label(self, text="Select Language:")
        self.language_label.grid(row=1, column=0, padx=10, pady=5)
        self.selected_language = tk.StringVar()
        self.language_dropdown = ttk.Combobox(self, width=20, textvariable=self.selected_language)
        self.language_dropdown['values'] = ['en', 'fr', 'es']  # Example languages: English, French, Spanish
        self.language_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Voice selection dropdown
        self.voice_label = ttk.Label(self, text="Select Voice:")
        self.voice_label.grid(row=2, column=0, padx=10, pady=5)
        self.selected_voice = tk.StringVar()
        self.voice_dropdown = ttk.Combobox(self, width=20, textvariable=self.selected_voice)
        self.voice_dropdown['values'] = ['Male', 'Female']  # Male and female voices
        self.voice_dropdown.grid(row=2, column=1, padx=10, pady=5)

        # Rate slider for adjusting speech rate
        self.rate_label = ttk.Label(self, text="Rate:")
        self.rate_label.grid(row=3, column=0, padx=10, pady=5)
        self.rate_slider = ttk.Scale(self, from_=50, to=200, length=200)
        self.rate_slider.set(100)  # Default rate
        self.rate_slider.grid(row=3, column=1, padx=10, pady=5)

        # Volume slider for adjusting speech volume
        self.volume_label = ttk.Label(self, text="Volume:")
        self.volume_label.grid(row=4, column=0, padx=10, pady=5)
        self.volume_slider = ttk.Scale(self, from_=0, to=1, length=200)
        self.volume_slider.set(1.0)  # Default volume
        self.volume_slider.grid(row=4, column=1, padx=10, pady=5)

        # Button to convert text to speech
        self.convert_button = ttk.Button(self, text="Convert", command=self.convert_text_to_speech)
        self.convert_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def convert_text_to_speech(self):
        text = self.text_entry.get()
        language = self.selected_language.get()
        voice = self.selected_voice.get()
        rate = self.rate_slider.get()
        volume = self.volume_slider.get()

        if text:
            if voice:
                engine = pyttsx3.init()
                engine.setProperty('rate', rate)
                engine.setProperty('volume', volume)
                if voice == 'Male':
                    voices = engine.getProperty('voices')
                    engine.setProperty('voice', voices[0].id)  # First male voice
                elif voice == 'Female':
                    voices = engine.getProperty('voices')
                    engine.setProperty('voice', voices[1].id)  # Second female voice
                engine.say(text)
                engine.runAndWait()
            else:
                tts = gTTS(text=text, lang=language)
                tts.save("output.mp3")
                os.system("start output.mp3")
        else:
            print("Error: Please enter text to convert.")

if __name__ == "__main__":
    app = TextToSpeechApp()
    app.mainloop()
