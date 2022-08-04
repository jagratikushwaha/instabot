import logging
from instabot import Bot
from getpass import getpass
from time import sleep
from os import remove


logging.basicConfig(filename="logdebug.txt",
                    filemode="a",
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")


mybot = Bot()
logging.info("BOT INITIALIZED.")

sleep(2)
print("connecting to https://instagram.com/", end="")
for i in range(3):
    sleep(1)
    print(".", end="")
print()
sleep(2)
print("Connection established!")
sleep(1)
logging.info("APPLICATION INITIALIZED.")

# # login
username = input('Username ')
password = getpass(prompt="Password ")
mybot.login(username=username, password=password)
print(f"-- USER {username} LOGGED IN --")
logging.info("USER LOGGED IN")
while True:
    try:
        print("1. Send Message To User\n0. Exit App")
        n = int(input("choose option "))
        if n == 1:
            user = input("enter username to send message: ")
            logging.info(f"Choose to send message to {user}.")
            message = input("enter your message: ")
            mybot.send_message(message, user)
            print(f"-- MESSEGE SENT TO {user} --")
            logging.info(f"message send to {user}.")

        elif n == 0:
            mybot.logout()
            logging.info(f"user logged out.")
            sleep(2)
            print("logging out in process", end="")
            for i in range(3):
                sleep(1)
                print(".", end="")
            print()
            sleep(2)
            print("Connection closed!")
            sleep(1)
            print("-- LOGGED OUT SUCCESSFULLY --")
            break
        else:
            print("-- WRONG INPUT CHOOSE AGAIN --")
    except Exception as err:
        logging.error(f"found err {err}")
        print(f"--ERROR {err}.")

# remove("config") //delete config folder
logging.critical("config deleted!")
