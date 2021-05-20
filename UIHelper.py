import tkinter as tk
from PIL import ImageTk, Image
import urllib.request
from io import BytesIO

window = tk.Tk()
window.title("DEPICTOREX")
# Frame A to hold image search term, submit button
frmA = tk.Frame(relief=tk.GROOVE, borderwidth=5)

lblSearch = tk.Label(text="Search Term:", master=frmA)
entSearch = tk.Entry(master=frmA)
btnSearch = tk.Button(master=frmA, text="Search!", width=8, height=2, bg="black", fg="white")
lblSearch.pack(side=tk.LEFT)
entSearch.pack(side=tk.LEFT)
btnSearch.pack(side=tk.LEFT)
frmA.pack()

# Frame B to hold top 10 images, Run button
frmB = tk.Frame(relief=tk.GROOVE, borderwidth=5)
d = {}
for i in range(3):
    for j in range(3):
        frm = tk.Frame(master=frmB, relief=tk.RAISED, borderwidth=3)
        frm.grid(row=i, column=j)
        url = "https://ctl.s6img.com/society6/img/UPB_Z6mA6neMT-KwPmKnXY1EvcU/w_700/prints/~artwork/s6-0024/a/9774180_2379400/~~/edgar-allan-poe-5fv-prints.jpg"
        response = urllib.request.urlopen(url).read()
        img = Image.open(BytesIO(response))
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        d[f"{i}{j}"] = img
        btnI = tk.Button(master=frm, image=d[f"{i}{j}"])
        btnI.pack()

frmB.pack()
window.mainloop()