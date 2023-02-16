import requests
import json
import os
import time
import sys

def clear_screen():
    """
    Detect operating system and clear terminal
    """
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear') ##used to design
def sleep(n):
    time.sleep(n) ##used for design

def viewperson(num):
    clear_screen()
    """
    take a number and display person info
    """
    try:
        response = requests.get('https://swapi.dev/api/people/%s/' % num)
    except KeyError:
        print("That character does not exist")
    data = json.loads(response.text)

    back = False
    while not back:

        print()
        try:
            print('Name: '+data['name'])
            print('URL: '+data['url'])
            print()

            options = ['Mass','Height','Hair_color','Skin_color','Eye_color','Birth_year','Gender','Homeworld', 'Films', 'Vehicles', 'Starships','Back']
            for i in options:
                print(i)

            choice = input("Enter option to view: ")
            choice.lower() ##capitalization doesnt work
            clear_screen()

            if choice == 'homeworld':
                viewhome(data['homeworld'])
            elif choice == 'films':
                numfilms = len(data['films'])
                print("There are %s films" % numfilms)
                n = int(input("Which film do you want to view? "))
                try:
                    viewfilm(data['films'][n-1])
                except (IndexError, KeyError, ValueError):
                    print("Unknown")
            elif choice == 'vehicles':
                numv = len(data['vehicles'])
                print("There are %s vehicles" % numv)
                n = int(input("Which vehicle do you want to view? "))
                try:
                    viewve(data['vehicles'][n-1])
                except (IndexError, KeyError, ValueError):
                    print("Unknown")
            elif choice == 'starships':
                numstas = len(data['starships'])
                print("There are %s ships" % numstas)
                n = int(input("Which starship do you want to view? "))
                try:
                    viewship(data['starships'][n-1])
                except (IndexError, KeyError, ValueError):
                    print("Unknown")
            elif choice == 'back':
                back = True
            else:
                print()
                try:
                    print(choice +': ' + data['%s' % choice])
                except KeyError:
                    print("That option does not exist")
                print()
                sleep(2)
                clear_screen()
            return
        except KeyError:
            print("404")
            print()
            back = True # like viewper but number only, only accessible from front page

def viewper(url):
    """
    take an url and display person info
    """
    clear_screen()
    try:
        response = requests.get('%s' % url)
    except KeyError:
        print("That character does not exist")
    data = json.loads(response.text)

    back = False
    while not back:

        print()
        print('Name: '+data['name'])
        print('URL: '+data['url'])
        print()


        options = ['Mass','Height','Hair_color','Skin_color','Eye_color','Birth_year','Gender','Homeworld', 'Films', 'Vehicles', 'Starships','Back']
        for i in options:
            print(i)

        choice = input("Enter option to view: ")
        choice.lower() ##capitalization doesnt work
        clear_screen()

        if choice == 'homeworld':
            viewhome(data['homeworld'])
        elif choice == 'films':
            numfilms = len(data['films'])
            print("There are %s films" % numfilms)
            n = int(input("Which film do you want to view? "))
            try:
                viewfilm(data['films'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'vehicles':
            numv = len(data['vehicles'])
            print("There are %s vehicles" % numv)
            n = int(input("Which vehicle do you want to view? "))
            try:
                viewve(data['vehicles'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'starships':
            numstas = len(data['starships'])
            print("There are %s ships" % numstas)
            n = int(input("Which starship do you want to view? "))
            try:
                viewship(data['starships'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'back':
            back = True
        else:
            print()
            try:
                print(choice +': ' + data['%s' % choice])
            except KeyError:
                print("That option does not exist")
            print()
            sleep(2)
            clear_screen()

    return #came from viewperson, with url

def viewhome(url):
    clear_screen()
    """
    take a url and display planet info
    """
    try:
        response = requests.get(url)
    except KeyError:
        print("Unknown")
        print()
        back = True
    data = json.loads(response.text)

    back = False
    while not back:

        print()
        print("Planet: " + data['name'])
        print("URL: "+ data['url'])
        print()

        options = ['Rotation_period','Orbital_period','Diameter','Climate','Gravity','Terrain','Surface_water','Population', 'Residents','Films','Back']
        for i in options:
            print(i)

        choice = input("Enter option to view: ")
        choice.lower()
        clear_screen()
        if choice == 'residents':
            numres = len(data['residents'])
            print("There are %s residents" % numres)
            n = int(input("Which resident do you want to view? "))
            try:
                viewper(data['residents'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'films':
            numfilms = len(data['films'])
            print("There are %s films" % numfilms)
            n = int(input("Which film do you want to view? "))
            try:
                viewfilm(data['films'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'back':
            return
        else:
            print()
            try:
                print(choice +': ' + data['%s' % choice])
            except KeyError:
                print("That option does not exist")
            print()
            sleep(2)
            clear_screen() # %

def viewfilm(url):
    """
    take url and show film info
    """
    clear_screen()
    try:
        response = requests.get(url)
    except KeyError:
        print("Unknown")
        print()
        back = True
    data = json.loads(response.text)

    back = False
    while not back:

        print()
        print("Title: " + data['title'])
        print('URL: '+data['url'])
        print()

        options = ['Episode_id','Opening_crawl','Director','Producer', 'Release_date','Characters','Planets','Starships','Vehicles','Species','Back']
        for i in options:
            print(i)

        choice = input("Enter option to view: ")
        choice.lower()
        clear_screen()
        if choice == 'back':
            back = True
        elif choice == 'characters':
            numchar = len(data['characters'])
            print("There are %s characters" % numchar)
            n = int(input("Which character do you want to view? "))
            try:
                viewper(data['characters'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'planets':
            numpl = len(data['planet'])
            print("There are %s planets" % numpl)
            n = int(input("Which planet do you want to view? "))
            try:
                viewhome(data['planets'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")

        elif choice == 'starships':
            numstas = len(data['starships'])
            print("There are %s ships" % numstas)
            n = int(input("Which starship do you want to view? "))
            viewship(data['starships'][n-1])

        elif choice == 'vehicles':
            numv = len(data['vehicles'])
            print("There are %s vehicles" % numv)
            n = int(input("Which vehicle do you want to view? "))
            viewve(data['vehicles'][n-1])
        elif choice == 'species':
            numspec = len(data['species'])
            print("There are %s species" % numspec)
            n = int(input("Which species do you want to view? "))
            viewspec(data['species'][n-1])
        else:
            print()
            try:
                print(choice +': ' + data['%s' % choice])
            except KeyError:
                print("That option does not exist")
            print()
            sleep(2)
            clear_screen()

def viewspec(url):
    """
    display species info from url
    """
    clear_screen()
    try:
        response = requests.get(url)
    except KeyError:
        print("Unknown")
        print()
        back = True
    data = json.loads(response.text)

    back = False
    while not back:

        print()
        print("Name: " + data['name'])
        print('URL: '+data['url'])
        print()

        options = ['Classification','Designation','Average_Height','Skin_Colors','Hair_Colors', 'Eye_Colors','Average_Lifespan','Homeworld','Language','People','Films']
        for i in options:
            print(i)

        choice = input("Enter option to view: ")
        choice.lower()
        clear_screen()
        if choice == 'back':
            back = True
        elif choice == 'people':
            numchar = len(data['people'])
            print("There are %s people" % numchar)
            n = int(input("Which person do you want to view? "))
            try:
                viewper(data['people'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")

        elif choice == 'homeworld':
            numpl = len(data['homeworld'])
            print("There are %s worlds" % numpl)
            n = int(input("Which world do you want to view? "))
            try:
                viewhome(data['homeworld'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'films':
            numfilms = len(data['films'])
            print("There are %s films" % numfilms)
            n = int(input("Which film do you want to view? "))
            try:
                viewfilm(data['films'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        else:
            print()
            try:
                print(choice +': ' + data['%s' % choice])
            except KeyError:
                print("That option does not exist")
            print()
            sleep(2)
            clear_screen() # %

def viewve(url):
    """
    show vehicle info from URL
    """
    clear_screen()
    try:
        response = requests.get(url)
    except KeyError:
        print("Unknown")
        print()
        back = True
    data = json.loads(response.text)

    back = False
    while not back:

        print()
        print("Name: " + data['name'])
        print('URL: '+data['url'])
        print()

        options = ['Model','Manufacturer','Cost_in_Credits','Length',"Max_Atmosphering_Speed",'Crew','Passengers','Cargo_capacity','Consumables','Vehicle_Class','Pilots','Films']
        for i in options:
            print(i)

        choice = input("Enter option to view: ")
        choice.lower()
        clear_screen()
        if choice == 'back':
            back = True
        elif choice == 'pilots':
            numchar = len(data['pilots'])
            print("There are %s pilots" % numchar)
            e = input("Which pilot do you want to view? ")
            try:
                n = int(e)
            except ValueError:
                print('Unknown')  ##gotta put a try thing for value error
            try:
                viewper(data['pilots'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'films':
            numpl = len(data['films'])
            print("There are %s films" % numpl)
            n = int(input("Which film do you want to view? "))
            try:
                viewfilm(data['films'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        else:
            print()
            try:
                print(choice +': ' + data['%s' % choice])
            except KeyError:
                print("That option does not exist")
            print()
            sleep(2)
            clear_screen() # %

def viewship(url):
    """
    show starship info from URL
    """
    clear_screen()
    try:
        response = requests.get(url)
    except KeyError:
        print("Unknown")
        print()
        back = True
    data = json.loads(response.text)

    back = False
    while not back:

        print()
        print("Name: " + data['name'])
        print('URL: '+data['url'])
        print()

        options = ['Model','Manufacturer','Cost_in_Credits','Length',"Max_Atmosphering_Speed",'Crew','Passengers','Cargo_Capacity','Consumables','Starship_Class','Pilots','Films']
        for i in options:
            print(i)

        choice = input("Enter option to view: ")
        choice.lower()
        clear_screen()
        if choice == 'back':
            back = True
        elif choice == 'pilots':
            numchar = len(data['pilots'])
            print("There are %s pilots" % numchar)
            n = int(input("Which pilot do you want to view? "))
            try:
                viewper(data['pilot'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        elif choice == 'films':
            numpl = len(data['films'])
            print("There are %s films" % numpl)
            n = int(input("Which film do you want to view? "))
            try:
                viewfilm(data['films'][n-1])
            except (IndexError, KeyError, ValueError):
                print("Unknown")
        else:
            print()
            try:
                print(choice +': ' + data['%s' % choice])
            except KeyError:
                print("That option does not exist")
            print()
            sleep(2)
            clear_screen() # %
