from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        #first image
        img=Image.open()
        #open k ander images ka path aaega:timestamp 26:57
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)



        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #2nd image
        img1=Image.open()
        #open k ander images ka path aaega:timestamp 26:57
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img1)



        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #3rd image
        img2=Image.open()
        #open k ander images ka path aaega:timestamp 26:57
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img2)



        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


if __name__ == "__main__":
    root=Tk()
    obj= Face_Recognition_System(root)
    root.mainloop()       