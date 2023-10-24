import tkinter as tk
from tkinter import Listbox, Scrollbar
import random

def roll_dice(num_rolls, dice_type):
    result = []
    for _ in range(num_rolls):
        if dice_type == "d4":
            result.append(random.randint(1, 4))
        elif dice_type == "d6":
            result.append(random.randint(1, 6))
        elif dice_type == "d8":
            result.append(random.randint(1, 8))
        elif dice_type == "d10":
            result.append(random.randint(1, 10))
        elif dice_type == "d12":
            result.append(random.randint(1, 12))
        elif dice_type == "d20":
            result.append(random.randint(1, 20))
        elif dice_type == "d100":
            result.append(random.randint(1, 100))
    
    # Update the result label
    result_label.config(text=f"Result: {', '.join(map(str, result))}")

    # Update the roll history
    roll_history.append(f"{num_rolls} {dice_type} rolls: {', '.join(map(str, result))}")

    # Update the Listbox with the updated roll history
    update_roll_history()

def update_roll_history():
    roll_history_listbox.delete(0, tk.END)
    for entry in roll_history:
        roll_history_listbox.insert(tk.END, entry)
    
    # Scroll the Listbox to the end
    roll_history_listbox.see(tk.END)

def sum_history():
    total_sum = 0
    for roll in roll_history:
        parts = roll.split(":")
        if len(parts) == 2:
            num_rolls = int(parts[0].split()[0])
            values = parts[1].strip().split(',')
            for value in values:
                total_sum += int(value.strip())
        else:
            num_rolls = 0
        total_sum += num_rolls
    sum_label.config(text=f"Total Sum: {total_sum}")

def clear_history():
    roll_history.clear()
    update_roll_history()
    sum_label.config(text="Total Sum: ")

app = tk.Tk()
app.title("Dice Roller Simulator")

# Set the window size
app.geometry("400x200")

# Number of rolls input
num_rolls_label = tk.Label(app, text="Number of Rolls:")
num_rolls_label.grid(row=0, column=0)
num_rolls_entry = tk.Entry(app)
num_rolls_entry.grid(row=0, column=1)

# Dice type selection
dice_types = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
dice_type_label = tk.Label(app, text="Select Dice:")
dice_type_label.grid(row=1, column=0)
dice_type_var = tk.StringVar()
dice_type_var.set("d6")  # Default selection
dice_type_menu = tk.OptionMenu(app, dice_type_var, *dice_types)
dice_type_menu.grid(row=1, column=1)

# Result label
result_label = tk.Label(app, text="Result: ")
result_label.grid(row=2, column=0, columnspan=2)

# Roll Dice button
roll_button = tk.Button(app, text="Roll Dice", command=lambda: roll_dice(int(num_rolls_entry.get()), dice_type_var.get()))
roll_button.grid(row=3, column=0, columnspan=2)

# Roll History Listbox and Scrollbar
roll_history_frame = tk.Frame(app)
roll_history_frame.grid(row=0, column=2, rowspan=4, columnspan=3)
roll_history_listbox = Listbox(roll_history_frame, selectbackground="white", exportselection=False)
roll_history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
roll_history_scrollbar = Scrollbar(roll_history_frame, orient=tk.VERTICAL)
roll_history_listbox.config(yscrollcommand=roll_history_scrollbar.set)
roll_history_scrollbar.config(command=roll_history_listbox.yview)
roll_history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Sum History button
sum_button = tk.Button(app, text="Sum History", command=sum_history)
sum_button.grid(row=4, column=0, columnspan=2)

# Sum label
sum_label = tk.Label(app, text="Total Sum: ")
sum_label.grid(row=4, column=2, columnspan=2)

# Clear History button
clear_button = tk.Button(app, text="Clear History", command=clear_history)
clear_button.grid(row=4, column=4)

# Roll history list
roll_history = []

# Run the application
app.mainloop()