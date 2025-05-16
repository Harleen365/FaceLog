import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import pymongo

class AnalyseAttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyse Attendance")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f2f5")
        self.root.resizable(False, False)

        title = tk.Label(self.root, text="Analyse Student Attendance", font=("Helvetica", 20, "bold"), bg="#f0f2f5", fg="#333")
        title.pack(pady=20)

        self.ask_email()

    def ask_email(self):
        email = simpledialog.askstring("Enter Email", "Please enter student's email to fetch attendance:")
        if email:
            self.fetch_attendance(email)
        else:
            messagebox.showinfo("Input Required", "No email entered.")

    def fetch_attendance(self, email):
        try:
            client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
            db = client["FaceLogDB"]
            collection = db["attendance"]

            # Correct case-sensitive field name
            records = list(collection.find({"Email": email}))

            if not records:
                messagebox.showinfo("No Records", f"No attendance records found for '{email}'.")
                return

            # Table Frame
            table_frame = tk.Frame(self.root, bg="#f0f2f5")
            table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            # Scrollbars
            scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
            scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)

            # Treeview Table
            self.attendance_table = ttk.Treeview(
                table_frame,
                columns=("Name", "Email", "Date", "Time"),
                xscrollcommand=scroll_x.set,
                yscrollcommand=scroll_y.set,
                show='headings',
                height=10
            )

            scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
            scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
            scroll_x.config(command=self.attendance_table.xview)
            scroll_y.config(command=self.attendance_table.yview)

            self.attendance_table.heading("Name", text="Name")
            self.attendance_table.heading("Email", text="Email")
            self.attendance_table.heading("Date", text="Date")
            self.attendance_table.heading("Time", text="Time")

            self.attendance_table.column("Name", width=150)
            self.attendance_table.column("Email", width=220)
            self.attendance_table.column("Date", width=100)
            self.attendance_table.column("Time", width=100)

            self.attendance_table.pack(fill=tk.BOTH, expand=True)

            # Insert records into the table
            for record in records:
                self.attendance_table.insert("", tk.END, values=(
                    record.get("Name", ""),
                    record.get("Email", ""),
                    record.get("Date", ""),
                    record.get("Time", "")
                ))

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")

def main():
    root = tk.Tk()
    app = AnalyseAttendanceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

