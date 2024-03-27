import os
import time
import pyperclip
import pyautogui
import ctypes



ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)



args = ' '.join(os.sys.argv[1:])

if "--password" in args:
    [args, password] = args.split("--password")
    password = password.strip()
else:
    password = None

if "--login" in args:
    [args, login] = args.split("--login")
    login = login.strip()
else:
    login = None

if "--cmd" in args:
    [args, cmd] = args.split("--cmd")
    cmd = cmd.strip()
else:
    cmd = None



time.sleep(0.3)

if cmd:
    time.sleep(0.1)
    pyperclip.copy(cmd)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

if login:
    time.sleep(0.1)
    pyperclip.copy(login)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

if password:
    time.sleep(0.1)
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
