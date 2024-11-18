import tkinter as tk

window = tk.Tk()
window.title("My Application")
window.geometry("500x400")

label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 20), fg="blue")
label2 = tk.Label(window, text="Hello, Tkinter!")

label.grid(row=0, column=0)
label2.grid(row=0, column=1)

input = tk.Entry(window)
input.grid(row=1, column=0)

button = tk.Button(
    window,
    text="Kirim",
    foreground="blue",
    background="white",
    font=("Arial", 24, "bold"),
)
button.grid(row=2, column=0)

window.mainloop()
