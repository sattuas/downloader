from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("downloader")
root.geometry("300x300")
root.resizable(False, False)

v = StringVar(root, "1")

Label(root, text="DOWNLOADER").pack()

values = {
    "YouTube": "1",
    "X/Twitter": "2"
}

for (text, value) in values.items():
    Radiobutton(root,
                text=text,
                variable=v,
                value=value).pack()


root.mainloop()
