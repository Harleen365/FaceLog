import cv2
import os
import shutil
import pymongo
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from deepface import DeepFace

class TakeAttendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Take Attendance")
        self.root.geometry("1000x700+100+50")

        # MongoDB Setup
        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.client["FaceLogDB"]
        self.students_collection = self.db["students"]
        self.attendance_collection = self.db["attendance"]

        self.recognized_email = None
        self.student_name = None
        self.captured_image_path = "captured.jpg"
        self.temp_db_dir = "temp_face_db"

        Label(root, text="Click below to mark your attendance", font=("Arial", 16)).pack(pady=20)
        Button(root, text="Start Camera", font=("Arial", 12), bg="green", fg="white", command=self.capture_image).pack(pady=10)

        self.image_label = Label(root)
        self.image_label.pack(pady=10)

        self.submit_button = Button(root, text="Submit Attendance", font=("Arial", 12), bg="blue", fg="white", command=self.submit_attendance, state=DISABLED)
        self.submit_button.pack(pady=10)

        Button(root, text="Close", font=("Arial", 12), bg="red", fg="white", command=self.root.quit).pack(pady=5)

    def load_student_images(self):
        if os.path.exists(self.temp_db_dir):
            shutil.rmtree(self.temp_db_dir)
        os.makedirs(self.temp_db_dir)

        self.student_map = {}  # Maps file name to student email and name

        students = list(self.students_collection.find())
        for student in students:
            photo_path = student.get("Photograph")
            email = student.get("Email")
            name = student.get("Name")
            if photo_path and os.path.exists(photo_path):
                file_name = f"{email.replace('@', '_at_')}.jpg"
                dest_path = os.path.join(self.temp_db_dir, file_name)
                shutil.copy(photo_path, dest_path)
                self.student_map[file_name] = {"email": email, "name": name}

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Failed to open webcam.")
            return

        messagebox.showinfo("Instructions", "Look at the camera. Press 's' to capture or 'q' to quit.")
        while True:
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to read from camera.")
                break

            cv2.imshow("Press 's' to Capture | 'q' to Quit", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                cv2.imwrite(self.captured_image_path, frame)
                break
            elif key == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return

        cap.release()
        cv2.destroyAllWindows()

        self.show_captured_image()
        self.load_student_images()
        self.perform_face_recognition()

    def show_captured_image(self):
        if os.path.exists(self.captured_image_path):
            image = Image.open(self.captured_image_path).resize((300, 300))
            img_tk = ImageTk.PhotoImage(image)
            self.image_label.configure(image=img_tk)
            self.image_label.image = img_tk

    def perform_face_recognition(self):
        try:
            # Load logged-in user's email
            try:
                with open("current_user.txt", "r") as f:
                    current_logged_in_email = f.read().strip()
            except FileNotFoundError:
                messagebox.showerror("Error", "No logged-in user found.")
                return

            results = DeepFace.find(
                img_path=self.captured_image_path,
                db_path=self.temp_db_dir,
                enforce_detection=False,
                model_name='VGG-Face',
                detector_backend='opencv'
            )

            if len(results) > 0 and not results[0].empty:
                top_match_path = results[0].iloc[0]["identity"]
                file_name = os.path.basename(top_match_path)
                matched = self.student_map.get(file_name)

                if matched:
                    recognized_email = matched["email"]
                    recognized_name = matched["name"]

                    if recognized_email == current_logged_in_email:
                        self.recognized_email = recognized_email
                        self.student_name = recognized_name
                        messagebox.showinfo("Recognized", f"Welcome, {self.student_name}!")
                        self.submit_button.config(state=NORMAL)
                    else:
                        self.recognized_email = None
                        self.student_name = None
                        messagebox.showerror("Error", "You are not the student who logged in.\nAttendance not allowed.")
                        self.submit_button.config(state=DISABLED)
                else:
                    messagebox.showerror("Error", "Face not recognized.")
            else:
                messagebox.showerror("Error", "No matching face found.")

        except Exception as e:
            messagebox.showerror("Error", f"Face recognition failed.\n{e}")


    def submit_attendance(self):
        if not self.recognized_email:
            messagebox.showerror("Error", "No recognized student.")
            return

        today = datetime.now().strftime("%Y-%m-%d")
        if self.attendance_collection.find_one({"Email": self.recognized_email, "Date": today}):
            messagebox.showinfo("Info", "Attendance already marked.")
        else:
            self.attendance_collection.insert_one({
                "Email": self.recognized_email,
                "Name": self.student_name,
                "Date": today,
                "Time": datetime.now().strftime("%H:%M:%S")
            })
            messagebox.showinfo("Success", "Attendance marked successfully!")

        self.submit_button.config(state=DISABLED)

        if os.path.exists(self.captured_image_path):
            os.remove(self.captured_image_path)

        if os.path.exists(self.temp_db_dir):
            shutil.rmtree(self.temp_db_dir)

if __name__ == "__main__":
    root = Tk()
    app = TakeAttendance(root)
    root.mainloop()
