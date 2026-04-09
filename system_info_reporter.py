import psutil
import os
import time

def get_cpu_usage():
    return psutil.cpu_percent(percpu=True)
    
def get_memory_info():
    mem =  psutil.virtual_memory()
    return {
        "total": f"{mem.total / (1024**3):.2f} GB",
        "available": f"{mem.available / (1024**3):.2f} GB",
        "used": f"{mem.used / (1024**3):.2f} GB",
        "percentage": f"{mem.percent}%"
    }

def get_disk_info():
    disk =  psutil.disk_usage('C:/')
    return {
        "total": f"{disk.total / (1024**3):.2f} GB",
        "used": f"{disk.used / (1024**3):.2f} GB",
        "free": f"{disk.free / (1024**3):.2f} GB",
        "percentage": f"{disk.percent}%"

    }

print("-----------------------SYSTEM INFO REPORTER----------------------")

while True:
    print("Choice:")
    print("1. View CPU usage")
    print("2. View memory information")
    print("3. View disk information")
    print("4. Exit")
    user_inp = input("\n Choose an option(1-4): ")
    if user_inp == '1':
        cpu = get_cpu_usage()
        print("The CPU usage of this device is: ")
        for i,usage in enumerate(cpu):
            print(f"Core {i}: {usage}%")
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Logical cores:", psutil.cpu_count(logical=True))


    elif user_inp=='2':
        mem = get_memory_info()
        print("The memory information of this device is: ")
        for key, value in mem.items():
            print(f"{key.capitalize()}: {value}")
        
    elif user_inp == '3':
        disk = get_disk_info()
        print("The disk information of this device is: ")
        for key, value in disk.items():
            print(f"{key.capitalize()}: {value}")

        import psutil

        
        

    elif user_inp == '4':
        print("Exiting the program....")
        break

    else:
        print(f"You entered {user_inp}. Invalid input.")
        

   
