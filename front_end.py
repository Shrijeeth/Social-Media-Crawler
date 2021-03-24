from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,messagebox,filedialog
import main

class search():
    def __init__(self,root):
        self.root = root
        self.root.title("Social Media Crawler")
        self.search_frame = LabelFrame(self.root, text='search', font=('arial', 15), bd=5, relief=RIDGE, bg="white")
        self.search_frame.place(x=50, y=50, width=300, height=200)
        self.find_button = Button(self.root, text="SEARCH", bd=4, bg='white', width=10, relief=RIDGE, command=self.find)
        self.find_button.place(x=60, y=150)
        self.entry=Entry(self.root,width=30)
        self.entry.grid(row=0,column=1)
        self.entry.place(x=60,y=80)

        self.search_frame = LabelFrame(self.root, text='report', font=('arial', 18), bd=5, relief=RIDGE, bg="white")
        self.search_frame.place(x=500, y=50, width=1000, height=500)
        self.l1 = Label(self.search_frame,text='',bg='white',font=('arial',30))
        self.l1.pack()
    
    def find(self) :
        query = self.entry.get()
        pos,neg,neu,ovr = main.search(query)
        out = f"Sentiment Report on '{query}'\n\n" + f"Positive Reviews : {pos}\n" + f"Negative Reviews : {neg}\n" + f"Neutral Reviews : {neu}\n" + f"Total Reviews : {pos+neg+neu}\n" + f"Overall Sentiment Score : {ovr*100:.2f}%"
        self.l1.config(text=out)

root = Tk()
root.geometry("1550x600")
s = search(root)
root.mainloop()