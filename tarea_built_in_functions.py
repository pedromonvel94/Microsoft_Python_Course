'''
 1. build a simple calculator using input(), arithmetic operators, and print() to display results. 
 
 2. Then try some data validation, write a program that uses len() and type() to validate user input, and make sure it meets specific criteria , like password length. 
 
 3. Finally, convert some data. Create a script that takes user input and converts it to different data types using int(), float(), and str(), and then perform an operation on each piece of converted data.
'''

which_problem = input("which problem you want to try (1, 2, 3)")

#1.
def calculator(user_operation, user_number1, user_number2):
    
    if user_operation == "+":
        print(user_number1 + user_number2)
    elif user_operation == "-":
        print(user_number1 - user_number2)
    elif user_operation == "*":
        print(user_number1 * user_number2)
    elif user_operation == "/":
        print(user_number1 / user_number2)
    else:
        print("Usea a valid arithmetic operator")

user_number1 = float(input("Add your first number"))
user_operation = input("Which operation you want (+, -, *, /)")
user_number2 = float(input("Add your second number"))


calc = calculator(user_operation, user_number1, user_number2)

#2.

print("2. Try some data validation, write a program that uses len() and type() to validate user input, and make sure it meets specific criteria , like password length.")

user_credentials = {
    "ShadowStrike99": "Shadow@2024",
    "PixelWarriorX": "PixelX!321",
    "NinjaGhost07": "Ninja#777",
    "DragonSlayer_21": "Dragon_123",
    "CyberKnight88": "Cyber!888",
    "EpicSniper24": "Sn1p3r!24",
    "BlazeStormYT": "Blaze2025!",
    "NoobMaster3000": "Noob$3000",
    "SilentHunterX": "Silent#X1",
    "ZombiCrafter10": "ZombieCra10!",
    "DarkWizard_77": "Wizard*77",
    "HeadshotHero": "HeadHero88",
    "StealthTiger": "TigerSte@lth",
    "GamerQueen23": "QueenGame23",
    "RageQuitKing": "RageQuit#9",
    "AlienBlasterX": "AlienX2024",
    "ToxicArrow12": "Toxic_Arrow",
    "FrozenFlame_9": "Flame@999",
    "BattleMage_01": "MageBattle1",
    "QuickScopeGod": "ScopeG0d!!"
}
controler = True
ask_login = ""

signup_or_login = input("¿You want to: Log in (li) / Sign up (su)?: ")

def signup_function(user_name, password):
    
        if len(password) >= 8 and type(password) == str:
            user_credentials[user_name] = password
            
            return False
        else:
            print("Your password should have more than 8 characters, and contain numbers and letters.")
            
            return True

while controler:
    
    if signup_or_login.lower() in ["su", "signup", "sign up"]:
        
        right_password = True
    
        while right_password:
            user_name = input("Please, write your username")
            password = input("Please write your password")
            
            right_password = signup_function(user_name, password)
        
        ask_login = input("You want to log in? Y/N")
        
    elif signup_or_login.lower() in ["li", "login", "log in"] or ask_login.lower() == "y":
        user_name = input("Please, write your username")
        password = input("Please write your password")
        
        if user_name in user_credentials:
            if user_credentials[user_name] == password:
                print("The credentials are correct! Enjoy!")
            else:
                print("Incorrect credentials")
        else:
            print("Username not found")
        
        controler = False
    elif ask_login.lower() == "n":
        print("Thanks for visiting us")
        
        controler = False
    else:
        signup_or_login = input("Incorrect answer, please choose between: Log in (li) / Sign up (su): ")     


