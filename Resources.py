class Player():
    def __init__(self,name, onstrike, runs, balls, status):
        self.onstrike=onstrike
        self.runs=runs
        self.balls=balls
        self.name=name
        self.status=status

class Team():
    def __init__(self, team_array, total_score, innings_over):
        self.team_array=team_array
        self.total_score=total_score
        self.innings_over=innings_over

def PairFaceBall(pair, run, ball):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:
        print("Error! both cant be on strike!")
        exit(0)    
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    if ind is 0:    alt_ind=1
    elif ind is 1:  alt_ind=0        
    pair[ind].runs += run
    pair[ind].balls += 1
    print("Player on strike: " + pair[ind].name + 
       str(pair[ind].runs) + " runs off " + str(pair[ind].balls))        
    #now if runs is 1/3/5, or if ball is a mul of 6 rotate strike
    if (run % 2 != 0) or (ball % 6 ==0):
        pair[ind].onstrike = False
        pair[alt_ind].onstrike = True
    return pair

def UpdateStat(team, extras, wkts_fell):
    total_runs=0
    for p in team.team_array:
        total_runs += p.runs
        if p.status is True:
            print("{0} : {1}* ( {2} )".format(p.name, str(p.runs), str(p.balls)))
        else:
            print("{0} : {1} ( {2} )".format(p.name, str(p.runs), str(p.balls)))

    print ("Extras: " + str(extras.runs))
    total_runs += extras.runs
    #calculate total
    print("TOTAL: {0} / {1}".format(str(total_runs), str(wkts_fell)))
    team.innings_over=True
    team.total_score=total_runs

def BatsmanOut(pair):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:
        print("Error! both cant be on strike!")
        exit(0)
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    if ind is 0:    alt_ind=1
    elif ind is 1:  alt_ind=0
    #bastman dismissed
    player_on_strike.status = False
    player_on_strike.balls += 1
    return pair

def Play(team, extras, pair):
    team_list=team.team_array
    total_wkts = len(team_list)-1
    wkts_fell = 0
    num_of_balls = 300
    for ball in range(1,num_of_balls+1):
        #input()
        print("Ball: " + str(ball))
        if wkts_fell == total_wkts:
            print("All out!")
            break
        #this is the main guy who generates runs
        import random
        run_array = [-1,0,0,0,0,0,1,1,1,1,1,1,1,1,2,3,4,5]
        run = random.choice(run_array)
        #run = randint(-1,6)
        #if run is 5, treat as a wide dont count ball, incr extras
        if run is 5:
            extras.runs += 1
            print("Wide, total extras: " + str(extras.runs))
        #-1 ==> out!
        elif run is -1:
            ball += 1
            pair=BatsmanOut(pair)
            player_dismissed = next((x for x in pair if x.status == False), None)
            ind=pair.index(player_dismissed)
            print ("Player dismissed: " + player_dismissed.name + " for " + str(player_dismissed.runs))
            wkts_fell += 1
            print ("Total wkts fell " + str(wkts_fell))
            #now bring the next batsman
            #if len(team)-wkts fell =2, stop
            if wkts_fell == total_wkts:
                print("All out!")
                break
            pair[ind] = team_list[wkts_fell + 1]
            pair[ind].onstrike=True
            print ("New Batsman: " + pair[ind].name)
        #if not out or wide, count runs
        else:
            ball += 1
            print ("Runs scored: " + str(run))
            PairFaceBall(pair, run, ball)
    #print scorecard
    UpdateStat(team, extras, wkts_fell)
