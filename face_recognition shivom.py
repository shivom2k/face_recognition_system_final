import numpy as np
import cv2
from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
from time import strftime
from datetime import datetime
import pandas as pd


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")
        self.var_batch= StringVar()
        self.var_batch_no= StringVar()
        self.var_subject= StringVar()
        self.var_roll=StringVar()
        self.var_att=StringVar()
        self.var_dat=StringVar()
        title_lbl = Label(
            self.root,
            text="MARK ATTENDANCE",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # left image
        #img1 = Image.open("Images/.jpeg")
        img1 = Image.open("Images/face_recog.jpeg")
        img1 = img1.resize((675, 855), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=45, width=675, height=855)

        # right image
        img2 = Image.open("Images/face_recog2.jpg")
        img2 = img2.resize((875, 855), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=675, y=45, width=875, height=855)
        # class student information
        class_Student_frame = LabelFrame(
             bg_img,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Class Student Information",
            font=("times new roman", 12, "bold"),
        )
        class_Student_frame.place(x=5, y=270, width=680, height=250)
        #===============================================#====================
        batch_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_batch,
            font=("times new roman", 15, "bold"),
            state="readonly",
            width=11,
        )
        batch_combo["values"] = ("Batch", "2CS", "COE", "EE")
        batch_combo.current(0)  # to give the bydeafault index
        batch_combo.grid(row=0, column=1, padx=3, pady=2, sticky=W)
        #=========================================#=================================
        batch_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_batch_no,
            font=("times new roman", 15, "bold"),
            state="readonly",
            width=11,
        )
        batch_combo["values"] = ("Batch_no", "10", "11", "12")
        batch_combo.current(0)  # to give the bydeafault index
        batch_combo.grid(row=0, column=2, padx=3, pady=2, sticky=W)
        #=========================================#=================================
        batch_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_subject,
            font=("times new roman", 15, "bold"),
            state="readonly",
            width=11,
        )
        batch_combo["values"] = ("subject", "DBMS", "CN")
        batch_combo.current(0)  # to give the bydeafault index
        batch_combo.grid(row=3, column=1, padx=3, pady=2, sticky=W)
        #===============================================#====================
        batch_combo = ttk.Combobox(
            class_Student_frame,
            textvariable=self.var_att,
            font=("times new roman", 15, "bold"),
            state="readonly",
            width=11,
        )
        batch_combo["values"] = ("attendance", "present", "absent")
        batch_combo.current(0)  # to give the bydeafault index
        batch_combo.grid(row=1, column=2, padx=3, pady=2, sticky=W)
         #studentid (roll no.)
        studentId_label = Label(
            class_Student_frame,
            text="Roll No",
            font=("times new roman", 17, "bold"),
            bg="white",
        )
        studentId_label.grid(row=2, column=1, padx=3, pady=2, sticky=W)

        studentID_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_roll,
            width=15,
            font=("times new roman", 13, "bold"),
        )
        studentID_entry.grid(row=2, column=2, padx=3, pady=2, sticky=W)
         #date
        studentId_label = Label(
            class_Student_frame,
            text="date in _DD_MM_YYYY",
            font=("times new roman", 17, "bold"),
            bg="white",
        )
        studentId_label.grid(row=4, column=1, padx=3, pady=2, sticky=W)

        studentID_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_dat,
            width=15,
            font=("times new roman", 13, "bold"),
        )
        studentID_entry.grid(row=4, column=2, padx=3, pady=2, sticky=W)
         
        # mark attandance  button
        b1_1 = Button(
            bg_img,
            command=self.face_recog,
            text="Mark Attendance",
            cursor="hand2",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=0, y=600, width=200, height=40)
        batch_combo.grid(row=1, column=1, padx=3, pady=2, sticky=W)
        #  export button
        b1_1 = Button(
            bg_img,
            command=self.export_attendance,
            text="export_attendance",
            cursor="hand2",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=250, y=600, width=200, height=40)
        batch_combo.grid(row=1, column=1, padx=3, pady=2, sticky=W)
        # update attandance button
        b1_1 = Button(
            bg_img,
            command=self.update_atendance,
            text="update_attendance",
            cursor="hand2",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=500, y=600, width=200, height=40)
    # ====================update_attandance =================#
    def update_atendance(self):
        roll_no=self.var_roll.get()
        batch=self.var_batch.get()
        batch_no=self.var_batch_no.get()
        subject=self.var_subject.get()
        table_name=subject+"_"+batch+batch_no
        dat=self.var_dat.get()
        att=str(self.var_att.get())
        att="'"+att+"'"

        try: 
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345",
                    database="face_recognizer",
                    auth_plugin="mysql_native_password",
                )
            #query="UPDATE cn_2cs10 SET email = 'present' WHERE roll_no = %s "
            #now = datetime.now()
            d1 = dat
            string="UPDATE {} SET {} = {} WHERE roll_no = {} ".format(str(table_name),str(d1),str(att),str(roll_no))
            print(string)
            my_cursor = conn.cursor()
            my_cursor.execute(string)
            #my_cursor.execute(
                #"UPDATE cn_2cs10 SET %s = %s WHERE roll_no = %s "%(d1),((str('present'),str(roll_num)),),)
            
    #         my_cursor = conn.cursor()
    #         query="select * from {}".format(str(batch))

    #         df=pd.read_sql(query,con=conn)
    #         print(df)
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print(e)            
         

        
    # ==================Attendance =============================
    def mark_attendance(self, i):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
                print(name_list)

            if str(i) not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{dtString},{d1},Present")
    # =======================mark attandance==========================#
    def mark__attendance(self,roll_num,batch):
        try: 
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345",
                    database="face_recognizer",
                    auth_plugin="mysql_native_password",
                )
            #query="UPDATE cn_2cs10 SET email = 'present' WHERE roll_no = %s "
            now = datetime.now()
            d1 = now.strftime("_%d_%m_%Y")
            string="UPDATE {} SET {} = {} WHERE roll_no = {} ".format(str(batch),str(d1),str("'present'"),str(roll_num))
            print(string)
            my_cursor = conn.cursor()
            my_cursor.execute(string)
            #my_cursor.execute(
                #"UPDATE cn_2cs10 SET %s = %s WHERE roll_no = %s "%(d1),((str('present'),str(roll_num)),),)
            
    #         my_cursor = conn.cursor()
    #         query="select * from {}".format(str(batch))

    #         df=pd.read_sql(query,con=conn)
    #         print(df)
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print(e)   


    #============== update_attendance#==========================================#
    def export_attendance(self):
        batch=self.var_batch.get()
        batch_no=self.var_batch_no.get()
        subject=self.var_subject.get()
        table_name=subject+"_"+batch+batch_no
        try: 
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345",
                    database="face_recognizer",
                    auth_plugin="mysql_native_password",
                )
          
            query="select * from {}".format(str(table_name))

            df=pd.read_sql(query,con=conn)
            df.to_csv("./excel/Modified attendance.csv")

            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print(e)        


    #=======================create date=============================#

    
    def create_date(self,batch):
        try: 
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345",
                    database="face_recognizer",
                    auth_plugin="mysql_native_password",
                )
            #query="UPDATE cn_2cs10 SET email = 'present' WHERE roll_no = %s "
            now = datetime.now()
            d1 = now.strftime("_%d_%m_%Y")
            string="alter table {} add {} varchar(100) ".format(str(batch),str(d1))
            print(string)
            my_cursor = conn.cursor()
            my_cursor.execute(string)
            #my_cursor.execute(
                #"UPDATE cn_2cs10 SET %s = %s WHERE roll_no = %s "%(d1),((str('present'),str(roll_num)),),)
            
    #         my_cursor = conn.cursor()
    #         query="select * from {}".format(str(batch))
    #         query="select * from {}".format(str(batch))

    #         df=pd.read_sql(query,con=conn)
    #         print(df)
            conn.commit()
            conn.close()
        except mysql.connector.Error as e:
            print(e)

    # ==================Face Recognition =========================
    def face_recog(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainer/trainer.yml")
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        batch=self.var_batch.get()
        batch_no=self.var_batch_no.get()
        subject=self.var_subject.get()
        table_name=subject+"_"+batch+batch_no
        print(table_name)
        
        self.create_date(table_name)
        #create_date(a)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # iniciate id counter
        id = 0

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)  # set video widht
        cam.set(4, 480)  # set video height

        # Define min window size to be recognized as a face
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:

            ret, img = cam.read()
            # img = cv2.flip(img, -1)  # Flip vertically

            if ret == False:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                id, confidence = recognizer.predict(gray[y : y + h, x : x + w])

                # conn = mysql.connector.connect(
                #     host="localhost",
                #     user="root",
                #     password="ShadowWalker77",
                #     database="Face_Recognition_db",
                #     auth_plugin="mysql_native_password",
                # )
                # my_cursor = conn.cursor()
                # my_cursor.execute(
                #     "select std_name from student_table where rollNum=" + str(id)
                # )
                # n = my_cursor.fetchone()
                # n = "+".join(n)

                # my_cursor.execute(
                #     "select batch from student_table where rollNum=" + str(id)
                # )
                # b = my_cursor.fetchone()
                # b = "+".join(b)

                # my_cursor.execute(
                #     "select batch_num from student_table where rollNum=" + str(id)
                # )
                # bn = my_cursor.fetchone()
                # bn = "+".join(str(bn))

                # Check if confidence is less them 100 ==> "0" is perfect match
                if confidence < 77:
                    confidence = "  {0}%".format(round(100 - confidence))
                    self.mark__attendance(id,table_name)

                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

                # cv2.putText(
                #     img, f"Name: {n}", (x + 5, y - 2), font, 0.6, (255, 255, 255), 2
                # )
                # cv2.putText(
                #     img, f"Roll: {id}", (x + 5, y - 7), font, 0.6, (255, 255, 255), 2
                # )
                # cv2.putText(
                #     img,
                #     f"Batch: {b}{bn}",
                #     (x + 5, y - 12),
                #     font,
                #     0.6,
                #     (255, 255, 255),
                #     2,
                # )

                cv2.putText(
                    img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1
                )

            cv2.imshow("Marking Attendance", img)

            k = cv2.waitKey(100) & 0xFF  # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
