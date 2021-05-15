import numpy as np
import cv2
from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os


class Student_attendance:  
    def __init__(self, root,data):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_rollNumText = StringVar()
        self.var_nameText = StringVar()
        self.var_yearText = StringVar()
        self.var_semesterText = StringVar()
        self.var_depText = StringVar()
        self.var_batchText = StringVar()
        self.var_emailText = StringVar()
        self.var_phoneText = StringVar()
        self.var_course1Text = StringVar()
        self.var_course2Text = StringVar()
        self.var_course3Text = StringVar()
        self.var_course4Text = StringVar()
        self.var_dobText = StringVar()
        self.var_genderText = StringVar()
        self.var_fatherText = StringVar()
        self.var_motherText = StringVar()
        self.mydata=data
        # self.var_rollNum.set("101916054")
        # self.var_name.set("Hello")
        # var_rollNumText.set("Hello")
        # var_nameText.set("Hello")
        # var_yearText.set("Hello")
        # var_semesterText.set("Hello")
        # var_depText.set("Hello")
        # var_batchText.set("Hello")
        # var_emailText.set("vmakan_be19@thapar.edu")
        # var_phoneText.set("Hello")
        # var_course1Text.set("Hello")
        # var_course2Text.set("Hello")
        # var_course3Text.set("Hello")
        # var_course4Text.set("Hello")
        # var_dobText.set("11-12-2000")
        # var_genderText.set("Hello")
        # var_fatherText.set("Hello")
        # var_motherText.set("Hello")

        # img1 = main background
        img1 = Image.open("Images/wall.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="ATTENDANCE DETAILS",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)

        ##########################################################

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=34, y=70, width=1480, height=800)
        # divide into label frame in main frame .... # label frame m ham title daal skte hai

        #########################################################

        # upper label frame
        upper_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        upper_frame.place(x=10, y=10, width=1460, height=250)

        # img2 = thapar logo
        img2 = Image.open("Images/db2.png")
        img2 = img2.resize((700, 230), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        logo_img = Label(upper_frame, image=self.photoimg2)
        logo_img.place(x=745, y=-3, width=700, height=230)

        # Enrollment no.
        rollNum_label = Label(
            upper_frame,
            text="Enrollment Number",
            font=("times new roman", 17),
            bg="white",
        )
        rollNum_label.place(x=10, y=10, anchor=NW)

        rollNum_entry = ttk.Entry(
            upper_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        rollNum_entry.place(x=245, y=10, anchor=NW)

        # date
        date_label = Label(
            upper_frame,
            text="Date  (dd/mm/yyyy)",
            font=("times new roman", 17),
            bg="white",
        )
        date_label.place(x=10, y=70, anchor=NW)

        date_entry = ttk.Entry(
            upper_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        date_entry.place(x=245, y=70, anchor=NW)

        # status label
        status_label = Label(
            upper_frame,
            text="Status",
            font=("times new roman", 17),
            bg="white",
        )
        status_label.place(x=10, y=130, anchor=NW)

        # combo is used for dropdown like entering text
        status_combo = ttk.Combobox(
            upper_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        status_combo["values"] = ("", "Present", "Absent")
        status_combo.current(0)  # to give the bydeafault index

        status_combo.place(x=245, y=130, anchor=NW)

        # time
        time_label = Label(
            upper_frame,
            text="Time (hh:mm) ",
            font=("times new roman", 17),
            bg="white",
        )
        time_label.place(x=10, y=190, anchor=NW)

        time_entry = ttk.Entry(
            upper_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        time_entry.place(x=245, y=190, anchor=NW)

        # --- buttons --- #

        updateAttendance_btn = Button(
            upper_frame,
            width=20,
            height=3,
            text="Update Student\n  Attendance",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        updateAttendance_btn.place(x=475, y=80)

        ###########################################################################################

        # lower label
        lower_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Attendance Details",
            font=("times new roman", 12, "bold"),
        )
        lower_frame.place(x=10, y=267, width=1460, height=520)

        # ========Search System=============
        Search_frame = LabelFrame(
            lower_frame,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        Search_frame.place(x=5, y=10, width=1450, height=115)

        # Label
        search_label = Label(
            Search_frame,
            text="Search By : ",
            font=("times new roman", 20, "bold"),
            height=1,
            width=15,
            relief=SUNKEN,
            bg="red",
            fg="white",
        )
        # search_label.grid(row=0, column=0, padx=10, pady=20, sticky=W)
        search_label.place(x=10, y=17)

        search_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=15,
        )
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)  # to give the bydeafault index
        search_combo.place(x=230, y=20)

        search_entry = ttk.Entry(
            Search_frame, width=25, font=("times new roman", 13, "bold")
        )
        search_entry.place(x=450, y=20)

        # Buttons
        search_btn = Button(
            Search_frame,
            width=20,
            text="Search",
            font=("time new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        search_btn.place(x=700, y=20)

        showAll_btn = Button(
            Search_frame,
            width=20,
            text="Show All",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        showAll_btn.place(x=950, y=20)

        exportAll_btn = Button(
            Search_frame,
            width=20,
            text="Export All Attendance",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        exportAll_btn.place(x=1200, y=20)

        # =========Table frame=================
        table_frame = Frame(lower_frame, bd=3, bg="white", relief=SUNKEN)
        table_frame.place(x=5, y=100, width=1450, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
               "Enroll no",
               "Name",
               "Year",
               "Sem",
               "Dep", 
               "Batch",
               "Email",
               "Phone_no", 
               "Father_no", 
               "Mother_no",  
               "Course1", 
               "Course2", 
               "Course3", 
               "Course4",
               "Gender",
               "DOB"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)

        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Enroll no", text="Enroll no")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Sem")
        self.student_table.heading("Dep", text="Dep")
        self.student_table.heading("Batch", text="Batch")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone_no", text="Phone_no")
        self.student_table.heading("Father_no", text="Father_no")
        self.student_table.heading("Mother_no", text="Mother_no")
        self.student_table.heading("Course1", text="Course1")
        self.student_table.heading("Course2", text="Course2")
        self.student_table.heading("Course3", text="Course3")
        self.student_table.heading("Course4", text="Course4")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table["show"] = "headings"

        self.student_table.column("Enroll no", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100) 
        self.student_table.column("Dep", width=100)
        self.student_table.column("Batch", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone_no", width=100)
        self.student_table.column("Father_no", width=100)
        # self.student_table.column("DOB", width=100)
        # self.student_table.column("email", width=100)
        # #self.student_table.column("email", width=200)
        # self.student_table.column("phone_no", width=100)
        # self.student_table.column("Father_contact", width=100)
        self.student_table.column("Mother_no", width=100)
        self.student_table.column("Course1", width=200)
        self.student_table.column("Course2", width=200)
        self.student_table.column("Course3", width=200)
        self.student_table.column("Course4", width=200)
        self.student_table.column("Gender", width=200)
        self.student_table.column("DOB", width=200)

        self.student_table.pack(fill=BOTH, expand=1)
        #self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ============================== Function Declaration ===================================#

    # =======================fetch data =================== #
    def fetch_data(self):
        year=self.mydata[0]
        batch=self.mydata[2]
        course=self.mydata[3]  
        table_name=year +"_"+batch
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shiv@2000",
            database="Face_Recognition_db",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()
        sql1="select * from {}".format(str(table_name))
        my_cursor.execute(sql1)
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

        else:
            self.student_table.delete(*self.student_table.get_children())

        conn.commit()
        conn.close()

    # ======================= get cursor =================#

    # def get_cursor(self, event=""):
    #     cursor_focus = self.student_table.focus()
    #     content = self.student_table.item(cursor_focus)
    #     data = content["values"]
    
    #     self.var_rollNumText.set(data[0])
    #     self.var_nameText.set(data[1])
    #     self.var_yearText.set(data[2])
    #     self.var_semesterText.set(data[3])
    #     self.var_depText.set(data[4])
    #     self.var_batchText.set(data[5])
    #     self.var_emailText.set(data[6])
    #     self.var_phoneText.set(data[7])
    #     self.var_course1Text.set(data[11])
    #     self.var_course2Text.set(data[12])
    #     self.var_course3Text.set(data[13])
    #     self.var_course4Text.set(data[14])
    #     self.var_dobText.set(data[16])
    #     self.var_genderText.set(data[15])
    #     self.var_fatherText.set(data[8])
    #     self.var_motherText.set(data[9])


if __name__ == "__main__":
    root = Tk()
    obj = Student_attendance(root)
    root.mainloop()
