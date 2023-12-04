import random


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
    

    trait = input("Choose your character's trait.  \n 1. Courageous \n 2. Talented \n" )
    if trait == "1":
        print(f"{characterName} is Courageous at heart!")
    else:
        print(f"Destiny blessed {characterName} with Talent!")
    
    

    #Character info
    print("\nCharacter Created!")
    print(f"Name: {characterName}")
    print(f"Gender: {gender}")
    print(f"Age: {age}")
    print(f"Trait: {trait}")
    
def actOnePartOne():
    
    filename = "ACT_I.txt"
    start = "start1"
    end = "end1"
    
    with open(filename, 'r') as file:
        content = ""
        
        foundWord = False
        
        for line in file:
            if start in line:
                foundWord = True
                continue
            
            if foundWord:
                content += line
                            
            if end in line:          #Having trouble getting code to not print "end1"
                 foundWord = True
                 break

        print(content)
    
def actOneChoiceOne(gameOver,actOnePartTwo):
    print("What would you like to do? \n 1. Stay where you are. \n 2. Take your chances and escape ")
    userInput = input()
    if userInput == ("1"):
        gameOver(actOneChoiceOne, actOnePartTwo)        
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
            if start in line:
                foundWord = True
                continue
            
            if foundWord:
                content += line
                            
            if end in line:           #Having trouble getting code to not print "end2"
                 foundWord = False
                 break

        print(content) 




def gameOver(actOneChoiceOne):
    print("You have lost")
    print("Continue? Y/N")
    
    userInput = input()
    
    if userInput == ("N"):
        exit()        
    if userInput == ("Y"):
        actOneChoiceOne()
def main():
    
    titleScreen(characterCreation)
    actOnePartOne()
    actOneChoiceOne(gameOver,actOnePartTwo)
    

main()


