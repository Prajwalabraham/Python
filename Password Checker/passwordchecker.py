from ast import main
from unicodedata import name

def PasswordCheck(password):
    
    #To get the length of the passsword
    n = len(password) #score is password > 8 = 10

    #variables to check conditions and rules to score
    startDigit = 0 #score = 10
    hasDigit = 0 #score = 25
    hasChar = 0 #score = 25
    hasUpper = False #score = 15
    hasLower = False #score = 15 
    normalChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 
    score = 0 
    count = 0
    
    #Iterating through each character
    for i in range(n):
        
        #checks if character is a digit.
        if password[i].isdigit():
            hasDigit += 1
        #checks if character is a speacialcharacter
        elif password[i] not in normalChar:
            hasChar += 1
        #checks if character is Uppercase
        elif password[i].isupper():
            hasUpper = True
        #checks if character is lowercase
        elif password[i].islower():
            hasLower = True
        else:
            continue
    #checks if the first character is a digit
    if password[0].isdigit():
            startDigit = 1

    #Scoring based on the rules
    if startDigit == 0:
        score += 10
    if hasLower:
        score += 15
    if hasUpper:
        score += 15
    if hasChar >= 2:
        score += 25
    if hasDigit >= 2:
        score += 25
    if n >= 8:
        score += 10

    #Printing the Grades for their respective scores.
    if score < 50:
        print('LOW')
    elif score >= 50 and score < 75:
        print('AVERAGE')
    elif score >= 75 and score < 90:
        print('GOOD')
    else:
        print('VERY GOOD')

    #Printing the rules that contribute to the least to the scoring
    if score < 75:
        print("The rules that contribute least towards your password strength\n")
        
        if startDigit == 0 and count < 2:
            print("Your password doesn't start with a Number")
            count += 1
        if n >= 8 and count < 2:
            print("Your password has atleast 8 characters") 
            count += 1
        if hasLower and count < 2:
            print("Your password has lowercase characters")
            count += 1
        if hasUpper and count < 2:
            print("Your password has uppercase characters")
            count += 1
        if hasChar >= 2 and count < 2:
            print("Your password contains more than 2 special characters")
            count += 1
        if hasDigit >= 2 and count < 2:
            print("Your password contains more than 2 numbers")
            count += 1

if __name__ == "__main__":
    password = input("Enter the Password:")
    PasswordCheck(password)