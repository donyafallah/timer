import time
while True :
    choice = input("Do you want to start? yes/no : ")
    if 'y' in  choice.lower() :
        hours=int(input("Enter amount of hours : "))
        minutes=int(input("Enter amount of minutes : "))
        seconds=int(input("Enter amount of seconds : "))
        total = seconds + hours * 3600 + minutes * 60
        print ("Timer is starting now ...")
        time.sleep(1)
        while total >= 1 :
            print(total)
            total -= 1
            time.sleep(1)
        print ("Timer end ...")
    elif 'n' in choice.lower():
        print("Exiting ...") 
        break
    else :
        print("Invalid input !")   
