import cv2
import os
import pymongo
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from deepface import DeepFace

class TakeAttendance:
    def __init__(self, root, logged_in_email):
        self.root = root
        self.root.title("Take Attendance")
        self.root.geometry("1000x700+100+50")
        self.logged_in_email = logged_in_email

        # MongoDB Setup
        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.client["FaceLogDB"]
        self.students_collection = self.db["students"]
        self.attendance_collection = self.db["attendance"]

        self.recognized_email = None
        self.student_name = None
        self.captured_image_path = "captured.jpg"
        self.cap = None

        Label(root, text="Click below to mark your attendance", font=("Arial", 16)).pack(pady=20)

        Button(root, text="Start Camera", font=("Arial", 12), bg="green", fg="white", command=self.start_camera).pack(pady=10)
        self.image_label = Label(root)
        self.image_label.pack(pady=10)

        self.submit_button = Button(root, text="Submit Attendance", font=("Arial", 12), bg="blue", fg="white", command=self.submit_attendance, state=DISABLED)
        self.submit_button.pack(pady=10)

        Button(root, text="Close", font=("Arial", 12), bg="red", fg="white", command=self.close_app).pack(pady=5)

    def load_student_images(self):
        student_images = {}
        students = list(self.students_collection.find())
        for student in students:
            photo_path = student.get("Photograph")
            email = student.get("Email")
            name = student.get("Name")
            if photo_path and email and os.path.exists(photo_path):
                student_images[email] = {"path": photo_path, "name": name}
        return student_images

    def start_camera(self):
        student_images = self.load_student_images()
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            messagebox.showerror("Error", "Failed to open webcam.")
            return

        self.recognized_email = None
        self.student_name = None

        messagebox.showinfo("Instructions", "Look into the camera. Press 's' to capture image or 'q' to quit.")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to read from camera.")
                break

            for email, data in student_images.items():
                try:
                    result = DeepFace.verify(frame, data["path"], enforce_detection=False)
                    if result["verified"]:
                        self.recognized_email = email
                        self.student_name = data["name"]
                        cv2.putText(frame, f"Student: {self.student_name}", (20, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        break
                except:
                    continue

            cv2.imshow("Press 's' to Capture | 'q' to Quit", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('s'):
                if self.recognized_email:
                    cv2.imwrite(self.captured_image_path, frame)
                else:
                    messagebox.showerror("Error", "Face not recognized.")
                break
            elif key == ord('q'):
                break

        self.stop_camera()

        if self.recognized_email:
            self.show_captured_image()
            self.submit_button.config(state=NORMAL)

    def stop_camera(self):
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()

    def show_captured_image(self):
        if os.path.exists(self.captured_image_path):
            image = Image.open(self.captured_image_path)
            image = image.resize((300, 300))
            img_tk = ImageTk.PhotoImage(image)
            self.image_label.configure(image=img_tk)
            self.image_label.image = img_tk

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

        # Disable button again
        self.submit_button.config(state=DISABLED)

        # Remove captured image
        if os.path.exists(self.captured_image_path):
            os.remove(self.captured_image_path)

    def close_app(self):
        self.stop_camera()
        self.root.quit()

if __name__ == "__main__":
    # Replace this with the email of the currently logged-in student
    logged_in_email = "student1@example.com"

    root = Tk()
    app = TakeAttendance(root, logged_in_email)
    root.mainloop()
