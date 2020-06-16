import pathlib
import re
import time




def check_chars(path):
    with open(path) as file:  # Use file to refer to the file object
        # remove all the check in wordlist
        data = file.read()


    # check for iligal charecters
    data = data.replace("\n", "")
    data = data.replace("\t", "")
    data = data.replace("\r", "")
    data = data.replace(" ", "")

    if (not data.isalnum()):
        print(str(time.ctime())+" Warning "+ path+" has illigal chrecters check it for Ransomware.\n")


def check_dictinary(path):
    with open(path) as file:  # Use file to refer to the file object
        # remove all the check in wordlist
        data = file.read()
    data=data.lower()
    data = data.replace(":", " ")
    data = data.replace(",", " ")
    data = data.replace(".", " ")
    data = data.replace("'", "")
    data = data.replace(";", " ")
    data = data.replace("’", " ")
    data = data.replace("“", " ")
    data = data.replace("-", "")
    data = data.replace("/", "")
    data = data.replace("'", "")
    data = data.replace("!", "")
    data = data.replace("?", "")
    data = data.replace("(", "")
    data = data.replace(")", "")
    data = data.replace("[", "")
    data = data.replace("]", "")
    data = data.replace("—", " ")
    data = data.replace("‘", "")
    data = data.replace("\"", "")
    data = data.replace('”', "")
    with open("english.txt") as file:
        english_list = file.read()

    english_list=english_list.lower()
    english_list = english_list.replace(":", " ")
    english_list = english_list.replace(",", " ")
    english_list = english_list.replace(".", " ")
    english_list = english_list.replace("'", "")


    splited_data = data.split()
    english_list_splited = english_list.split()
    illigal_words = []

    count= 0
    for word in splited_data:
        if len(word)>25:
            print(str(time.ctime()) + " Warning " + path + " has more than word with a length bigger than 25 chars check it for Ransomware. The word is :"+word)
        isIn = False
        for dict in english_list_splited:
            if word in dict:
                isIn = True
        if isIn ==False and len(word)>1 and  not word.isalnum():
            count+=1
            illigal_words.append(word)



    if (len(illigal_words) > (len(splited_data)/20)):
        print(str(time.ctime())+" Warning "+ path+" has more than 5% unrecognised word's that don't appere in the dictinary check it for Ransomware.")
        print("The unrecognised words"+str(illigal_words))




def minitor():
    path = pathlib.Path('.')
    for entry in path.iterdir():
        path = str(entry)
        if entry.is_file() and "txt" in path and path not in "english.txt":
            check_dictinary(path)
            check_chars(path)


def main() :
    print("Service monitor created by Simon Pikalov")
    print('''----------------------//\\
---------------------// ¤ \\
---------------------\\ ¤ //
---------------------- \\//
-------------------- (___)
---------------------(___)
---------------------(___)
---------------------(___)_________
--------\_____/\__/----\__/\_____/
------------\ _°_[------------]_ _° /
----------------\_°_¤ ---- ¤_°_/
--------------------\ __°__ /
---------------------|\_°_/|
---------------------[|\_/|]
---------------------[|[¤]|]
---------------------[|;¤;|]
---------------------[;;¤;;]
--------------------;;;;¤]|]\\
-------------------;;;;;¤]|]-\\
------------------;;;;;[¤]|]--\\
-----------------;;;;;|[¤]|]---\\
----------------;;;;;[|[¤]|]|---|
---------------;;;;;[|[¤]|]|---|
----------------;;;;[|[¤]|/---/
-----------------;;;[|[¤]/---/
------------------;;[|[¤/---/
-------------------;[|[/---/
--------------------[|/---/
---------------------/---/
--------------------/---/|]
-------------------/---/]|];
------------------/---/¤]|];;
-----------------|---|[¤]|];;;
-----------------|---|[¤]|];;;
------------------\--|[¤]|];;
-------------------\-|[¤]|];
---------------------\|[¤]|]
----------------------\\¤//
-----------------------\|/
------------------------V
''')
    isLightRunning = False
    isFulllRunning = False
    menuMessege = "please choose a action mode\nfor manual type manual , for full mode type full and for light mode tight light"
    print(menuMessege)


    while(True):

        mode = input("\nchoose an action \n")

        if mode == "full" or  mode == "f" :
            if isFulllRunning == True:
                print("\nThe program is already running at full mode \n")
            else:
                print("full Mode ")
                isFulllRunning == True
                sleepTime = input("\nchoose an Interval Time for the program in seconds:  \n")
                try:
                    val = float(sleepTime)
                    if val < 0:
                        print("Not valid Input")
                    else:
                        isLightRunning = True
                except ValueError:
                    print("Not valid Input")


        elif mode == "light" or mode == "l" :
            if isLightRunning == True:
                print("\nThe program is already running\n")

            else:
                sleepTime = input("\nchoose an Interval Time for the program in seconds:  \n")
                try:
                    val = float(sleepTime)
                    if val<0:
                        print("Not valid Input")
                    else:
                        isLightRunning = True
                except ValueError:
                    print("Not valid Input")





        elif mode == "help" :

            print(
                "\n\n\n@author Simon Pikalov\nThis program helps monitor system services by whriting a log file that contain all the changes in the services on you machine.\n" + menuMessege)


        elif mode == "exit":
                exit()






main()

