#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the startof each line of
#text on the clipboard.

import pyperclip

#Step 1: Paste from the Clipboard

text = pyperclip.paste()

#Step 2: Separate the Lines of Text and Add the Star

lines = text.split('\n')

for i in range(len(lines)):
    #Loop through all indexes in the "lines" list.

    lines[i] = '* ' + lines[i] #Add star to each string in "lines" list.

text = '\n'.join(lines)

#Step 3: Copy from the Clipboard

pyperclip.copy(text)
