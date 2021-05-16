from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk


class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_memType = StringVar()  # memberType
        
        self.var_get_email = StringVar()  # memberType
        self.var_otp = StringVar()
        self.final_otp = ""
        self.var_password = StringVar()
        self.var_password_again = StringVar()
        self.var_after_5_min = ''
        

        # img1 = main background
        img1 = Image.open("Images/thapar1.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # img2 = thapar logo
        img2 = Image.open("Images/thaparLogo.png")
        img2 = img2.resize((432, 93), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        logo_img = Label(self.root, image=self.photoimg2)
        logo_img.place(x=20, y=20, width=432, height=93)

        # login frame
        login_frame = Frame(bg_img, bd=2, bg="white", highlightthickness=5)
        login_frame.place(x=510, y=220, width=500, height=320)

        login_frame.config(highlightbackground="black", highlightcolor="black")

        # account label
        account_label = Label(
            login_frame,
            text="Reset Password",
            font=("times new roman", 22),
            bg="white",
            fg="red",
        )
        account_label.grid(row=0, column=0, padx=0)

        # Email
        email_label = Label(
            login_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=50, y=50, anchor=NW)

        email_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_get_email,
            width=22,
            font=("times new roman", 13),
        )
        email_entry.place(x=275, y=50, anchor=NW)

        # otp button
        otpSend_btn = Button(
            login_frame,
            # command=self.add_data,
            highlightthickness=1,
            width=17,
            height=2,
            text="Send OTP",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        otpSend_btn.place(x=50, y=95, anchor=NW)
        otpSend_btn.config(highlightbackground="grey", highlightcolor="grey")

        # otp label
        otp_label = Label(
            login_frame,
            text="OTP :",
            font=("times new roman", 17),
            bg="white",
        )
        otp_label.place(x=220, y=100, anchor=NW)

        otp_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_otp,
            width=22,
            font=("times new roman", 13),
        )
        otp_entry.place(x=275, y=100, anchor=NW)

        # password
        password_label = Label(
            login_frame,
            text="New Password",
            font=("times new roman", 17),
            bg="white",
        )
        password_label.place(x=50, y=150, anchor=NW)

        password_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_password,
            width=22,
            font=("times new roman", 13),
        )
        password_entry.place(x=275, y=150, anchor=NW)

        # confirm Password
        confirmPassword_label = Label(
            login_frame,
            text="Confirm Password",
            font=("times new roman", 17),
            bg="white",
        )
        confirmPassword_label.place(x=50, y=200, anchor=NW)

        password_entry = ttk.Entry(
            login_frame,
            textvariable=self.var_password_again,
            width=22,
            font=("times new roman", 13),
        )
        password_entry.place(x=275, y=200, anchor=NW)

        # update button
        update_btn = Button(
            login_frame,
            # command=self.add_data,
            width=48,
            height=2,
            text="Update Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )

        update_btn.place(x=50, y=250, anchor=NW)

    # ---- functions -----#
    def get_otp(self):
        if (
            self.var_get_email.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            temp_email = self.var_get_email.get()
            
            try: # Now we will connect with SQL
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Shiv@2000",
                    database="face_recogniser",
                    auth_plugin="mysql_native_password",
                )
                my_cursor = conn.cursor() # To store the values given by the user
                temp_email1 = "'"+temp_email+"'"
                print(temp_email1)
                sql = 'select email from credentials where email={}'.format(str(temp_email1))
                my_cursor.execute(sql)

                my_email = my_cursor.fetchall()
                
                conn.commit()
                #self.fetch_data()
                conn.close() # Closing teh connection
                
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

            if(len(my_email)>0):
                if str(my_email[0][0])==str(temp_email):
                    # Give OTP
                    admin_email = 'sphinxphoenix.adm@gmail.com'
                    admin_password = "Suv.square"

                    # Now wend the OTP

                    self.final_otp = np.random.randint(100000,900000)
                    self.var_after_5_min = datetime.datetime.now() + datetime.timedelta(minutes = 1)
                    
                    try: 
                        # creates SMTP session
                        s = smtplib.SMTP('smtp.gmail.com', 587)

                        # start TLS for security
                        s.starttls()

                        # Authentication
                        s.login(admin_email, admin_password)

                        # message to be sent
                        message = "Otp is "+str(self.final_otp)+". OTP is valid for 5 minutes only."

                        # sending the mail
                        s.sendmail(admin_email, temp_email, message)

                        # terminating the session
                        s.quit()

                        messagebox.showinfo("Success", "OTP has been sent to your registered email id", parent=self.root)
                    
                    except Exception as es:
                        messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

                    
                else:
                    messagebox.showerror("Error", "Invalid Email (Enter the registered thapar mail", parent=self.root)
            else:
                messagebox.showerror("Error", "Invalid Email (Enter the registered thapar mail", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = login(root)
    root.mainloop()