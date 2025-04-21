from tkinter import *
from PIL import Image, ImageTk
import pymongo
import os

class ViewData:
    def __init__(self, root):
        self.root = root
        self.root.title("View Student Data")
        self.root.geometry("1550x850+0+0")

        self.image_refs = []

        # MongoDB Setup
        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.client["FaceLogDB"]
        self.collection = self.db["students"]

        # Background
        bg_image = Image.open(r"C:\Users\ishut\Downloads\FaceLog\Images\Viewdatabackground.jpeg").resize((1550, 850))
        bg_image = bg_image.convert("RGBA")
        bg_image.putalpha(180)
        self.bg = ImageTk.PhotoImage(bg_image)
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Navbar
        navbar = Frame(self.root, bg="darkgreen", height=60)
        navbar.pack(side=TOP, fill=X)
        Label(navbar, text="Student Records", font=("Helvetica", 20, "bold"), fg="white", bg="darkgreen").pack(side=LEFT, padx=20)
        Button(navbar, text="Back", font=("Arial", 12), bg="red", fg="white", command=self.root.destroy).pack(side=RIGHT, padx=20, pady=10)

        # Scrollable Frame
        self.canvas = Canvas(self.root, bg="white", highlightthickness=0)
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, bg="white")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=10)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.display_data_grouped()

        # Footer
        footer = Label(self.root, text="© 2025 FaceLog System", font=("Arial", 10), bg="darkgreen", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def display_data_grouped(self):
        records = list(self.collection.find())

        grouped = {}
        for record in records:
            key = f"{record.get('Branch', '')}-{record.get('Course', '')}-{record.get('Group', '')}-{record.get('Mentor', '')}"
            grouped.setdefault(key, []).append(record)

        for key, students in grouped.items():
            # Group Header
            group_label = Label(self.scrollable_frame, text=key, font=("Arial", 16, "bold"), bg="white", anchor="w")
            group_label.pack(fill=X, pady=(15, 5), padx=10)

            # Table Headers
            header_frame = Frame(self.scrollable_frame, bg="#e0e0e0")
            header_frame.pack(fill=X, padx=30)

            headers = ["Photo", "Name", "Email", "Accommodation", "Course", "Branch", "Group", "Mentor"]
            widths = [60, 130, 180, 130, 130, 130, 100, 130]
            for text, w in zip(headers, widths):
                Label(header_frame, text=text, font=("Arial", 10, "bold"), bg="#e0e0e0", width=w//10, anchor="center").pack(side=LEFT, padx=2)

            # Student Entries
            for student in students:
                entry_frame = Frame(self.scrollable_frame, bg="white")
                entry_frame.pack(fill=X, padx=30, pady=2)

                img_path = student.get("Photograph", "")
                img = self.load_image_thumbnail(img_path)
                self.image_refs.append(img)

                Label(entry_frame, image=img, bg="white").pack(side=LEFT, padx=5, pady=5)

                Label(entry_frame, text=student.get("Name", ""), width=13, anchor="center", bg="white").pack(side=LEFT, padx=5)
                Label(entry_frame, text=student.get("Email", ""), width=18, anchor="center", bg="white").pack(side=LEFT, padx=5)
                Label(entry_frame, text=student.get("Accommodation", ""), width=13, anchor="center", bg="white").pack(side=LEFT, padx=5)
                Label(entry_frame, text=student.get("Course", ""), width=13, anchor="center", bg="white").pack(side=LEFT, padx=5)
                Label(entry_frame, text=student.get("Branch", ""), width=13, anchor="center", bg="white").pack(side=LEFT, padx=5)
                Label(entry_frame, text=student.get("Group", ""), width=10, anchor="center", bg="white").pack(side=LEFT, padx=5)
                Label(entry_frame, text=student.get("Mentor", ""), width=13, anchor="center", bg="white").pack(side=LEFT, padx=5)

    def load_image_thumbnail(self, path):
        try:
            if path and os.path.exists(path):
                img = Image.open(path).resize((50, 50))
            else:
                img = Image.new("RGB", (50, 50), color="gray")
        except:
            img = Image.new("RGB", (50, 50), color="gray")
        return ImageTk.PhotoImage(img)

# Run the App
if __name__ == "__main__":
    root = Tk()
    app = ViewData(root)
    root.mainloop()

