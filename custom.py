import customtkinter as ctk

# Set theme and initialize main window
ctk.set_default_color_theme("dark-blue")
main = ctk.CTk()
main.geometry("700x600")
main.title("Simple CustomTkinter Main")

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "user" and password == "pass":
        newlabel = ctk.CTkLabel(main, text="Login Successful", font=("Verdana", 20))
        newlabel.grid(row=5, column=0, columnspan=2, pady=20, padx=10)
        newwindow()
    else:
        label_message.configure(text="Login Failed", text_color="red")

def signup():
    signup_window = ctk.CTkToplevel()
    signup_window.geometry("400x300")
    signup_window.title("Signup")
    #signup_window.attributes("-topmost", True) 

    label_signup_title = ctk.CTkLabel(signup_window, text="Signup", font=("Arial", 20))
    label_signup_title.pack(pady=10)

    entry_signup_username = ctk.CTkEntry(signup_window, placeholder_text="Username", width=200)
    entry_signup_username.pack(pady=10)

    entry_signup_password = ctk.CTkEntry(signup_window, placeholder_text="Password", show="*", width=200)
    entry_signup_password.pack(pady=10)

    button_signup = ctk.CTkButton(signup_window, text="Create Account", command=lambda: newacc(entry_signup_username.get(), entry_signup_password.get()))
    button_signup.pack(pady=20)

def newacc(username, password):
    # Here, you can add logic to save the new account (e.g., in a database or file)
    print(f"New account created for: {username} with password: {password}")
    # Close the signup window after account creation
    for widget in main.winfo_children():
        if isinstance(widget, ctk.CTkToplevel):
            widget.destroy()

def newwindow():
    newwin = ctk.CTkToplevel()
    newwin.geometry("600x600")
    newwin.title("Dashboard")
    label_dashboard = ctk.CTkLabel(newwin, text="Welcome to the Dashboard", font=("Arial", 40))
    label_dashboard.grid(row=3, column=0)
    button_close = ctk.CTkButton(newwin, text="Close", command=close)
    button_close.grid(row=5, column=0, columnspan=2, pady=20)

    main.withdraw()

# Create labels
label = ctk.CTkLabel(main, text="Sustainable Investment", font=("Verdana", 50))
label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

label_title = ctk.CTkLabel(main, text="Login", font=("Verdana", 40))
label_title.grid(row=1, column=0, columnspan=2, pady=20)

label_message = ctk.CTkLabel(main, text="", font=("Arial", 14))
label_message.grid(row=4, column=0)

# Create entry fields
entry_username = ctk.CTkEntry(main, placeholder_text="Username", width=200)
entry_username.grid(row=2, column=0, columnspan=2, pady=10)

entry_password = ctk.CTkEntry(main, placeholder_text="Password", show="*", width=200)
entry_password.grid(row=3, column=0, columnspan=2, pady=10)

def close():
    main.destroy()

# Create buttons
button_new_user = ctk.CTkButton(main, text="New User", command=signup)
button_new_user.grid(row=4, column=0, padx=10, pady=20)

button_login = ctk.CTkButton(main, text="Login Now", command=login)
button_login.grid(row=4, column=1, padx=10, pady=20)

button_close = ctk.CTkButton(main, text="Close", command=close)
button_close.grid(row=5, column=0, columnspan=2, pady=20)

# Start the main loop
main.mainloop()
