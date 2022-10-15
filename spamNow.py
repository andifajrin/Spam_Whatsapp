import pyautogui, time

position =pyautogui.position()
pesan = "Type Your Message Here"
for a in range(100):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])