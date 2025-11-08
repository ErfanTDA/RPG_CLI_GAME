from auth import load_users
from colorama import Fore, Style, init
from commands import *

init(autoreset=True)


def banner():
    print(r"""
     ▌ ▐·      ▪  ·▄▄▄▄   
    ▪█·█▌ ▄█▀▄ ██ ██· ██ 
    ▐█▐█•▐█▌.▐▌▐█·▐█▪ ▐█▌
     ███ ▐█▌.▐▌▐█▌██. ██ 
    . ▀   ▀█▄▀▪▀▀▀▀▀▀▀▀•
""")

def show_menu():
    print("* login")
    print("* signup")
    print("* status")
    print("* exit")
    print()


def main():
    banner()
    show_menu()

    commands = {}
    register_commands(commands)


    current_user = None

    while True:

        if current_user:
            prompt = f"{Fore.GREEN}[{current_user}@rpg]{Style.RESET_ALL} >> "
        else:
            prompt = f"{Fore.YELLOW}[guest@rpg]{Style.RESET_ALL} >> "

        raw = input(prompt).strip()
        if raw == "":
            continue

        parts = raw.split()
        command = parts[0].lower()
        args = parts[1:]


        # ---------------------------
        #          LOGIN
        # ---------------------------
        if command == "login":
            if len(args) == 0:
                user = login()
                if user:
                    current_user = user
                continue

            # login <user> <pass>
            elif len(args) == 2:
                username = args[0]
                password = args[1]

                users = load_users()

                if username in users and users[username]["password"] == password:
                    print(Fore.GREEN + "Login successful!\n")
                    current_user = username
                else:
                    print(Fore.RED + "Incorrect username or password.\n")
                continue

            else:
                print(Fore.RED + "Usage: login <username> <password>\n")
                continue


        # ---------------------------
        #          SIGNUP
        # ---------------------------
        if command == "signup":
            signup()
            continue
        
        # ---------------------------
        #          LOGOUT
        # ---------------------------
        if command == "logout":
            current_user = logout(current_user)
            continue

        # ---------------------------
        #          STATUS
        # ---------------------------
        if command == 'status':
            status_cmd(current_user)
            continue
        # ---------------------------
        #          QUIZ
        # ---------------------------
        if command == "quiz":
            cmd_quiz(current_user)
            continue
        
       

        # ---------------------------
        #          HELP
        # ---------------------------
        if command in commands:
            if command == "help":
                commands["help"](commands)
            else:
                commands[command](current_user)
            continue


        # ---------------------------
        #          EXIT
        # ---------------------------
        if command == "exit":
            print("Goodbye!")
            break


        # ---------------------------
        #     INVALID COMMAND
        # ---------------------------
        print(Fore.RED + f"Invalid command: {command}\n")


if __name__ == "__main__":
    main()
