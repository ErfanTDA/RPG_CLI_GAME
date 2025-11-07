import json, random, time, sys

USER_FILE = "users.json"

def load_users():
    try:
        with open(USER_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}
    

def save_users(users):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False , indent=2)


def loading(text, success=True, min_sec=0.1, max_sec=1):

    spinner = "/-\\|"
    total = random.uniform(min_sec, max_sec)
    frame_time = 0.1
    frames = int(total / frame_time)

    sys.stdout.write(f"{text} ")
    sys.stdout.flush()

    for i in range(frames):
        ch = spinner[i % len(spinner)]
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(frame_time)
        sys.stdout.write("\b") 
        sys.stdout.flush()

    if success:
        sys.stdout.write("✔\n")
    else:
        sys.stdout.write("✖\n")
    sys.stdout.flush()