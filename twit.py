import sys
import twitter
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# import time


api = twitter.Api(consumer_key='Sac39Y6C6fJ3yAcX3xme80Hz7',
consumer_secret='bHeBpGBFJFe66kRXcHeQWU6TKp6uiu7QO9wTCX83lw8B2lJMpM',
access_token_key='189239506-XsfaRhqtPja2Qt9Xpc2CleLtNgvuxPYBMLA5nPWn',
access_token_secret='Bdd4pRQNNEoCv1V4vtZyGyjyh4ke9wgbFSPe0YAIhjOxa')


def mainmenu():
    print(chr(27) + "[2J")
    cprint(figlet_format('Twit!', font='doh'), 'white', 'on_blue', attrs=['bold'])
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "Welcome to Twit! A little thing for Twitter."
    menuquestion()

def menuquestion():
    print "What would you like to do?"
    print "Select (S)earch keywords, get (U)ser statuses or (Q)uit"
    menuchoice = raw_input(">").upper()
    if menuchoice == "S":
        search()
    elif menuchoice == "U":
        userstatuses()
    elif menuchoice == "Q":
        print(chr(27) + "[2J")
        quit()
    elif menuchoice != "Q" and menuchoice != "Q" and menuchoice != "Q":
        print "\n"
        print "Please enter S, U or Q"
        print "\n"
        menuquestion()



def search():
    query = raw_input("Enter Twitter search term: \n>")
    resultnum = raw_input("How many results? \n>")
    if not resultnum:
        resultnum = 15
    results = api.GetSearch(term=query, count=resultnum)
    resultlist = [x.text for x in results]
    print "\n".join(resultlist)
    print "\n\n\n\n\n\n\n"
    choice = raw_input("Now what? Options: (N)ew Search, (M)ain page\n>").upper()
    if choice == "N":
        print(chr(27) + "[2J")
        search()
    if choice == "M":
        print(chr(27) + "[2J")
        mainmenu()


def userstatuses():
    chosenuser = raw_input("Whose statuses do you want to check out? \n@")
    # cuformatted = "\'%s\'" % chosenuser
    print "Searching for statuses by %s" % chosenuser
    statuses = api.GetUserTimeline(screen_name=chosenuser)
    statuslist = [s.text for s in statuses]
    print "\n".join(statuslist)
    # friends = api.GetFriends()
    # print [u.name for u in friends]
    print "\n\n\n\n\n\n\n"
    choice = raw_input("Now what? Options: (N)ew user, (M)ain page\n>").upper()
    if choice == "N":
        print(chr(27) + "[2J")
        userstatuses()
    if choice == "M":
        print(chr(27) + "[2J")
        mainmenu()

mainmenu()
