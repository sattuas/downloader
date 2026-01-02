from tkinter import *
from tkinter.ttk import *
from youtube import youtube_downloader
from twitter import twitter_downloader


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Downloader")

        self.v = StringVar(self, "1")
        self.count = 1

        self.values = {
            "YouTube": "1",
            "X/Twitter": "2"
        }



        self.title_lbl = Label(self, text="Downloader a media :)")

        self.link_lbl = Label(self, text="Paste a link here:")
        self.link_entry = Entry(self)
        self.link_btn = Button(self, text="Search")

        self.platform_lbl = Label(self, text="Choose a platform:")
        for (text, value) in self.values.items():
            Radiobutton(self,
                        text=text,
                        variable=self.v,
                        value=value).grid(row=2, column=self.count)
            self.count += 1

        self.list_box = Listbox(self)
        self.list_box.insert(1, "Select a resolution")

        self.download_btn = Button(self, text="Download")

        self.title_lbl.grid(row=0, column=1)
        self.link_lbl.grid(row=1, column=0, sticky="w")
        self.link_entry.grid(row=1, column=1)
        self.link_btn.grid(row=1, column=2)

        self.platform_lbl.grid(row=2, column=0)

        self.list_box.grid(row=3, column=0, columnspan=3, sticky="ew")
        
        self.download_btn.grid(row=4, column=1)


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
