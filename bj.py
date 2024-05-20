import os
import platform
import tkinter as tk
from tkinter import messagebox

def clear_terminal():
    os_name = platform.system()
    if os_name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def hard_total(dealer, player):
    if player == 8:
        return "Hit"
    elif player == 9:
        if dealer == 2 or dealer >= 7:
            return "Hit"
        else:
            return "Double"
    elif player == 10:
        if dealer <= 9:
            return "Double"
        else:
            return "Hit"
    elif player == 11:
        return "Double"
    elif player == 12:
        if dealer < 4 or dealer > 6:
            return "Hit"
        else:
            return "Stand"
    elif player in range(13, 17):  # 13...16
        if dealer < 7:
            return "Stand"
        else:
            return "Hit"
    elif player >= 17:
        return "Stand"
    return "Invalid input"

def soft_total(dealer, player):
    if player in range(2, 4):  # 2, 3
        if dealer < 5 or dealer > 6:
            return "Hit"
        else:
            return "Double"
    elif player in range(4, 6):  # 4, 5
        if dealer < 4 or dealer > 6:
            return "Hit"
        else:
            return "Double"
    elif player == 6:
        if dealer == 2 or dealer > 6:
            return "Hit"
        else:
            return "Double"
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
        total_type = entry_total_type.get().lower()

        if total_type not in ['h', 's', 'p']:
            raise ValueError("Invalid total type")

        action = determine_action(dealer_card, player_card, total_type)
        messagebox.showinfo("Suggested Action", action)
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))


# GUI Setup
root = tk.Tk()
root.title("Blackjack Strategy Helper")


tk.Label(root, text="Dealer upcard:").grid(row=0, column=0, padx=10, pady=10)
entry_dealer = tk.Entry(root)
entry_dealer.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Player total:").grid(row=1, column=0, padx=10, pady=5)
entry_player = tk.Entry(root)
entry_player.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Total type (h/s/p):").grid(row=2, column=0, padx=10, pady=5)
entry_total_type = tk.Entry(root)
entry_total_type.grid(row=2, column=1, padx=10, pady=5)

btn_submit = tk.Button(root, text="Submit", command=on_submit)
btn_submit.grid(row=3, columnspan=2, pady=10)

tk.OptionMenu(root, text="test").grid(row=2, column=0, padx=10, pady=5)
option_menu = tk.Entry(root)
option_menu.grid(row=3, columnspan=3, pady=10)

root.mainloop()