from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk # To crop and change size of images used -------- PIL stands for Pillow library

from Student import Student
import os

from face_recognition import Face_Recognition
from attendance import Attendance


class face_recognition_system:
    def __init__(self, root): # Root is the name of the window
        self.root = root # Made the window of face recognition i.e. - root and assigned root variable which we got from init
        self.root.geometry("1550x900+0+0") # Now we will set the Geometry (width x height + x_start + y_start)
        self.root.title("Face Recognition Attendance System") # Setting the title of the window
        # THESE ABOVE 3 LINES WILL CREATE A BLANK WINDOW

        # img1 = main background -------------- THESE 5 LINES WILL CREATE AND PUT THE IMAGE ON THE WINDOW
        img1 = Image.open("Images/db2.png") # Opening the image  ---------------------  To convert '\' to '/' in python we use 'r' in front of the path  ----"Images/db2.png"-------OR---------
        img1 = img1.resize((1550, 900), Image.ANTIALIAS) # Resizing the image, Image.ANTIALIAS is used to convert a high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(img1) # Now converting the above image to the class variable as as to put in the window

        bg_img = Label(self.root, image=self.photoimg1) # This tells on which window we should place the image , i.e.-self.root --------- This widget (LABEL) implements a display box where you can place text or images  aking the specified block in the window so as to put the image there 
        bg_img.place(x=0, y=0, width=1550, height=900) # Placing/ showing the image on the window ---------- (x,y are with respect to bg_img)****
        # We can also add self with bg_img, i.e. - self.bg_img

        #Label is a object and do hatever we want it to do - contains images, contains text and many more


        # title
        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # buttons

        # img2 .. student details
        img2 = Image.open("Images/student.png")
        img2 = img2.resize((220, 220), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Below command arguments helps us to link two pages
        b1 = Button(
            bg_img,
            command=self.student_details,
            image=self.photoimg2,
            cursor="hand2",
            borderwidth=3,
        ) # This creates the button and we used cursor in this so as to bring hand when the user points to the button
        # Wrote bg_img as first argument to tell ki kiske upar ye image honi chaiye
        b1.place(x=200, y=150, width=230, height=230)

        b1_1 = Button(
            bg_img,
            command=self.student_details,
            text="Student Details",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=200, y=350, width=230, height=40)

        # img3 .. face detector
        img3 = Image.open("Images/face_detector1.jpeg")
        img3 = img3.resize((220, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(
            bg_img,
            command=self.face_data,
            image=self.photoimg3,
            cursor="hand2",
            borderwidth=3,
        )
        b1.place(x=650, y=150, width=230, height=230)

        b1_1 = Button(
            bg_img,
            command=self.face_data,
            text="Face Detector",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=650, y=350, width=230, height=40)

        # img4 .. Attendance
        img4 = Image.open("Images/attendance.jpeg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img, command=self.attendance_data, image=self.photoimg4, cursor="hand2"
        )
        b1.place(x=1100, y=150, width=230, height=230)

        b1_1 = Button(
            bg_img,
            command=self.attendance_data,
            text="Attendance",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=1100, y=350, width=230, height=40)

        # img5 .. Train Data
        img5 = Image.open("Images/trainData2.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=200, y=450, width=230, height=230)

        b1_1 = Button(
            bg_img,
            text="Train Data",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=200, y=650, width=230, height=40)

        # img6 .. Photos
        img6 = Image.open("Images/photos.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, command=self.open_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=650, y=450, width=230, height=230)

        b1_1 = Button(
            bg_img,
            command=self.open_img,
            text="Photos",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=650, y=650, width=230, height=40)

        # img7 .. Exit
        img7 = Image.open("Images/exit2.jpeg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=450, width=230, height=230)

        b1_1 = Button(
            bg_img,
            text="Exit",
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        b1_1.place(x=1100, y=650, width=230, height=40)

    ######################functions buttons###########################

    def student_details(self):
        self.new_window = Toplevel(self.root) # This asks where we want to open our window
        self.app = Student(self.new_window)
        # Now we will insert its functionality by adding 'command' argument in the student's button

    def open_img(self):
        os.startfile("dataset")

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk() # It is a python made interface or the blank page on which we add the elements like boxes, rectangle, etc.
    obj = face_recognition_system(root) # Making the object of the class
    root.mainloop() # root. mainloop() is a method on the main window which we execute when we want to run our application. This method will loop forever, waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program with a keyboard interrupt in the console
    # It listens to the users command to close the window
