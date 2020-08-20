import pyttsx3
import os

print("Hello! What would you like to do today?")
pyttsx3.speak("Hello! What would you like to do today?")


while True:
    print("Chat with me with your requirements: ", end='')
    p = input().lower()

    if ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p) or("execute" in p):
        
        if ("chrome" in p) or ("browser" in p):
            print("Would you like to go to any specific website? ")
            website = input()
            if ("No" in website) or ("NO" in website) or ("no" in website):
                os.system("start chrome")
            else:
                os.system("start chrome {website}".format(website))
                
        elif ("notepad" in p) or ("editor" in p) or ("texteditor" in p) :
            if "notepad" in editor:
                os.system("notepad")
                
        elif ("music" in p) or ("musicplayer" in p) or ("song" in p):
            os.system("start wmplayer")
        
        elif ("cmd" in p) or ("command prompt" in p):
            os.system("start cmd")
            
    elif ("exit" in p) or ("quit" in p) or ("bye" in p) or ("terminate" in p) or("terminate" in p):
        break
    else:
        print("Option not supported")
        pyttsx3.speak("option not supported") 