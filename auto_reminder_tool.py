import time
from datetime import timedelta, datetime

print("\n\n------------------AUTO REMINDER TOOL------------------\n\n")


reminder_time_input = input("Enter your reminder time(IN HH:MM:SS format): ").strip()
message = input("Enter your message: ").strip()

early_minute = int(input("How many minutes early do you want to get the reminder? (enter 0 for none): "))

now = datetime.now()

#converting to datetime
reminder_time = datetime.strptime(reminder_time_input, "%H:%M:%S")

#set for todays date
reminder_time = reminder_time.replace(year=now.year, month=now.month, day=now.day)

#if time has already passed today, set reminder for next day
if reminder_time < now:
    reminder_time += timedelta(days=1)

#calculate early_reminder
early_reminder = reminder_time - timedelta(minutes=early_minute)

print("\n Reminder is running....")


#set flages to prevent repeated alerts
early_done = False
final_done = False


while True:
    current_time = datetime.now()


    if not early_done and current_time >= early_reminder:
        print(f" Reminder: {message}")
        early_done = True 
    
    if not final_done and current_time >= reminder_time:
        print(f" Reminder: {message}")
        final_done = True 
        break 

    time.sleep(1)





