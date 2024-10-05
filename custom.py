import customtkinter as ctk
from PIL import Image,ImageTk

# Set theme and initialize main window
#ctk.set_default_color_theme("dark-blue")
main = ctk.CTk()
main.geometry("700x600")
main.title("Simple CustomTkinter Main")

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "a" and password == "a":
        label_title.configure(text='Login Successfull')
        newwindow(username)
    else:
        label_title.configure(text="Login Failed", text_color="red",font=20)

def signup():
    signup_window = ctk.CTkToplevel()
    signup_window.geometry("400x300")
    signup_window.title("Signup")
    signup_window.attributes("-topmost", True) 

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
    newwin.geometry('1350x750+100+20')
    newwin.title("Dashboard")
    
    top=ctk.CTkFrame(newwin,width=1000,height=100,fg_color='#a69080')
    top.pack(side=ctk.TOP,fill=ctk.X)

    left=ctk.CTkFrame(newwin,height=940,width=300,fg_color='#ac8968')
    left.pack(side=ctk.LEFT)
    
    right=ctk.CTkFrame(newwin,height=940,width=1060,fg_color='#e1d4c8')
    right.pack(side=ctk.RIGHT)

    bg_image = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\\user.png")  
    bg_image = bg_image.resize((80,60))  
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = ctk.CTkLabel(top, image=bg_photo,text='')
    bg_label.place(x=20,y=15)

    bg_image2 = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\\icon3.webp")  
    bg_image2 = bg_image2.resize((80,60))  
    bg_photo2 = ImageTk.PhotoImage(bg_image2)
    bg_label2 = ctk.CTkLabel(right, image=bg_photo2,text='')
    bg_label2.place(x=400,y=80)

    labeld = ctk.CTkLabel(top, text=f"Welcome, {username}" , font=("Arial bold", 40))
    labeld.place(x=100,y=12)
    
    labeld1 = ctk.CTkLabel(right, text="Lets Start Your Investment Journey!!", font=("Arial bold", 28))
    labeld1.place(x=300,y=50)

    labeld2 = ctk.CTkLabel(right, text="Enter your monthly salary", font=("Arial bold", 22))
    labeld2.place(x=50,y=130)

    entry1= ctk.CTkEntry(right, placeholder_text="Salary", width=200)
    entry1.place(x=400,y=130)

    labeld3 = ctk.CTkLabel(left, text="Savings Categories: ", font=("Arial bold", 22))
    labeld3.place(x=50,y=50)

    labeld3_2=ctk.CTkLabel(left, text="Category A- 0-10% \n Category B- 10-15% \n Category C-15-20% ", font=("Arial bold", 18))
    labeld3_2.place(x=50,y=75)

    labeld3 = ctk.CTkLabel(right, text="Enter your savings of this month", font=("Arial bold", 20))
    labeld3.place(x=55,y=180)

    entry2= ctk.CTkEntry(right, placeholder_text="Savings", width=200)
    entry2.place(x=400,y=180)

    labeld4 = ctk.CTkLabel(right, text="Your Saving Category is ", font=("Arial bold", 20))
    labeld4.place(x=50,y=350)



    button_close = ctk.CTkButton(left, text="Close", command=newwin.destroy,bg_color='black')
    button_close.place(x=100,y=450)



    
    # Hide the main window
    main.withdraw()

bg_image = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\\icon3.webp")  # Make sure the path is correct
bg_image = bg_image.resize((150,130))  # Resize if necessary
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = ctk.CTkLabel(main, image=bg_photo,text='')
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
