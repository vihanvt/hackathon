import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

# Set theme and initialize main window
main = ctk.CTk()
main.geometry("700x600")
main.title("Simple CustomTkinter Main")

# MySQL connection details
db_config = {
    'host': 'localhost',  # Use 'localhost' instead of 'local'
    'database': 'signup',  # Replace with your actual database name
    'user': 'vihan',       # Username
    'password': 'Aadivnt24#'  # Password
}

def create_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM udata WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        label_title.configure(text='Login Successful')
        newwindow(username)
    else:
        label_title.configure(text="Login Failed", text_color="red", font=20)

def signup():
    signup_window = ctk.CTkToplevel()
    signup_window.geometry("400x400")
    signup_window.title("Signup")
    signup_window.attributes("-topmost", True)

    label_signup_title = ctk.CTkLabel(signup_window, text="Signup", font=("Arial", 20))
    label_signup_title.pack(pady=10)

    entry_signup_uid = ctk.CTkEntry(signup_window, placeholder_text="Enter User ID (e.g., U1)", width=200)
    entry_signup_uid.pack(pady=10)
    
    entry_signup_username = ctk.CTkEntry(signup_window, placeholder_text="Username", width=200)
    entry_signup_username.pack(pady=10)

    entry_signup_password = ctk.CTkEntry(signup_window, placeholder_text="Password", show="*", width=200)
    entry_signup_password.pack(pady=10)

    button_signup = ctk.CTkButton(signup_window, text="Create Account", command=lambda: handle_create_account(entry_signup_uid.get(), entry_signup_username.get(), entry_signup_password.get(), signup_window))
    button_signup.pack(pady=20)

def handle_create_account(uid, username, password, signup_window):
    if uid and username and password:  # Simple validation
        connection = create_connection()
        cursor = connection.cursor()

        try:
            # Insert new user into the database
            cursor.execute("INSERT INTO udata (uid, username, password) VALUES (%s, %s, %s)", (uid, username, password))
            connection.commit()
            print(f"New account created for: {username}")
            label_title.configure(text="Account created successfully!", text_color="green", font=20)
            signup_window.destroy()
        except Error as e:
            print(f"The error '{e}' occurred")
            label_title.configure(text="Error creating account", text_color="red", font=20)
        finally:
            cursor.close()
            connection.close()  # Ensure the connection is closed
    else:
        print("User ID, username, and password cannot be empty.")
        label_title.configure(text="User ID, username, and password cannot be empty", text_color="red", font=20)

def newwindow(username):
    newwin = ctk.CTkToplevel()
    newwin.geometry('1350x750+100+20')
    newwin.title("Dashboard")
    
    top = ctk.CTkFrame(newwin, width=1000, height=100, fg_color='#a69080')
    top.pack(side=ctk.TOP, fill=ctk.X)

    left = ctk.CTkFrame(newwin, height=940, width=300, fg_color='#ac8968')
    left.pack(side=ctk.LEFT)
    
    right = ctk.CTkFrame(newwin, height=940, width=1060, fg_color='#e1d4c8')
    right.pack(side=ctk.RIGHT)

    bg_image = Image.open(r"C:\Users\Vihan\Desktop\user.png")  
    bg_image = bg_image.resize((80, 60))  
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = ctk.CTkLabel(top, image=bg_photo, text='')
    bg_label.place(x=20, y=15)

    bg_image2 = Image.open(r"C:\Users\Vihan\Desktop\icon3.webp")  
    bg_image2 = bg_image2.resize((80, 60))  
    bg_photo2 = ImageTk.PhotoImage(bg_image2)
    bg_label2 = ctk.CTkLabel(right, image=bg_photo2, text='')
    bg_label2.place(x=400, y=80)

    labeld = ctk.CTkLabel(top, text=f"Welcome, {username}", font=("Arial bold", 40))
    labeld.place(x=100, y=12)
    
    labeld1 = ctk.CTkLabel(right, text="Let's Start Your Investment Journey!!", font=("Arial bold", 28))
    labeld1.place(x=300, y=50)

    labeld2 = ctk.CTkLabel(right, text="Enter your monthly salary", font=("Arial bold", 22))
    labeld2.place(x=50, y=130)

    entry1 = ctk.CTkEntry(right, placeholder_text="Salary", width=200)
    entry1.place(x=400, y=130)

    labeld3 = ctk.CTkLabel(left, text="Savings Categories: ", font=("Arial bold", 22))
    labeld3.place(x=50, y=50)

    labeld3_2 = ctk.CTkLabel(left, text="Category A- 0-10% \n Category B- 10-15% \n Category C-15-20% ", font=("Arial bold", 18))
    labeld3_2.place(x=50, y=75)

    labeld3 = ctk.CTkLabel(right, text="Enter your savings of this month", font=("Arial bold", 20))
    labeld3.place(x=55, y=180)

    entry2 = ctk.CTkEntry(right, placeholder_text="Savings", width=200)
    entry2.place(x=400, y=180)

    labeld4 = ctk.CTkLabel(right, text="Your Saving Category is ", font=("Arial bold", 20))
    labeld4.place(x=50, y=350)

    button_close = ctk.CTkButton(left, text="Close", command=newwin.destroy, bg_color='black')
    button_close.place(x=100, y=450)

    # Hide the main window
    main.withdraw()

bg_image = Image.open(r"C:\Users\Vihan\Desktop\icon3.webp")  
bg_image = bg_image.resize((150, 130))  
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = ctk.CTkLabel(main, image=bg_photo, text='')
bg_label.place(x=290, y=10)

# Create labels
name = ctk.CTkLabel(main, text="SustainVest", font=("Arial ", 40))
name.place(x=240, y=120)
label = ctk.CTkLabel(main, text="Make Sustainable Investment", font=("Arial", 30), bg_color="transparent", fg_color='transparent')
label.place(x=170, y=180)

label_title = ctk.CTkLabel(main, text="", font=("arial", 20))
label_title.place(x=290, y=440)

# Create entry fields
entry_username = ctk.CTkEntry(main, placeholder_text="Username", width=300)
entry_username.place(x=200, y=260)

entry_password = ctk.CTkEntry(main, placeholder_text="Password", show="*", width=300)
entry_password.place(x=200, y=310)

# Define button actions
def close():
    main.destroy()

# Create buttons
button_new_user = ctk.CTkButton(main, text="New User", command=signup)
button_new_user.place(x=190, y=360)

button_login = ctk.CTkButton(main, text="Login Now", command=login)
button_login.place(x=360, y=360)

button_close = ctk.CTkButton(main, text="Close", command=close)
button_close.place(x=280, y=410)

# Start the main loop
main.mainloop()
