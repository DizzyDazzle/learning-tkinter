import tkinter as tk

window = tk.Tk()
window.geometry("325x325")

bg_image = tk.PhotoImage(file = "insulin.png")
frame = tk.Frame(window)
ypad = 2

halfdose_needed = tk.StringVar(frame)

top_label = tk.Label(frame, text="Dosage for Corrections", image = bg_image
)
top_label.pack(pady = ypad)


lbl_bg_input_text = tk.Label(frame, text = "Enter Current Blood Glucose:")
ety_bg_input = tk.Entry(frame, width=5)
lbl_bg_input_text.pack(pady = ypad)
ety_bg_input.pack(pady = ypad)

lbl_targetbg_input_text = tk.Label(frame, text = "What is your Target BG?")
ety_targetbg_input = tk.Entry(frame,width=5)
lbl_targetbg_input_text.pack(pady = ypad)
ety_targetbg_input.pack(pady = ypad)

lbl_correction_input_text = tk.Label(frame, text = "What is your Correction Factor?")
ety_correction_input = tk.Entry(frame,width=5)
lbl_correction_input_text.pack(pady = ypad)
ety_correction_input.pack(pady = ypad)



def calculate():
    try:
        bg = float(ety_bg_input.get())
        target_bg = float(ety_targetbg_input.get())
        correction = float(ety_correction_input.get())
        result = (bg - target_bg) / correction
        if halfdose_needed.get() == "yes":
            result = result / 2
        if bg > 200:
            ety_bg_input["bg"] = "red"
        if result < 0:
            top = tk.Toplevel(window)
            top.geometry("100x100")
            top.title("Warning")
            lbl_wrong_input_text = tk.Label(top, text = "Do not dose\ndue to no\ninsulin needed")
            lbl_wrong_input_text.pack(pady = ypad)
        ety_dosage_input.delete(0, tk.END)
        ety_dosage_input.insert(0, str(result))
    except:
        top = tk.Toplevel(window)
        top.geometry("100x100")
        top.title("Error")
        lbl_wrong_input_text = tk.Label(top, text = "Please enter\nnumerical value")
        lbl_wrong_input_text.pack(pady = ypad)

lbl_halfdose_input_text = tk.Label(frame, text = "Do you need a half dose?")
check = tk.Checkbutton(frame, text="Yes", variable = halfdose_needed,
	    onvalue='yes', offvalue='no')
check.deselect()
lbl_halfdose_input_text.pack(pady = ypad)
check.pack(pady = ypad)

btn_calcuate = tk.Button(frame, text="Calculate Dosage", command = calculate)
                        #(frame is parent, label, command runs a function)
btn_calcuate.pack(pady = ypad)

lbl_dosage_input_text = tk.Label(frame, text = "Your dosage is:")
ety_dosage_input = tk.Entry(frame,width=5)
lbl_dosage_input_text.pack(pady = ypad)
ety_dosage_input.pack(pady = ypad)



frame.pack(pady = ypad)
window.mainloop()
