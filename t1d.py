import tkinter as tk
from PIL import ImageTk, Image     #Python Image Library   to install run "pip install Pillow" in bash with no ""
import pprint

screen_width, screen_height = 350, 540
ypadding = screen_height // 4

font_size = int(((screen_width + screen_height) // 2) * 0.035)#this may look lie some genius shit but it was just a great guess
main_font = f"Helvetica {font_size} bold"
gap = font_size




window = tk.Tk()
window.geometry(f"{screen_width}x{screen_height}")
window.minsize(screen_width, screen_height)
bg_image = Image.open("bkgrnd.png")
canvas = tk.Canvas(window, width = screen_width, height = screen_height)


def calculate():
    try:
        current_bg = float(ety_current_bg.get())
        target_bg = float(ety_target_bg.get())
        correction = float(ety_correction.get())
        result = (current_bg - target_bg) / correction
        if halfdose_needed.get() == "yes":
            result = result / 2
        if current_bg > 200:
            ety_current_bg["bg"] = "red"
        if result < 0:
            top = tk.Toplevel(window)
            top.geometry("100x100")
            top.title("Warning")
            lbl_wrong = tk.Label(top, text = "Do not dose\ndue to no\ninsulin needed")
            lbl_wrong.pack()
        ety_dosage.delete(0, tk.END)
        ety_dosage.insert(0, str(result))
    except:
        top = tk.Toplevel(window)
        top.geometry("100x100")
        top.title("Error")
        lbl_wrong_text = tk.Label(top, text = "Please enter\nnumerical value")
        lbl_wrong_text.pack()





def resize_window(e):#e is for event, anytime we resize the window window.bind calls this function and passes in the event of the window size changing so we can get new w and h
    global bg_image_resize, new_bg, bg_image, screen_width, screen_height, font_size, main_font, ypadding
    canvas.delete("all")
    screen_width = e.width
    screen_height = e.height
    bg_image_resize = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
    new_bg = ImageTk.PhotoImage(bg_image_resize)
    canvas.create_image(0, 0, image=new_bg, anchor="nw")
    font_size = int(((screen_width + screen_height) // 2) * 0.035)
    main_font = f"Helvetica {font_size} bold"
    ypadding = screen_height // 4
    load_widgits()


halfdose_needed = tk.StringVar(window)
ety_current_bg = tk.Entry(window, width=5, font=main_font)
ety_target_bg = tk.Entry(window,width=5, font=main_font)
ety_correction = tk.Entry(window,width=5, font=main_font)
cb_halfdose_needed = tk.Checkbutton(window, text="Yes", variable = halfdose_needed,
        onvalue='yes', offvalue='no', font=main_font)
cb_halfdose_needed.deselect()
btn_calcuate = tk.Button(window, text="Calculate Dosage", command = calculate, font=main_font)
ety_dosage = tk.Entry(window,width=5, font=main_font)



def load_widgits():
    global ypadding


    widgits = [
            "Enter Current Blood Glucose:",
            [ety_current_bg, None],
            "What is your Target BG?",
            [ety_target_bg, None],
            "What is your Correction Factor?",
            [ety_correction, None],
            "Do you need a half dose?",
            [cb_halfdose_needed, None],
            [btn_calcuate, None],
            "Your dosage is:",
            [ety_dosage, None],
        ]
    for i in range(len(widgits)):

        x = screen_width // 2
        y = (i * font_size) + (i * gap) + ypadding
        if type(widgits[i]) == str:
            canvas.create_text(x, y + font_size // 4, text=widgits[i], font=main_font, fill="yellow", justify='center', anchor="n")
        else:
            canvas.create_window(x, y, anchor="n", window=widgits[i][0])
            widgits[i][0].configure(font=main_font, fg="black", bg="white")


canvas.pack(fill= "both", expand=True)
canvas.bind("<Configure>", resize_window)
canvas.addtag_all("all")
window.mainloop()
