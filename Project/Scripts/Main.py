from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import editor

# Creating TK Container
root = Tk()
# Passing Root to TextEditor Class
textEditor = editor.TextEditor(root)
# Root Window Looping
textEditor.root.mainloop()