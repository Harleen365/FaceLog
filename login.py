from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk    
from tkinter import messagebox  

class Login_Window:
    def __init__(self, root):  
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Load and resize the background image
        image_path = r"C:\Users\ishut\Downloads\FaceLog\Images\Login Background.jpg"
        bg_image = Image.open(image_path).resize((1550, 800))
        self.bg = ImageTk.PhotoImage(bg_image)

        # Set background image
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Login App Icon (Top)
        img1 = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\LoginAppIcon-removebg-preview.png").resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(frame, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=120, y=10, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username Icon
        img2 = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\loginicon.webp").resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(frame, image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=10, y=155, width=25, height=25)  # Align with "Username" label

        # Username Label & Input Field
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=40, y=155)  # Moved right to align with icon

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password Icon
        img3 = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\passwordicon.webp").resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(frame, image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=10, y=225, width=25, height=25)  # Align with "Password" label

        # Password Label & Input Field
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=40, y=225)  # Moved right to align with icon

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")  # Hide password
        self.txtpass.place(x=40, y=250, width=270)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register & Forgot Password Buttons
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        forgetpassbtn = Button(frame, text="Forgot Password?", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetpassbtn.place(x=20, y=380, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "ishi" and self.txtpass.get() == "1234":
            messagebox.showinfo("Success", "Welcome to FaceLog")
        else:
            messagebox.showerror("Error", "Invalid username or password")

if __name__ == "__main__":  
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
