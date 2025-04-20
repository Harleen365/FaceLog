from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pymongo
import base64

# MongoDB connection
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["FaceLogDB"]
students_collection = db["students"]

class NewStudentRegister:
    def __init__(self, root):
        self.root = root
        self.root.title("Register New Student")
        self.root.geometry("1550x800+0+0")

        # Variables
        self.branch_var = StringVar()
        self.course_var = StringVar()
        self.name_var = StringVar()
        self.group_var = StringVar()
        self.hosteler_var = IntVar()
        self.dayscholar_var = IntVar()
        self.mentor_var = StringVar()
        self.photo_data = None

        # Background Image
        bg_image = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\newstudentregister.jpg").resize((1550, 800))
        self.bg = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Navbar
        navbar = Frame(self.root, bg="darkblue", height=60)
        navbar.pack(side=TOP, fill=X)
        title = Label(navbar, text="Register New Student", font=("Helvetica", 20, "bold"), fg="white", bg="darkblue")
        title.pack(side=LEFT, padx=20)

        # Form Frame
        form_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        form_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=750, height=500)

        # Labels and Entries
        Label(form_frame, text="Branch:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.branch_var, font=("Arial", 12), width=30).grid(row=0, column=1, padx=10)

        Label(form_frame, text="Course:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.course_var, font=("Arial", 12), width=30).grid(row=1, column=1, padx=10)

        Label(form_frame, text="Name:", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.name_var, font=("Arial", 12), width=30).grid(row=2, column=1, padx=10)

        Label(form_frame, text="Group:", font=("Arial", 12), bg="white").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.group_var, font=("Arial", 12), width=30).grid(row=3, column=1, padx=10)

        Label(form_frame, text="Mentor:", font=("Arial", 12), bg="white").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        Entry(form_frame, textvariable=self.mentor_var, font=("Arial", 12), width=30).grid(row=4, column=1, padx=10)

        Label(form_frame, text="Accommodation:", font=("Arial", 12), bg="white").grid(row=5, column=0, padx=10, pady=10, sticky=W)
        Checkbutton(form_frame, text="Hosteler", variable=self.hosteler_var, bg="white").grid(row=5, column=1, sticky=W, padx=10)
        Checkbutton(form_frame, text="Day Scholar", variable=self.dayscholar_var, bg="white").grid(row=5, column=1, sticky=E, padx=10)

        # Upload photo
        Button(form_frame, text="Upload Photograph", font=("Arial", 12), command=self.upload_photo, bg="#007bff", fg="white").grid(row=6, column=0, columnspan=2, pady=10)
        self.photo_label = Label(form_frame, bg="white")
        self.photo_label.grid(row=7, column=0, columnspan=2)

        # Submit Button
        Button(form_frame, text="Submit", font=("Arial", 14, "bold"), bg="green", fg="white", command=self.submit_data).grid(row=8, column=0, columnspan=2, pady=20)

        # Footer
        footer = Label(self.root, text="© 2025 Student Registration | FaceLog System", font=("Arial", 10), bg="darkblue", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if file_path:
            with open(file_path, "rb") as file:
                self.photo_data = base64.b64encode(file.read()).decode("utf-8")

            img = Image.open(file_path).resize((100, 100))
            self.img = ImageTk.PhotoImage(img)
            self.photo_label.config(image=self.img)

    def submit_data(self):
        if not all([self.branch_var.get(), self.course_var.get(), self.name_var.get(), self.group_var.get(), self.mentor_var.get(), self.photo_data]):
            messagebox.showerror("Error", "Please fill all the fields and upload a photograph.")
            return

        accommodation = []
        if self.hosteler_var.get():
            accommodation.append("Hosteler")
        if self.dayscholar_var.get():
            accommodation.append("Day Scholar")

        student_data = {
            "Branch": self.branch_var.get(),
            "Course": self.course_var.get(),
            "Name": self.name_var.get(),
            "Group": self.group_var.get(),
            "Mentor": self.mentor_var.get(),
            "Accommodation": accommodation,
            "Photograph": self.photo_data
        }

        students_collection.insert_one(student_data)
        messagebox.showinfo("Success", "Student data has been stored successfully.")
        self.clear_form()

    def clear_form(self):
        self.branch_var.set("")
        self.course_var.set("")
        self.name_var.set("")
        self.group_var.set("")
        self.mentor_var.set("")
        self.hosteler_var.set(0)
        self.dayscholar_var.set(0)
        self.photo_data = None
        self.photo_label.config(image="")

def main():
    root = Tk()
    app = NewStudentRegister(root)
    root.mainloop()

if __name__ == "__main__":
    main()
