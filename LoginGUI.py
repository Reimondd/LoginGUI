import pyautogui
import time
import json
# temporary storage that will move to the json file
LoginStorage = json.load(open("Cool_Database.json", "r+"))
local = time.localtime()
localtime = time.strftime("%H:%M", local)


def main():

    # gives u an option to login or create an account
    option = pyautogui.confirm(title="Login", text="Welcome", buttons=['Login', 'Create Account'])

    if option == 'Login':
        username = pyautogui.prompt(title="Login", text="Enter your username").lower()

        if username in LoginStorage["Name"]:    # You can login by typing username but it needs to be
            # in the json file same for the password
            # If username in 'database' u can enter the password that matches|| mask password *
            password = pyautogui.password(title="Login", text="Type your password", mask='*')
        else:
            pyautogui.alert(title="404 not found", text="Username was not found")
            return main()

        if password in LoginStorage["Password"]:
            while True:  # you access this part after login
                    very_hard_choice = pyautogui.confirm(title="Hello" + username, text="Your current time " + localtime +"\n What would you like to do?",
                                                         buttons=['Monke', 'Exit'])

                    if very_hard_choice == 'Exit':    # if you quit it exits the program
                        pyautogui.alert(title="Exit", text="See you later")
                        time.sleep(1)
                        exit(1)
                    else:
                        pyautogui.alert(title="Monke", text="🐵 🐵 🐵")    # mature option you can choose
        else:   # if anything you typed was not in any of the lists
            pyautogui.alert(title="404 Not found", text="Did not recognise input", button="Retry")
            time.sleep(0.5)
            return main()
    elif option == 'Create Account':
        add_username = pyautogui.prompt(title="Registration", text="Enter your username").lower()
        if add_username in LoginStorage["Name"]:
            pyautogui.alert(title="Registration", text="Someone already has that username")
            return main()
        else:
            LoginStorage["Name"].append(add_username)
            with open("Cool_Database.json", "r+") as DB:
                data = json.load(DB)
                data.update(LoginStorage)
                DB.seek(0)
                json.dump(data, DB)

            while True:
                add_password = pyautogui.password(title="Registration", text="Create a password At least 8 characters")
                if len(add_password) < 9:
                    pyautogui.alert(title="Registration", text="Password does not meet requirements", button="Retry")
                    pass

                else:
                    pyautogui.alert(title="Success", text="Your registration was a success")
                    if add_password in LoginStorage["Password"]:
                        return main()  # prevents the same password being in 'database' over and over again
                    else:
                        LoginStorage["Password"].append(add_password)
                        with open("Cool_Database.json", "r+") as DB:
                            data = json.load(DB)
                            data.update(LoginStorage)
                            DB.seek(0)
                            json.dump(data, DB)
                        return main()


main()
