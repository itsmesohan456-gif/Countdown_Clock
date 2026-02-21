import time
import os

def ctd_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)

        timer_display = f"{mins:02d}: {secs:02d}"

        print(f"Time remaining: {timer_display}", end="\r")


        time.sleep(1)
        seconds -= 1

    print("\nTIME'S UP!")