import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("exectutables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()
        
def runApps():
    for app in apps:
        os.startfile(app)
    

canvas = tk.Canvas(root, height=500, width= 400, bg="lightblue")
canvas.pack()

frame = tk.Frame(root, bg="white")

frame.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="lightblue", command=addApp) 
openFile.pack()

runApps = tk.Button(root, text="Run App", padx=10, pady=5, fg="white", bg="lightblue", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
