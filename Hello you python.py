import sys

number = 17

print("Hello You!, ik ben Piter.")

print("Wie ben jij?")
x = input()

print("Hello " + x )
print(x +  ", hoe oud ben jij?")

print("Ik ben 17 jaar oud." )
xe = input()


while True:
    if (int(xe) < number ):
        print(xe + ", ik ben dan ouder.")

    elif (int(xe) == number ):
        print(xe + ", wij zijn dan even oud.")

    elif (int(xe) > number ):
        print(xe + ", dan ben jij ouder.")
    
    wait = input()
    sys.exit()
          
        
    



