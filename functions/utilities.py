
#randomize
def Randomize(list):
    import random
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
    from colorama import Style
    import time
    col_width = max(len(word) for row in data_to_print for word in row) + 1
    for row in data_to_print:
        msg = "".join(word.ljust(col_width) for word in row)
        PrintInColor(msg, Style.BRIGHT)
        if logger is not None:
            logger.info(msg)
        time.sleep(seconds)

#print in color
def PrintInColor(msg, color):
    import sys
    from colorama import Style,AnsiToWin32,init
    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream
    print(color + msg + Style.RESET_ALL, file=stream)

#just error and exit
def Error_Exit(msg):
    import sys
    import os
    if 'nt' in os.name: print(msg)
    else:
        import colorama
        from colorama import Fore
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