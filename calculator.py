"""The program utilises the tkinter module to createa a simple addition and minus graphical user interface calculator"""

import tkinter as tk
## store calculator calculations
calculation = ""

## function to calculate and text box display
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end") #delets text result field
    text_result.insert(1.0, calculation)

## function to evaluate 
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        
## function to clear field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    
## function to togle display
def toggle_mode():
    current_bg = root.cget("background")
    if current_bg == "black":
        # Switch to light mode
        root.configure(background="white")
        set_text_color("black")
        text_result.configure(bg="white", fg="black")
    else:
        # Switch to night mode
        root.configure(background="black")
        set_text_color("white")
        text_result.configure(bg="black", fg="white")

## function to change text colour
def set_text_color(color):
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Button, tk.Text)):
            widget.configure(foreground=color)
    

root = tk.Tk()
root.geometry("300x300")

## text box and grid space
text_result = tk.Text(root, height = 2, width =16, font=("Arial",24))
text_result.grid(columnspan = 5)

## button interfaces
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14)) ## lambda allows number to be added to calculation
btn_0.grid(row=5, column=2)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))
btn_equals.grid(row=6, column=4)

btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14)) 
btn_clear.grid(row=5, column=1)

btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multiply.grid(row=4, column=4)

btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14)) 
btn_divide.grid(row=5, column=4)

btn_bracket1 = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_bracket1.grid(row=6, column=1)

btn_bracket2 = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14)) 
btn_bracket2.grid(row=6, column=2)

btn_night_mode = tk.Button(root, text="Night", command=toggle_mode, width=5, font=("Arial", 14))
btn_night_mode.grid(row=5, column=3)

btn_light_mode = tk.Button(root, text="Light", command=toggle_mode, width=5, font=("Arial", 14))
btn_light_mode.grid(row=6, column=3)


## runs the program window
root.mainloop()
