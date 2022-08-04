from instabot import Bot
from time import sleep
from getpass import getpass

my_bot = Bot()

# APP INITIALIZATION
print("Initializing Instabot app", end='')
for i in range(3):
    sleep(1)
    print(".", end="")
print()
print("Connecting to https://www.instagram.com", end="")
for i in range(3):
    sleep(1)
    print(".", end="")
print()
sleep(3)
print("Connection established!")


# login info
username = input("Username: ")
password = getpass(prompt='Password: ')
my_bot.login(username=username, password=password)


# instagram operations
while(True):
    print("""Choose an Option:
    1. Follow User 
    2. Unfollow User
    3. Send Message
    0. To Exit""")
    try:
        i = int(input("Your Input: "))

        if i == 0:
            print("")
            my_bot.logout()
            print("Logging out the user", end='')
            for i in range(3):
                sleep(1)
                print(".", end="")
            print()
            sleep(3)
            print("User successfully logged out")
            print("Connection ended!")
            break
        # follow a single user
        if i == 1:
            user = input("enter username to follow: ")
            my_bot.follow(user)
            print("--USER FOLLOWED SUCCESSFULLY--")
        elif i == 2:
            user = input("enter username to unfollow: ")
            my_bot.unfollow(user)
            print("--USER UNFOLLOWED SUCCESSFULLY--")
        elif i == 3:
            user = input("enter username to send message: ")
            msg = input("enter your message: ")
            my_bot.send_message(msg, user)
            print("--MESSAGE SENT SUCCESSFULLY--")
    except Exception as err:
        print('**SERVER ERROR OR INVALID INPUTS**')
