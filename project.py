from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
import os

def play():
    text = myentry.get() 
    if text.strip():  
        tts = gTTS(text=text, lang='en') 
        tts.save("speech.mp3") 
        playsound("speech.mp3")  
        os.remove("speech.mp3")  
    else:
        messagebox.showwarning("Warning", "Please enter some text!")

def exit():
    root.destroy() 

def set():
    myentry.delete(0, END) 

root = Tk()
root.title("Text to Speech")  
root.geometry("300x200")

mylable1 = Label(root, text="Text to Speech").grid(row=0, column=1)
mylable2 = Label(root, text="Enter your text:").grid()
myentry = ttk.Entry(root)
myentry.grid(row=3, column=1, pady=10)

button1 = ttk.Button(root, text="Play", command=play)
button1.grid(row=4, column=0, pady=10)

button2 = Button(root, text="Exit", bg="red", command=exit)
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(root, text="Set", bg="blue", command=set)
button3.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
