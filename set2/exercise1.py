"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
#The "platform" is a placeholder for the operating system, so this line will "import" whatever we want to print next.
import platform
#It allowed for the process to begin and move towards the next line. This is where the next printing code will be.
# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#I think this line is here to take the words in the brackets and state them. Therefore, this line, when its run, would say "what does this line do?"
some_words = ["what", "does", "this", "line", "do", "?"]
#It's a variable name. It represents a string, so the string of words, "what does this line do?" shows up each time its played until the letters run out.
#I think will code the "word" in "some_words" to be printed
for word in some_words:
    print(word)
#The first word within the "some_words" string was printed. This word being "what". This is because the "word" in "some_words" was programmed to do this.
#x is equal to the "some_words", and since we have finished the string, it will begin to replay.
for x in some_words:
    print(x)
#It repreated the line and was begining to replay the string.
#Since this line is before the other code, I belive this will print this = (what does this line do?) as a full sentence instead of each individual word needing a manual push to play next.
print(some_words)
#This line played the original phrase, ('what','does','this','line','do','?')
#I think this next line will print the line that I just said above and then followed up with,"contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words")
#This line printed the phrase "some_words contains more than 3 words"
#def will define the new function and then usefulFunction is gonna be the name of that function.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #This will return a name tuple with some attributes.
    print(platform.uname())
#The tuple returned the attributes 'system','node','release','version','machine' and'processor'

usefulFunction()
