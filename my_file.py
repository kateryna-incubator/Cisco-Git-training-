def main():
 password=input("Please enter your password::")
 if password=="student":
 student()
 elif password=="teacher":
 teacher()
 elif password=="headmaster":
Page 6 of 7
 headmaster()
 elif password=="janitor":
 janitor()
 else:
 print("incorrect password. We cannot take you any further,
goodbye!")
def student():
 print("****WELCOME STUDENT****")
def teacher():
 print("****WELCOME TEACHER****")
def headmaster():
 print("****WELCOME HEADMASTER****")
def janitor():
 print("****WELCOME JANITOR****")
main()


#printing text to the screen is easy - just use the print() command like shown below:

print("This will be printed to the screen")
print("And so will this")
print() #this will leave a space between the previous line printed and the next....
print("This line will have a space before it")
print()
print(""" Triple quotes are hugely useful..................

...........................They allow you to include long strings without having to keep using the print command
For instance, creating a main menu:
=====================MAIN MENU==========================

1...........Play Game
2.......... Save Scores
3.......... Quit

and finally, use triple quotes to quit!!

""")
