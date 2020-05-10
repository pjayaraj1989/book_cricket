
#randomize
def Randomize(list):
    import secrets
    op = secrets.choice(list)
    return op

#print in color
def PrintInColor(msg, color):
    import os
    #colorama crashes on windows, so dont use it in windows
    if 'nt' in os.name: print(msg)
    else:
        import colorama
        from colorama import Style
        colorama.init()
        print(color + msg + Style.RESET_ALL)

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