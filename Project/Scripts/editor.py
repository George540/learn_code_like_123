# Importing Required libraries & Modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
# Defining TextEditor Class


class TextEditor:
    # Defining Constructor
    def __init__(self, root, inputSentense=""):
        # Assigning root
        self.root = root
        self.inputSentense = inputSentense

        self.windowWidth = 1200
        self.windowHeight = 800
        self.root.geometry(str(self.windowWidth)+'x'+str(self.windowHeight))

        # Title of the window
        self.root.title("Learning Coding like 1, 2, 3")
        # Initializing filename
        self.filename = None
        # Declaring Title variable
        self.title = StringVar()

        self.sentenceIndex = 0

        # --------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------

        # Set color and other properties
        self.titlebar = Label(self.root, textvariable=self.title, font=(
            "Roboto", 12, "bold"), background="#e9ecef")  # Creating Titlebar
        self.body = Frame(self.root, background="#fff")
        self.sentences = Frame(self.body, background="#e9ecef")
        self.results = Frame(self.body, background="#ced4da")
        self.sentenceInput = Frame(self.sentences, background="#ced4da")
        self.sentenceArea = Frame(self.sentences, background="#e9ecef")
        self.sentenceRun = Frame(self.sentences, background="#e9ecef")
        self.sentenceInputBox = Entry(self.sentenceInput, font=(
            "Roboto", 12), bg="#e9ecef", relief="flat")
        self.resultsHeading = Frame(
            self.results, background="#ced4da", height=40)

        self.resultsHeadingTextVariable = StringVar()
        self.resultsHeadingText = Label(
            self.resultsHeading, textvariable=self.resultsHeadingTextVariable, font=(
                "Roboto", 12, "bold"), anchor="w", background="#ced4da", fg="#7A7A7A")
        self.resultsHeadingTextVariable.set("Results")
        self.resultOutputs = Frame(self.results, background="#ced4da")

        # Creating Scrollbar for sentence area
        self.sentenceScrollbar = Scrollbar(
            self.sentenceArea, orient=VERTICAL)
        self.sentenceAreaBox = Listbox(
            self.sentenceArea, yscrollcommand=self.sentenceScrollbar.set, background="#e9ecef", bd=0, highlightcolor="#e9ecef", selectbackground="#C1BED7", font=("Roboto", 14))

        self.sentenceScrollbar.config(command=self.sentenceAreaBox.yview)

        self.sentenceAreaBox.bind("<<ListboxSelect>>", self.doSelection)

        # Creating Scrollbar for resultOutputs
        self.resultsScrollbar = Scrollbar(
            self.resultOutputs, orient=VERTICAL)
        self.resultsAreaBox = Listbox(
            self.resultOutputs, yscrollcommand=self.resultsScrollbar.set, background="#ced4da", bd=0, highlightcolor="#e9ecef", selectbackground="#C1BED7", font=("Roboto", 14))

        # for i in range(0, 10):
        #     self.resultsAreaBox.insert(0, i)

        self.resultsScrollbar.config(command=self.resultsAreaBox.yview)

        # Create Run button
        self.runphoto = PhotoImage(file=r"Images/run_button.png")
        self.runButton = Button(
            self.sentenceRun, image=self.runphoto, command=self.append_to_SentenceArea, background="#ced4da", height=30, width=70, relief="flat", bd=0, activebackground="#ced4da")

        # --------------------------------------------------------------------------------

        # Assign component locations
        self.titlebar.grid(row=0, column=0, sticky="nsew")
        self.body.grid(row=1, column=0, sticky="nsew")
        self.sentences.grid(row=0, column=0, sticky="nsew")
        self.results.grid(row=0, column=1, sticky="nsew")
        self.sentenceInput.grid(row=0, column=0, sticky="nsew")
        self.sentenceArea.grid(row=1, column=0, sticky="nsew")
        self.sentenceRun.grid(row=2, column=0, sticky="nsew")
        self.sentenceInputBox.grid(row=0, column=0, sticky="ew", padx=20)
        self.sentenceAreaBox.grid(
            row=0, column=0, sticky="nsew", padx=(50, 0), pady=(20, 0))
        self.sentenceScrollbar.grid(row=0, column=1, sticky="ns")
        self.runButton.grid(row=0, column=0, sticky="w", padx=50)
        self.resultsHeading.grid(row=0, column=0, sticky="nsew")
        self.resultsHeadingText.grid(row=0, column=0, sticky="nsew")
        self.resultOutputs.grid(row=1, column=0, sticky="nsew")
        self.resultsAreaBox.grid(row=0, column=0, sticky="nsew", padx=(20, 0))
        self.resultsScrollbar.grid(row=0, column=1, sticky="ns")

        # configure layouts (dimensions/sizing)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=50)

        self.body.grid_columnconfigure(0, weight=5)
        self.body.grid_columnconfigure(1, weight=3)
        self.body.grid_rowconfigure(0, weight=1)

        self.sentences.grid_columnconfigure(0, weight=1)
        self.sentences.grid_rowconfigure(0, weight=0)
        self.sentences.grid_rowconfigure(1, weight=1)
        self.sentences.grid_rowconfigure(2, weight=0)

        self.results.grid_columnconfigure(0, weight=1)
        self.results.grid_rowconfigure(0, weight=0)
        self.results.grid_rowconfigure(1, weight=1)

        self.sentenceArea.grid_columnconfigure(0, weight=1)
        self.sentenceArea.grid_columnconfigure(1, weight=0)
        self.sentenceArea.grid_rowconfigure(0, weight=1)

        self.sentenceInput.grid_columnconfigure(0, weight=1)
        self.sentenceInput.grid_rowconfigure(0, weight=1, minsize=40)

        self.sentenceRun.grid_columnconfigure(0, weight=1)
        self.sentenceRun.grid_rowconfigure(0, weight=1, minsize=80)

        self.resultsHeading.grid_columnconfigure(0, weight=1)
        self.resultsHeading.grid_rowconfigure(0, weight=1, minsize=40)

        self.resultOutputs.grid_columnconfigure(0, weight=1)
        self.resultOutputs.grid_columnconfigure(1, weight=0)
        self.resultOutputs.grid_rowconfigure(0, weight=1)

        # --------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------
        # header layout

        # Creating Menubar
        self.menubar = Menu(self.root, font=("times new roman",
                            15, "bold"), activebackground="skyblue")

        # Configuring menubar on header
        self.root.config(menu=self.menubar)

        # --------------------------------------------------------------------------------
        # Calling Settitle Function
        self.settitle()

        # --------------------------------------------------------------------------------
        # Creating File Menu
        self.filemenu = Menu(self.menubar, font=(
            "Roboto", 11), activebackground="skyblue", tearoff=0)
        # Adding New file Command
        self.filemenu.add_command(
            label="New", accelerator="Ctrl+N", command=self.newfile)
        # Adding Open file Command
        self.filemenu.add_command(
            label="Open", accelerator="Ctrl+O", command=self.openfile)
        # Adding Save File Command
        self.filemenu.add_command(
            label="Save", accelerator="Ctrl+S", command=self.savefile)
        # Adding Save As file Command
        self.filemenu.add_command(
            label="Save As", accelerator="Ctrl+A", command=self.saveasfile)
        # Adding Seprator
        self.filemenu.add_separator()
        # Adding Exit window Command
        self.filemenu.add_command(
            label="Exit", accelerator="Ctrl+E", command=self.exit)
        # Cascading filemenu to menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # --------------------------------------------------------------------------------
        # Creating Edit Menu
        self.editmenu = Menu(self.menubar, font=(
            "Roboto", 11), activebackground="skyblue", tearoff=0)
        # Adding Cut text Command
        self.editmenu.add_command(
            label="Cut", accelerator="Ctrl+X", command=self.cut)
        # Adding Copy text Command
        self.editmenu.add_command(
            label="Copy", accelerator="Ctrl+C", command=self.copy)
        # Adding Paste text command
        self.editmenu.add_command(
            label="Paste", accelerator="Ctrl+V", command=self.paste)
        # Adding Seprator
        self.editmenu.add_separator()
        # Adding Undo text Command
        self.editmenu.add_command(
            label="Undo", accelerator="Ctrl+U", command=self.undo)
        # Cascading editmenu to menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        # --------------------------------------------------------------------------------
        # Creating Help Menu
        self.helpmenu = Menu(self.menubar, font=(
            "Roboto", 11), activebackground="skyblue", tearoff=0)
        # Adding Dictionary Command
        self.helpmenu.add_command(
            label="Dictionary", command=self.infodictionary)
        # Adding Tips command
        self.helpmenu.add_command(label="Tips", command=self.infotips)

        # Cascading helpmenu to menubar
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        # --------------------------------------------------------------------------------

        # Calling shortcuts function
        self.shortcuts()

    # Defining settitle function
    def settitle(self):
        # Checking if Filename is not None
        if self.filename:
            # Updating Title as filename
            self.title.set(self.filename)
        else:
            # Updating Title as Untitled
            self.title.set("Untitled")

      # Defining New file Function

    def newfile(self, *args):
        # Clearing the Text Area
        self.sentenceInputBox.delete()
        # Updating filename as None
        self.filename = None
        # Calling settitle funtion
        self.settitle()
        # updating status
        self.status.set("New File Created")

      # Defining Open File Funtion

    def openfile(self, *args):
        # Exception handling
        try:
            # Asking for file to open
            self.filename = filedialog.askopenfilename(title="Select file", filetypes=(
                ("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))
            # checking if filename not none
            if self.filename:
                # opening file in readmode
                infile = open(self.filename, "r")
                # Clearing text area
                self.sentenceInputBox.delete()
                # Inserting data Line by line into text area
                for line in infile:
                    self.sentenceInputBox.insert(END, line)
                # Closing the file
                infile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set("Opened Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

      # Defining Save File Funtion

    def savefile(self, *args):
        # Exception handling
        try:
            # checking if filename not none
            if self.filename:
                # Reading the data from text area
                data = self.sentenceInputBox.get()
                # opening File in write mode
                outfile = open(self.filename, "w")
                # Writing Data into file
                outfile.write(data)
                # Closing File
                outfile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set("Saved Successfully")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("Exception", e)

        # Defining Save As File Funtion

    def saveasfile(self, *args):
        # Exception handling
        try:
            # Asking for file name and type to save
            untitledfile = filedialog.asksaveasfilename(title="Save file As", defaultextension=".txt", initialfile="Untitled.txt", filetypes=(
                ("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))
            # Reading the data from text area
            data = self.sentenceInputBox.get()
            # opening File in write mode
            outfile = open(untitledfile, "w")
            # Writing Data into file
            outfile.write(data)
            # Closing File
            outfile.close()
            # Updating filename as Untitled
            self.filename = untitledfile
            # Calling Set title
            self.settitle()
            # Updating Status
            self.status.set("Saved Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

    # Defining Exit Funtion
    def exit(self, *args):
        op = messagebox.askyesno("WARNING", "Your Unsaved Data May be Lost!!")
        if op > 0:
            self.root.destroy()
        else:
            return

    # Defining Cut Funtion
    def cut(self, *args):
        self.sentenceInputBox.event_generate("<<Cut>>")

    # Defining Copy Funtion
    def copy(self, *args):
        self.sentenceInputBox.event_generate("<<Copy>>")

    # Defining Paste Funtion
    def paste(self, *args):
        self.sentenceInputBox.event_generate("<<Paste>>")

    # Defining Undo Funtion
    def undo(self, *args):
        # Exception handling
        try:
            # checking if filename not none
            if self.filename:
                # Clearing Text Area
                self.sentenceInputBox.delete()
                # opening File in read mode
                infile = open(self.filename, "r")
                # Inserting data Line by line into text area
                for line in infile:
                    self.sentenceInputBox.insert(END, line)
                # Closing File
                infile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set("Undone Successfully")
            else:
                # Clearing Text Area
                self.sentenceInputBox.delete()
                # Updating filename as None
                self.filename = None
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set("Undone Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

    # Defining Dictionary Function
    def infodictionary(self):
        messagebox.showinfo("Reserved Keywords", "add...to...\nsubstract...from...\nmultiple...by... \n" +
                            "divide...by... \nif... is even/odd then...\n")

    def infotips(self):
        messagebox.showinfo("Tips for Success",
                            "Make sure you use integers for if statements")

    # Defining shortcuts Funtion
    def shortcuts(self):
        # Binding Ctrl+n to newfile funtion
        self.sentenceInputBox.bind("<Control-n>", self.newfile)
        # Binding Ctrl+o to openfile funtion
        self.sentenceInputBox.bind("<Control-o>", self.openfile)
        # Binding Ctrl+s to savefile funtion
        self.sentenceInputBox.bind("<Control-s>", self.savefile)
        # Binding Ctrl+a to saveasfile funtion
        self.sentenceInputBox.bind("<Control-a>", self.saveasfile)
        # Binding Ctrl+e to exit funtion
        self.sentenceInputBox.bind("<Control-e>", self.exit)
        # Binding Ctrl+x to cut funtion
        self.sentenceInputBox.bind("<Control-x>", self.cut)
        # Binding Ctrl+c to copy funtion
        self.sentenceInputBox.bind("<Control-c>", self.copy)
        # Binding Ctrl+v to paste funtion
        self.sentenceInputBox.bind("<Control-v>", self.paste)
        # Binding Ctrl+u to undo funtion
        self.sentenceInputBox.bind("<Control-u>", self.undo)

    def append_to_SentenceArea(self):
        if self.sentenceInputBox.get():
            sentence = " ".join(self.sentenceInputBox.get().split())
            self.inputSentense = sentence
            self.sentenceAreaBox.insert(0, sentence)

        # textFile = open('Editor/textArea.txt', 'w')
        # textFile.write()

    def append_to_ResultsArea(self, output):
        self.resultsAreaBox.insert(0, output)

    def getInputSentense(self):
        return self.inputSentense

    def doSelection(self, event):
        w = event.widget
        selected_index = int(w.curselection()[0])
        self.resultsAreaBox.selection_set(selected_index)
