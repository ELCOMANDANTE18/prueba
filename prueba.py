def campeon(x):
    x = int(input("Cuantas copas tenes??? "))
    if x == 1:
        decison = int(input("Quien sos??? (1 ó 2) "))
        if decison == 1:
            print("Sos inglaterra ")
        if decison == 2:
            print("Sos España ")
        
    if x == 2:
        print("Sos Francia")
        
    if x == 3:
        print("Sos el vigente campeón del Mundo Argentina")
        
    if x == 4:
        argumento = int(input("Quien sos ?? (1,2 ó 3)")) 
        if argumento == 1:
            print("Uruguay")
        if argumento == 2:
            print("Italia")
        if argumento == 3:
            print("Alemania")
            
    if x == 5:
        print("Sos Brasil") 
   
        
        
campeon(3)        
                               