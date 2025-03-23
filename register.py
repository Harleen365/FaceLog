from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk    
from tkinter import messagebox      

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Load and resize background image to fit the window
        image_path = r"C:\Users\ishut\Downloads\FaceLog\Images\registerbackgroundfinal.jpg"
        bg_image = Image.open(image_path).resize((1600, 900))
        self.bg = ImageTk.PhotoImage(bg_image)

        # Set the background image
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame=Frame(self.root, bg="white")
        frame.place(x=(1600-800)//2, y=(900-550)//2, width=800, height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)


        #row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
 
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)


        #row2

        contact=Label(frame,text="Contact Number",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        #row3
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your  First Pet Name","Your favourite Teacher")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)


        #row 4
        psswd = Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        psswd.place(x=50,y=310)

        self.txt_psswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_psswd.place(x=50,y=340,width=250)

        confirm_psswd = Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_psswd.place(x=370,y=310)

        self.txt_confirm_psswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_confirm_psswd.place(x=370,y=340,width=250)



        # checkbutton
        checkbtn=Checkbutton(frame,text="I agree to the terms and conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


        #button
        regisbutton = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\registerbutton.jpg")
        regisbutton = regisbutton.resize((200, 55), Image.LANCZOS)
        
        self.photoimage = ImageTk.PhotoImage(regisbutton)

        # Create button
        b1 = Button(frame, image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=50, y=420, width=200)


        loginbutton = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\loginbutton.jpg")
        loginbutton = loginbutton.resize((200, 55), Image.LANCZOS)
        
        self.photoimagelogin = ImageTk.PhotoImage(loginbutton)

        # Create button
        b2 = Button(frame, image=self.photoimagelogin, borderwidth=0, cursor="hand2")
        b2.place(x=380, y=420, width=200)
        


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
