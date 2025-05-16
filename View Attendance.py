from tkinter import *
from PIL import Image, ImageTk
import subprocess

class ViewAttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("View Attendance")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(False, False)

        # Load background image (no blur)
        bg_image = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\Viewattendance.jpg").resize((1550, 800))
        self.bg = ImageTk.PhotoImage(bg_image)

        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Navbar
        navbar = Frame(self.root, bg="#003366", height=60)
        navbar.pack(side=TOP, fill=X)

        Label(navbar, text="📋 View Attendance", font=("Helvetica", 20, "bold"), fg="white", bg="#003366").pack(side=LEFT, padx=20)

        Button(navbar, text="Analyse Attendance", font=("Arial", 12, "bold"), bg="#0056b3", fg="white",
               activebackground="#004494", activeforeground="white", command=self.open_analyse_attendance,
               padx=10, pady=5).pack(side=LEFT, padx=10, pady=10)

        Button(navbar, text="Update Attendance", font=("Arial", 12, "bold"), bg="#ffcc00", fg="black",
               activebackground="#e6b800", activeforeground="black", command=self.open_update_attendance,
               padx=10, pady=5).pack(side=LEFT, padx=10, pady=10)

        Button(navbar, text="Logout", font=("Arial", 12, "bold"), bg="red", fg="white",
               activebackground="#cc0000", command=self.root.quit,
               padx=10, pady=5).pack(side=RIGHT, padx=20)

        # Body frame (centered)
        body_frame = Frame(self.root, bg="#ffffff", bd=2, relief=RIDGE)
        body_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        Label(body_frame, text="Manage Attendance", font=("Helvetica", 26, "bold"), fg="#003366", bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=30)

        # Horizontal layout for the buttons
        analyse_btn = Button(body_frame, text="📊 Analyse Attendance", font=("Arial", 14, "bold"),
                             bg="#007bff", fg="white", width=25, height=2,
                             activebackground="#006ae6", activeforeground="white",
                             command=self.open_analyse_attendance)
        analyse_btn.grid(row=1, column=0, padx=30, pady=20)

        update_btn = Button(body_frame, text="✏️ Update Attendance", font=("Arial", 14, "bold"),
                            bg="#ffc107", fg="black", width=25, height=2,
                            activebackground="#e6b800", activeforeground="black",
                            command=self.open_update_attendance)
        update_btn.grid(row=1, column=1, padx=30, pady=20)

        # Footer
        footer = Label(self.root, text="© 2025 FaceLog System | Attendance Management",
                       font=("Arial", 10, "italic"), bg="#003366", fg="white", pady=5)
        footer.pack(side=BOTTOM, fill=X)

    def open_analyse_attendance(self):
        subprocess.Popen(["python", "AnalyseAttendance.py"])

    def open_update_attendance(self):
        subprocess.Popen(["python", "UpdateAttendance.py"])

def main():
    root = Tk()
    app = ViewAttendanceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
