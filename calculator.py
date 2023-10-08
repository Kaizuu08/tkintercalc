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
    

root = tk.Tk()
root.geometry("300x300")

## text box and grid space
text_result = tk.Text(root, height = 2, width =16, font=("Arial",24))
text_result.grid(columnspan = 5)

#runs the program window
root.mainloop()
