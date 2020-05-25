
#randomize
def Randomize(list):
    import secrets
    op = secrets.choice(list)
    return op

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