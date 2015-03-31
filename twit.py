# -*- coding: utf-8 -*-

# To Do:
# -get out of stream somehow, figure out keyboardinterrupt

import sys
import twitter
from colorama import init
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
reload(sys)
sys.setdefaultencoding("utf8")

# get access to the Api with michaelhazani's keys
api = twitter.Api(consumer_key='wrNczJOfwAVb5g7UdOENTEgK0',
                  consumer_secret='XwKCnpTfZKASNaGUWUT3wtCcTcTtLiHNpXN1F0YcfgT'
                                  'zp4dzXT',
                  access_token_key='3124478422-6puXKn7aPN69LJQzYXfsexHt9NBi9rs'
                                  'NAZyOM61',
                  access_token_secret='pE9blQ7F6NMkbAY6bFAnUW7ExN2rKVrhszu44OH'
                                  'nk8nRo')


# Main Menu and question
def mainmenu():
    """Start Screen"""
    print(chr(27) + "[2J")
    cprint(figlet_format('TWiT!', font='doh'), 'white', 'on_blue',
           attrs=['bold'])
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    cprint("Welcome to Twit! A little thing for Twitter.", 'cyan')
    menuquestion()


def menuquestion():
    """Prompt the user to choose an option"""
    cprint("What would you like to do?", 'cyan')
    cprint("Select (S)earch keywords, get (U)ser statuses, "
           "see current (T)rends, access the (L)ivestream or (Q)uit", 'red',
           attrs=['reverse'])
    menuchoice = raw_input(">").upper()
    if menuchoice == "S":
        search()
    elif menuchoice == "U":
        userstatuses()
    elif menuchoice == "T":
        trends()
    elif menuchoice == "Q":
        print(chr(27) + "[2J")
        quit()
    elif menuchoice == "L":
        print(chr(27) + "[2J")
        stream()

    elif menuchoice != "Q" and menuchoice != "Q" and menuchoice != "Q":
        print "\n"
        cprint("Please enter S, U or Q", 'red', attrs=['reverse'])
        print "\n"
        menuquestion()


# Search for Terms
def search():
    """Search for specific terms"""
    print(chr(27) + "[2J")
    cprint(figlet_format('Keyword Search!', font='big'), 'white', 'on_blue',
           attrs=['bold'])
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    query = raw_input("Enter Twitter search term: \n>")
    resultnum = raw_input("How many results? \n>")
    if not resultnum:
        resultnum = 15
    results = api.GetSearch(term=query, count=resultnum)
    resultlist = [x.text for x in results]
    resultuser = [s.user.name for s in results]
    resultfinal = zip(resultuser, resultlist)
    resultfinallist = list(resultfinal)
    cprint("\n\n".join([str(x) for x in resultfinallist]),
           'green', attrs=['bold'])
    print "\n\n\n\n\n\n\n"
    searchprompt()


def searchprompt():
    choice = raw_input("Now what? Options: "
                       "(N)ew Search, (M)ain page\n>").upper()
    if choice == "N":
        print(chr(27) + "[2J")
        search()
    elif choice == "M":
        print(chr(27) + "[2J")
        mainmenu()
    elif choice != "N" and choice != "M":
        print "\n"
        print "Please enter M or N"
        print "\n"
        searchprompt()


# Get User Statuses
def userstatuses():
    """Get statuses from specific users"""
    print(chr(27) + "[2J")
    cprint(figlet_format('Find Statuses', font='big'), 'white', 'on_yellow',
           attrs=['bold'])
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    chosenuser = raw_input("Whose statuses do you want to check out? \n@")
    # cuformatted = "\'%s\'" % chosenuser
    cprint("Searching for statuses by @%s" % chosenuser, 'red',
           attrs=['reverse'])
    statuses = api.GetUserTimeline(screen_name=chosenuser)
    mutstatuses = list(statuses)
    for s in mutstatuses:

        cprint(s.created_at + " @" + s.user.name + ": " + s.text + "\n",
               'green', attrs=['bold'])
    statusprompt()


def statusprompt():
    choice = raw_input("Now what? Options: (N)ew user, (M)ain page\n>").upper()
    if choice == "N":
        print(chr(27) + "[2J")
        userstatuses()
    elif choice == "M":
        print(chr(27) + "[2J")
        mainmenu()
    elif choice != "N" and choice != "M":
        print "\n"
        print "Please enter M or N"
        print "\n"
        statusprompt()


# Get Trends
def trends():
    """Get current trends"""
    print(chr(27) + "[2J")
    cprint(figlet_format('Get Current Trends!', font='big'), 'white', 'on_red',
           attrs=['bold'])
    print "\n\n"
    trendresults = api.GetTrendsCurrent()
    trendformatted = " \n".join(str(e) for e in trendresults)
    cprint(trendformatted, 'green', attrs=['bold'])
    print "\n\n\n\n\n\n\n"
    trendsprompt()


def trendsprompt():
    choice = raw_input("Now what? Options: (R)epeat Trend Search, "
                       "(M)ain page\n>").upper()
    if choice == "R":
        print(chr(27) + "[2J")
        trends()
    elif choice == "M":
        print(chr(27) + "[2J")
        mainmenu()
    elif choice != "R" and choice != "M":
        print "\n"
        print "Please enter M or R"
        print "\n"
    trendsprompt()


def stream():
    try:
        trackphrase = raw_input("Enter words to filter the stream by: \n>")
        if trackphrase == "":
            trackphrase = "a"
        current = api.GetStreamFilter(track=[trackphrase])
        for tweet in current:
            if tweet.get('text'):
                cprint("(%s) @%s %s" % (tweet["created_at"], tweet["user"]
                                             ["screen_name"], tweet["text"]),
                       'green', attrs=['bold'])
    except KeyboardInterrupt:
        mainmenu()

mainmenu()
