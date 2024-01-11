"""Method for drawing all the spell's text data on the screen."""
"""function to break strings into lines by words.
Inputs the string, boolean for indentation on first line, and max length of line by character."""
def text_wrap(text, indentMode, scale):
    #split text into words
    textList = text.split(" ")
    #if indent desired, start first line with long gap
    if (indentMode):
        word = "        "
    #otherwise, start as empty string
    else:
        word = ""
    textLines = []
    #loop to add words to lines
    for i in textList:
        #if adding the next word does not go over character limit, add it
        if (len(word + " " + i) < scale):
            word += " " + i
        #otherwise save the line to list and start a new line with the omitted word
        else:
            textLines.append(word)
            word = i
    #add final incomplete line to list
    textLines.append(word)
    #remove null character from initialization of first line and replace the first line
    removedGap = textLines[0][1:]
    textLines[0] = removedGap
    #return lines
    return textLines