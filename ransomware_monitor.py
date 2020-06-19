import pathlib
import re
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FullHandler(FileSystemEventHandler):
    def on_modified(self, event):
        path = str(event.src_path)
        path=path[2:]
        path=replase_char_with_space(path,"~","")

        if  "txt" in path and path not in "english.txt" and path not in "log.txt":
            print(f'time: {time.ctime()}event type: {event.event_type}  path : {path}')
            check_dictinary(path)
            check_chars(path)


class LightHandler(FileSystemEventHandler):
    def on_modified(self, event):
        path = str(event.src_path)
        path=path[2:]
        path=replase_char_with_space(path,"~","")

        if  "txt" in path and path not in "english.txt" and path not in "log.txt":
            print(f'time: {time.ctime()}event type: {event.event_type}  path : {path}')
            check_chars(path)





def check_chars(path):
    log = open('log.txt', 'a')


    with open(path) as file:  # Use file to refer to the file object
        # remove all the check in wordlist
        data = file.read()


    # check for iligal charecters
    data = data.replace("\n", "")
    data = data.replace("\t", "")
    data = data.replace("\r", "")
    data = data.replace(" ", "")

    if (not data.isalnum()):
        log = open('log.txt', 'a')
        warning = ("\n"+str(time.ctime())+" Warning "+ path+" has illigal chrecters check it for Ransomware.\n")
        print(warning)
        log.write(warning)
        log.close()


# delimeter_to_delete - a str with chars you want to delete.
# delimeter_to_space - a str with chars you want to replase withe space.
def replase_char_with_space(word,delimeter_to_delete,delimeter_to_space):
    word=str(word)
    for d in delimeter_to_delete:
        word=word.replace(d,"")
    for d in delimeter_to_space:
        word=word.replace(d," ")
    return  word




def check_dictinary(path):
    log = open('log.txt', 'a')
    with open(path) as file:  # Use file to refer to the file object
        # remove all the check in wordlist
        data = file.read()
    data=data.lower()
    data =replase_char_with_space(data,":'\"-/!?()[]'‘",",.;_")
    with open("english.txt") as file:
        english_list = file.read()

    english_list=english_list.lower()
    english_list= replase_char_with_space(english_list,"'",".,;:")



    splited_data = data.split()
    english_list_splited = english_list.split()
    illigal_words = []

    count= 0
    first_length = True
    for word in splited_data:
        if len(word)>25:
            if first_length:
                first_length=False
                log = open('log.txt', 'a')
                warning= (str(time.ctime()) + " Warning " + path + " :\nhas more than word with a length bigger than 25 chars check it for Ransomware.\nThe word is :"+word)
                print(warning)
                log.write(warning)
                log.close()
                log.close()
        isIn = False
        for dict in english_list_splited:
            if word in dict:
                isIn = True
        if isIn ==False and len(word)>1 and  not word.isnumeric():
            count+=1
            illigal_words.append(word)



    if (len(illigal_words) > (len(splited_data)/20)):
        log = open("log.txt",'a')
        warning = (str(time.ctime())+" Warning "+ path+" has more than 5% unrecognised word's that don't appere in the dictinary check it for Ransomware.")
        details = ("The unrecognised words"+str(illigal_words[0:10]))
        print(warning)
        print(details)
        log.write(warning)
        log.write(details)
        log.close()





class full_monitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sleep_time = 1
        event_handler = FullHandler()
        self.observer = Observer()
        self.observer.schedule(event_handler, path='.', recursive=False)
        self.observer.start()

    def run(self):
        try:
            while True:
                time.sleep(self.sleep_time)
                path = pathlib.Path('.')
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class light_monitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sleep_time = 1
        event_handler = LightHandler()
        self.observer = Observer()
        self.observer.schedule(event_handler, path='.', recursive=False)
        self.observer.start()

    def run(self):
        try:
            while True:
                time.sleep(self.sleep_time)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()



def main() :
    print("Ransomware Protector created by Simon Pikalov")
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
                        full = full_monitor()
                        full.sleep_time = val
                        full.start()
                        isFulllRunning = True
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
                        light = light_monitor()
                        light.sleep_time = val
                        light.start()
                        isLightRunning = True
                except ValueError:
                    print("Not valid Input")





        elif mode == "help" :

            print(
                "\n\n\n@author Simon Pikalov\nThis program helps monitor folder txt files  by whriting a log file,\nthat contain all the changes in the file that  may be causing encryption of your data\n"
                "for more information read the readme at https://github.com/simon-pikalov/Ransomware_Protector.\n" + menuMessege)

        elif mode == "exit":
                exit()






main()

