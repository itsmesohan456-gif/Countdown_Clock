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

    if os.name == 'nt': # For Windows
        import winsound
        winsound.Beep(1000, 1000) # Frequency 1000 Hz, Duration 1000ms
    else:
        print('\a') # For Mac/Linux

try:
    raw_input = input("Enter the time in seconds:")

    user_time = int(raw_input)

    ctd_timer(user_time)

except Exception as e:
    
    print("Error! The program could not run because of {e}")