from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymongo
import subprocess

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        try:
            self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
            self.db = self.client["FaceLogDB"]
            self.collection = self.db["users"]
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to MongoDB: {str(e)}")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_role = StringVar()

        image_path = r"C:\Users\ishut\Downloads\FaceLog\Images\registerbackgroundfinal.jpg"
        bg_image = Image.open(image_path).resize((1600, 900))
        self.bg = ImageTk.PhotoImage(bg_image)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=(1600-800)//2, y=(900-550)//2, width=800, height=550)

        Label(frame, text="Register Here", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white").place(x=20, y=20)

        # First Name and Last Name
        Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15)).place(x=50, y=130, width=250)

        Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=100)
        ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15)).place(x=370, y=130, width=250)

        # Contact and Email
        Label(frame, text="Contact Number", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=170)
        ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15)).place(x=50, y=200, width=250)

        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=170)
        ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15)).place(x=370, y=200, width=250)

        # Security Question
        Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your First Pet Name", "Your Favourite Teacher")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50, y=270, width=250)

        Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=240)
        ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15)).place(x=370, y=270, width=250)

        # Password and Confirm
        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=310)
        ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*").place(x=50, y=340, width=250)

        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=310)
        ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*").place(x=370, y=340, width=250)

        # Role (Student / Teacher)
        Label(frame, text="I am a:", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=380)
        self.combo_role = ttk.Combobox(frame, textvariable=self.var_role, font=("times new roman", 15), state="readonly")
        self.combo_role["values"] = ("Select", "Student", "Teacher")
        self.combo_role.current(0)
        self.combo_role.place(x=150, y=380, width=200)

        self.var_check = IntVar()
        Checkbutton(frame, variable=self.var_check, text="I agree to terms and conditions", font=("times new roman", 12), onvalue=1, offvalue=0).place(x=50, y=420)

        regisbutton = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\registerbutton.jpg").resize((200, 55))
        self.photoimage = ImageTk.PhotoImage(regisbutton)
        Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2").place(x=50, y=460)

        loginbutton = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\loginbutton.jpg").resize((200, 55))
        self.photoimagelogin = ImageTk.PhotoImage(loginbutton)
        Button(frame, image=self.photoimagelogin, command=self.open_login, borderwidth=0, cursor="hand2").place(x=380, y=460)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select" or self.var_role.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords do not match")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to terms and conditions")
        else:
            user_data = {
                "First Name": self.var_fname.get(),
                "Last Name": self.var_lname.get(),
                "Contact": self.var_contact.get(),
                "Email": self.var_email.get(),
                "Security Question": self.var_securityQ.get(),
                "Security Answer": self.var_securityA.get(),
                "Password": self.var_pass.get(),
                "Role": self.var_role.get()
            }
            self.collection.insert_one(user_data)
            messagebox.showinfo("Success", "Registered Successfully")

    def open_login(self):
        self.root.destroy()
        subprocess.run(["python", "login.py"])

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
