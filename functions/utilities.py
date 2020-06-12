import random

import colorama
from colorama import Style, AnsiToWin32, init, Fore
import time
import sys
import os

#choose from options a list
def ChooseFromOptions(options, msg):
    print (msg)
    option_selected = None
    options_dict = {}
    for x in range(len(options)):
        options_dict[str(x)] = options[x]
    msg = ''
    for k, v in options_dict.items():    msg += '{0}.{1} '.format(k, v)
    keys = list(options_dict.keys())
    n = 3
    while n > 0:
        opt = input("Select from : {0}".format(msg))
        if opt not in keys:
            n -= 1
            if n == 0:
                Error_Exit("exiting!")
            else:
                print('Invalid choice! Try again')
                continue
        else:
            for k, v in options_dict.items():
                if opt == k:
                    option_selected = v
                    print("Selected : " + v)
                    break
        break
    return option_selected

#randomize
def Randomize(list):
    op = random.choice(list)
    return op

#get short name
def GetShortName(name):
	shortname=name
	#get first part and make it initial
	pieces = name.split(' ')
	initials=' '
	firstname,lastname = pieces[0],pieces[-1]
	if '.' in firstname:
		initials=firstname
	else:
		initials = firstname[0] + '.'
	shortname = initials + ' ' + lastname
	return shortname

#print nested array in formatted way
def PrintListFormatted(data_to_print, seconds, logger):
    # now print it
    col_width = max(len(word) for row in data_to_print for word in row) + 1
    for row in data_to_print:
        msg = "".join(word.ljust(col_width) for word in row)
        PrintInColor(msg, Style.BRIGHT)
        if logger is not None:
            logger.info(msg)
        time.sleep(seconds)

#print in color
def PrintInColor(msg, color):
    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream
    print(color + msg + Style.RESET_ALL, file=stream)

#just error and exit
def Error_Exit(msg):
    if 'nt' in os.name: print(msg)
    else:
        colorama.init()
        PrintInColor("Error: " + msg, Fore.RED)
    input('Press enter to continue..')
    sys.exit(0)

#balls to overs
def BallsToOvers(balls):
    overs=0.0
    if balls >=0:
        overs = float(str(int(balls/6)) + '.' + str(balls%6))
    return overs