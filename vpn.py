################################### Windscribe ############################################
# import pyautogui
# import subprocess
# import time

# # Windscribe application ko open karein
# subprocess.Popen('C:\Program Files\Windscribe\Windscribe.exe')

# # Application khulne ka wait karein (wait time depend karta hai application par)
# time.sleep(5)

# # Screen par 'Connect' button ki location ka pata lagayein
# # Yeh coordinates example ke liye hain, aapko inhe apne screen ke hisab se adjust karna padega
# connect_button_location = pyautogui.locateCenterOnScreen('connect_button.png')

# # Agar 'Connect' button mil jaye toh us par click karein
# if connect_button_location is not None:
#     pyautogui.click(connect_button_location)
# else:
#     print("Connect button not found on the screen.")


################################### Proton ##############################################
import subprocess
import pyautogui
import time

# Proton VPN ka path. Apne actual path ke hisab se adjust karein.
proton_vpn_path = r"C:\Program Files\Proton\VPN\ProtonVPN.Launcher.exe"
subprocess.Popen(proton_vpn_path)
time.sleep(3)  # Proton VPN ko load hone ka time dein.
# Pehle 'connect_button.png' ka screenshot lein aur ise project directory me save karein.
button_location = pyautogui.locateCenterOnScreen('connect_it.png', confidence=0.8)
if button_location:
    pyautogui.click(button_location)
else:
    print("Connect button nahi mila.")
