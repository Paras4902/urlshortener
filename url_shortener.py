"""a Python Program to shorten the URL using python(pyshorteners)"""
from tkinter import Tk, messagebox as msgbx, Entry, Label, Button, END
import pyperclip  # pip install pyperclip
import pyshorteners  # pip install pyshorteners

root = Tk()
root.title("URL Shortener")
root.geometry("900x500")
root.resizable(0, 0)
root.config(bg="grey")

l1 = Label(root, text="Welcome to Url Shortener", font=("Helvetica", 35, "bold underline"), bg="grey", fg="Black")
l1.pack()

l2 = Label(root, text="Enter Url: ", font=("Helvetica", 35, "bold"), bg="grey", fg="blue")
l2.place(x=10, y=70)

e1 = Entry(root, bd=10, font=("Helvetica", 25))
e1.place(x=230, y=70, height=70, width=640)


def geturl():
    """function to convert url to a new short url"""
    msgbx.showwarning("Warning", "Do not copy paste url, it might result in opening the url directly, Enter url manually.")
    link = e1.get()
    s = pyshorteners.Shortener()
    x = s.tinyurl.short(link)
    e2.delete(0, END)
    e2.insert(END, x)


b1 = Button(root, text="Get Shortened URL", font=("Helvetica", 20, "bold"), bd=10, command=geturl)
b1.place(x=240, y=150)

l3 = Label(root, text="New Url: ", font=("Helvetica", 35, "bold"), bg="grey", fg="Blue")
l3.place(x=10, y=235)

e2 = Entry(root, bd=10, font=("Helvetica", 25))
e2.place(x=210, y=235, height=70, width=660)


def copytoclip():
    """function to copy new shortened url to device clipboard"""
    pyperclip.copy(e2.get())
    msgbx.showinfo("Link Copied", "Your new URL has been copied to clipboard")


b2 = Button(root, text="Copy to Clipboard", font=("Helvetica", 20, "bold"), bd=10, command=copytoclip)
b2.place(x=240, y=315)

label = Label(root, text="Program@Paras4902", font=("Helvetica", 25, "italic"), bg="grey", fg="red")
label.place(x=570, y=450)

root.mainloop()
