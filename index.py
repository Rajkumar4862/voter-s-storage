from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    sys.exit() 
def pos():
    root.destroy()
    os.system('python login.py')
    




        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("Voter ID List")
    root.configure(bg='#68BBE3')
    



   
    b1=Button(root,text="Click to Start",command=pos,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=200)
    
    root.mainloop()


