import sys
import datetime
import os


def Start():
    x = ""
    date_time = datetime.datetime.now()

    print("Hello You!, ik ben Piter.")

    print("Wie ben jij?")
    x = input()

    print("Hello " + x + "\n")
    print("Het is nu " + str(date_time) + "\n")

    print(x +  ", hoe oud ben jij?" + "\n")


    

Start()

def checkAge():
    number = 17
    xe = ""
    print("Ik ben namelijk 17 jaar oud." )
    xe = input()
    
    if (int(xe) < number ):
        print(xe + ", ik ben dan ouder." + "\n")
        

    elif (int(xe) == number ):
        print(xe + ", wij zijn dan even oud." + "\n")
        

    elif (int(xe) > number ):
        print(xe + ", dan ben jij ouder." + "\n")
checkAge()


def checkAwnser():
    print("Wil je dit programma nog een keer opnieuw uitvoeren (y / n)")
    yes_no = input()
    if (yes_no == "y"):
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)  
        
    if (yes_no == "n"):      
        print("Doei!")
        sys.exit()
    else:
        print('Invalid input, voer alstublieft "y" / "n" in.' + "\n")
        checkAwnser()

checkAwnser()

#gemaakt door Piter Groot SD1DA

          
        
    



