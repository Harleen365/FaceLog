from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\loginbutton.jpg")  # Replace with your image path
        img = img.resize((500, 130), Image.LANCZOS)  # Updated: Use Image.LANCZOS instead of Image.ANTIALIAS
        self.photoimg1 = ImageTk.PhotoImage(img)  # Store separately to prevent garbage collection

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\loginbutton.jpg")  # Replace with your image path
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\loginbutton.jpg")  # Replace with your image path
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=500, height=130)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
