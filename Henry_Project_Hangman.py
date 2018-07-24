import random

words = ["Kenny really wants a Macbook Pro", "Henry Woodhouse", "Angelo Ededas", "Gus Pollard", "Alan Richards", "Jade Wong", "Kalan Malhotra", "Nicola Ha", "Paromita Roy", "Lauxsh Balaratnam", "Michael Hoy", "Raj Mahan", "Mark Aldridge", "User Acceptance Testing", "Prod", "Hashicorp Terraform", "Hashicorp Packer", "Hashicorp Vault", "Puppet", "Jenkins", "Chef", "Ansible", "Docker and Kubernetes", "Amazon Web Services", "Microsoft Azure", "Google Cloud Platform", "Klynveld Peat Marwick Goerdeler KPMG", "Atlassian Jira", "Atlassian Bitbucket", "Atlassian Confluence", "Hipchat", "New Relic", "CDD Customer Due Diligence", "Oracle Virtualbox", "VMWare vSphere", "Nginx", "RESTful API", "VMWare Workstation", "Postman", "Linux Academy", "CloudGuru", "Pluralsight", "Ubuntu", "Debian", "Python", "Ruby", "Perl", "Bash Terminal", "Windows Powershell", "Site Reliability Engineer", "DevOps Engineer", "AWS Lambda", "AWS Virtual Private Cloud", "AWS Elastic Container Service", "AWS Simple Storage Service", "AWS DynamoDB", "AWS Organizations", "AWS API Gateway", "AWS Cloudwatch", "AWS Aurora", "AWS Simple Queue Service", "AWS Simple Notification Service", "AWS Identity and Access Management", "AWS Elastic Compute Cloud ", "Amazon Machine Image", "Infrastructure as Code", "Infrastructure as a Service", "Platform as a Service", "Software as a Service"]
player = "N/A"
chosenWords = ""
dump = []


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.life = 6
        self.answers = [""]
        self.answer = "N/A"
        self.count = 0
        self.guess = ""
        self.win = "False"


def start():
    global startGame
    startGame = input("--Hello there! Would you like to try this game of Hangman?\nPress 'y' to confirm. Otherwise press 'n' to exit... : ")
    checkStatus(startGame)

def reset():
    player.life = 6
    player.answers = [""]
    player.answer = "N/A"
    player.count = 0
    player.guess = ""
    player.win = "False"
    return print("\n")

def getWords(usedWords):
    global chosenWords
    global dump
    dump.append(usedWords)
    chosenWords = random.choice(words)
    random.shuffle(words)
    for i in dump:
        if chosenWords == i:
            getWords("")
    return chosenWords

def wildGuess():
    if player.life > 0:
        player.guess = ""
        checkWin()
        take_guess = input("Do you feel like you have an idea of what the answer could be?\nIf you guess correctly, you will automatically win the game. Otherwise, if your answer \nis wrong you lose all your remaining lives and the game will end.\n--Would you like to take a wild guess? [y/n] ... :  ")
        while take_guess != "y" and take_guess != "Y" and take_guess != "yes" and take_guess != "n" and take_guess != "N" and take_guess != "no":
            take_guess = input("--Invalid input! Please try again : ")
        if take_guess == "y" or take_guess == "Y" or take_guess == "yes":
            player.guess = input("\n--Input your wild guess... : ")
            if player.guess.lower() == chosenWords.lower():
                player.win = "True"
                generateLines()
                print("Wow! Your wild guess was successful. YOU WIN!\n")
            else:
                player.life -= 2
                drawHangman()
                generateLines()
                print("\nSorry that is the wrong answer! Better luck next time...  (-2 lives)\n")
                # print(f"\nGAME OVER!\nSorry that is the wrong answer. You have been hung...\nThe correct answer was:  {chosenWords}\nBetter luck next time!")
                # player.score = 0
                # main(".")
        else:
            player.guess = "(placeholder)"
            print("\n\n")
    else:
        player.guess = "(placeholder)"
    return player.win

def generateLines():
    count = 0
    lines = "  "
    for i in chosenWords:
        if player.win == "True":
            lines += i.upper() + " "
        else:
            if i == " ":
                lines += "    "
            else:
                for j in player.answers:
                    count += 1
                    if j == i.upper():
                        lines += i.upper() + " "
                        count = 0
                        break
                    else:
                        if count == len(player.answers):
                            lines += "_ "
                            count = 0
    player.answers.pop(0)
    if player.answers != [] and player.win == "False":
        print("____Used Answers____ :  " + str(player.answers))
    player.answers.insert(0, "")
    return print("\n\n" + lines + "\n\n")

def introTitle():
    intro = "Loading hangman.py.................#......................\............!............%...........................*....................................%.....................(................%.................#......................**.....\n\n\n []      []     [][]     []      []   [][][][]    []        []     [][]     []      []\n []      []   []    []   [][]]   []  []      [[]  [][]    [][]   []    []   [][]]   []\n []][][][[]  [][][][][]  []  []  []  []           [] [[  ]] []  [][][][][]  []  []  []\n []      []  []      []  []   [[][]  []    [[][]  []  [[]]  []  []      []  []   [[][]\n []      []  []      []  []      []   [][][][][]  []   []   []  []      []  []      []\n---------------------------------------------------------------------------------------\n                                                                               By klyuk\n---------------------------------------------------------------------------------------"
    return print(intro + "\n")

def drawHangman():
    space = "                   "
    stage = "         ~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~\n         |                               |\n         |                               ~~~~~~~~\n         |                                       |\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    if player.life <= 5:
        hangman = "".join((f"{space}-----------------\n{space}|\n{space}|\n{space}|\n{space}|\n{space}|\n{space}|\n{space}|\n{space}|\n{space}|\n", stage))  # add stick
    else:
        hangman = stage
    if player.life <= 4:
        hangman = "".join((f"{space}-----------------\n{space}|\n{space}|\n{space}|              (_)\n{space}|\n{space}|\n{space}|\n{space}|\n{space}|\n{space}|\n", stage))  # add head
    if player.life <= 3:
        hangman = "".join((f"{space}-----------------\n{space}|\n{space}|\n{space}|              (_)\n{space}|               |  \n{space}|               |   \n{space}|               |\n{space}|\n{space}|\n{space}|\n", stage))  # add body
    if player.life <= 2:
        hangman = "".join((f"{space}-----------------\n{space}|\n{space}|\n{space}|              (_)\n{space}|              /|\ \n{space}|             / | \ \n{space}|               |\n{space}|\n{space}|\n{space}|\n", stage))  # add arms
    if player.life <= 1:
        hangman = "".join((f"{space}-----------------\n{space}|\n{space}|\n{space}|              (_)\n{space}|              /|\ \n{space}|             / | \ \n{space}|               |\n{space}|              / \ \n{space}|             /   \ \n{space}|\n", stage))  # add legs
    if player.life <= 0:
        hangman = "".join((f"{space}-----------------\n{space}|               |\n{space}|               |\n{space}|              (_)\n{space}|              /|\ \n{space}|             / | \ \n{space}|               |\n{space}|              / \ \n{space}|             /   \ \n{space}|\n", stage))  # Dead
    # elif player.life == 0:
    #     hangman = "                   -----------------\n
    #               "                   |               |\n
    #               "                   |               |\n
    #               "                   |              (_)\n
    #               "                   |              /|\ \n
    #               "                   |             / | \ \n
    #               "                   |               |\n
    #               "                   |              / \ \n
    #               "                   |             /   \ \n
    #               "                   |\n
    #               "         ~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~\n
    #               "         |                               |\n
    #               "         |                               ~~~~~~~~\n
    #               "         |                                       |\n
    #               "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"  # add rope
    return print("\n\n" + hangman + "\n")

def checkStatus(startGame):
    global player
    if startGame == "y" or startGame == "Y" or startGame == "yes":
        if player == "N/A":
            name = input("\n\n--Enter your name:  ")
            player = Player(name)
        introTitle()
        print(f"\nWelcome {player.name}!\n\n***********************************LET'S PLAY HANGMAN***********************************\n")
        pressEnter = input("                              [Press ENTER to continue...]")
        print("\n\n")
        drawHangman()
        main(startGame)
    elif startGame == "n" or startGame == "N" or startGame == "no":
        print("Thank you for playing! Come back next time :)")
        exit()
    else:
        print("[ERROR] Invalid input.")
        startGame = input("--Press 'y' to play a game of Hangman. Otherwise press 'n' to close the game... :  ")
        checkStatus(startGame)

def checkAnswer():
    count = [0, 0]
    check = ""
    player.answer = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while len(player.answer) != 1:
        player.answer = input("--[Please pick a letter from A-Z] :  ")
        if len(player.answer) != 1:
            print("\n[ERROR] Invalid input. Only one letter can be accepted...")
    else:
        for i in alphabet:
            if player.answer.upper() == i:
                for j in player.answers:
                    count[0] += 1
                    if player.answer.upper() == j:
                        print("\n[ERROR] You have already used this letter. Try another input...")
                        player.answer = ""
                        main("y")
                    else:
                        if count[0] == len(player.answers):
                            check = "Valid"
                            break
                if check == "Valid":
                    break
            elif i == "Z" and check != "Valid":
                print("\n[ERROR] Invalid input. Please only use letters...")
                player.answer = ""
                main("y")

    if check == "Valid":
        player.answers.append(player.answer.upper())
        for x in chosenWords:
            count[1] += 1
            if player.answer.upper() == x or player.answer.lower() == x:
                generateLines()
                print(f"Correct guess!\nYou have {player.life} remaining lives\n")
                break
            else:
                if count[1] == len(chosenWords):
                    player.life -= 1
                    drawHangman()
                    generateLines()
                    print(f"Incorrect guess. Get some more luck!  (-1 life)\nYou have {player.life} remaining lives\n")
                    break

def checkWin():
    count = 0
    for j in chosenWords.upper():
        if player.answers[len(player.answers)-1] == j:
            player.count += 1
            count += 1
            if player.count == len(chosenWords.replace(" ", "")):
                player.win = "True"
                player.guess = "N/A"
                break
    if player.guess == "":
        player.count -= count
    if player.win == "True":
        player.score += 1
        print(f"\nCONGRATULATIONS!!! Your score is now {player.score} .")
        main(".")

def main(startGame):
    if len(player.answers) < 2 and player.answer == "N/A":
        if chosenWords == "":
            getWords("")
        else:
            getWords(chosenWords)
    while startGame == "y" or startGame == "Y" or startGame == "yes":
        if player.life > 0:
            if player.answer == "":
                checkAnswer()
                wildGuess()
                checkWin()
            else:
                generateLines()
                print(f"You have {player.life} guesses remaining. (Use them wisely!)")
                print("\nInput your next guess... ")
                checkAnswer()
                wildGuess()
                checkWin()
        else:
            print(f"GAME OVER!\nYou have used up all of your guesses. Now hang in shame {player.name} !!\nThe correct answer was:  {chosenWords}")
            player.score = 0
            startGame = "."
    else:
        if startGame == ".":
            print("\n\n...Preparing next game..............")
            startGame = input(f"\n--Would you like to play another round of Hangman {player.name}?\nPress 'y' to confirm. Otherwise press 'n' to exit the application... : ")
            reset()
            checkStatus(startGame)

if __name__ == "__main__":
    start()
