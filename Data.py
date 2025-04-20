from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import subprocess

class StudentDataPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Data Management")
        self.root.geometry("1550x800+0+0")

        # Load and blur background image
        original_image = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\Dataimageback.jpeg").resize((1550, 800))
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(2))
        self.bg = ImageTk.PhotoImage(blurred_image)

        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Navbar
        navbar = Frame(self.root, bg="darkblue", height=60)
        navbar.pack(side=TOP, fill=X)

        title = Label(navbar, text="Student Data Management", font=("Helvetica", 20, "bold"), fg="white", bg="darkblue")
        title.pack(side=LEFT, padx=20)

        logout_btn = Button(navbar, text="Logout", font=("Arial", 12, "bold"), bg="red", fg="white", cursor="hand2", command=self.root.quit)
        logout_btn.pack(side=RIGHT, padx=20, pady=10)

        # Buttons on navbar for navigation
        Button(navbar, text="New Student", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.open_new_student).pack(side=RIGHT, padx=10, pady=10)
        Button(navbar, text="View All", font=("Arial", 12, "bold"), bg="#ffc107", fg="black", command=self.open_view_data).pack(side=RIGHT, padx=10, pady=10)

        # Functional Buttons in horizontal layout
        btn_frame = Frame(self.root, bg="white")
        btn_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(btn_frame, text="➕ Store Data of New Student", font=("Arial", 16, "bold"), width=30, height=2, bg="#28a745", fg="white", command=self.open_new_student).grid(row=0, column=0, padx=20, pady=20)
        Button(btn_frame, text="📁 View Data of All Students", font=("Arial", 16, "bold"), width=30, height=2, bg="#17a2b8", fg="white", command=self.open_view_data).grid(row=0, column=1, padx=20, pady=20)

        # Footer
        footer = Label(self.root, text="© 2025 Data Management | FaceLog System", font=("Arial", 10), bg="darkblue", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def open_new_student(self):
        subprocess.Popen(["python", "NewStudentRegister.py"])

    def open_view_data(self):
        subprocess.Popen(["python", "ViewData.py"])

def main():
    root = Tk()
    app = StudentDataPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
