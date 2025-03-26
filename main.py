from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\Users\kharl\OneDrive\Desktop\FaceLog\Images\Chitkara_img.jpg")  # Replace with your image path
        img = img.resize((500, 130), Image.LANCZOS)  # Updated: Use Image.LANCZOS instead of Image.ANTIALIAS
        self.photoimg1 = ImageTk.PhotoImage(img)  # Store separately to prevent garbage collection

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\kharl\OneDrive\Desktop\FaceLog\Images\Chitkara_img.jpg")  # Replace with your image path
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\kharl\OneDrive\Desktop\FaceLog\Images\Chitkara_img.jpg")  # Replace with your image path
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=500, y=0, width=500, height=130)

       
        #bgimg
        img3 = Image.open(r"C:\Users\kharl\OneDrive\Desktop\FaceLog\Images\back_pic.jpg")  # Replace with your image path
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(text="Face recognition System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        #student button
        img4 = Image.open(r"C:\Users\kharl\OneDrive\Desktop\FaceLog\Images\Chitkara_img.jpg")  # Replace with your image path
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4, cursor="hand2")
        b1.place(x = 200 , y = 100, width=220,height=220)
        b1_1=Button(bg_img,text="Student Details", cursor="hand2", font=("times new roman", 15,"bold"),bg="white",fg="red")
        b1_1.place(x = 200,y = 300, width=220,height=40)

        #detect face button
        img5 = Image.open(r"C:\Users\kharl\OneDrive\Desktop\FaceLog\Images\Chitkara_img.jpg")  # Replace with your image path
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5, cursor="hand2")
        b1.place(x = 500 , y = 100, width=220,height=220)
        b1_1=Button(bg_img,text="Face detector", cursor="hand2", font=("times new roman", 15,"bold"),bg="white",fg="red")
        b1_1.place(x = 500,y = 300, width=220,height=40)
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

