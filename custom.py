import customtkinter as ctk

# Set theme and initialize main window
ctk.set_default_color_theme("dark-blue")
main = ctk.CTk()
main.geometry("700x600")
main.title("Simple CustomTkinter Main")

# Create labels
label = ctk.CTkLabel(main, text="Sustainable Investment", font=("Verdana", 50))
label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

label_title = ctk.CTkLabel(main, text="Login", font=("Verdana", 40))
label_title.grid(row=1, column=0, columnspan=2, pady=20)

# Create entry fields
entry_username = ctk.CTkEntry(main, placeholder_text="Username", width=200)
entry_username.grid(row=2, column=0, columnspan=2, pady=10)

entry_password = ctk.CTkEntry(main, placeholder_text="Password", show="*", width=200)
entry_password.grid(row=3, column=0, columnspan=2, pady=10)

# Define button actions
def clickme():
    label.configure(text="Button clicked!")

def close():
    main.destroy()

# Create buttons
button_new_user = ctk.CTkButton(main, text="New User", command=clickme)
button_new_user.grid(row=4, column=0, padx=10, pady=20)

button_login = ctk.CTkButton(main, text="Login Now", command=clickme)
button_login.grid(row=4, column=1, padx=10, pady=20)

button_close = ctk.CTkButton(main, text="Close", command=close)
button_close.grid(row=5, column=0, columnspan=2, pady=20)

# Start the main loop
main.mainloop()
