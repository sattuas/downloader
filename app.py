from tkinter import *
from tkinter.ttk import *
from youtube import youtube_downloader
from twitter import twitter_downloader


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("Downloader")
        self.frames = {}

        for F in (MainPage, ConfigPage):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.show_frame(ConfigPage)


    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

        
class MainPage(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)

        title_lbl = Label(self, text="Download a media :)")
        settings_btn = Button(self, text="Settings", command=lambda: master.show_frame(ConfigPage))

        title_lbl.grid(row=0, column=0, sticky="w")
        settings_btn.grid(row=0, column=2, sticky="e")


class ConfigPage(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)

        title_lbl = Label(self, text="Settings")
        back_btn = Button(self, text="Back", command=lambda: master.show_frame(MainPage))

        title_lbl.grid(row=0, column=0, sticky="w")
        back_btn.grid(row=0, column=2, sticky="e")


if __name__ == "__main__":
    app = App()
    app.mainloop()

'''
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

'''
