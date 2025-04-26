from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import subprocess

class StudentDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Dashboard")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(False, False)

        # Load and blur background image
        bg_image = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\attendancematters.jpg").resize((1550, 800))
        blurred_bg = bg_image.filter(ImageFilter.GaussianBlur(radius=3))
        self.bg = ImageTk.PhotoImage(blurred_bg)

        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Load current user email
        try:
            with open("current_user.txt", "r") as f:
                self.logged_in_email = f.read().strip()
        except FileNotFoundError:
            self.logged_in_email = "Unknown User"

        # Navbar
        navbar = Frame(self.root, bg="navy", height=60)
        navbar.pack(side=TOP, fill=X)

        title = Label(navbar, text="Student Dashboard", font=("Helvetica", 20, "bold"), fg="white", bg="navy")
        title.pack(side=LEFT, padx=20)

        # Display user email on the right side
        Label(navbar, text=f"Logged in as: {self.logged_in_email}", font=("Arial", 12, "bold"), fg="white", bg="navy").pack(side=RIGHT, padx=20)

        Button(navbar, text="Take Attendance", font=("Arial", 12, "bold"), bg="#28a745", fg="white",
               command=self.take_attendance).pack(side=LEFT, padx=10, pady=10)
        Button(navbar, text="View Past Attendance", font=("Arial", 12, "bold"), bg="#007bff", fg="white",
               command=self.view_attendance).pack(side=LEFT, padx=10, pady=10)

        logout_btn = Button(navbar, text="Logout", font=("Arial", 12, "bold"), bg="red", fg="white",
                            command=self.root.quit)
        logout_btn.pack(side=RIGHT, padx=20)

        # Main Action Cards
        card_frame = Frame(self.root, bg='', pady=40)
        card_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

        self.create_card(card_frame, "📸 Take Attendance", "#28a745", self.take_attendance, 0)
        self.create_card(card_frame, "📂 View Past Attendance", "#007bff", self.view_attendance, 1)

        # Footer
        footer = Label(self.root, text="© 2025 Student Panel | FaceLog System", font=("Arial", 10), bg="navy", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def create_card(self, parent, text, color, command, col):
        card = Frame(parent, bg="white", width=280, height=180, highlightbackground=color, highlightthickness=3)
        card.grid(row=0, column=col, padx=30)
        card.grid_propagate(False)

        Label(card, text=text, font=("Arial", 14, "bold"), wraplength=240, bg="white", fg="black").pack(pady=25)
        Button(card, text="Open", font=("Arial", 12, "bold"), bg=color, fg="white", width=15, command=command).pack(pady=10)

    def take_attendance(self):
        subprocess.Popen(["python", "TakeAttendance.py"])

    def view_attendance(self):
        subprocess.Popen(["python", "StudentAttendance.py"])

def main():
    root = Tk()
    app = StudentDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
