print("Use commands: \nquit\nstart \nstop \nhelp")

command = ""
started = False

while command != "quit":
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started moving.....")
    
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped!!")

    elif command == "help":
        print("\nstart - car starts moving\nstop - car stops moving\nquit - quits the loop\n")

    elif command == "quit":
        break
    else :  
        print("Use command words")