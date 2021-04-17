import random
import datetime

db={}
now = datetime.datetime.now()

def init():
    isValidOptionSelected=False
    print("Welcome to Our Bank System")

    while isValidOptionSelected == False:
        haveAccount=int(input("Do You have an Account with Us: 1.(yes) 2.(no)\n"))

        if (haveAccount==1):
            isValidOptionSelected=True
            login()

        elif(haveAccount==2):
            isValidOptionSelected=True;
            register()

        else:
            print("Invalid Option Selected.")



def AccountNoGeneration():
    
    return random.randrange(111111111, 9999999999)


def login():
    print("**********Login********************")
    isLoginSuccessful=False
    while isLoginSuccessful==False:
        UserAccNo=int(input("Enter Your Account Number: \n"))
        passw = input("Enter Correct Password: \n")
        
        for accNo, userdetails in db.items():
            if (accNo == UserAccNo):
                if (userdetails[3] == passw):
                    isLoginSuccessful=True
                else:
                    print("Invalid account or Password.")

            else:
                print("Invalid account or Password.")


    BankOperations(userdetails)


def register():
    print("******Register*****")

    email = input("Enter email address: ")
    first_name= input("Enter First name: ")
    lastname = input("Enter Lastname: ")
    password = input("Enter Password: ")

    accNo= AccountNoGeneration()
    db[accNo]= [first_name, lastname, email, password]

    print("\n Your Account has been created Successfully.")
    print("Your Account No. is: ", accNo ,"\n")
    print("###############################################################\n")
    print("Please keep your account account number and password secret.")
    print("############################################################################  \n \n")

    login()


def BankOperations(user):
    print("\n \n Welcome %s %s" %(user[0], user[1]))

    print('Current date and time is:')
    print(now.strftime('%y-%m-%d %H:%M:%S \n \n'))
    print('These are the available options:')
    print('\n 1.Deposit \n 2.Withdraw \n 3.Complaint \n ')
    selectedOption=int(input('Please select Option: \n'))
        
    if (selectedOption==1):
        print('You have selected option 1.\n')
        deposit()
       
        
        
    elif (selectedOption==2):
        print('You have selected option 2.\n')
        withdrawal()
        

    elif (selectedOption==3):
        print('You have selected option 3.\n')
        complain()

    else:
        
        print('Invalid option selected, Please try again.')
        BankOperations(user)

def withdrawal():
    withdraw= float(input('How much do you want to withdraw? \n'))
    print('Please take your cash.')

    aob()

def deposit():
    deposit = float(input('How much do you want to deposit? \n'))
    print('Your Current balance is',deposit)
    
    aob()

def complain():
    complain =input(print('What issue will you like to report?\n'))
    print('Thank you for contacting us.')
    aob()

def logout():
    print("Thank You for Banking with us.\n \n")
    login()

def aob():
    others =int(input("Would you like to: \n 1.Logout \n 2.Press any other number to Exit \n"))
    if (others==1):
        logout()


    else:
        exit()





 
init()
