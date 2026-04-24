import requests

print("\n\n------------------WEBSITE CHECKER TOOL------------------\n\n")

while True:
    url = input("Enter the url of website: ").strip()   

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("The website is up!")
        else:
            print(f"Website is reachable but returned status code {response.status_code}")

    except requests.exceptions.RequestException:
        print("Website is down or invalid URL")

    user_inp = input("Do you want to check again?(y/n): ").strip().lower()
    if user_inp != 'y':
        print("Exiting the program...")
        break










