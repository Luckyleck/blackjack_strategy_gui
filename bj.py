import os
import platform
import tkinter as tk
from tkinter import ttk, messagebox

# Actions
hit = "Hit"
stand = "Stand"
double = "Double Down"
split = "Split the pair"
surrender = "Surrender"
no_split = "Don't split the pair"
double_or_stand = "Double if allowed, otherwise stand"
double_or_hit = "Double if allowed, otherwise hit"

def clear_terminal():
    os_name = platform.system()
    if os_name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def hard_total(dealer, player):
    if player == 8:
        return hit
    elif player == 9:
        if dealer == 2 or dealer >= 7:
            return hit
        else:
            return double
    elif player == 10:
        if dealer <= 9:
            return double
        else:
            return hit
    elif player == 11:
        return double
    elif player == 12:
        if dealer < 4 or dealer > 6:
            return hit
        else:
            return stand
    elif player in range(13, 17):  # 13...16
        if dealer < 7:
            return stand
        else:
            return hit
    elif player >= 17:
        return stand
    return "Invalid input"

def soft_total(dealer, player):
    if player in range(2, 4):  # 2, 3
        if dealer < 5 or dealer > 6:
            return hit
        else:
            return double
    elif player in range(4, 6):  # 4, 5
        if dealer < 4 or dealer > 6:
            return hit
        else:
            return double
    elif player == 6:
        if dealer == 2 or dealer > 6:
            return hit
        else:
            return double
    elif player == 7:
        if dealer < 7:
            return double_or_stand
        elif dealer < 9:
            return stand
        else:
            return hit
    elif player == 8:
        if dealer == 6:
            return double_or_stand
        else:
            return stand
    elif player == 9:
        return stand
    return "Invalid input"

def pair_total(dealer, player):
    # Implement pair strategy if needed
    return "Pair splitting strategy not implemented"

def determine_action(dealer_card, player_card, total_type):
    if total_type == "h":
        return hard_total(dealer_card, player_card)
    elif total_type == "s":
        return soft_total(dealer_card, player_card)
    elif total_type == "p":
        return pair_total(dealer_card, player_card)
    return "Invalid total type"

def on_submit():
    try:
        dealer_card = int(entry_dealer.get())
        player_card = int(entry_player.get())
        total_type = total_type_var.get().lower()

        if total_type not in ['h', 's', 'p']:
            raise ValueError("Invalid total type")

        action = determine_action(dealer_card, player_card, total_type)
        action_label.config(text=f"Suggest Action: {action}")
    except ValueError as ve:
        action_label.config(text=f"Input Error: {str(ve)}")

# GUI Setup
root = tk.Tk()
root.title("Blackjack Strategy Helper")

# Apply a theme using ttk.Style
style = ttk.Style(root)
style.theme_use("clam")  # Change to 'clam', 'alt', 'default', 'classic', etc.

# Custom styles for widgets
style.configure('TLabel', background='lightgrey', font=('Roboto', 14))
style.configure('TEntry', font=('Roboto', 14))
style.configure('TRadiobutton', background='lightgrey', font=('Roboto', 12, 'italic'))
style.configure('TButton', font=('Roboto', 12, 'bold'))

# Set background color of the main window
root.configure(background='lightgrey')

# Create and place widgets using ttk
ttk.Label(root, text="Dealer upcard:").grid(row=0, column=0, padx=10, pady=5)
entry_dealer = ttk.Entry(root)
entry_dealer.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Player total:").grid(row=1, column=0, padx=10, pady=5)
entry_player = ttk.Entry(root)
entry_player.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Total type:").grid(row=2, column=0, padx=10, pady=5)

# Create a StringVar to hold the value of the selected radio button
total_type_var = tk.StringVar(value='h')  # Default to 'h' (hard)

# Create radio buttons for Hard, Soft, and Pair
radio_hard = ttk.Radiobutton(root, text="Hard", variable=total_type_var, value='h')
radio_soft = ttk.Radiobutton(root, text="Soft", variable=total_type_var, value='s')
radio_pair = ttk.Radiobutton(root, text="Pair", variable=total_type_var, value='p')

# Place the radio buttons in a row
radio_hard.grid(row=2, column=1, padx=5, pady=5, sticky="w")
radio_soft.grid(row=2, column=1, padx=5, pady=5)
radio_pair.grid(row=2, column=1, padx=5, pady=5, sticky="e")

btn_submit = ttk.Button(root, text="Submit", command=on_submit)
btn_submit.grid(row=3, columnspan=2, pady=10)

action_label = ttk.Label(root, text="", foreground="black")
action_label.grid(row=4, columnspan=2, pady=10)

# Update the window's idle tasks to calculate required dimensions
root.update_idletasks()

# Set the minimum size of the window to its current size
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
