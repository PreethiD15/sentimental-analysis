from tkinter import *
import tkinter.messagebox
import sqlite3
from tkinter import filedialog
import speech_recognition as sr

conn = sqlite3.connect('database.db')
print("SUCCESSFULLY CONNECTED")
c = conn.cursor()
class Application:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="SENTIMENTAL ANALYSIS USING CNN",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=120, y=0)
        self.right = Frame(master, width=380, height=600, bg='steelblue')
        self.right.pack(side=RIGHT)

        self.idpatient= Label(master, text="ENTER PATIENT's ID", font=('arial 18 bold'))
        self.idpatient.place(x=0, y=160)

        self.idpat= Entry(master, width=30)
        self.idpat.place(x=350, y=162)

        # search button
        self.search = Button(master, text="SEARCH", width=12, height=1, bg='steelblue', command=self.searchid_db)
        self.search.place(x=400, y=202)
    # function to search
    def searchid_db(self):
        self.input = self.idpat.get()
        # execute sql

        sql = "SELECT * FROM appointments WHERE id LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.id1 = self.row[0]
            self.name1 = self.row[1]
            self.time = self.row[5]
            self.idpatient = self.idpat.get()
            self.uname = Label(self.master, text="PATIENT'S NAME", font=('arial 18 bold'))
            self.uname.place(x=0, y=260)
            self.utime = Label(self.master, text="ANALYSIS TYPE", font=('arial 18 bold'))
            self.utime.place(x=0, y=300)

            # entries for each labels==========================================================

            self.ent1 = Entry(self.master, width=30)
            self.ent1.place(x=350, y=260)
            self.ent1.insert(END, str(self.name1))

            self.ent5 = Entry(self.master, width=30)
            self.ent5.place(x=350, y=300)
            self.ent5.insert(END, str(self.time))


        if(self.time=="audio" or self.time == "AUDIO"):
            tkinter.messagebox.showinfo("Alert", "PlEASE ENTER YOUR AUDIO REVIEW")
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("Audio files", "*.wav"), ("all files", "*.*")))
            print(root.filename)
            self.uraudio= Label(self.master, text="ENTER AUDIO LOCATION", font=('arial 18 bold'))
            self.uraudio.place(x=0, y=350)
            self.uraudio1 = Entry(self.master, width=40)
            self.uraudio1.place(x=350, y=350)
            self.uraudio1.insert(END, str(root.filename))
            self.audiofile = self.uraudio1.get()
            self.textfile="NULL"
            if self.audiofile == '':
                tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
            else:
                self.add = Button(self.master, text="ADD", width=12, height=1, bg='steelblue', command=self.adddb1)
                self.add.place(x=400, y=402)
            audio_file = (self.audiofile)
            r = sr.Recognizer()
            with sr.AudioFile(audio_file) as source:
                audio = r.record(source)
                try:
                    print("audio file contain " + r.recognize_google(audio))
                    autxt = r.recognize_google(audio)
                except sr.UnknownValueError:
                    print("Google speech recognizer cant understand your audio")
                except sr.RequestError:
                    print("Couldnt get the result from Google Speach Recognition")

            from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
            # load the SentimentIntensityAnalyser
            analyser = SentimentIntensityAnalyzer()
            sentence = autxt
            # find the polarity scores, i.e. sentiment score in form of positive, negative, neutral and compound scores
            scores = analyser.polarity_scores(sentence)
            print(scores)
            self.positive=scores['pos']
            self.negative = scores['neg']
            self.compound= scores['compound']
            self.box =Label(self.right,text="POSITIVE RATING",font=('arilal 14 bold'))
            self.box.place(x=20, y=60)
            self.box1 =Entry(self.right, width=35)
            self.box1.place(x=20, y=100)
            self.box1.insert(END,str(scores['pos']))
            self.boxa =Label(self.right,text="NEGATIVE RATING",font=('arilal 14 bold'))
            self.boxa.place(x=20, y=140)
            self.box12 =Entry(self.right, width=35)
            self.box12.place(x=20, y=180)
            self.box12.insert(END, str(scores['neg']))
            self.boxB=Label(self.right,text="OVER DESCRIPITION OF RATING",font=('arilal 14 bold'))
            self.boxB.place(x=20, y=220)
            self.box13 =Entry(self.right, width=35)
            self.box13.place(x=20, y=260)
            self.box14 = Entry(self.right, width=35)
            self.box14.place(x=20, y=300)
            self.box13.insert(END, str(scores['compound']))

            if (scores['pos'] > scores['neg']):
                if (scores['pos'] > 0.25):
                    a="STRONGLY POSITIVE"
                    print("STRONGLY POSITIVE")
                    self.box14.insert(END, str(a))

                else:
                    b="WEAKLY POSITIVE"
                    print("WEAKLY POSITIVE")
                    self.box14.insert(END, str(b))

            else:
                if (scores['neg'] > 0.25):
                    a="STRONGLY NEGATIVE"
                    print("STRONGLY NEGATIVE")
                    self.box14.insert(END, str(a))

                else:
                    b="WEAKLY NEGATIVE"
                    print("WEAKLY NEGATIVE")
                    self.box14.insert(END, str(b))
        else:
            tkinter.messagebox.showinfo("Alert", "PlEASE ENTER YOUR TEXT REVIEW")
            self.urtext= Label(self.master, text="ENTER TEXT REVIEW", font=('arial 18 bold'))
            self.urtext.place(x=0, y=350)
            self.urtext1 = Entry(self.master, width=40)
            self.urtext1.place(x=350, y=350)
            # ADD button
            self.add = Button(self.master, text="ADD", width=12, height=1, bg='steelblue', command=self.adddb)
            self.add.place(x=400, y=402)


    def adddb(self):
        self.audiofile="NULL"
        self.txtfile=self.urtext1.get()

        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        # load the SentimentIntensityAnalyser
        analyser = SentimentIntensityAnalyzer()
        sentence = self.txtfile
        # find the polarity scores, i.e. sentiment score in form of positive, negative, neutral and compound scores
        scores = analyser.polarity_scores(sentence)
        print(scores)
        self.positive = scores['pos']
        self.negative = scores['neg']
        self.compound = scores['compound']
        self.box = Label(self.right, text="POSITIVE RATING", font=('arilal 14 bold'))
        self.box.place(x=20, y=60)
        self.box1 = Entry(self.right, width=35)
        self.box1.place(x=20, y=100)
        self.box1.insert(END, str(scores['pos']))
        self.boxa = Label(self.right, text="NEGATIVE RATING", font=('arilal 14 bold'))
        self.boxa.place(x=20, y=140)
        self.box12 = Entry(self.right, width=35)
        self.box12.place(x=20, y=180)
        self.box12.insert(END, str(scores['neg']))
        self.boxB = Label(self.right, text="OVER DESCRIPITION OF RATING", font=('arilal 14 bold'))
        self.boxB.place(x=20, y=220)
        self.box13 = Entry(self.right, width=35)
        self.box13.place(x=20, y=260)
        self.box14 = Entry(self.right, width=35)
        self.box14.place(x=20, y=300)
        self.box13.insert(END, str(scores['compound']))

        if (scores['pos'] > scores['neg']):
            if (scores['pos'] > 0.25):
                a = "STRONGLY POSITIVE"
                print("STRONGLY POSITIVE")
                self.box14.insert(END, str(a))

            else:
                b = "WEAKLY POSITIVE"
                print("WEAKLY POSITIVE")
                self.box14.insert(END, str(b))

        else:
            if (scores['neg'] > 0.25):
                a = "STRONGLY NEGATIVE"
                print("STRONGLY NEGATIVE")
                self.box14.insert(END, str(a))

            else:
                b = "WEAKLY NEGATIVE"
                print("WEAKLY NEGATIVE")
                self.box14.insert(END, str(b))
        tkinter.messagebox.showinfo("Alert", "ADDED TO THE DATABASE SUCCESSFULLY")
        sql = "INSERT INTO 'sentimental'(id,audiofile,textfile,positive,negative,over_rating) VALUES(?,?,?,?,?,?)"
        c.execute(sql, (self.idpatient,self.audiofile, self.txtfile,self.positive,self.negative,self.compound))
        conn.commit()
        print("ADDED TO THE DATABASE SUCCESSFULLY")


    def adddb1(self):
        sql ="INSERT INTO 'sentimental'(id,audiofile,textfile,positive,negative,over_rating) VALUES(?,?,?,?,?,?)"
        c.execute(sql, (self.idpatient,self.audiofile,self.textfile,self.positive,self.negative,self.compound))
        conn.commit()
        print("ADDED TO THE DATABASE SUCCESSFULLY")
        tkinter.messagebox.showinfo("Alert", "ADDED TO THE DATABASE SUCCESSFULLY")



# creating the object
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()
