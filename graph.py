
import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from mysql.connector import Errorimport yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime


# Set theme and initialize main window
main = ctk.CTk()
main.geometry("700x600")
main.title("Simple CustomTkinter Main")

# MySQL connection details
db_config = {
    'host': 'localhost',  # Use 'localhost' instead of 'local'
    'database': 'signup',  # Replace with your actual database name
    'user': 'root',       # Username
    'password': 'K110406VIR'  # Password
}

def create_connection():
    try:
        connection = mysql.connector.connect(**db_config)
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
            messagebox.showinfo('Success','Your account was created')
            signup_window.destroy()
        except Error as e:
            print(f"The error '{e}' occurred")
            messagebox.showerror("Error",'Error Creating Account')
        finally:
            cursor.close()
            connection.close()  # Ensure the connection is closed
    else:
        print("User ID, username, and password cannot be empty.")
        messagebox.showerror("Error",'Fields cannot be empty')

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

    bg_image = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\user.png")  
    bg_image = bg_image.resize((80, 60))  
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = ctk.CTkLabel(top, image=bg_photo, text='')
    bg_label.place(x=20, y=15)

    bg_image2 = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\icon3.webp")  
    bg_image2 = bg_image2.resize((200, 180))  
    bg_photo2 = ImageTk.PhotoImage(bg_image2)
    bg_label2 = ctk.CTkLabel(right, image=bg_photo2, text='')
    bg_label2.place(x=800,y=400)

    labeld = ctk.CTkLabel(top, text=f"Welcome, {username}", font=("Arial bold", 40))
    labeld.place(x=100, y=12)
    
    labeld1 = ctk.CTkLabel(right, text="Let's Start Your Investment Journey!!", font=("Arial bold", 28))
    labeld1.place(x=300, y=50)

    labeld2 = ctk.CTkLabel(right, text="Enter your monthly salary", font=("Arial bold", 22))
    labeld2.place(x=50, y=130)

    entry1 = ctk.CTkEntry(right, placeholder_text="Salary", width=200)
    entry1.place(x=420, y=130)

    labeld3 = ctk.CTkLabel(left, text="Savings Categories: ", font=("Arial bold", 22))
    labeld3.place(x=50, y=50)

    labeld3_2 = ctk.CTkLabel(left, text="Category A- 0-10% \n Category B- 10-15% \n Category C-15-20% ", font=("Arial bold", 18))
    labeld3_2.place(x=50, y=75)

    labeld3 = ctk.CTkLabel(right, text="Enter your savings of this month", font=("Arial bold", 22))
    labeld3.place(x=50, y=180)

    entry2 = ctk.CTkEntry(right, placeholder_text="Savings", width=200)
    entry2.place(x=420, y=180)

    labeld4 = ctk.CTkLabel(right, text="Your Saving Category is ", font=("Arial bold", 20))
    labeld4.place(x=50, y=350)

    category_label=ctk.CTkLabel(right, text="Your Saving Category is: ", font=("Arial bold", 20))
    category_label.place(x=50, y=350)

    button_close = ctk.CTkButton(left, text="Close", command=newwin.destroy, bg_color='black',fg_color='black')
    button_close.place(x=100, y=450)

    def categorize_savings(salary, savings):
        savings_percent = (float(savings) / float(salary)) * 100
        if savings_percent <= 10:
            return "Category A (0-10%)"
        elif savings_percent <= 15:
            return "Category B (10-15%)"
        elif savings_percent <= 20:
            return "Category C (15-20%)"
        else:
            return "Above Category C (20%+)"

    def show_savings_category():
        salary = entry1.get()
        savings = entry2.get()
        
        if salary and savings:
            try:
                category = categorize_savings(salary, savings)
                category_label.configure(text=f"Your Saving Category is: {category}")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values for salary and savings.")
        else:
            messagebox.showerror("Error", "Both salary and savings fields must be filled.")

    # Submit button that triggers the category display
    submit_button = ctk.CTkButton(right, text='Submit', command=show_savings_category, fg_color='black')
    submit_button.place(x=200, y=500)

    def ret():
        login_window()
        newwin.destroy()

    goback = ctk.CTkButton(left, text="Return", command=newwin.destroy, bg_color='black',fg_color='black')
    goback.place(x=100, y=500)
    
    username = entry_username.get()
    next=ctk.CTkButton(right,text='Next',command=lambda:gonext(username),fg_color='black')
    next.place(x=300,y=500)

    # Hide the main window
    main.withdraw()

    def gonext(username):
        cfilter = ctk.CTkToplevel()
        cfilter.geometry('1350x750+100+20')
        cfilter.title("Dashboard")

        top = ctk.CTkFrame(cfilter, width=1000, height=100, fg_color='#ccc27b')
        top.pack(side=ctk.TOP, fill=ctk.X)

        left = ctk.CTkFrame(cfilter, height=940, width=300, fg_color='#ccc27b')
        left.pack(side=ctk.LEFT)
        
        right = ctk.CTkFrame(cfilter, height=940, width=1060, fg_color='white')
        right.pack(side=ctk.RIGHT)
        bg_image = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\user.png")  
        bg_image = bg_image.resize((80, 60))  
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = ctk.CTkLabel(top, image=bg_photo, text='')
        bg_label.place(x=20, y=15)

        labeld = ctk.CTkLabel(top, text=f"Welcome, {username}", font=("Arial bold", 40))
        labeld.place(x=100, y=12)

        label_filtered=ctk.CTkLabel(right,text="The companies based on your filters are",font=('arial',22))
        label_filtered.place(x=0,y=20)

        secvalue=ctk.StringVar()
        f_label=ctk.CTkLabel(left,text='FILTERS',font=('arial',20))
        f_label.place(x=100,y=8)
        f1_label=ctk.CTkLabel(left,text='SECTOR',font=('arial',14))
        f1_label.place(x=5,y=35)
        combobox = ctk.CTkComboBox(left, values=['None',"IT", "Pharma", "Banks",'Consumer Goods','Cement','Construction','Metals and Minings','Finance:Non-Banking','Automobile','Textiles','Power','Fertilisers & Pesticides','Banking:Non Finance','Services','Telecom','Industrial Manufacturing','Oil & Gas','Chemicals'])
        combobox.place(x=90,y=35)
        combobox.set("None") 

        gvalue=ctk.StringVar()
        f2_label=ctk.CTkLabel(left,text='ESG GRADE',font=('arial',14))
        f2_label.place(x=5,y=70)
        combobox2=ctk.CTkComboBox(left, values=['None','A','B+','B','B-','C+','C'])
        combobox2.place(x=90,y=70)
        combobox2.set("None")

        def filtered():
            m=combobox.get()
            n=combobox2.get()
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute('Use hackathon')
            if m=='None' and n=='None':
                cursor.execute('SELECT * FROM data ORDER BY CAST(Sno AS UNSIGNED) ASC')
            elif m=='None':
                cursor.execute('Select * from data where esg="{}" ORDER BY CAST(Sno AS UNSIGNED) ASC'.format(n))
            elif n=='None':
                cursor.execute('Select * from data where sector="{}" ORDER BY CAST(Sno AS UNSIGNED) ASC'.format(m))
            else:
                cursor.execute('Select * from data where sector="{}" and esg="{}" ORDER BY CAST(Sno AS UNSIGNED) ASC'.format(m,n))
            global data
            data=cursor.fetchall()
            if data==[]:
                messagebox.showinfo("None",'No companies available with the above filters')
            else:
                list.configure(state='normal')
                list.delete(1.0,'end')
                for i in data:  
                    list.insert('end',i[0]+'.'+i[1]+'\t\t\t\t\t\t'+i[2]+'\t\t\t'+i[3]+'\n')
                list.configure(state='disabled')


        fbutton=ctk.CTkButton(left,text='Filter',height=40,width=60,command=filtered)
        fbutton.place(x=145,y=110)

        closeb=ctk.CTkButton(left,text='Close',height=40,width=60,command=cfilter.destroy)
        closeb.place(x=90,y=500)

        username = entry_username.get()
        newbutton=ctk.CTkButton(left,text='View Stock Price',height=40,width=60,command=lambda:StockWin(username))
        newbutton.place(x=165,y=500)

        def StockWin(username):
            stockfilter = ctk.CTkToplevel()
            stockfilter.geometry('1350x750+100+20')
            stockfilter.title("Dashboard")

            top = ctk.CTkFrame(stockfilter, width=1000, height=100, fg_color='#ccc27b')
            top.pack(side=ctk.TOP, fill=ctk.X)

            left = ctk.CTkFrame(stockfilter, height=940, width=300, fg_color='#ccc27b')
            left.pack(side=ctk.LEFT)
            
            right = ctk.CTkFrame(stockfilter, height=940, width=1060, fg_color='white')
            right.pack(side=ctk.RIGHT)

            labeld = ctk.CTkLabel(top, text=f"Welcome, {username}", font=("Arial bold", 40))
            labeld.place(x=100, y=12)

            bg_image = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\user.png")  
            bg_image = bg_image.resize((80, 60))  
            bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = ctk.CTkLabel(top, image=bg_photo, text='')
            bg_label.place(x=20, y=15)

            clable=ctk.CTkLabel(left,text='Company Name',font=('arial',15))
            clable.place(x=30,y=10)
            cname=[]
            for i in data:
                cname.append(i[1])
            company_name=ctk.CTkComboBox(left,values=cname)
            company_name.place(x=60,y=40)

            def fetch_stock_data(symbol):
                """Fetch stock data for a given symbol."""
                try:
                    stock = yf.Ticker(symbol)
                    df = stock.history(period='1d', interval='1m')
                    if df.empty:
                        raise ValueError(f"No data found for symbol: {symbol}")
                    return df
                except Exception as e:
                    print(f"Error fetching data: {e}")
                    return None

            def plot_stock(symbol):
                """Plot the stock data for a given symbol."""
                df = fetch_stock_data(symbol)
                if df is None:
                    return plt.figure()  # Return an empty figure in case of error

                times = df.index.strftime('%H:%M:%S')
                prices = df['Close']

                fig, ax = plt.subplots()
                ax.plot(times, prices, label=f"{symbol} Price")
                ax.set_xlabel('Time')
                ax.set_ylabel('Price')
                ax.set_title(f"{symbol} Stock Price on {datetime.now().strftime('%Y-%m-%d')}")
                ax.legend()

                return fig

            def update_plot():
                """Update the plot every minute."""
                fig = plot_stock(stock_symbol)
                canvas.figure = fig
                canvas.draw()
                root.after(60000, update_plot)

            # Create the Tkinter window
            root = ctk.CTk()
            root.title("Live Stock Price")
            root.geometry("800x600")

            # Fetch the stock symbol from the database
            cursorob.execute('SELECT * FROM data')
            results = cursorob.fetchall()

            # Change this to the desired company name
            company_name = 'Infosys Ltd.'
            stock_symbol = None

            for record in results:
                if record[1] == company_name:
                    stock_symbol = record[2]  # Store the company symbol
                    break

            if stock_symbol is None:
                print(f"Stock symbol not found for the specified company: {company_name}")
                exit()

            # Initial plot
            fig = plot_stock(stock_symbol)
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            # Start the update loop
            update_plot()

        
        


    
        #listbox
        def fcompany():
            global list
            list=ctk.CTkTextbox(right,width=1000,height=560,font=("Arial",20))
            list.insert('end','    Company Name'+'\t\t\t\t\t\t'+'Sector'+'\t\t\t'+'ESG GRADE'+'\n\n')
            list.place(x=0,y=80)
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute('Use hackathon')
            cursor.execute('SELECT * FROM data ORDER BY CAST(Sno AS UNSIGNED) ASC')
            m=cursor.fetchall()
            for i in m:
                list.insert('end',i[0]+'.'+i[1]+'\t\t\t\t\t\t'+i[2]+'\t\t\t'+i[3]+'\n')
            
            list.configure(state='disabled')
        fcompany()


        f_image = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\finance.jpg")  
        f_image = f_image.resize((380,350))  
        f_photo = ImageTk.PhotoImage(f_image)
        foto_label = ctk.CTkLabel(left, image=f_photo, text='')
        foto_label.place(x=0, y=200)

        newwin.destroy()




    

def login_window():
    bg_image = Image.open(r"C:\Users\kusha\OneDrive\Desktop\Kushagra\Tkinter\hackathon\icon3.webp")  
    bg_image = bg_image.resize((150, 130))  
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = ctk.CTkLabel(main, image=bg_photo, text='')
    bg_label.place(x=290, y=10)

    # Create labels
    name = ctk.CTkLabel(main, text="SustainVest", font=("Arial ", 40))
    name.place(x=240, y=120)
    label = ctk.CTkLabel(main, text="Make Sustainable Investment", font=("Arial", 30), bg_color="transparent", fg_color='transparent')
    label.place(x=170, y=180)

    global label_title
    label_title = ctk.CTkLabel(main, text="", font=("arial", 20))
    label_title.place(x=290, y=440)

    # Create entry fields
    global entry_username
    entry_username = ctk.CTkEntry(main, placeholder_text="Username", width=300)
    entry_username.place(x=200, y=260)
    global entry_password

    entry_password = ctk.CTkEntry(main, placeholder_text="Password", show="*", width=300)
    entry_password.place(x=200, y=310)

    # Define button actions
    def close():
        main.withdraw()

    # Create buttons
    button_new_user = ctk.CTkButton(main, text="New User", command=signup)
    button_new_user.place(x=190, y=360)

    button_login = ctk.CTkButton(main, text="Login Now", command=login)
    button_login.place(x=360, y=360)

    button_close = ctk.CTkButton(main, text="Close", command=close)
    button_close.place(x=280, y=410)

for i in range(1):
    login_window()

# Start the main loop
main.mainloop()
