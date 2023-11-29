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
    
    

    # Display character information
    print("\nCharacter Created!")
    print(f"Name: {characterName}")
    print(f"Gender: {gender}")
    print(f"Age: {age}")
    print(f"Trait: {trait}")
    
    
characterCreation()