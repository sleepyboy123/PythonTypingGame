from tkinter import *
from timeit import default_timer as timer
from random import randrange
import json
import os


def key(event):                                                 # Function that is Called When Space Key is Pressed
    if event.keysym == "space":
        global counter
        global correctWords
        global currentChar
        global startTime
        wordsTyped.append(input.get("1.0", "end-1c"))           # Append Input to wordsTyped List
        input.delete("1.0", "end-1c")                           # Clear Input Box
        if wordsTyped[counter] == passageWords[counter]:        # Check if Input Matches Text
            passage.tag_add("correct", "1." + str(currentChar), "1." + str(len(passageWords[counter]) + currentChar))
            passage.tag_config("correct", foreground="green")   # Text Becomes Green
            currentChar += len(passageWords[counter])
            correctWords += 1
        else:                                                   # Input does not match text
            passage.tag_add("wrong", "1." + str(currentChar), "1." + str(len(passageWords[counter]) + currentChar))
            passage.tag_config("wrong", foreground="red")       # Text Becomes Red
            currentChar += len(passageWords[counter])
        if counter == 0:
            startTime = timer()                                 # Start Timer
        counter += 1
        if counter == len(passageWords):
            endTime = timer()                                   # Stop Timer
            print("You typed " + str(correctWords) + " correct words in " + str(round(endTime - startTime)) + " seconds")
            print("Your wpm is " + str(correctWords / round(endTime - startTime) * 60))
            root.quit()


counter = 0                                                     # Declare "Static" Variables
correctWords = 0
currentChar = 0
wordsTyped = []
startTime = 0

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Quotes.json')                 # Relative File Path
with open(filename, 'r') as json_file:                          # Open JSON File
    data = json.load(json_file)
    choice = randrange(len(data))                               # Random Object Index
    quote = data[choice]['Text']                                # Random Quote
    print(data[choice]['Source'])                               # Print Source
json_file.close()                                               # Close JSON File
placeholder = quote.split()                                     # Split Quote into List
passageWords = [word + " " for word in placeholder]

root = Tk()                                                     # Create Blank Window
root.title("Sleepy Typer")
root.bind_all('<Key>', key)
upperFrame = Frame(root)                                        # Create Upper Frame
upperFrame.pack(fill=BOTH, expand=True)
lowerFrame = Frame(root)                                        # Create Lower Frame
lowerFrame.pack(fill=BOTH, expand=True)
passage = Text(upperFrame, height=5, font="Calibri 20")         # Create Passage Text Box
passage.pack(fill=BOTH, expand=True)
input = Text(lowerFrame, height=1, font="Calibri 20")           # Create Input Text Box
input.pack(fill=BOTH, expand=True)

passage.insert(END, quote)                                      # Insert Quote into Passage
passage.config(state=DISABLED)

root.mainloop()                                                 # Continuously Display Window
