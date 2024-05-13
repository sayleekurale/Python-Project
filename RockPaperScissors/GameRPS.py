from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="#088")
root.resizable(False,False)

# pictures
rock_image = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_image = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_image = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_image_com = ImageTk.PhotoImage(Image.open("rock.png"))
paper_image_com = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_image_com = ImageTk.PhotoImage(Image.open("scissors-user.png"))

# user image label
user_label = Label(root, image=scissors_image, bg="#088")
user_label.grid(row=1, column=4)

# computer image label
computer_label = Label(root, image=scissors_image_com,background="#088")
computer_label.grid(row=1, column=0)

#score
playerscore = Label(root,text=0,font=1000,bg="#088",fg="white")
computerscore=Label(root,text=0,font=100,bg="#088",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="USER",bg="#088")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#088")
comp_indicator.grid(row=0,column=1)
user_indicator.grid(row=0,column=3)

#messages
msg=Label(root,bg="#088",fg="white",font="times 20 bold")
msg.grid(row=1,column=2)


#update message
def updatemessage(x):
    msg['text'] = x

#update users score
def updateuserScore():
    score= int(playerscore["text"])
    score +=1
    playerscore["text"]=str(score)


#update computer score
def updatecompScore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)


#checkwinner
def checkwin(player,computer):
    if player==computer:
        updatemessage("Its a Tie !!")
    elif player == "rock":
        if computer == "paper":
            updatemessage("You lose !!!")
            updatecompScore()
        else:
            updatemessage("Congrats You Win")
            updateuserScore()
    elif player=="paper":
        if computer == "scissors":
            updatemessage("You lose!!!")
            updatecompScore()
        else:
            updatemessage("Congrats You Win")
            updateuserScore()

    elif player == "scissor":
        if computer == "rock":
            updatemessage("You lose!!!")
            updatecompScore()
        else:
            updatemessage("Congrats You Win")
            updateuserScore()
    else:
        pass

#update choices
choices=["rock","paper","scissors"]
def updatechoices(x):
# for computer
    comp_choices=choices[randint(0,2)]
    if comp_choices=="rock":
        computer_label.configure(image=rock_image_com)
    elif comp_choices=="paper":
        computer_label.configure(image=paper_image_com)
    else:
        computer_label.configure(image=scissors_image_com)



#for user

    if x=="rock":
        user_label.configure(image=rock_image)
    elif x=="paper":
        user_label.configure(image=paper_image)
    else :
        user_label.configure(image=scissors_image)
    checkwin(x,comp_choices)



#buttons
rock=Button(root,width=20,height=2,text="ROCK",background="#FF3E4D",fg="purple",font="times 20 bold",command=lambda:updatechoices("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",background="#FAD02E",fg="red",font="times 20 bold",command=lambda:updatechoices("paper")).grid(row=2,column=2)
scissors=Button(root,width=20,height=2,text="SCISSORS",background="#0ABDE3",fg="green",font="times 20 bold",command=lambda:updatechoices("scissors")).grid(row=2,column=3)


root.mainloop()