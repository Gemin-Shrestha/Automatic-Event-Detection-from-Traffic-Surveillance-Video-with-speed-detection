import tkinter as tk
from PIL import Image, ImageTk
import os
root=tk.Tk()
root.title('Automatic Event Detection from Traffic Surveillance Video')
root.geometry('1000x800+0+0')
root.configure(bg='Black')
lbl1 = tk.Label(root,text='Automatic Event Detection from Traffic Surveillance Video',font = "verdana 20 bold",bg='White',fg='Blue')
lbl1.pack(side='top')
def rule_breaker():
    root.destroy()
    os.system('python RuleBreaker.py')

def speed_licence():
    root.destroy()
    os.system('python /Users/ganeshkumarshrestha/Desktop/Delection_Speed/VehicleMoniter.py') 

def  billing():
    root.destroy()
    os.system('python bill.py') 

def vechicle_couting():
    root.destroy()
    os.system('python Vechicle_Couting.py')

img = ImageTk.PhotoImage(Image.open('snapbutton/tl.jpg').resize((200,200), Image.ANTIALIAS))
panel = tk.Button(root, image = img,command=rule_breaker)
panel.place(x=150,y=100)

img1 = ImageTk.PhotoImage(Image.open('snapbutton/toll.jpg').resize((200,200), Image.ANTIALIAS))
panel = tk.Button(root, image = img1,command=vechicle_couting)
panel.place(x=400,y=100)

img2 = ImageTk.PhotoImage(Image.open('snapbutton/speed.jpg').resize((200,200), Image.ANTIALIAS))
panel = tk.Button(root, image = img2,command=speed_licence)
panel.place(x=250,y=350)

img3 = ImageTk.PhotoImage(Image.open('snapbutton/stos.jpg').resize((200,200), Image.ANTIALIAS))
panel = tk.Button(root, image = img3,command=rule_breaker)
panel.place(x=650,y=100)
img4 = ImageTk.PhotoImage(Image.open('snapbutton/billing.png').resize((200,200), Image.ANTIALIAS))
panel = tk.Button(root, image = img4,command=billing)
panel.place(x=500,y=350)
lbl2 = tk.Label(root,text='PROJECT MEMBER :\n(101803077) Satyam Sheel\n (101803094) Abhishek Sah\n (101803335) Gemin Shrestha\n ',font = "verdana 15 bold",bg='White',fg='orange')
lbl2.place(x=700,y=600)
lbl3 = tk.Label(root,text='Mentor : Dr Jhilik Bhattacharya\nAssociate Professor ',font = "verdana 15 bold",bg='White',fg='Blue')
lbl3.place(x=50,y=600)

root.mainloop()
