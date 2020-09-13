import pyautogui
import time
import os
import sys


def restart(name):
    countg = 0
    # closes the league process
    os.system("TASKKILL /F /IM LeagueClient.exe")
    time.sleep(5)
    # open the league client
    os.startfile("C:\Riot Games\League of Legends\LeagueClient.exe")
    time.sleep(60)

    openStore(name, countg)


def window_closed():
    # checks if the window is open
    if pyautogui.locateOnScreen('src/pyw.png') is None:
        sys.exit()


def changeName(name, countg):
    window_closed()
    countverify = 0

    while True:
        window_closed()
        print('Looking for the text box :)')
        form = pyautogui.locateOnScreen('src/form.png')

        if form is not None:
            pyautogui.moveTo(form)
            pyautogui.click()
            pyautogui.typewrite(name, interval=0.001)
            break

    while True:
        window_closed()
        print('Looking for the verify button :)')
        verify = pyautogui.locateOnScreen('src/verify.png')

        if verify is not None:
            pyautogui.moveTo(verify)
            pyautogui.click()
            break

    while True:
        window_closed()
        time.sleep(1)
        cicles = 20
        countverify += 1

        print('Looking for the price button :)')
        price = pyautogui.locateOnScreen('src/price.png')

        if price is not None:
            pyautogui.moveTo(price)
            pyautogui.click()
            print('YOU GOT IT, CONGRATULATIONS')
            break

        elif countverify >= cicles:
            print('The verify button has been already pressed {} times,'
                  ' restarting the process from the home page'.format(cicles))
            while True:
                print('Looking for the home button :)')
                home = pyautogui.locateOnScreen('src/home.png')
                if home is not None:
                    pyautogui.moveTo(home)
                    pyautogui.click()
                    break
            openStore(name, countg)

        else:
            pyautogui.moveTo(form)
            pyautogui.moveTo(verify)
            pyautogui.click()
            print('Verify button pressed {} times'.format(countverify))


def openStore(name, countg):
    window_closed()
    countg += 1

    if countg >= 30:
        print('The League client will be restarted')
        restart(name)

    # locate the store button
    while True:
        window_closed()
        print('Looking for the store button :)')
        close = pyautogui.locateOnScreen('src/close.png')

        if close is not None:
            pyautogui.moveTo(close)
            pyautogui.move(-349, 30)
            pyautogui.click()
            break

    # locate the account button
    while True:
        window_closed()
        print('Looking for the account button :)')
        account = pyautogui.locateOnScreen('src/account.png')

        if account is not None:
            pyautogui.moveTo(account)
            pyautogui.click()
            break

    # locate the page icon
    while True:
        window_closed()
        print('Looking for the page icon :)')
        page = pyautogui.locateOnScreen('src/page.png')

        if page is not None:
            pyautogui.moveTo(page)
            pyautogui.click()
            break

    print('Trying "{}" summoner name'.format(name))

    # at this point the program begins to try try and try to change your nickname
    changeName(name, countg)


def main(nickname):
    name = nickname
    print('Okay, the process will start now, the desired summoner name is {}'.format(name))

    countg = 0
    openStore(name, countg)


if __name__ == "__main__":
    main()
