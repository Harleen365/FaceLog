from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import subprocess

class TeacherDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Dashboard")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(False, False)

        # Load and blur background image
        bg_image = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\teacherdashboardbackground.jpg").resize((1550, 800))
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

        title = Label(navbar, text="Teacher Dashboard", font=("Helvetica", 20, "bold"), fg="white", bg="navy")
        title.pack(side=LEFT, padx=20)

        # Display user email on the right side
        Label(navbar, text=f"Logged in as: {self.logged_in_email}", font=("Arial", 12, "bold"), fg="white", bg="navy").pack(side=RIGHT, padx=20)

        Button(navbar, text="Store Data", font=("Arial", 12, "bold"), bg="#28a745", fg="white",
               command=self.open_data).pack(side=LEFT, padx=10, pady=10)
        Button(navbar, text="View Attendance", font=("Arial", 12, "bold"), bg="#007bff", fg="white",
               command=self.view_attendance).pack(side=LEFT, padx=10, pady=10)
        Button(navbar, text="Update Attendance", font=("Arial", 12, "bold"), bg="#ffc107", fg="black",
               command=self.update_attendance).pack(side=LEFT, padx=10, pady=10)

        logout_btn = Button(navbar, text="Logout", font=("Arial", 12, "bold"), bg="red", fg="white",
                            command=self.root.quit)
        logout_btn.pack(side=RIGHT, padx=20)

        # Main Button Cards (horizontally aligned)
        card_frame = Frame(self.root, bg='', pady=40)
        card_frame.place(relx=0.5, rely=0.55, anchor=CENTER)

        self.create_card(card_frame, "📁 Store Student Data", "#28a745", self.open_data, 0)
        self.create_card(card_frame, "📊 View Attendance", "#007bff", self.view_attendance, 1)
        self.create_card(card_frame, "✏️ Update Attendance", "#ffc107", self.update_attendance, 2)

        # Footer
        footer = Label(self.root, text="© 2025 Teacher Panel | FaceLog System", font=("Arial", 10), bg="navy", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def create_card(self, parent, text, color, command, col):
        card = Frame(parent, bg="white", width=250, height=180, highlightbackground=color, highlightthickness=3)
        card.grid(row=0, column=col, padx=20)
        card.grid_propagate(False)  # Fix size

        Label(card, text=text, font=("Arial", 14, "bold"), wraplength=220, bg="white", fg="black").pack(pady=20)
        Button(card, text="Open", font=("Arial", 12, "bold"), bg=color, fg="white", width=15, command=command).pack(pady=10)

    def open_data(self):
        subprocess.Popen(["python", "Data.py"])

    def view_attendance(self):
        subprocess.Popen(["python", "View Attendance.py"])

    def update_attendance(self):
        subprocess.Popen(["python", "Update Attendance.py"])

def main():
    root = Tk()
    app = TeacherDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
