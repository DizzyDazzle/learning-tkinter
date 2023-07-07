import tkinter as tk

window = tk.Tk()

frame = tk.Frame(window)

label = tk.Label(frame, text="This is a label")
label.pack()

button_label_text = tk.StringVar()
button_label = tk.Label(frame, textvariable = button_label_text)
def click():
    button_label_text.set(entry.get())

button = tk.Button(frame, text="Click Me", command = click)
button.pack()
button_label.pack()


entry = tk.Entry(frame, width=30)
entry.insert(0, "This is an entry")
entry.pack()

frame.pack()


frame2 = tk.Frame(window)
sum = tk.StringVar(frame2, "Result", "sum")


def button2_click():
    x = int(entry1.get())
    y = int(entry2.get())
    sum.set(str(x + y))
    entry3.delete(0, tk.END)
    entry3.insert(0, sum.get())




entry1 = tk.Entry(frame2, width=5)
entry1.insert(0, "1")
entry1.pack()
entry2 = tk.Entry(frame2, width=5)
entry2.insert(0, "2")
entry2.pack()

button2 = tk.Button(frame2, text="Add", command = button2_click)
button2.pack()
entry3 = tk.Entry(frame2, width=5)

entry3.pack()
entry3.insert(0, sum.get())
button2.pack()
frame2.pack()
window.mainloop()
