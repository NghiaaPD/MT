import os
import keyboard

def disconnect_mouse():
    os.system("C:/Program Files/devmanview-x64/DevManView.exe /disable \"HID-compliant mouse\"")

def connect_mouse():
    os.system("C:/Program Files/devmanview-x64/DevManView.exe /enable \"HID-compliant mouse\"")

keyboard.on_press_key("f", lambda _: disconnect_mouse())
keyboard.on_press_key("o", lambda _: connect_mouse())

keyboard.wait()
