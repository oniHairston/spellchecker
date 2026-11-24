#Oni H
#This is going to be a GUI Python Project that checks the spelling of a word 

from tkinter import * #import all functions from library
from textblob import TextBlob

#functino that checks spelling of word
def checkSpelling():
    
    #clear labels
    for widget in window.winfo_children():
        if isinstance(widget, Label) and widget != text_heading and widget != text_check:
            widget.destroy()

    word = TextBlob(spell_check.get()) #gets the word from entry widget
    corrected = word.correct()

   #if user word is already spelled correctly then just return this, else show cprrect spelling
    if corrected == word:
        correctText = Label(window, text = "The word is spelled correctly!", font = ("Helvetica", 25, "bold"), bg = "darksalmon", fg = "seashell")
        correctText.pack()
    else: 
        spell = Label(window, text = "The correct spelling is: ", font = ("Helvetica", 25, "bold"), bg = "darksalmon", fg = "seashell")
        spell.pack()

        correctText = Label(window, text = str(corrected), font = ("Helvetica", 25, "bold"), bg = "indianred", fg = "seashell")
        correctText.pack()

    

window = Tk() #this is the main window for the spell checker
window.title("My Spell Checker")
window.geometry("800x600")
window.config(background = "peachpuff")

text_heading = Label(window, text = "Spell Checker", font = ("Helvetica", 50, "bold"), bg = "darksalmon", fg = "seashell")
text_heading.pack()

text_check = Label(window, text = "Enter a word to check its spelling", font = ("Helvetica", 25), bg = "darksalmon", fg = "seashell")
text_check.pack()

spell_check = Entry(window, font = ("Helvetica", 45, "bold"), width = 500, bg = "linen")
spell_check.pack() #packs the entry widget into the main window

Check_button = Button(window, text = "Check it!", font = ("Helvetica", 30, "bold"), bg = "indianred", fg = "seashell", command = checkSpelling)
Check_button.pack()

window.bind("<Return>", lambda event: checkSpelling()) #binds the enter key to check spelling


window.mainloop() #runs main window of program


