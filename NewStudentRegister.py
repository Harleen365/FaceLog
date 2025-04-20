from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pymongo
import os

class NewStudentRegister:
    def __init__(self, root):
        self.root = root
        self.root.title("New Student Registration")
        self.root.geometry("1550x800+0+0")

        self.photo_path = ""

        # MongoDB setup
        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.client["FaceLogDB"]
        self.collection = self.db["students"]

        # Background
        bg_image = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\newstudentregister.jpg").resize((1550, 800))
        bg_image = bg_image.convert("RGBA")
        bg_image.putalpha(180)
        self.bg = ImageTk.PhotoImage(bg_image)
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Navbar
        navbar = Frame(self.root, bg="darkblue", height=60)
        navbar.pack(side=TOP, fill=X)
        Label(navbar, text="Register New Student", font=("Helvetica", 20, "bold"), fg="white", bg="darkblue").pack(side=LEFT, padx=20)
        Button(navbar, text="Back", font=("Arial", 12), bg="red", fg="white", command=self.root.destroy).pack(side=RIGHT, padx=20, pady=10)

        # Form Frame
        form_frame = Frame(self.root, bg="white")
        form_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

        # Labels and Entry Fields
        Label(form_frame, text="Branch", font=("Arial", 14), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=E)
        self.branch_entry = Entry(form_frame, font=("Arial", 14), width=30)
        self.branch_entry.grid(row=0, column=1, padx=10)

        Label(form_frame, text="Course", font=("Arial", 14), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=E)
        self.course_entry = Entry(form_frame, font=("Arial", 14), width=30)
        self.course_entry.grid(row=1, column=1, padx=10)

        Label(form_frame, text="Name", font=("Arial", 14), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=E)
        self.name_entry = Entry(form_frame, font=("Arial", 14), width=30)
        self.name_entry.grid(row=2, column=1, padx=10)

        Label(form_frame, text="Group", font=("Arial", 14), bg="white").grid(row=3, column=0, padx=10, pady=10, sticky=E)
        self.group_entry = Entry(form_frame, font=("Arial", 14), width=30)
        self.group_entry.grid(row=3, column=1, padx=10)

        Label(form_frame, text="Accommodation", font=("Arial", 14), bg="white").grid(row=4, column=0, padx=10, pady=10, sticky=E)
        self.accommodation_var = StringVar()
        self.accommodation_dropdown = OptionMenu(form_frame, self.accommodation_var, "Hosteler", "Day Scholar")
        self.accommodation_dropdown.config(font=("Arial", 13), width=28)
        self.accommodation_dropdown.grid(row=4, column=1, padx=10)

        Label(form_frame, text="Mentor", font=("Arial", 14), bg="white").grid(row=5, column=0, padx=10, pady=10, sticky=E)
        self.mentor_entry = Entry(form_frame, font=("Arial", 14), width=30)
        self.mentor_entry.grid(row=5, column=1, padx=10)

        Label(form_frame, text="Photograph", font=("Arial", 14), bg="white").grid(row=6, column=0, padx=10, pady=10, sticky=E)
        Button(form_frame, text="Upload Photo", font=("Arial", 12), command=self.upload_photo).grid(row=6, column=1, padx=10, sticky=W)

        self.photo_label = Label(form_frame, text="", font=("Arial", 10), bg="white", fg="gray")
        self.photo_label.grid(row=7, column=1, sticky=W, padx=10)

        Button(form_frame, text="Submit", font=("Arial", 14, "bold"), bg="green", fg="white", command=self.submit_form).grid(row=8, column=0, columnspan=2, pady=20)

        # Footer
        footer = Label(self.root, text="© 2025 FaceLog System", font=("Arial", 10), bg="darkblue", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.photo_path = file_path
            filename = os.path.basename(file_path)
            self.photo_label.config(text=filename)

    def submit_form(self):
        student_data = {
            "Branch": self.branch_entry.get(),
            "Course": self.course_entry.get(),
            "Name": self.name_entry.get(),
            "Group": self.group_entry.get(),
            "Accommodation": self.accommodation_var.get(),
            "Mentor": self.mentor_entry.get(),
            "Photograph": self.photo_path
        }

        if all(student_data.values()):
            self.collection.insert_one(student_data)
            messagebox.showinfo("Success", "Student data saved successfully!")
            self.clear_form()
        else:
            messagebox.showwarning("Missing Info", "Please fill all fields.")

    def clear_form(self):
        self.branch_entry.delete(0, END)
        self.course_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.group_entry.delete(0, END)
        self.accommodation_var.set("")
        self.mentor_entry.delete(0, END)
        self.photo_label.config(text="")
        self.photo_path = ""

if __name__ == "__main__":
    root = Tk()
    app = NewStudentRegister(root)
    root.mainloop()
