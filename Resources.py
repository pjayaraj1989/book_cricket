class Player():
    def __init__(self,name, onstrike, runs, balls):
        self.onstrike=onstrike
        self.runs=runs
        self.balls=balls
        self.name=name

def PairFaceBall(pair, run, ball):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:
        print("Error! both cant be on strike!")
        exit(0)
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    pair[ind].runs += run
    pair[ind].balls += 1
    print("Player on strike: " + pair[ind].name + 
           str(run) + " runs off " + str(pair[ind].balls))

    if ind is 0:    alt_ind=1
    elif ind is 1:  alt_ind=0
    #now if runs is 1/3/5, or if ball is a mul of 6 rotate strike
    if (run % 2 != 0) or (ball % 6 ==0):
        pair[ind].onstrike = False
        pair[alt_ind].onstrike = True
    return pair

def PrintStat(pair):
    for p in pair:
        print("Player: " + p.name +
            " Runs: " + str(p.runs) +
            " Balls: " + str(p.balls) +
            " On strike: " + str(p.onstrike))

def Play(pair):
    from random import randint
    for ball in range(1,10):
        print("Ball: " + str(ball))
        run = randint(0,6)
        PairFaceBall(pair, run, ball)
    PrintStat(pair)
