
import customtkinter as ctk
from PIL import Image,ImageTk

# Set theme and initialize main window
ctk.set_default_color_theme("dark-blue")
main = ctk.CTk()
main.geometry("700x600")
main.title("Simple CustomTkinter Main")

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "Vihan" and password == "pass":
        label_title.configure(text='Login Successfull')
        newwindow(username)
    else:
        label_title.configure(text="Login Failed", text_color="red",font=20)

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

def newwindow(username):
    newwin = ctk.CTkToplevel()
    newwin.geometry("1000x1000")
    newwin.title("Dashboard")
    
    labeld = ctk.CTkLabel(newwin, text=f"Welcome, {username}" , font=("Arial", 40))
    labeld.grid(row=3, column=1)
    
    labeld1 = ctk.CTkLabel(newwin, text="Lets Start Your Investment Journey!!", font=("Arial", 28))
    labeld1.grid(row=4, column=2)

    labeld2 = ctk.CTkLabel(newwin, text="Enter your monthly salary", font=("Arial", 22))
    labeld2.grid(row=5, column=2)

    entry1= ctk.CTkEntry(newwin, placeholder_text="Salary", width=300)
    entry1.grid(row=5, column=3)

    labeld3 = ctk.CTkLabel(newwin, text="Savings Categories: \n Category A- 0-10% \n Category B- 10-15% \n Category C-15-20% ", font=("Arial", 22))
    labeld3.grid(row=2, column=2)

    labeld3 = ctk.CTkLabel(newwin, text="Enter your savings of this month", font=("Arial", 22))
    labeld3.grid(row=6, column=2)

    entry2= ctk.CTkEntry(newwin, placeholder_text="Savings", width=300)
    entry2.grid(row=6, column=3)

    labeld4 = ctk.CTkLabel(newwin, text="Your Saving Category is ", font=("Arial", 22))
    labeld4.grid(row=9, column=2)



    button_close = ctk.CTkButton(newwin, text="Close", command=newwin.destroy)
    button_close.grid(row=9, column=2, columnspan=2, pady=20)



    
    # Hide the main window
    main.withdraw()

bg_image = Image.open(r"C:\Users\Vihan\desktop\icon3.webp")  # Make sure the path is correct
bg_image = bg_image.resize((150,130))  # Resize if necessary
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = ctk.CTkLabel(main, image=bg_photo)
bg_label.place(x=290,y=10)

# Create labels
name=ctk.CTkLabel(main,text="SustainVest",font=("Arial ",40))
name.place(x=240,y=120)
label = ctk.CTkLabel(main, text="Make Sustainable Investment", font=("Arial", 30),bg_color="transparent",fg_color='transparent')
label.place(x=170,y=180)

label_title = ctk.CTkLabel(main, text="", font=("arial", 20))
label_title.place(x=290,y=440)

# Create entry fields
entry_username = ctk.CTkEntry(main, placeholder_text="Username", width=300)
entry_username.place(x=200,y=260)


entry_password = ctk.CTkEntry(main, placeholder_text="Password", show="*", width=300)
entry_password.place(x=200,y=310)

# Define button actions
def clickme():
    label.configure(text="Button clicked!")

def close():
    main.destroy()

# Create buttons
button_new_user = ctk.CTkButton(main, text="New User", command=signup)
button_new_user.place(x=190,y=360)

button_login = ctk.CTkButton(main, text="Login Now", command=login)
button_login.place(x=360,y=360)
button_close = ctk.CTkButton(main, text="Close", command=close)
button_close.place(x=280,y=410)

# Start the main loop
main.mainloop()
