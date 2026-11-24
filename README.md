# A Python Spellchecker Application


<img width="794" height="623" alt="SpellChkProj" src="https://github.com/user-attachments/assets/b1a3bbf5-1bbc-445e-9f54-3fe291da329d" />


This is a very simple desktop spell checker built with Python and tkinter! 
Type in a word and it tells you whether or not it's spelled correctly, or suggets the correct spelling.


## Features
- Checks the spelling of a word using TextBlob
- Shows the corrected spelling if the word is wrong
- Press enter or click the "Check it!" button
- Clears old results before showing new ones

## How to run
1. Install Python 3
2. Download or clone this repo
3. Install the required library:

'''
pip install textblob
'''

4. Run the program:

'''
python spellcheck.py
'''

tkinter comes with Python, therefore TextBlob is the only extra install.

## How it works
The program takes the word you type into the entry box and passes it to TextBlob's "correct()" method. If the corrected word matches what the user types, it's spelled correctly. If not, the program displays the suggested spelling.

## What I Learned
- Building a GUI with tkinter (labels, entry boxes, buttons)
- Using an external library (TextBlob)
- Binding keyboard events, and using 'lambda' to adapt a function to an event
- Debugging the order of operations: results being cleared after shown to the user

## Limitations
TextBlob works best on single words, and it can sometimes "correct" real words it doesn't recognize, especially names.

## Future improvements
- Support checking whole sentences 
- Showing multiple word suggestions
