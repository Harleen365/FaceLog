from tkinter import *
from tkinter import messagebox

def main():
    root = Tk()
    root.title("Student Dashboard")
    root.geometry("600x400")

    Label(root, text="Welcome to Student Dashboard", font=("Arial", 20, "bold")).pack(pady=50)
    Button(root, text="Logout", font=("Arial", 14), command=root.destroy).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
