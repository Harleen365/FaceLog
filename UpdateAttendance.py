import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import pymongo

class UpdateAttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Update Attendance")
        self.root.geometry("600x400")
        self.root.configure(bg="#eef2f7")
        self.root.resizable(False, False)

        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.client["FaceLogDB"]
        self.attendance_collection = self.db["attendance"]

        self.init_ui()

    def init_ui(self):
        title = tk.Label(self.root, text="Update Student Attendance", font=("Helvetica", 20, "bold"),
                         bg="#eef2f7", fg="#2c3e50")
        title.pack(pady=30)

        # Ask for student email
        self.email = simpledialog.askstring("Student Email", "Enter student email:")
        if not self.email:
            messagebox.showwarning("Input Needed", "Student email is required.")
            self.root.destroy()
            return

        # Ask for date
        self.date = simpledialog.askstring("Attendance Date", "Enter date to update attendance (YYYY-MM-DD):")
        if not self.date:
            messagebox.showwarning("Input Needed", "Attendance date is required.")
            self.root.destroy()
            return

        try:
            # Validate date
            datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")
            self.root.destroy()
            return

        # Action Buttons
        btn_frame = tk.Frame(self.root, bg="#eef2f7")
        btn_frame.pack(pady=40)

        tk.Button(btn_frame, text="Add Attendance", width=18, bg="#27ae60", fg="white",
                  font=("Helvetica", 12, "bold"), command=self.add_attendance).grid(row=0, column=0, padx=15)

        tk.Button(btn_frame, text="Delete Attendance", width=18, bg="#c0392b", fg="white",
                  font=("Helvetica", 12, "bold"), command=self.delete_attendance).grid(row=0, column=1, padx=15)

    def add_attendance(self):
        try:
            name = simpledialog.askstring("Student Name", "Enter student name:")
            if not name:
                messagebox.showwarning("Input Needed", "Student name is required.")
                return

            current_time = datetime.now().strftime("%H:%M:%S")
            record = {
                "Name": name,
                "Email": self.email,
                "Date": self.date,
                "Time": current_time
            }

            # Prevent duplicate entry
            existing = self.attendance_collection.find_one({"Email": self.email, "Date": self.date})
            if existing:
                messagebox.showinfo("Already Exists", f"Attendance already exists for {self.date}.")
                return

            self.attendance_collection.insert_one(record)
            messagebox.showinfo("Success", f"Attendance added for {name} on {self.date}.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_attendance(self):
        try:
            result = self.attendance_collection.delete_one({"Email": self.email, "Date": self.date})
            if result.deleted_count == 0:
                messagebox.showinfo("Not Found", "No attendance record found to delete.")
            else:
                messagebox.showinfo("Deleted", f"Attendance on {self.date} has been deleted.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = UpdateAttendanceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
