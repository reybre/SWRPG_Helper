from tkinter import *
from tkinter import ttk
import random

def dice_roll(die,die_quantity,misc = 0):
    return_val = misc
    return_string = ""
    for roll in range(0,die_quantity):
        rolled_die = random.randint(1,die)
        return_val += rolled_die
        return_string += ("Roll "+str(roll+1)+": "+str(rolled_die)+"\n")
    return_string += ("------------\n")
    return_string += ("Result: "+str(return_val))
    
    return return_string
  

def dice_interpreter(*args):
    
    try:
        die_value = dice_input.get()
        if ("d" in die_value):
            if("+" in die_value):
                die_type = int(die_value[die_value.find("d")+1:die_value.find("+")])
                misc_val = int(die_value[die_value.index("+")+1:])
            else:
                die_type = int(die_value[die_value.find("d")+1:])
                misc_val = 0
            die_multiple = int(die_value[:die_value.index('d')])
            dice_output.set(die_value + "\n\n" + dice_roll(die_type,die_multiple,misc_val))
            
        else:
            dice_output.set(int(die_value))
           
        dice_input.set("")
        dice_entry.focus()
    except ValueError:
        dice_output.set("Bad input, try again")
        dice_input.set("")
        pass
root = Tk()
root.title("Dice App")

dice_input = StringVar()
dice_output = StringVar()

mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text= "Brennan's amazing Dice app").grid(column=0, row=0, sticky=(W, N))
ttk.Label(mainframe, text= "^ Enter dice combo (4d6+2) here ^").grid(column=0, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Roll Dice", command=dice_interpreter).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, textvariable=dice_output).grid(column=2, row=1, sticky=(W, E))

dice_entry = ttk.Entry(mainframe, width=7, textvariable=dice_input)
dice_entry.grid(column=0, row=1, sticky=(W, E))
dice_entry.focus()

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>', dice_interpreter)




root.mainloop()