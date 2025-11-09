import random 
from colorama import Fore
from auth import load_users, save_users, loading

# ---------------------------
#          LOGIN
# ---------------------------
def login():
    users = load_users()

    print("\n--- Login ---")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in users and users[username]["password"] == password:
        loading("Checking username") 
        loading("Checking password")
        loading("Searching username and password")
        loading("Finalizing login")


        print("Login successful!\n")
        return username
    
    else:
        loading("Checking username", success=False) 
        loading("Checking password", success=False)
        loading("Searching username and password", success=False)


        print("Incorrect username or password.\n")
        return None

# ---------------------------
#          LOGOUT
# ---------------------------  
def logout(current_user):
    if current_user == None:
        print(Fore.RED + "You are not logged in.\n")
        return current_user
    
    else:
        print(f'You are logout from {current_user}')
        return None 
        
        

# ---------------------------
#          SIGNUP
# ---------------------------
def signup():
    users = load_users()
    print("\n--- Sign up ---")

    username = input("New username: ").strip()
    
    if username in users:
        loading("checking username", success=False)
      # loading("checking password", success=False)

        print("This username already exists.")
        return
    
    password = input("New password: ").strip()

    users[username] = {"password": password}
    save_users(users)
    

    loading("Checking username") 
    loading("Checking password")    
    loading("Finalizing signup")

    print("Signup successful!\n")


# ---------------------------
#          QUIZ
# ---------------------------
def cmd_quiz(current_user):
    """Run a math quiz and reward gold."""

    if current_user is None:
        print(Fore.RED + "You are not logged in.\n")
        return

    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b

    print(f"Solve: {a} {op} {b}")
    user_ans = input("Your answer: ").strip()

    if not (user_ans.lstrip("-").isdigit()):
        print(Fore.RED + "Invalid number.\n")
        return

    user_ans = int(user_ans)

    users = load_users()
    profile = users.get(current_user, {})

    profile.setdefault("money", 0)  
    if user_ans == answer:
        gold = random.randint(5, 10)
        profile["money"] += gold
        print(Fore.GREEN + f"Correct! You earned {gold} gold.\n")
    else:
        print(Fore.RED + f"Wrong answer! Correct answer was {answer}.\n")

    users[current_user] = profile
    save_users(users)

# ---------------------------
#          level
# ---------------------------
def cmd_level(current_user):
    if current_user is None:
        print(Fore.RED + "You are not logged in.\n")
        return
    
    users = load_users()
    profile = users.get(current_user, {})

    level = profile.get("level", {profile.get('level', 'N/A')})

    print(f"\n{current_user}'s Level: {level}\n")



# ---------------------------
#          HELP
# ---------------------------
def help_cmd(commands_dict):
    print("\nAvailable commands:")
    for cmd in commands_dict.keys():
        print(f" - {cmd}")

# ---------------------------
#          STATUS
# ---------------------------
def status_cmd(current_user):
    if current_user is None:
        print(Fore.RED + "You are not logged in.\n")
        return

    users = load_users()
    profile = users.get(current_user, {})

    print(f"\nStatus of {current_user}:")
    print(f"  Level: {profile.get('level', 'N/A')}")
    print(f"  XP:    {profile.get('xp', 'N/A')}")
    print(f"  Gold:  {profile.get('money', profile.get('gold', 'N/A'))}")
    print(f"  Inventory: {profile.get('inventory', [])}\n")


def register_commands(commands):
    commands["quiz"] = cmd_quiz
    commands['help']= help_cmd
    commands['login'] = login
    commands['signup'] = signup
    commands['status'] = status_cmd
    commands['logout'] = logout
    commands['level'] = cmd_level