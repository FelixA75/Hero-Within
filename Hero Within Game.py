import random
from tkinter import *

def button():
    
    count = 0
    window = Tk()
    button = Button(window,text='Start Adventure')
    button.config(command=lambda: titleScreen(characterCreation))
    
    button.config(font=('Magneto',50,'bold'))
    button.config(bg='#081f83')
    button.config(fg='#fa5a13')
    
    button.config(activebackground='#fa5a13')
    button.config(activeforeground='#081f83')
    
    image = PhotoImage(file='shenron.png')
    button.config(image=image)
    button.config(compound='top')
    button.pack()
    label2 = Label(window,image=image)
    window.mainloop()
    
def d20Roll():
    return random.randint(1, 20)

#roll = d20Roll()
#print(f"You rolled a {roll}")

def titleScreen(characterCreation):
    print("H E R O \n within \n\n 1. Start New Game \n 2. Load Game \n 3. Quit Game \n")
    
    userInput = input()
    
    if userInput == "1":
        characterCreation()
    elif userInput == "2":
        # LoadGame Function here
        pass
    elif userInput == "3":
        quit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

def characterCreation():
    print("Create your character \n")
    characterName = input("Enter your character's name: ")
    
    gender = input(f"Choose {characterName}'s gender: M or F ").upper()
    
    if gender == 'M':
        print(f"{characterName} is a Male")
        
    else:
        print(f"{characterName} is a Female")

    age = input(f"Choose {characterName}'s age: ")
    print(f"{characterName} is {age} years old.")
    
    traits = {
        "1": "Courageous at heart",
        "2": "Blessed with Talent"
        }   
    while True:
        
        trait = input("Choose your character's trait.  \n 1. Courageous \n 2. Talented \n" )
        if trait in traits:
            print(f"{characterName} is {traits[trait]}!")
            break
        else:
            print("Please select one of the options")
    
    #Character info
    print("\nCharacter Created!")
    print(f"Name: {characterName}")
    print(f"Gender: {gender}")
    print(f"Age: {age}")
    print(f"Trait: {traits[trait]}")
    
def actOnePartOne():
    
    filename = "ACT_I.txt"
    start = "start1"
    end = "end1"
    
    with open(filename, 'r') as file:
        content = ""
        
        foundWord = False
        
        for line in file:
            if line.startswith(start):
                foundWord = True
                continue
            
            if foundWord:
                if line.startswith(end):
                    foundWord = False
                else:
                    content += line

        print(content)
    
def actOneChoiceOne(gameOver,actOnePartTwo):
    print("What would you like to do? \n 1. Stay where you are. \n 2. Take your chances and escape ")
    userInput = input()
    if userInput == ("1"):
        gameOver(actOneChoiceOne)        
    if userInput == ("2"):
        actOnePartTwo()

def actOnePartTwo():
    
    filename = "ACT_I.txt"
    start = "start2"
    end = "end2"
    
    with open(filename, 'r') as file:
        content = ""
        
        foundWord = False
        
        for line in file:
            if line.startswith(start):
                foundWord = True
                continue
            
            if foundWord:
                if line.startswith(end):
                    foundWord = False
                else:
                    content += line

        print(content) 




def gameOver(actOneChoiceOne):
    print("You have lost")
    print("Continue? Y/N")
    
    userInput = input()
    
    if userInput == ("N" or "n"):
        exit()        
    if userInput == ("Y" or "y"):
        actOneChoiceOne(gameOver,actOnePartTwo)
def main():
    button()
    titleScreen(characterCreation)
    actOnePartOne()
    actOneChoiceOne(gameOver,actOnePartTwo)
    

main()



