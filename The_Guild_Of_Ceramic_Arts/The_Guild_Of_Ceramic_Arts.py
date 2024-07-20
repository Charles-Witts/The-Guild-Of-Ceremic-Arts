import re, sqlite3
import os
import tkinter as tk
import tkinter.font
from tkinter import ttk, Canvas, Label, Entry, Button, messagebox, Toplevel, Text, OptionMenu, StringVar, Tk, PhotoImage, Frame
from datetime import datetime, timedelta, date

root = Tk()

typeFont = tk.font.Font(family="Libre Franklin", size=27, weight="normal")
typeFont2 = tk.font.Font(family="Libre Franklin", size=14, weight="normal")
typeFont3 = tk.font.Font(family="Libre Franklin", size=14, underline=True)
typeFont4 = tk.font.Font(family="Libre Franklin", size=10, weight="normal")
typeFont5 = tk.font.Font(family="Libre Franklin", size=12, weight="normal")
limelightFont = tk.font.Font(family="Limelight", size=56, weight="normal")
mavenProFontMED = tk.font.Font(family="Maven Pro", size=17, weight="normal")
mavenProFontBOLD = tk.font.Font(family="Maven Pro", size=36, weight="bold")
mavenProFontBOLDLogIn = tk.font.Font(family="Maven Pro", size=28, weight="bold")
typeFontsignUpPage = tk.font.Font(family="Libre Franklin", size=15, weight="normal")
limelightFontsignUpPage = tk.font.Font(family="Limelight", size=40, weight="normal")
mavenProFontMEDsignUpPage = tk.font.Font(family="Maven Pro", size=14, weight="normal")

GOCA_background_art = PhotoImage(file = "GoCA_WindowImage.png")


def _main_():
    
    folder_path = "GuildOfCeramicArts"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    db_file_path = os.path.join(folder_path, "GuildOfCeramicArts.db")
    global conn
    conn = sqlite3.connect(db_file_path)
    conn.executescript(''' CREATE TABLE IF NOT EXISTS guildMembers(gMID NUMBER PRIMARY KEY NOT NULL, userPassword TEXT, userName TEXT, phoneNumber TEXT, postCode TEXT, Email TEXT, Age NUMBER)''' )
    conn.executescript(''' CREATE TABLE IF NOT EXISTS items(itemID NUMBER PRIMARY KEY NOT NULL, itemName TEXT, pricePer REAL)''' )
    conn.executescript(''' CREATE TABLE IF NOT EXISTS orders(orderID NUMBER PRIMARY KEY NOT NULL, gMID TEXT, itemName TEXT, howMany NUMBER, datePurchased DATE, totalPrice REAL, dateToPayInvoice DATE, invoicePaid BOOLEAN DEFAULT 0)''' )
    _login_()
    
def _login_():
    
    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    #function that creates the gradient
    def _create_gradient_(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def _interpolate_(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def _hex_to_rgb_(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = _hex_to_rgb_(start_color)
        end_color_rgb = _hex_to_rgb_(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = _interpolate_(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)

      

    for widget in root.winfo_children():
        widget.destroy()
    

    

    root.configure(bg = "#D3C9A3")
    root.title("GoCA Login")
    root.geometry("1519x793")
    root.resizable(False, False)

    canvas = Canvas(root,  background=root.cget('bg'), highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    _create_gradient_(canvas, 1519, 793, "#ffffff", "#D3C9A3")
    
    canvas.create_text(330, 130, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")



    # Background rectangle on the left side
    rect_width = 450
    rect_height = 540
    rect_x1 = 100
    rect_y1 = (root.winfo_screenheight() - (1.15*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")


# Frame for login form inside the rectangle


    login_frame = Frame(root, bg="white")
    login_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    login_label1 = Label(root, text="Log in", bg="white")
    login_label1.place(x = 130, y = 245)
    login_label1.configure(font=mavenProFontBOLDLogIn)

    gMID_label = Label(root, text="GuildmemberID:", bg="white")
    gMID_label.place(x = 130, y = 370)
    gMID_label.configure(font=mavenProFontMED)

    gMID_entry = Entry(root, width = "15")
    gMID_entry.place(x = 130, y = 410)
    gMID_entry.configure(font=typeFont)

    user_Password_label = Label(root, text="Password:", bg="white")
    user_Password_label.place(x = 130, y = 510)
    user_Password_label.configure(font=mavenProFontMED)

    user_Password_entry = Entry(root, width = "15", show="*")
    user_Password_entry.place(x = 130, y = 550)
    user_Password_entry.configure(font=typeFont)

    logIn_button = Button(root, text="             Log In           ", bg="#D3C9A3", fg = "white", command=lambda:_validate_Login_(gMID_entry.get(), user_Password_entry.get())) 
    logIn_button.place(x=130, y=655) 
    logIn_button.configure(font=mavenProFontBOLDLogIn)

    Sign_Up_Text = Label(root, text ="Don't already have an account? ",fg = "grey", bg = "white")
    Sign_Up_Text.place(x=130 , y =300)
    Sign_Up_Text.configure(font=typeFont2)


    label = Label(root, image=GOCA_background_art)
    label.place(x=690, y=0)
    
    Sign_Up_Button = Label(root, text="Sign up.", fg="black", bg = "white", cursor="hand2")
    Sign_Up_Button.configure(font=typeFont3)
    Sign_Up_Button.place(x= 410, y =300)
    Sign_Up_Button.bind("<Button-1>", lambda e: _new_Guild_Member_Window_())

def _validate_Login_(gMID, user_Password):
    
    if (len(conn.execute("SELECT * FROM guildMembers WHERE gMID = '{}' AND userPassword = '{}'".format(gMID, user_Password)).fetchall()) != 0):
        _main_Menu_(gMID)
        
    else:
        messagebox.showerror("Error","\n Guild Member Id or Password is incorrect. \n Please check if your Guild Member ID is in the format below : gMIDn  : where n is your tailored ID number")
        _login_()

def _main_Menu_(gMID):

    for widget in root.winfo_children():
        widget.destroy()
        
    root.configure(bg = "#D3C9A3")
    root.title("GoCA Login")
    root.geometry("1519x793")
    root.resizable(False, False)


    def create_gradient(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)


    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")

    #create the Guild Of Ceramic Arts title in the upper left of the window
    canvas.create_text(380, 110, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")


    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    # Background rectangle on the left side
    rect_width = 550
    rect_height = 500
    rect_x1 = 100
    rect_y1 = (root.winfo_screenheight() - (1.25*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")

    newGuildMember_button = Button(root, text="New Guild Member", width="23", bg="#D3C9A3", fg = "white", command=lambda:_new_Guild_Member_Window_())  
    newGuildMember_button.place(x=105, y=230)
    newGuildMember_button.configure(font=mavenProFontBOLDLogIn)

    newItem_button = Button(root, text="New Item", width="23",bg="#D3C9A3", fg = "white", command=lambda: _new_Item_Window_(gMID))  
    newItem_button.place(x=105, y=330)
    newItem_button.configure(font=mavenProFontBOLDLogIn)

    order_button = Button(root, text="Order Items", width="23",bg="#D3C9A3", fg = "white", command=lambda: _make_Order_Window_(gMID))  
    order_button.place(x=105, y=430)
    order_button.configure(font=mavenProFontBOLDLogIn)

    invoices_button = Button(root, text="Pay/Cancel Invoices", width="23",bg="#D3C9A3", fg = "white", command=lambda: _check_Invoices_(gMID))  
    invoices_button.place(x=105, y=530)
    invoices_button.configure(font=mavenProFontBOLDLogIn)

    checkall_button = Button(root, text="Check All Unpaid Invoices", width="23", bg="#D3C9A3", fg = "white",command=lambda: _all_Unpaid_Invoices_(gMID))  
    checkall_button.place(x=105, y=630)
    checkall_button.configure(font=mavenProFontBOLDLogIn)

    
   

    label = Label(root, image=GOCA_background_art)
    label.place(x=690, y=0)

def _new_Guild_Member_Window_():


    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    #function that creates the gradient
    def _create_gradient_(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def _interpolate_(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def _hex_to_rgb_(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = _hex_to_rgb_(start_color)
        end_color_rgb = _hex_to_rgb_(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = _interpolate_(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)

      
    for widget in root.winfo_children():
        widget.destroy()

    
    
    root.configure(bg = "#D3C9A3")
    root.title("GoCA Sign Up")
    root.geometry("1519x793")
    root.resizable(False, False)

    canvas = Canvas(root,  background=root.cget('bg'), highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    _create_gradient_(canvas, 1519, 793, "#ffffff", "#D3C9A3")
    
    canvas.create_text(330, 100, text="The Guild of\nCeramic Arts", font=limelightFontsignUpPage, fill="black", anchor="center")





    rect_width = 450
    rect_height = 600
    rect_x1 = 100
    rect_y1 = (root.winfo_screenheight() - (1.25*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")

    signUp_frame = Frame(root, bg="white")
    signUp_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    SignUpText = Label(root, text ="Sign up and make a new account ",fg = "grey", bg = "white")
    SignUpText.place(x=130 , y =215)
    SignUpText.configure(font=typeFont2)


    signUp_label1 = Label(root, text="Sign Up", bg="white")
    signUp_label1.place(x = 130, y = 165)
    signUp_label1.configure(font=mavenProFontBOLDLogIn)
    
    userName_label = Label(root, text="Username: ", bg="white")
    userName_label.place(x = 130, y = 255)
    userName_label.configure(font=mavenProFontMEDsignUpPage)
    
    userName_entry = Entry(root, width = "27")
    userName_entry.place(x = 130, y = 285)
    userName_entry.configure(font=typeFontsignUpPage)

    
    Age_label = Label(root, text="Age: ", bg="white")
    Age_label.place(x = 130, y = 535)
    Age_label.configure(font=mavenProFontMEDsignUpPage)
    
    Age_entry = Entry(root, width = "27")
    Age_entry.place(x = 130, y = 565)
    Age_entry.configure(font=typeFontsignUpPage)


    
    Email_label = Label(root, text="Email: ", bg="white")
    Email_label.place(x = 130, y = 465)
    Email_label.configure(font=mavenProFontMEDsignUpPage)
    
    Email_entry = Entry(root, width = "27")
    Email_entry.place(x = 130, y = 495)
    Email_entry.configure(font=typeFontsignUpPage)

    
    postCode_label = Label(root, text="Post Code: ", bg="white")
    postCode_label.place(x = 130, y = 605)
    postCode_label.configure(font=mavenProFontMEDsignUpPage)

    postCode_entry = Entry(root, width = "27")
    postCode_entry.place(x = 130, y = 635)
    postCode_entry.configure(font=typeFontsignUpPage)

    
    password1_label = Label(root, text="Password: ", bg = "white")
    password1_label.place(x = 130, y = 325)
    password1_label.configure(font=mavenProFontMEDsignUpPage)
    
    password1_entry = Entry(root, show="*", width = "27")
    password1_entry.place(x = 130, y = 355)
    password1_entry.configure(font=typeFontsignUpPage)


    password2_label = Label(root, text="Re-enter password: ", bg="white")
    password2_label.place(x = 130, y = 395)
    password2_label.configure(font=mavenProFontMEDsignUpPage)
    
    password2_entry = Entry(root, show="*", width = "27")
    password2_entry.place(x = 130, y = 425)
    password2_entry.configure(font=typeFontsignUpPage)


    
    register_button = Button(root, text="Register", bg="#D3C9A3", fg = "white", command=lambda: _new_Guild_Member_(userName_entry.get(), password1_entry.get(), password2_entry.get(), Age_entry.get(), postCode_entry.get(), Email_entry.get()))
    register_button.place(x=129, y=675) 
    register_button.configure(font=mavenProFontBOLDLogIn)


    loginPage_button = Button(root, text="  Cancel  ", bg="#D3C9A3", fg = "white", command=lambda: _login_())
    loginPage_button.place(x=322, y=675)
    loginPage_button.configure(font=mavenProFontBOLDLogIn)



    label = Label(root, image = GOCA_background_art)
    label.place (x=690, y = 0)
    


    
    
def _new_Guild_Member_(userName, password1, password2, Age, postCode, Email):
    
    
    
    if not (len(conn.execute("SELECT * FROM guildMembers WHERE userName ='{}'".format(userName)).fetchall()) == 0):
        messagebox.showerror("Error","This user name is already taken")
        _new_Guild_Member_Window_()
        
    Age = int(Age)
    if (Age < 16) or (Age > 125):
        messagebox.showerror("Error","The age inputed is not a acceptable age")
        _new_Guild_Member_Window_()
        
        
    if not len(postCode) == 8:
        messagebox.showerror("Error" , "Invalid Post Code")
        _new_Guild_Member_Window_()
        
    if (not re.search("[@]",Email)):
        messagebox.showerror("Error","The e-mail inputed is not valid")
        _new_Guild_Member_Window_()
        
    if (len(password1) < 8) or(not re.search("[0-9]",password1)) or(not re.search("[a-z]",password1)) or(not re.search("[A-Z]",password1)):
        messagebox.showerror("Error", "Password must be at least 8 characters long and contain at least one digit, one lowercase letter, and one uppercase letter.")
        _new_Guild_Member_Window_()
        
    if not password1 == password2:
        messagebox.showerror("Error","The two passwords inputed do not match")
        _new_Guild_Member_Window_()
        
    userPassword = password2
    
    gMID = "gMID{}".format((len(conn.execute('SELECT * FROM guildMembers').fetchall()) + 1))
    
    
    
    for widget in root.winfo_children():
        widget.destroy()



    #function that creates the gradient
    def _create_gradient_(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def _interpolate_(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def _hex_to_rgb_(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = _hex_to_rgb_(start_color)
        end_color_rgb = _hex_to_rgb_(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = _interpolate_(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    
    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    gradient = _create_gradient_(canvas, 1519, 793, "#ffffff", "#D3C9A3")
    canvas.create_text(330, 100, text="The Guild of\nCeramic Arts", font=limelightFontsignUpPage, fill="black",)

    # Background rectangle on the left side
    rect_width = 450
    rect_height = 600
    rect_x1 = 100
    rect_y1 = (root.winfo_screenheight() - (1.25*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")


    signUp_frame = Frame(root, bg="white")
    signUp_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    signUp_label = Label(root, text="Sign Up", bg="white")
    signUp_label.place(x = 130, y = 190)
    signUp_label.configure(font=mavenProFontBOLDLogIn)

    ValidationName_label = Label(root, text="Your Username is  ", bg="white", )
    ValidationName_label.place(x=130, y=260)
    ValidationName_label.configure(font=typeFont2)

    ValidationNameVar_label = Label(root, text= userName, bg="white", )
    ValidationNameVar_label.place(x=330, y=260)
    ValidationNameVar_label.configure(font=typeFont2)

    ValidationRhif_label = Label(root, text="Your E-Mail is ", bg="white", )
    ValidationRhif_label.place(x=130, y=310)
    ValidationRhif_label.configure(font=typeFont2)

    ValidationRhifVar_label = Label(root, text= Email , bg="white", )
    ValidationRhifVar_label.place(x=330, y=310)
    ValidationRhifVar_label.configure(font=typeFont2)

    ValidationAge_label = Label(root, text= "Your age is  ", bg="white", )
    ValidationAge_label.place(x=130, y=360)
    ValidationAge_label.configure(font=typeFont2)

    ValidationAgeVar_label = Label(root, text= Age , bg="white", )
    ValidationAgeVar_label.place(x=330, y=360)
    ValidationAgeVar_label.configure(font=typeFont2)

    ValidationPost_label = Label(root, text= "Your Post code is  ", bg="white", )
    ValidationPost_label.place(x=130, y=410)
    ValidationPost_label.configure(font=typeFont2)

    ValidationPostVar_label = Label(root, text= postCode , bg="white", )
    ValidationPostVar_label.place(x=330, y=410)
    ValidationPostVar_label.configure(font=typeFont2)

    ValidationText_label = Label(root, text="Are you sure this is correct?", bg="white", )
    ValidationText_label.place(x=130, y=460)
    ValidationText_label.configure(font=typeFont2)

    ValidationGMID_label = Label(root, text="REMEMBER: Your Guild Member ID is 'gMID2'.\n you will need this to log in.", bg="white", fg = "light gray")
    ValidationGMID_label.place(x=120, y=570)
    ValidationGMID_label.configure(font=typeFont2)

    Yes_button = Button(root, text="Yes", bg="#D3C9A3", fg = "white", width = 8, command=lambda: print("Yipee!"))  
    Yes_button.place(x=120, y=665) 
    Yes_button.configure(font=mavenProFontBOLDLogIn)

    Cancel_button = Button(root, text="Cancel", bg="#D3C9A3", fg = "white", width = 8, command=lambda: print("Yipee!"))  
    Cancel_button.place(x=322, y=665) 
    Cancel_button.configure(font=mavenProFontBOLDLogIn)

    
    label = Label(root, image = GOCA_background_art)
    label.place (x=690, y = 0)
    

    
def _insert_Into_Guild_Members_(gMID,userName,Age,postCode,userPassword,Email):
    
    
    conn.execute("INSERT INTO guildMembers(gMID,userName,Age,postCode,userPassword,Email) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(gMID,userName,Age,postCode,userPassword,Email))
    conn.commit()
    
    _login_()
    
def _new_Item_Window_(gMID):
    
    def create_gradient(canvas, width, height, start_color, end_color):
    # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)


    
    root.configure(bg = "#D3C9A3")
    root.title("GoCA Login")
    root.geometry("1519x793")
    root.resizable(False, False)


    canvas = Canvas(root,  background=root.cget('bg'), highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")
    
    canvas.create_text(770, 120, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")


    rect_width = 700
    rect_height = 450
    rect_x1 = 416
    rect_y1 = (root.winfo_screenheight() - (1.35*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")


    NewItem_frame = Frame(root, bg="white")
    NewItem_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    NewItem_label1 = Label(root, text="New Item", bg="white")
    NewItem_label1.place(x = 440, y = 245)
    NewItem_label1.configure(font=mavenProFontBOLDLogIn)

    Item_label = Label(root, text="Item name:", bg="white")
    Item_label.place(x = 440, y = 340)
    Item_label.configure(font=mavenProFontMED)

    Item_entry = Entry(root, width = "26")
    Item_entry.place(x = 440, y = 380)
    Item_entry.configure(font=typeFont)

    Price_label = Label(root, text="Price per:", bg="white")
    Price_label.place(x = 440, y = 480)
    Price_label.configure(font=mavenProFontMED)

    Price_entry = Entry(root, width = "26")
    Price_entry.place(x = 440, y = 520)
    Price_entry.configure(font=typeFont)

    ItemText = Label(root, text ="Add a new item to the database",fg = "grey", bg = "white")
    ItemText.place(x=440 , y =300)
    ItemText.configure(font=typeFont2)

    Register_button = Button(root, text="Register", bg="#D3C9A3", fg = "white", width = "13", command=lambda: _new_Item_Validate_(Item_entry.get(), Price_entry.get(), gMID))
    Register_button.place(x=440, y=590) 
    Register_button.configure(font=mavenProFontBOLDLogIn)

    Cancel_button = Button(root, text="  Cancel  ", bg="#D3C9A3", fg = "white", width = "13", command=lambda: _main_Menu_(gMID))  
    Cancel_button.place(x=788, y=590) 
    Cancel_button.configure(font=mavenProFontBOLDLogIn)



    label = Label(root, image = GOCA_background_art)
    label.place (x=1251, y = 0)


    label2 = Label(root, image = GOCA_background_art)
    label2.place (x=-552, y = 0)






def _new_Item_Validate_(itemName, pricePer,gMID):
    

    
    if not (len(conn.execute("SELECT * FROM items WHERE itemName ='{}'".format(itemName)).fetchall()) == 0):
        messagebox.showerror("Error","Eitem o'r enw ma yn bodoli yn barod")
        _new_Item_Window_(gMID)
        
    itemID = "itemID{}".format((len(conn.execute('SELECT * FROM items').fetchall()) + 1))
    
    for widget in root.winfo_children():
        widget.destroy()

    _insert_Into_Items_(itemID,itemName,pricePer, gMID)

    
def _insert_Into_Items_(itemID,itemName,pricePer, gMID):
    
    conn.execute("INSERT INTO items(itemID,itemName,pricePer) VALUES ('{}','{}','{}')".format(itemID,itemName,pricePer))
    conn.commit()
    _main_Menu_(gMID)





    
def _make_Order_Window_(gMID):

    
    for widget in root.winfo_children():
        widget.destroy()
        
    root.configure(bg = "#D3C9A3")
    root.title("GoCA - Order")
    root.geometry("1519x793")
    root.resizable(False, False)
    
    def create_gradient(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)



    #creates the canvas to set gradient 
    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")

    #create the Guild Of Ceramic Arts title in the upper left of the window
    canvas.create_text(750, 110, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    # Background rectangle on the left side
    rect_width = 700
    rect_height = 300
    rect_x1 = 396
    rect_y1 = (root.winfo_screenheight() - (2*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")

    Order_frame = Frame(root, bg="white")
    Order_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    Order_label1 = Label(root, text="Order", bg="white")
    Order_label1.place(x = 403, y = 245)
    Order_label1.configure(font=mavenProFontBOLDLogIn)

    
    combo = ttk.Combobox(root, width=110, height=1000, state="readonly")
    combo.place(x = 403, y = 310)


    Details_button = Button(root, text="Details", bg="#D3C9A3", fg = "white", width=14, command=lambda: itemDetails(combo.get(), gMID))  
    Details_button.place(x=403, y=390) 
    Details_button.configure(font=mavenProFontBOLDLogIn)

    Back_button = Button(root, text="Back", bg="#D3C9A3", fg = "white", width = 14, command=lambda: _main_Menu_(gMID))  
    Back_button.place(x=755, y=390) 
    Back_button.configure(font=mavenProFontBOLDLogIn)

    
    itemDetails_button = Button(root, text = "Check Item Details", command=lambda: itemDetails(combo.get(), gMID))
    itemDetails_button.grid(row=1, column=1, padx=5, pady=5)
    
    label = Label(root, image = GOCA_background_art)
    label.place (x=1251, y = 0)


    label2 = Label(root, image = GOCA_background_art)
    label2.place (x=-552, y = 0)
    
    combo['values'] = makeOrderDropDown()

def makeOrderDropDown():
    
    cur = conn.cursor()
    
    cur.execute('SELECT itemName FROM items')
    
    query = cur.fetchall()
    data = []
    
    for row in query:
        data.append(row[0])
    return data

def itemDetails(selectedItem, gMID):
    for widget in root.winfo_children():
        widget.destroy()

    def create_gradient(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)

    root.configure(bg = "#D3C9A3")
    root.title("GoCA - Details")
    root.geometry("1519x793")
    root.resizable(False, False)
    
    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")
        
    canvas.create_text(750, 110, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    # Background rectangle on the left side
    rect_width = 700
    rect_height = 450
    rect_x1 = 396
    rect_y1 = (root.winfo_screenheight() - (1.35*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")

    
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE itemName = '{}'".format(selectedItem))
    itemDetailsList = cur.fetchone()
    if itemDetailsList:
        itemId, itemName, pricePer = itemDetailsList[0], itemDetailsList[1], itemDetailsList[2]


        ItemID_label = Label(root, text="Item ID:", bg="white")
        ItemID_label.place(x = 450, y = 310)
        ItemID_label.configure(font=mavenProFontMED)

        ItemIDDB_label = Label(root, text=itemId, bg="white")
        ItemIDDB_label.place(x = 840, y = 310)
        ItemIDDB_label.configure(font=mavenProFontMED)
        
        ItemName_label = Label(root, text="Item Name:", bg="white")
        ItemName_label.place(x = 450, y = 365)
        ItemName_label.configure(font=mavenProFontMED)

        ItemNameDB_label = Label(root, text=itemName, bg="white")
        ItemNameDB_label.place(x = 840, y = 365)
        ItemNameDB_label.configure(font=mavenProFontMED)

        ItemPricePer_label = Label(root, text="Price Per:", bg="white")
        ItemPricePer_label.place(x = 450, y = 420)
        ItemPricePer_label.configure(font=mavenProFontMED)

        ItemPricePerDB_label = Label(root, text=pricePer, bg="white")
        ItemPricePerDB_label.place(x = 840, y = 420)
        ItemPricePerDB_label.configure(font=mavenProFontMED)

        
        HowMany_label = Label(root, text="How Many?:", bg="white")
        HowMany_label.place(x = 450, y = 475)
        HowMany_label.configure(font=mavenProFontMED)

        validate_input = root.register(lambda P: P.isdigit() or P == "")
        
        howMany_entry = Entry(root, validate="key", validatecommand=(validate_input, "%P"))
        howMany_entry.place(x = 780, y = 475)
        howMany_entry.configure(font=mavenProFontMED)
        
        checkOut_button = Button(root, text="Check Out", bg="#D3C9A3", fg = "white", command=lambda:_order_Validation_(howMany_entry.get(), selectedItem, gMID, pricePer, itemId, itemName))
        checkOut_button.place(x=440, y=560)
        checkOut_button.configure(font=mavenProFontBOLDLogIn)
        
        mainMenu_button = Button(root, text="Main Menu", bg="#D3C9A3", fg = "white",command=lambda:_main_Menu_(gMID))
        mainMenu_button.place(x=667, y=560) 
        mainMenu_button.configure(font=mavenProFontBOLDLogIn)
        
        back_button = Button(root, text="Back", bg="#D3C9A3", fg = "white",command=lambda:_make_Order_Window_(gMID))
        back_button.place(x=905, y=560)
        back_button.configure(font=mavenProFontBOLDLogIn)

        label = Label(root, image = GOCA_background_art)
        label.place (x=1251, y = 0)


        label2 = Label(root, image = GOCA_background_art)
        label2.place (x=-552, y = 0)
        
    else:
        
        messagebox.showerror("Error","No details found for selected item.")
        _make_Order_Window_(gMID)
        
def _order_Validation_(howMany, selectedItem, gMID, pricePer, itemId, itemName):
    
    for widget in root.winfo_children():
        widget.destroy()
        
    shipping = float(5.99)
    howMany = int(howMany)
    pricePer = int(pricePer)
    price = pricePer * howMany 
    if price > 50:
        price = price * 0.95
        messagebox.showinfo("Discount!","You are entilted to a 5% discount because you spend over £50 with us, Wowie!")
    totalPrice = price + shipping
    orderID = "orderID{}".format((len(conn.execute('SELECT * FROM orders').fetchall()) + 1))
    datePurchased = datetime.now().date()
    invoiceDueDate = datePurchased + timedelta(days=31)
    
    root.configure(bg = "#D3C9A3")
    root.title("GoCA - Basket")
    root.geometry("1519x793")
    root.resizable(False, False)
    
    


    def create_gradient(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)


    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")

    canvas.create_text(750, 110, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")


    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    rect_width = 700
    rect_height = 500
    rect_x1 = 396
    rect_y1 = (root.winfo_screenheight() - (1.25*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")

    NewItem_frame = Frame(root, bg="white")
    NewItem_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    Details_label = Label(root, text="Basket", bg="white")
    Details_label.place(x = 420, y = 240)
    Details_label.configure(font=mavenProFontBOLDLogIn)

    ValidationText_name = Label(root, text="Your basket contains  ", bg="white", )
    ValidationText_name.place(x=450, y=300)
    ValidationText_name.configure(font=typeFont2)

    ValidationNameVar_label = Label(root, text= itemName, bg="white", )
    ValidationNameVar_label.place(x=750, y=300)
    ValidationNameVar_label.configure(font=typeFont2)



    ValidationText_price = Label(root, text="The price of goods come to  ", bg="white", )
    ValidationText_price.place(x=450, y=340)
    ValidationText_price.configure(font=typeFont2)

    ArthurPainter = pricePer * howMany
    ValidationPriceVar_label = Label(root, text=ArthurPainter , bg="white", )
    ValidationPriceVar_label.place(x=750, y=340)
    ValidationPriceVar_label.configure(font=typeFont2)



    ValidationText_label3 = Label(root, text="Shipping is  ", bg="white", )
    ValidationText_label3.place(x=450, y=380)
    ValidationText_label3.configure(font=typeFont2)

    ValidationShippingVar_label = Label(root, text= shipping, bg="white", )
    ValidationShippingVar_label.place(x=750, y=380)
    ValidationShippingVar_label.configure(font=typeFont2)




    ValidationText_label4 = Label(root, text= "Your total price is £  ", bg="white", )
    ValidationText_label4.place(x=450, y=420)
    ValidationText_label4.configure(font=typeFont2)

    ValidationTotalPriceVar_label = Label(root, text= price , bg="white", )
    ValidationTotalPriceVar_label.place(x=750, y=420)
    ValidationTotalPriceVar_label.configure(font=typeFont2)




    ValidationText_label5 = Label(root, text="Your order ID will be ", bg="white", )
    ValidationText_label5.place(x=450, y=460)
    ValidationText_label5.configure(font=typeFont2)
    
    ValidationIDVar_label = Label(root, text= orderID , bg="white", )
    ValidationIDVar_label.place(x=750, y=460)
    ValidationIDVar_label.configure(font=typeFont2)




    ValidationText_label6 = Label(root, text="Todays Date is ", bg="white", )
    ValidationText_label6.place(x=450, y=500)
    ValidationText_label6.configure(font=typeFont2)

    ValidationTodayVar_label = Label(root, text= datePurchased , bg="white", )
    ValidationTodayVar_label.place(x=750, y=500)
    ValidationTodayVar_label.configure(font=typeFont2)



    ValidationText_label7 = Label(root, text="This means your invoice will be due on the ", bg="white", )
    ValidationText_label7.place(x=450, y=540)
    ValidationText_label7.configure(font=typeFont2)

    ValidationInvoiceVar_label = Label(root, text= invoiceDueDate , bg="white", )
    ValidationInvoiceVar_label.place(x=750, y=540)
    ValidationInvoiceVar_label.configure(font=typeFont2)
    

    ValidationText_label8 = Label(root, text="(Failure to comply with the due date of said invoice will result in you being smitten from the heavens above)", bg="white", fg = "light gray")
    ValidationText_label8.place(x=400, y=680)
    ValidationText_label8.configure(font=typeFont4)

    ValidationText_label9 = Label(root, text="[T&C's apply]", bg="white", fg = "light gray")
    ValidationText_label9.place(x=700, y=700)
    ValidationText_label9.configure(font=typeFont4)

    Purchase_button = Button(root, text="Purchase", bg="#D3C9A3", fg = "white", width = 13, command=lambda: insertIntoOrders(orderID, gMID, itemName, howMany, totalPrice, datePurchased, invoiceDueDate))  
    Purchase_button.place(x=420, y=585) 
    Purchase_button.configure(font=mavenProFontBOLDLogIn)

    Cancel_button = Button(root, text="Cancel", bg="#D3C9A3", fg = "white", width = 13, command=lambda: _main_Menu_(gMID))  
    Cancel_button.place(x=760, y=585) 
    Cancel_button.configure(font=mavenProFontBOLDLogIn)


    label = Label(root, image = GOCA_background_art)
    label.place (x=1251, y = 0)


    label2 = Label(root, image = GOCA_background_art)
    label2.place (x=-552, y = 0)

 
def insertIntoOrders(orderID, gMID, itemName, howMany, totalPrice, datePurchased, invoiceDueDate):
    
    
    conn.execute("INSERT INTO orders(orderID, gMID, itemName, howMany, datePurchased, totalPrice, dateToPayInvoice) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(orderID, gMID, itemName, howMany, datePurchased, totalPrice, invoiceDueDate))
    conn.commit()
    _main_Menu_(gMID)



def _check_Invoices_(gMID):

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM orders WHERE gMID = ? AND invoicePaid = 0", (gMID,))
    unpaid = cursor.fetchone()[0]
    if unpaid == 0:
        messagebox.showinfo("No Unpaid Invoices", "You have no unpaid invoices")
        _main_Menu_(gMID)
    else:
        _Invoices_Window_(gMID)
        
def _Invoices_Window_(gMID):

    for widget in root.winfo_children():
        widget.destroy()
        
    root.configure(bg = "#D3C9A3")
    root.title("GoCA - Pay / Cancel invoice")
    root.geometry("1519x793")
    root.resizable(False, False)
    
    def create_gradient(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)




    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")

    canvas.create_text(750, 110, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")
    
    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)
    
    rect_width = 700
    rect_height = 250
    rect_x1 = 396
    rect_y1 = (root.winfo_screenheight() - (2*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")

    Invoices_frame = Frame(root, bg="white")
    Invoices_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    Invoices_label = Label(root, text="Invoices", bg="white")
    Invoices_label.place(x = 665, y = 300)
    Invoices_label.configure(font=mavenProFontBOLDLogIn)

    Pay_button = Button(root, text="Pay Invoice", bg="#D3C9A3", fg = "white", width=14, command=lambda:_invoice_Paid_(gMID))  
    Pay_button.place(x=403, y=420) 
    Pay_button.configure(font=mavenProFontBOLDLogIn)

    Cancel_button = Button(root, text="Cancel Invoice", bg="#D3C9A3", fg = "white", width = 14, command=lambda: _invoice_Cancelled_(gMID))  
    Cancel_button.place(x=755, y=420) 
    Cancel_button.configure(font=mavenProFontBOLDLogIn)

    Back_button = Button(root,text="Back",bg="#D3C9A3",fg="white",width=14,command=lambda:_main_Menu_(gMID))
    Back_button.place(x=600,y=600)
    Back_button.configure(font=mavenProFontBOLDLogIn)

    label = Label(root, image = GOCA_background_art)
    label.place (x=1251, y = 0)

    label2 = Label(root, image = GOCA_background_art)
    label2.place (x=-552, y = 0)

def _invoice_Paid_(gMID):
    
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg = "#D3C9A3")
    root.title("GoCA - Pay / Cancel invoice")
    root.geometry("1519x793")
    root.resizable(False, False)


    def create_gradient(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)

    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")

    canvas.create_text(750, 110, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    rect_width = 700
    rect_height = 350
    rect_x1 = 396
    rect_y1 = (root.winfo_screenheight() - (1.4*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")


    cursor = conn.cursor()
    cursor.execute("SELECT orderID, itemName, howMany, datePurchased, totalPrice FROM orders WHERE gMID = ? AND invoicePaid = 0", (gMID,))
    unpaidOrders = cursor.fetchall()

    Invoices_frame = Frame(root, bg="white")
    Invoices_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)
    
    selectedOrder = StringVar(root)
    selectedOrder.set("Select Order to Pay")

    Invoices_label = Label(root, text="Invoices", bg="white")
    Invoices_label.place(x = 403, y = 300)
    Invoices_label.configure(font=mavenProFontBOLDLogIn)
    
    options = [f"OrderID: {order[0]}" for order in unpaidOrders]
    order_dropdown = OptionMenu(root, selectedOrder, *options)
    order_dropdown.place(x = 412, y = 400)
    order_dropdown.configure(bg="#D3C9A3", fg = "white",font = mavenProFontMED)
    
    
    orderDetails_label = Label(root, text="", bg="white")
    orderDetails_label.place(x = 400, y = 455)
    orderDetails_label.configure(font = typeFont2)
    
    def showOrderDetailsPay():
        orderDisplay = selectedOrder.get().split(": ")[1]
        
        for order in unpaidOrders:
            if orderDisplay == str(order[0]):
                
                orderDetails = f"Item Name: {order[1]}\nQuantity: {order[2]}\nDate Purchased: {order[3]}\nTotal Price: {order[4]}"
                orderDetails_label.config(text=orderDetails)
                break
            
    showDetails_button = Button(root, text="Show Order Details", bg="#D3C9A3", fg = "white", width = 18, command=showOrderDetailsPay)
    showDetails_button.place(x=665, y=420)
    showDetails_button.configure(font=mavenProFontBOLDLogIn)
    
    def pay():
        
        orderToPay = selectedOrder.get().split(": ")[1]
        
        cursor.execute("UPDATE orders SET invoicePaid = 1 WHERE orderID = ?", (orderToPay,))
        conn.commit()
        
        
        messagebox.showinfo("Invoice Paid", "Wahoo you've paid your invoice! :)")
        _main_Menu_(gMID)
        
    pay_button = Button(root, text="Pay Selected Invoice",bg="#D3C9A3", fg = "white", width=18, command=lambda:pay())
    pay_button.place(x=665, y=520)
    pay_button.configure(font=mavenProFontBOLDLogIn)

    Back_button = Button(root,text="Back",bg="#D3C9A3",fg="white",width=14,command=lambda:_main_Menu_(gMID))
    Back_button.place(x=600,y=700)
    Back_button.configure(font=mavenProFontBOLDLogIn)
    
    label = Label(root, image = GOCA_background_art)
    label.place (x=1251, y = 0)

    label2 = Label(root, image = GOCA_background_art)
    label2.place (x=-552, y = 0)
    
def _invoice_Cancelled_(gMID):
    
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg = "#D3C9A3")
    root.title("GoCA - Pay / Cancel invoice")
    root.geometry("1519x793")
    root.resizable(False, False)

    def create_gradient(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)

    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")

    canvas.create_text(750, 110, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    # Background rectangle on the left side
    rect_width = 700
    rect_height = 350
    rect_x1 = 396
    rect_y1 = (root.winfo_screenheight() - (1.4*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")

    Invoices_frame = Frame(root, bg="white")
    Invoices_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    Order_label = tk.Label(root, text="Invoices", bg="white")
    Order_label.place(x = 403, y = 300)
    Order_label.configure(font=mavenProFontBOLDLogIn)


        
    cursor = conn.cursor()
    cursor.execute("SELECT orderID, itemName, howMany, datePurchased, totalPrice FROM orders WHERE gMID = ? AND invoicePaid = 0", (gMID,))
    unpaidOrders = cursor.fetchall()
    
    selectedOrder = StringVar(root)
    selectedOrder.set("Select Order")
    


    options = [f"OrderID: {order[0]}" for order in unpaidOrders]
    order_dropdown = OptionMenu(root, selectedOrder, *options)
    order_dropdown.place(x = 403, y = 400)
    order_dropdown.configure(bg="#D3C9A3", fg = "white",font = mavenProFontMED)
    
    
    orderDetails_label = Label(root, text="", bg="white")
    orderDetails_label.place(x = 400, y = 455)
    orderDetails_label.configure(font = typeFont2)
    
    def showOrderDetailsCancel():
        
        orderDisplay = selectedOrder.get().split(": ")[1]
        
        for order in unpaidOrders:
            if orderDisplay == str(order[0]):
                orderDetails = f"Item Name: {order[1]}\nQuantity: {order[2]}\nDate Purchased: {order[3]}\nTotal Price: {order[4]}"
                orderDetails_label.config(text=orderDetails)
                break
            
    Check_button = Button(root, text="Order Details", bg="#D3C9A3", fg = "white", width = 18,command=showOrderDetailsCancel)  
    Check_button.place(x=665, y=420) 
    Check_button.configure(font=mavenProFontBOLDLogIn)
    
    def cancel():
        orderToCancel = selectedOrder.get().split(": ")[1]
        totalPrice = None
        
        for order in unpaidOrders:
            if orderToCancel == str(order[0]):
                totalPrice = order[4]
                totalPrice = float(totalPrice)
                break
            
        if totalPrice is not None:
            totalPrice = totalPrice - 5.99
            totalPrice = totalPrice * 0.20
            
            cursor.execute("UPDATE orders SET totalPrice = ?, howMany = ?, invoicePaid = 1 WHERE orderID = ?", (totalPrice, 0, orderToCancel))
            conn.commit()
            

            messagebox.showinfo( "You've cancelled your invoice :(, you will still be charged 20% = £", totalPrice)
            _main_Menu_(gMID)
            
    Cancel_button = Button(root, text="Cancel Invoice", bg="#D3C9A3", fg = "white", width=18, command=lambda:cancel())  
    Cancel_button.place(x=665, y=520) 
    Cancel_button.configure(font=mavenProFontBOLDLogIn)

    Back_button = Button(root,text="Back",bg="#D3C9A3",fg="white",width=14,command=lambda:_main_Menu_(gMID))
    Back_button.place(x=600,y=700)
    Back_button.configure(font=mavenProFontBOLDLogIn)
    
    label = Label(root, image = GOCA_background_art)
    label.place (x=1251, y = 0)

    label2 = Label(root, image = GOCA_background_art)
    label2.place (x=-552, y = 0)
    
def _all_Unpaid_Invoices_(gMID):
    
    for widget in root.winfo_children():
        widget.destroy()
        
    root.configure(bg = "#D3C9A3")
    root.title("GoCA - Pay / Cancel invoice")
    root.geometry("1519x793")
    root.resizable(False, False)

    def create_gradient(canvas, width, height, start_color, end_color):
        # Function to interpolate between two colors
        def interpolate(color1, color2, factor):
            return [
                int(color1[i] + (color2[i] - color1[i]) * factor)
                for i in range(3)
            ]

        # Convert HEX color to RGB
        def hex_to_rgb(hex_color):
            return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        start_color_rgb = hex_to_rgb(start_color)
        end_color_rgb = hex_to_rgb(end_color)

        steps = height
        for i in range(steps):
            factor = i / steps
            color = interpolate(start_color_rgb, end_color_rgb, factor)
            color_hex = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
            canvas.create_line(0, i, width, i, fill=color_hex)

    canvas = Canvas(root, highlightthickness=0)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    create_gradient(canvas, 1519, 793, "#ffffff", "#D3C9A3")

    canvas.create_text(750, 110, text="The Guild of\nCeramic Arts", font=limelightFont, fill="black", anchor="center")

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    # Background rectangle on the left side
    rect_width = 800
    rect_height = 500
    rect_x1 = 366
    rect_y1 = (root.winfo_screenheight() - (1.2*rect_height)) // 2
    rect_x2 = rect_x1 + rect_width
    rect_y2 = rect_y1 + rect_height

    rRectangle = round_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, radius=20, fill="white")
    
    Invoices_frame = Frame(root, bg="white")
    Invoices_frame.place(x=rect_x1 + 50, y=rect_y1 + 50, width=rect_width - 100, height=rect_height - 100)

    Order_label1 = Label(root, text="Unpaid Invoices", bg="white")
    Order_label1.place(x = 603, y = 240)
    Order_label1.configure(font=mavenProFontBOLDLogIn)




    cursor = conn.cursor()
    cursor.execute("SELECT orderID, gMID, itemName, howMany, datePurchased, totalPrice FROM orders WHERE invoicePaid = 0")
    unpaidInvoices = cursor.fetchall()
    
    if unpaidInvoices:
        row = 1
        for invoice in unpaidInvoices:
            invoice_label = Label(Invoices_frame, text=f"Order ID: {invoice[0]}, Customer ID: {invoice[1]}, Item: {invoice[2]}, Quantity: {invoice[3]}, Date Purchased: {invoice[4]}, Total Price: {invoice[5]}",bg="white")
            invoice_label.grid(row=row, column=0, columnspan=2)
            row += 1
    else:
        messagebox.showerror("No Unpaid Invoices",":)")

    Back_button = Button(root,text="Back",bg="#D3C9A3",fg="white",width=14,command=lambda:_main_Menu_(gMID))
    Back_button.place(x=600,y=600)
    Back_button.configure(font=mavenProFontBOLDLogIn)
            
_main_()

