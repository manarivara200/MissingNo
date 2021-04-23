from tkinter import *
import time
import random


#variables
symbols = ['*']
global score, livesleft, resultlab, question, root
scoreupdate = object();
equationbox = object();
livesleft = object();
results = object();
root = Tk();
score = 0
userinput = object();
username = object();
name = object();
useranswer = str();
question = 0
resultlab = "unanswered"
lives = 25
leftposition = 25

def quit(): 
    root.destroy()

#brings up menu for quit or start, explains rules
def menu():
    global startbut, quitbut, rectanglewhite, radius
    radius = 15
    rectanglewhite = canvas.create_rectangle(15, 25, 390, 375, fill = "tan", outline = "tan")
    rectanglewhite = canvas.create_rectangle(400, 50, 435, 325, fill = "peru", outline = "peru")
    rectanglewhite = canvas.create_rectangle(25, 45, 375, 350, fill = "light blue", outline = "tan")
    canvas.create_text(90, 60, font = (12),  text = "MissingNo!")
    canvas.create_text(130, 110,  text = "The aim is simple, answer math  questions correctly and you will gain pages.", width = 200)
    canvas.create_text(130, 300,  text = "Produced by Big Chungus.", width = 200)
    startbut = Button(canvas, text = "start",bg='#FFDEAD', activebackground="yellow", relief=FLAT, command = name.askname)
    startbut.place(x = 400, y = 150)
    quitbut = Button(canvas, text = "quit", bg='#FFDEAD', activebackground="yellow", relief=FLAT, command = quit)
    quitbut.place(x = 400, y = 200)  

class button(object):
    def _init_(self, button):
        self.button = buttondesign

#gives the user a box to enter their name and displays it at the top of the GUI when enter is pressed
class name(object):
    def _init_ (self, name):
        self.name = username

    def askname():
        global nameinput
        startbut.destroy()
        quitbut.destroy()
        sv = StringVar()
        nameinput = object();
        displayname = str();
        canvas.create_text(70, 190,  text = "Enter you name", width = 200)
        canvas.create_text(110, 225,  text = "press Enter when complete", width = 200)
        canvas.create_text(128, 248,  text = "please input only between 3 and 8 please only use letters", width = 200)
        nameinput = Entry(canvas, textvariable = name.displayname)
        nameinput.place(x = 37, y = 200)
        nameinput.focus()
        root.bind("<Return>", name.displayname)         

    def displayname(event):
        global nameinput
        x = 0
        username = (nameinput.get())
        while x == 0:
            try:
                int(username)
                nameinput.delete(0, 'end')
                x = 0
                x = 1
            except:
                if len(username) >= 3:
                    name = Label(canvas, text = "Your name:  " + str(username))
                    name.place (x = 120, y = 5)
                    x = 1
                    labels()
                else:
                    nameinput.delete(0, 'end')
                    x = 0
                    x = 1
        x -= 1        
    
#initiation of program after name chosen displays score, lives equations and input textbox etc.
def labels():
    global score, userinput, lives, livesleft, results, resultlab, equationbox, question, scoreupdate
    nameinput.destroy()
    equationbox = Label(canvas, text = "Answer this: " + str(question))
    equationbox.place(x = leftposition, y = 378)
    livesleft = Label(canvas, text = "Lives: " + str(lives))
    livesleft.place(x = leftposition, y = 5)
    results = Label(canvas, text = "Your answer is: " + str(resultlab))
    results.place (x = leftposition, y = 400)
    scoreupdate = Label(canvas, text= "You have " + str(score) + " pages")
    scoreupdate.place(x = 300, y = 5)
    userinput = Entry(canvas, textvariable = useranswer)
    userinput.place(x = leftposition, y = 420)
    userinput.focus()
    root.bind("<Return>", useranswer)
    rectanglewhite = canvas.create_rectangle(25, 45, 375, 350, fill = "light blue", outline = "light blue")
    equationcreation()

class animation(object):
    def create():
        global root, lastid, q, ball, canvas, radius
        radius = 15
        multi = 0
        ball = list()
        q = list()
        lastid = len(ball)
        ball.append(multi)
        q.append(multi)
        multi = multi + 1
        ball[lastid] = canvas.create_rectangle(75 ,75 ,25 ,25 , fill="white", outline="black")
        q[lastid] = int(random.randint(40,361))
        animation.movement(lastid);

    def movement(lastid):
        global canvas, ball, q, root
        y = ((canvas.coords(ball[lastid])[3]) - 1)
        if y < 341:
            canvas.coords(ball[lastid], q[lastid] - radius, (((canvas.coords(ball[lastid])[1]) -1) + radius), q[lastid] + radius, (((canvas.coords(ball[lastid])[3]) - 1) + radius))
            canvas.after(150, animation.movement, lastid)
        else:
            equationcreation()

#randomly generates an equation and works out the answer to compare to userinput
def equationcreation():
    global hiddenanswer, equationbox, question
    startbut.destroy()
    quitbut.destroy()
    userinput.configure(state="normal")
    n1 = int(random.randint(1,12)) #this line and the next are to generate the 2 random numbers
    n2 = int(random.randint(1,12))
    question = str(n1) + "*" + str(n2)
    solution = n1 * n2 #structures the question and *
    equationbox.config(text = "Answer this: " + str(question))
    results.config(text = "Your answer is: Unanswered")
    hiddenanswer=str(eval(question))
    
#when user inputs the answer this decides whether they are right or wrong and sends
#them back to get another random equation if correct or deducts lives if incorrect
def useranswer(event):
    f = 0
    global score, results, lives, livesleft, resultlab, scoreupdate, userinput, hiddenanswer
    useans = (userinput.get())
    while f == 0:
        f = 1
        if len(useans) > 3:
            results.config(text="Below 3 characters please")
            userinput.delete(0, 'end')
            f = 0
            f = 1
        else:
            try:
                int(useans)
                if (str(useans) == hiddenanswer): #if user is correct
                        score += 1
                        equationbox.config(text = "Answer this:")
                        results.config(text = "Correct!")
                        scoreupdate.config(text= "You have " + str(score) + " pages")
                        userinput.delete(0, 'end')
                        userinput.configure(state="disabled")
                        animation.create()
                else:
                    if lives > 0:
                        lives -= 1  #if user is incorrect
                        livesleft.config(text = "live: " + str(lives))
                        userinput.delete(0, 'end')
                        if lives == 0: #if user is out of lives
                                restart()
                        else:
                                resultlab = "Incorrect, try again"
                                results.config(text = "Your answer is: " + str(resultlab))
                    else:
                        startbut.destroy()
                        quitbut.destroy()
                        restart()
            except:
                userinput.delete(0, 'end')
                results.config(text = "Please input numbers")
                f = 0
                f = 1
    f -= 1

#once lives run out the restart menu is displayed and this you can restart or quit
def restart():
    global startbut, score, equationbox, quitbut
    question = 0
    equationbox.config(text = "Answer this: " + str(question))
    canvas.create_rectangle(25, 45, 375, 350, fill = "white", outline = "white")
    canvas.create_text(200, 165, font = (22),  text = "Gameover!")
    canvas.create_text(200, 190, font = (22),  text = "You collected " + str(score) + " page(s)!")
    canvas.create_text(200, 215, font = (22),  text = "Well done, would you like to play again?" )
    startbut = Button(canvas, text = "yes",bg='#eee9e9', activebackground="gray", relief=FLAT,  command = varreset)
    startbut.place(x = 160, y = 230)
    quitbut = Button(canvas, text = "no",bg='#eee9e9', activebackground="gray", relief=FLAT,  command = quit)
    quitbut.place(x = 190, y = 230)

#resets the variables if the user choses to restart
def varreset():
    global lives, score
    score = 0
    lives = 3
    livesleft.config(text = "Lives: " + str(lives))
    scoreupdate.config(text= "Your score is: " + str(score))
    canvas.delete("all")
    rectanglewhite = canvas.create_rectangle(25, 45, 375, 350, fill = "light blue", outline = "light blue")
    equationcreation()

#runs the main code
def main():
    global root, canvas
    root.title("MissingNo")
    canvas = Canvas(root, width = 450, height = 450, bg = "saddle brown")
    canvas.pack()
    menu()

    root.mainloop()

main()
