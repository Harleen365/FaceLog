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

        # MongoDB Connection
        try:
            self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
            self.db = self.client["FaceLogDB"]
            self.collection = self.db["users"]
            print("Connected to MongoDB successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to MongoDB: {str(e)}")

        # Text variables 
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Load and resize background image
        image_path = r"C:\Users\ishut\Downloads\FaceLog\Images\registerbackgroundfinal.jpg"
        bg_image = Image.open(image_path).resize((1600, 900))
        self.bg = ImageTk.PhotoImage(bg_image)

        # Set background
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=(1600-800)//2, y=(900-550)//2, width=800, height=550)

        register_lbl = Label(frame, text="Register Here", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # Row 1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # Row 2
        contact = Label(frame, text="Contact Number", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # Row 3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your First Pet Name", "Your Favourite Teacher")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # Row 4
        psswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        psswd.place(x=50, y=310)

        self.txt_psswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_psswd.place(x=50, y=340, width=250)

        confirm_psswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_psswd.place(x=370, y=310)

        self.txt_confirm_psswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confirm_psswd.place(x=370, y=340, width=250)

        # Checkbutton
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree to the terms and conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # Register button
        regisbutton = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\registerbutton.jpg").resize((200, 55), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(regisbutton)

        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=50, y=420, width=200)

        # Login button
        loginbutton = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\loginbutton.jpg").resize((200, 55), Image.LANCZOS)
        self.photoimagelogin = ImageTk.PhotoImage(loginbutton)

        b2 = Button(frame, image=self.photoimagelogin, command=self.open_login, borderwidth=0, cursor="hand2")
        b2.place(x=380, y=420, width=200)

    # Register function (Save data in MongoDB)
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_confpass.get() != self.var_pass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions")
        else:
            user_data = {
                "First Name": self.var_fname.get(),
                "Last Name": self.var_lname.get(),
                "Contact": self.var_contact.get(),
                "Email": self.var_email.get(),
                "Security Question": self.var_securityQ.get(),
                "Security Answer": self.var_securityA.get(),
                "Password": self.var_pass.get()
            }
            self.collection.insert_one(user_data)
            messagebox.showinfo("Success", "Registration Successful")

    # Open login.py when login button is clicked
    def open_login(self):
        self.root.destroy()
        subprocess.run(["python", "login.py"])

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
