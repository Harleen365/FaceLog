from tkinter import *
from tkinter import ttk, messagebox
import pymongo

class StudentAttendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance Records")
        self.root.geometry("800x600+300+100")
        self.root.configure(bg="lightblue")

        # MongoDB Setup
        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.client["FaceLogDB"]
        self.attendance_collection = self.db["attendance"]

        # Load current logged-in user
        try:
            with open("current_user.txt", "r") as f:
                self.logged_in_email = f.read().strip()
        except FileNotFoundError:
            self.logged_in_email = None

        # Title
        title = Label(self.root, text="Student Attendance Records", font=("Helvetica", 20, "bold"), bg="#0a3d62", fg="white", pady=10)
        title.pack(fill=X)

        # Frame for records
        self.records_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        self.records_frame.place(x=50, y=100, width=700, height=400)

        # Scrollbars
        scroll_x = Scrollbar(self.records_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.records_frame, orient=VERTICAL)

        # Treeview (Table)
        self.attendance_table = ttk.Treeview(
            self.records_frame,
            columns=("date", "time"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table["show"] = "headings"

        self.attendance_table.column("date", anchor=CENTER, width=100)
        self.attendance_table.column("time", anchor=CENTER, width=100)

        self.attendance_table.pack(fill=BOTH, expand=1)

        self.load_attendance_records()

        # Footer
        footer = Label(self.root, text="© 2025 Student Attendance System", font=("Arial", 10), bg="#0a3d62", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def load_attendance_records(self):
        if not self.logged_in_email:
            messagebox.showerror("Error", "No logged-in student found!")
            return

        # Fetch attendance for logged-in email
        records = list(self.attendance_collection.find({"Email": self.logged_in_email}))

        if records:
            for record in records:
                self.attendance_table.insert("", END, values=(record.get("Date", ""), record.get("Time", "")))
        else:
            messagebox.showinfo("Info", "No attendance records available.")

def main():
    root = Tk()
    app = StudentAttendance(root)
    root.mainloop()

if __name__ == "__main__":
    main()
