#Rock Paper Scissor Game


from tkinter import *
from PIL import Image, ImageTk
from random import randint


root = Tk()
root.title("Rock  Paper Scissor")
root.configure(background="#332e30")


image_size = (500, 500)

rock_img = ImageTk.PhotoImage(Image.open("RockImage.jpeg").resize(image_size))
paper_img = ImageTk.PhotoImage(Image.open("PaperImage.jpg").resize(image_size))
scissor_img = ImageTk.PhotoImage(Image.open("SciessorImage.webp").resize(image_size))
rock_img_robot = ImageTk.PhotoImage(Image.open("RockRobot.jpg").resize(image_size))
paper_img_robo = ImageTk.PhotoImage(Image.open("RobotPaper.Jpg").resize(image_size))
scissor_img_robot = ImageTk.PhotoImage(Image.open("RobotScissor.jpg").resize(image_size))


user_label = Label(root, image=scissor_img, bg="Black")
comp_label = Label(root, image=scissor_img_robot, bg="Black")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


playerScore = Label(root, text=0, font=("arial", "40", "bold"), bg="Red", fg="Black")
computerScore = Label(root, text=0, font=("arial", "40", "bold"), bg="Blue", fg="Black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)


user_indicator = Label(root, font=("Times new roman", "20", "bold"), text="\n: USER : ", bg="#332e30", fg="white")
comp_indicator = Label(root, font=("Times new roman", "20", "bold"), text="\n: COMPUTER : ", bg="#332e30", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

msg = Label(root, font=("arial", "20", "bold"), bg="#525252", fg="white")
msg.grid(row=3, column=2)


def updateMessage(x):
    msg['text'] = x


def updateHumanScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateComputerScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

def checkwinner(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose!!!")
            updateComputerScore()
        else:
            updateMessage("You win!!!")
            updateHumanScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose!!!")
            updateComputerScore()
        else:
            updateMessage("You win!!!")
            updateHumanScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose!!!")
            updateComputerScore()
        else:
            updateMessage("You win!!!")
            updateHumanScore()

# List of choices
choices = ["rock", "paper", "scissor"]

# Function to update choice
def updateChoice(x):
    computerSelection = choices[randint(0, 2)]
    if computerSelection == "rock":
        comp_label.configure(image=rock_img_robot)
    elif computerSelection == "paper":
        comp_label.configure(image=paper_img_robo)
    else:
        comp_label.configure(image=scissor_img_robot)

    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkwinner(x, computerSelection)


rock = Button(root, width=20, height=2, font=("Times new Roman", "10", "bold"), text="ROCK",
              bg="Grey", fg="Black", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1)

paper = Button(root, width=20, height=2, font=("Times new Roman", "10", "bold"), text="PAPER",
               bg="white", fg="black", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2)

scissor = Button(root, width=20, height=2, font=("arial", "10", "bold"), text="SCISSOR",
                 bg="Gold", fg="red", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3)

root.mainloop()
