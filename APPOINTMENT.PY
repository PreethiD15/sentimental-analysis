from tkinter import *
import sqlite3
import tkinter.messagebox
path= r"C:/Users/elcot.elcot-pc.000/PycharmProjects/untitled1/database.db"
conn= sqlite3.connect(path)
print("SUCESSFULLY CONNECTED")
# cursor
c = conn.cursor()
# tinker window
ids=[]
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lightblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="SENTIMENTAL ANALYSIS RECORD", font=('arial 30 bold'), fg='black', bg='lightblue')
        self.heading.place(x=0, y=0)
        # patients name
        self.name = Label(self.left, text="PATIENT'S NAME", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.name.place(x=0, y=100)

        # age
        self.age = Label(self.left, text="AGE", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.age.place(x=0, y=140)

        # gender
        self.gender = Label(self.left, text="GENDER", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.gender.place(x=0, y=180)

        # location
        self.location = Label(self.left, text="LOCATION", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.location.place(x=0, y=220)

        # appointment time
        self.time = Label(self.left, text="ANALYSIS TYPE", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.time.place(x=0, y=260)

        # phone
        self.phone = Label(self.left, text="PHONE NUMBER", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.phone.place(x=0, y=300)

        self.phone = Label(self.left, text="HOSPITAL NAME", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.phone.place(x=0, y=340)

        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)
        self.hospital_ent = Entry(self.left, width=30)
        self.hospital_ent.place(x=250, y=340)
        # button to perform a command
        self.submit = Button(self.left, text="ADD RECORD", width=20, height=2, bg='steelblue',command=self.add_appointment)
        self.submit.place(x=270, y=380)
        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="LOGS", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=45, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END,"TOTAL SENTIMENTAL RECORD TILL NOW:  " + str(self.final_id))

        #add appointment
    def add_appointment(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()
        self.val7= self.hospital_ent.get()


        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone,hospital_name) VALUES(?, ?, ?, ?, ?, ?,?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6,self.val7))
            a =c.execute( "SELECT ID FROM 'appointments' where name=? and  age = ? and gender = ? and location=? and scheduled_time=? and phone= ? and hospital_name=?",(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6,self.val7))
            for r in a:
                self.b=r[0]
                #print(b)
            conn.commit()

            tkinter.messagebox.showinfo("Success", "SENTIMENTAL RECORD FOR THE PATIENT " + str(self.val1) + " HAS BEEN CREATED")

            self.box.insert(END, '\n RECORD FOR THE ' + str(self.val1) + ' IS OF THE TYPE ' + str(self.val5)+" \n THE ID "+str(self.b))

            print("SUCESSFULLY ADDED TO THE DATABASE")


# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
