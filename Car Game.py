"""">help
start - to start the car
stop - to stop the car
quit - to exit
in Z: Structure
›asd
I don't understand that..
›start
Car started. Ready to go!"""

# Initialize variables: command, stop_count, start_count
command = ""
stop_count = 0
start_count = 0

# Start an infinite loop

while True:
    # Prompt the user to input a command using the input() function and convert it to lowercase using the lower() method.
    command = input("Print your command: ").lower()
    # Use if-elif-else statements to check the user's input against the available commands.
    # If the user enters "stop" and start_count is 0, print "You need at least start to ride" and break out of the loop.
    if start_count == 0 and command == "stop":
        print("You need at least start to ride")
        break
    # If the user enters "start" and start_count is 1, print "You already ride the car" and break out of the loop.
    elif start_count == 1 and command == "start":
        print("You already ride the car")
        break
    # If the stop_count is 1, print "You already stop the car" and break out of the loop.
    elif stop_count == 1:
        print("You already stop the car")
        break
    # If the user enters "quit", print "You exit the car" and break out of the loop.
    if command == "quit":
        print("You exit the car")
        break
    # If the user enters "start", print "Let's go!", increment start_count by 1, and decrement stop_count by 1.
    elif command == "start":
        pass
        print("Let's go!")
        start_count += 1
        stop_count -= 1
    # If the user enters "help", print the available commands.
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    # If the user enters "stop" and start_count is 1, print "Take a break, bro ;-)", increment stop_count by 1, and decrement start_count by 1.
    elif command == "stop" and start_count == 1:
        print("Take a break, bro ;-)")
        stop_count += 1
        start_count -= 1
    # If the user enters anything else, print "I don't understand you".
    else:
        print("I don't understand you")
# The loop will repeat until the user enters "quit" and breaks out of the loop.
