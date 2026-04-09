print("---------SCREENSHOT TAKER---------")

import pyautogui
import time
import os


class ScreenshotTaker:
    def __init__(self, folder, interval, img_format):
        self.save_folder = folder
        self.interval = interval
        self.img_format = img_format
        self.count = 1

    def start(self):
        print("Screenshot capturing started... Press CTRL+C to stop.")

        while True:
            # Step 2: Capture screenshot
            img = pyautogui.screenshot()

            # Step 3: Save screenshot
            filename = f"screen{self.count}.{self.img_format}"
            filepath = os.path.join(self.save_folder, filename)

            img.save(filepath)

            print(f"Screenshot saved: {filename}")

            self.count += 1

            # Step 4: Wait
            time.sleep(self.interval)


# user input
save_folder = input("Enter the folder path where screenshots will be saved: ")

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

time_interval = input("Enter the interval (in seconds) between screenshots: ")
interval = float(time_interval)

img_format = input("Enter image format (png/jpg): ").lower()

taker = ScreenshotTaker(save_folder, interval, img_format)

try:
    taker.start()
except KeyboardInterrupt:
    print("\nScreenshot capturing stopped by user.")
