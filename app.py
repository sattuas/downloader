from tkinter import *
from tkinter.ttk import *
from youtube import youtube_downloader
from twitter import twitter_downloader


def select():
    if v.get() == "1":
        youtube_downloader(link.get())
    if v.get() == "2":
        twitter_downloader(link.get())


root = Tk()
root.title("downloader")
root.geometry("300x300")
root.resizable(False, False)

link = StringVar()
v = StringVar(root, "1")

Label(root, text="DOWNLOADER").pack()

option_frame = Frame(root)
option_frame.pack()

values = {
    "YouTube": "1",
    "X/Twitter": "2"
}

for (text, value) in values.items():
    Radiobutton(option_frame,
                text=text,
                variable=v,
                value=value).pack(side="left")

link_frame = Frame(root)
link_frame.pack()

link_label = Label(link_frame, text="Link:")
link_entry = Entry(link_frame, textvariable=link)
link_button = Button(root, text="download", command=select)
link_label.pack(side="left")
link_entry.pack(side="left")
link_button.pack()


root.mainloop()
