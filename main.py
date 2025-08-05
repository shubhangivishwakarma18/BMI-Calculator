import tkinter as tk
from gui2 import GUI

def main():
    root = tk.Tk()
    root.title("BMI Calculator")
    gui2 = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
