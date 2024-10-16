import tkinter as tk
import os

root = tk.Tk()
root.geometry("400x250")
root.title("Python to EXE converter")
root.configure(bg="grey")

def conv(path):
    cmd = "cmd /c title Log Console (Do not close) & pyinstaller --onefile \"" + path + "\""
    os.system(cmd)
    print("\n\nDone!")

def send():
    value = in1.get()

    if os.path.exists(value):
        conv(value)

tx1 = tk.Label(root, text="Python to EXE converter")
tx1.configure(fg="#ffffff", font=("Helvetica", 20, "bold"), bg="grey")

marg1 = tk.Label(root, text=" ")
marg1.configure(bg="grey", fg="grey", font=("Arial", 10))

tx2 = tk.Label(root, text="PY file path:")
tx2.configure(bg="grey", fg="#ffffff", font=("Arial", 10))

in1 = tk.Entry(root, width=60)
in1.configure(bg="#ffffff")

marg2 = tk.Label(root, text=" ")
marg2.configure(bg="grey", fg="grey", font=("Arial", 5))

in2 = tk.Button(root, text="GENERATE", command=send)
in2.configure(bg="#ffffff", fg="green", font=("Helvetica", 15, "bold"))

tx1.pack()
marg1.pack()
tx2.pack()
in1.pack()

marg2.pack(side="bottom")
in2.pack(side="bottom")

root.mainloop()