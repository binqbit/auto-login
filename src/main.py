import os
import time
import pyautogui
import dotenv
import ctypes

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
dotenv.load_dotenv()

PASSWORDS = {}

passwords = os.getenv("PASSWORDS")
if passwords:
    passwords = passwords.split(",")
    for password in passwords:
        password = password.split(":")
        if len(password) == 2:
            PASSWORDS[password[0].strip()] = password[1].strip()

def get_param(name):
    for i in range(len(os.sys.argv)):
        if os.sys.argv[i] == name:
            value = ""
            for j in range(i + 1, len(os.sys.argv)):
                if os.sys.argv[j].startswith("--"):
                    break
                value += os.sys.argv[j] + " "
            value = value.strip()
            if value:
                return value
    return None

cmd = get_param("--cmd")
cmd_wait = float(get_param("--cmd-wait") or "0.3")

login = get_param("--login")
login_wait = float(get_param("--login-wait") or "0.1")

password = get_param("--password")
password_wait = float(get_param("--password-wait") or "0.0")

password_from_name = PASSWORDS.get(password)
if password_from_name:
    password = password_from_name

time.sleep(0.1)

if cmd:
    pyautogui.typewrite(cmd)
    pyautogui.press('enter')
    time.sleep(cmd_wait)

if login:
    pyautogui.typewrite(login)
    pyautogui.press('enter')
    time.sleep(login_wait)

if password:
    pyautogui.typewrite(password)
    pyautogui.press('enter')
    time.sleep(password_wait)
