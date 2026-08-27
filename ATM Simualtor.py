print("Welcome To BOI Bank ")
Trials = 3
UserPin = 1234

while Trials != 0:
    Pin = int(input("Enter Your 4 Digit Pin Number :"))
    if Pin!=UserPin:
        Trials-=1
        print(f"Invalid Pin, You Have {Trials} Left")
        
    else:
        UserChoice = input("d : Deposite or w : Withdraw :")
        
        if UserChoice == "d":
            UserDeposite = int(input("Enter Your Deposite Amount :"))
            print(UserDeposite,"$ Has Been Deposite Into Your Accounts")
            
        if UserChoice == "w":
            UserWithdraw = int(input("Enter Your Withdrawal Amount :"))
            print(UserWithdraw,"$ Has Been Withdraw Into Your Accounts")
            
    UserExit = input("Would To Like To Continue? Y/N :")
    if UserExit=="N":
        print("Thanks For Using BOi Bank")
        break
    else:
        continue