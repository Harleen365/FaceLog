from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk      

class Login_Window:
    def __init__(self, root):  
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Load and resize the image
        image_path = r"C:\Users\ishut\Downloads\FaceLog\Images\Login Background.jpg"  # Ensure this file exists
        bg_image = Image.open(image_path)  
        bg_image = bg_image.resize((1550, 800))  # Resize to fit window
        self.bg = ImageTk.PhotoImage(bg_image)

        # Set background image
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\LoginAppIcon-removebg-preview.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=180,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


        img2=Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\loginicon.webp")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\passwordicon.webp")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)


        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        

if __name__ == "__main__":  
    root = Tk()
    app = Login_Window(root)
    root.mainloop()

