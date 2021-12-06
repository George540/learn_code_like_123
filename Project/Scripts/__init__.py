from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sys
sys.path.append('Project/Scripts/Editor')
import editor

def main():
    # Creating TK Container
    root = Tk()
    # Passing Root to TextEditor Class
    textEditor = editor.TextEditor(root)
    sentense = textEditor.current_sentence
    print(sentense)
    # Root Window Looping
    textEditor.root.mainloop()

if __name__ == "__main__":
    main()