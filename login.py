from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk    
from tkinter import messagebox
import pymongo
import subprocess

class Login_Window:
    def __init__(self, root):  
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # MongoDB Connection
        try:
            self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
            self.db = self.client["FaceLogDB"]
            self.collection = self.db["users"]
            print("Connected to MongoDB successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to MongoDB: {str(e)}")

        # Load and resize background image
        image_path = r"C:\Users\ishut\Downloads\FaceLog\Images\Login Background.jpg"
        bg_image = Image.open(image_path).resize((1550, 800))
        self.bg = ImageTk.PhotoImage(bg_image)

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

        # Username Label & Input Field
        username = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=40, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password Label & Input Field
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=40, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register Button
        registerbtn = Button(frame, text="New User Register", command=self.open_register, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # Forgot Password Button
        forgetpassbtn = Button(frame, text="Forgot Password?", command=self.forgot_password, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetpassbtn.place(x=20, y=380, width=160)

    def login(self):
        email = self.txtuser.get()
        password = self.txtpass.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        user = self.collection.find_one({"Email": email, "Password": password})

        if user:
            messagebox.showinfo("Success", "Login Successful")
            self.root.destroy()
            subprocess.run(["python", "main.py"])
        else:
            messagebox.showerror("Error", "Invalid email or password")

    def open_register(self):
        self.root.destroy()
        subprocess.run(["python", "register.py"])

    def forgot_password(self):
        email = self.txtuser.get()
        if email == "":
            messagebox.showerror("Error", "Enter your registered email to reset password")
            return

        user = self.collection.find_one({"Email": email})
        if not user:
            messagebox.showerror("Error", "Email not found")
            return

        # Forgot Password Window
        self.forgot_pass_win = Toplevel(self.root)
        self.forgot_pass_win.title("Reset Password")
        self.forgot_pass_win.geometry("400x300+600+300")

        Label(self.forgot_pass_win, text="Reset Password", font=("times new roman", 20, "bold")).pack(pady=10)

        Label(self.forgot_pass_win, text="New Password", font=("times new roman", 15)).pack(pady=5)
        self.new_password = ttk.Entry(self.forgot_pass_win, font=("times new roman", 15), show="*")
        self.new_password.pack(pady=5)

        Label(self.forgot_pass_win, text="Confirm Password", font=("times new roman", 15)).pack(pady=5)
        self.confirm_password = ttk.Entry(self.forgot_pass_win, font=("times new roman", 15), show="*")
        self.confirm_password.pack(pady=5)

        Button(self.forgot_pass_win, text="Reset", command=lambda: self.reset_password(email), font=("times new roman", 15, "bold"), bg="green", fg="white").pack(pady=20)

    def reset_password(self, email):
        new_pass = self.new_password.get()
        confirm_pass = self.confirm_password.get()

        if new_pass == "" or confirm_pass == "":
            messagebox.showerror("Error", "All fields are required", parent=self.forgot_pass_win)
        elif new_pass != confirm_pass:
            messagebox.showerror("Error", "Passwords do not match", parent=self.forgot_pass_win)
        else:
            self.collection.update_one({"Email": email}, {"$set": {"Password": new_pass}})
            messagebox.showinfo("Success", "Password reset successfully", parent=self.forgot_pass_win)
            self.forgot_pass_win.destroy()

if __name__ == "__main__":  
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
