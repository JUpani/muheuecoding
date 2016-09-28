
print("                      NGAZETUNGUE MUHEUE                     ")
print("                        P.O BOX 000000                       ")
print("                       +264 81 000 0000                      ")
print("                           WINDHOEK                          ")
print("                           NAMIBIA                           ")
print("   ----------------------------------------------------------")

print("\n\tIF YOU ARE NOT A REGISTER MEMBER YOU ARE ADVICE\n\t TO BRING ALONG YOUR DOCTOR CERTIFICATE AND X-RAY\n\n")
log=("Y" and "N")# choice between new member and old member
log=input("ARE YOU A NEW MEMBER,ENTER YOUR CHOICE BY PRESSING Y KEY OR N KEY: ")#
while log!=("Y") and log!=("N"):
    print("YOU ENTER AN INVALID OPTION,TRY AGAIN")
    log=input("ARE YOU A NEW MEMBER,ENTER YOUR CHOICE BY PRESSING Y KEY OR N KEY: ")
if log ==("Y"):
    print("           WELCOME TO OUR PHYSIOTHERAPY            ")
    print("===================================================")
    print("                PERSONAL DETAILS                   ")
    print("===================================================")
    name=input("ENTER YOUR NAME:")#name of new member
    print("YOU REGISTER",name," YOUR DEFAULT PASSWORD IS:muheue")#Providing a password and storing a new member into the system.
    print("ENTER A PASSWORD THAT WAS PROVIDED FOR YOU\n")
elif log == ("N"):#name of old member
    print("            LOG IN          ")#prompting old member to login
    name=input("ENTER YOUR NAME:")
    while name!="zizou":# if name is not zizou the system 
        print("NAME ENTERED NOT RECOGNIZE BY OUR SYSYEM, PLEASE TRY AGAIN:")
        name=input("ENTER YOUR NAME:")#The system will keep asking a user to enter a correct name,if correct name not entered.
    if name=="zizou":#This is a correct name the user suppose to enter into the system
        print("THANK YOU FOR VISITING US AGAIN",name.upper())#Welcoming the user 
        print("ENTER A PASSWORD THAT WAS PROVIDED TO YOU DURING REGISTRATION\n") 
                        
count = 1
password = "muheue"
enter_password = input("ENTER YOUR PASSWORD? ")
while count < 3 and enter_password.lower() != password:    # .lower allows things like muheue to still match, and password should be only entered 3 times.
    print("wrong password!")
    enter_password = input("ENTER YOUR PASSWORD? ")#re-ente the password if,wrong password entered at first attempt.
    count = count + 1#everytime the user enter incorrect password the system will keep count
if enter_password.lower() != password:
    print("Access Denied!") # this message isn't printed in the third chance, so we print it now
    print("You ran out of chances:",name.upper())#Telling the user that s/he ran out of time, of entering a password
else:
    print("                                                   ")
    print("|=================================================|")
    print("| WELCOME TO MUHEUE ELECTRONIC TECHNOLOGY HUB    |")
    print("|=================================================|")
    print("|            SERVICES WE PROVIDE AT OUR HUB       |")
    print("|===============|===============|=================|")
    print("|=================================================|")
    print("|   DEPARTMENTS NAME                NUMBER        |")
    print("|=================================================|")
    print("|   COMPUTER MAINTENANCE         |    1           |")
    print("|=================================================|")
    print("|   GRAPHIC DESIGN               |    2           |")
    print("|=================================================|")
    print("|=================================================|")

    count = 0
    number = int(input("ENTER NUMBER TO SEE PRODUCTS: "))
    while number < 1 or number > 2:    
        print("wrong number!")
        number= int(input("ENTER NUMBER TO SEE PRODUCTS  "))#re-enter the number if,wrong number entered at first attempt.
        count+=1
    if number == 1:
            print("|=============================================================================|")
            print("| WELCOME TO MUHEUE ELECTRONIC TECHNOLOGY HUB                                |")
            print("|=============================================================================|")
            print("|            SERVICES WE PROVIDE AT OUR HUB                                   |")
            print("|===============|===============|=============================================|")
            print("|=============================================================================|")
            print("|                        COMPUTER MAINTENANCE DEPARTMENT                      |")
            print("|=============================================================================|")
            print("|       SERVICES                     PRICES              DESCRIPTION          |")
            print("|=============================================================================|")
            print("|   SOFTWARE INSTALLATION    |    N$ 150             |installing new softwares|")
            print("|=============================================================================|")
            print("|   VIRUS REMOVAL            |    N$ 100             |Computer security       |")
            print("|=============================================================================|")
            print("|   HARDWARE TROUBLESHOOTING |    N$ 200             |                        |")
            print("|=============================================================================|")

    elif number == 2:

            print("|=========================================================================|")
            print("| WELCOME TO MUHEUE ELECTRONIC TECHNOLOGY HUB                            |")
            print("|=========================================================================|")
            print("|            SERVICES WE PROVIDE AT OUR HUB                               |")
            print("|===============|===============|=========================================|")
            print("|=========================================================================|")
            print("|                         GRAPHIC DESIGN DEPARTMENT                       |")
            print("|=========================================================================|")
            print("|     SERVICES                     PRICES              DESCRIPTION        |")
            print("|=========================================================================|")
            print("|   LOGO                     |    N$ 90-00       |Designing logo          |")
            print("|=========================================================================|")
            print("|   PRINTING                 |    N$ 10-00       |Printing services       |")
            print("|=========================================================================|")
            print("|   WEDDING CARD             |    N$ 100-00      |Designing wedding cards |")
            print("|=========================================================================|")
     
    print("\n\n")
    
print("WRITTEN BY  :NGAZETUNGUE MUHEUE       ")
print("UNIVERSITY  :UNIVERSITY OF NAMIBIA    ")
print("COURSE      :COMPUTER SCIENCE (STUDENT) ")#Details of the person who wrote the program.
print("CELL        :+264 (0) 81 0000000       ")
print ("2016")
