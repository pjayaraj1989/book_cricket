from helper import*
from test_data import*

def Error_Exit(msg):
    print("Error: " + msg)
    exit(0)

def GetMatchInfo():
    match=None
    teams=team_names
    overs=input('Select overs\n')
    overs=int(overs)
    if overs > 50 or overs <= 0: Error_Exit('Invalid overs')    
    
    t1=input('Select teams from : {0}\n'.format('/'.join(teams)))
    if t1 not in teams: Error_Exit('Invalid team')
    else:
        print ('Selected ' + t1)
        teams.remove(t1)
        t2=input('Select teams from : {0}\n'.format('/'.join(teams)))
        if not t2 in teams: Error_Exit('Invalid team')
        else:   print('Selected {0} and {1}'.format(t1,t2))
    #find teams from user input
    for t in list_of_teams:
        if t.name == t1:    team1=t
        if t.name == t2:    team2=t
    match=Match(team1=team1, team2=team2, overs=overs, result=None)
    return match

def CalculateTotal(team):
    total=0
    for player in team.team_array:
        total += player.runs
    total += team.extras
    return total

def CalculateResult(team1, team2):
    result = Result(team1=team1, team2=team2)
    #see who won
    loser=None
    if team1.total_score == team2.total_score:
        result.winner=None
        result.result_str="Match Tied"
    elif team1.total_score > team2.total_score:
        result.winner=team1
        loser=team2
        result.result_str="{0} won".format(team1.name)
    elif team2.total_score > team1.total_score:
        result.winner=team2
        loser=team1
        result.result_str="{0} won".format(team2.name)
    else:
        None
    if result.winner is not None:
        win_margin = 0
        #if batting first, simply get diff between total runs
        #else get how many wkts remaining
        if result.winner.batting_second == True:
            win_margin = 10 - result.winner.wickets_fell
            if win_margin is not 0:
                result.result_str += " by {0} wickets".format(str(win_margin))
        elif result.winner.batting_second == False:
            win_margin = abs(result.winner.total_score - loser.total_score)
            if win_margin is not 0:
                result.result_str += " by {0} runs".format(str(win_margin))
    return result

def PairFaceBall(pair, run):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:   Error_Exit("Error! both cant be on strike!")  
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    if ind is 0:    alt_ind=1
    elif ind is 1:  alt_ind=0        
    pair[ind].runs += run
    pair[ind].balls += 1
    print("On strike: {0} on {1}({2})".format(pair[ind].name, str(pair[ind].runs), str(pair[ind].balls)))        
    #now if runs is 1/3
    if (run % 2 != 0):
        pair[ind].onstrike = False
        pair[alt_ind].onstrike = True
    return pair

def UpdateScore(team, extras, wkts_fell, balls):
    total_runs=0
    for p in team.team_array:
        total_runs += p.runs        
    total_runs += extras.runs
    #calculate total
    team.total_score=total_runs
    team.total_balls=balls

def DisplayScore(team):
    for p in team.team_array:
        if p.status is True:
            print("{0} : {1}* ( {2} )".format(p.name, str(p.runs), str(p.balls)))
        else:
            print("{0} : {1} ( {2} )".format(p.name, str(p.runs), str(p.balls)))
    print ("Extras: " + str(team.extras))
    #calculate total
    total=CalculateTotal(team)
    print('{0} {1}/{2} ({3})'.format(team.name, str(total), str(team.wickets_fell), str(team.total_balls)))

def BatsmanOut(pair):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:
        Error_Exit("Error! both cant be on strike!")
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    if ind is 0:    alt_ind=1
    elif ind is 1:  alt_ind=0
    #bastman dismissed
    player_on_strike.status = False
    player_on_strike.balls += 1
    return pair

def Ball(run, pair, bowler, batting_team, bowling_team):
    #get who is on strike
    import random
    fielder=random.choice(bowling_team.team_array)
    on_strike = next((x for x in pair if x.onstrike == True), None)
    #if out
    if run is -1:
            bowler.wkts += 1
            bowler.balls_bowled += 1
            batting_team.wickets_fell += 1
            batting_team.total_balls += 1
            pair=BatsmanOut(pair)
            print("OUT!")
            print ("Total wkts fell " + str(batting_team.wickets_fell))            
            player_dismissed = next((x for x in pair if x.status == False), None)
            print ("Player dismissed " + player_dismissed.name)
            if batting_team.wickets_fell < 10:
                ind=pair.index(player_dismissed)
                pair[ind] = batting_team.team_array[batting_team.wickets_fell + 1]
                pair[ind].onstrike=True
                print ("New Batsman: " + pair[ind].name)        
    else:
            print ("Run: " + str(run)) 
            bowler.balls_bowled += 1
            bowler.runs_given += run
            PairFaceBall(pair, run)
            batting_team.total_balls += 1

def Chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def Play(batting_team, bowling_team, pair, total_balls):
    import random
    run_array = [-1,0,0,0,0,0,1,1,1,1,1,1,1,1,2,3,4,5,]
    bowlers = [plr for plr in bowling_team.team_array if plr.attr.bowling > 5]
    max_balls = total_balls / 5
    #bowl one over, then switch bowler
    overs=Chunks(range(1,total_balls+1), 6)
    #now run for each over
    for over in overs:
        if batting_team.wickets_fell == 10:
            print("All out")
            break
        bowler = random.choice(bowlers)
        print ("New Bowler: " + bowler.name)
        #now with this bowler, do an over
        for ball in over:
            player_on_strike = next((x for x in pair if x.onstrike == True), None)
            print ('Ball {0}, {1} to {2}'.format(str(ball), bowler.name, player_on_strike.name))
            run = random.choice(run_array)
            if run is 5:
                ball = ball - 1
                print ("Wide")
                bowler.runs_given += 1
                batting_team.extras += 1
            Ball(run, pair, bowler, batting_team, bowling_team)
        print("Bowler stat: " + bowler.name  + " balls: " + str(bowler.balls_bowled) + " Runs: " + str(bowler.runs_given) + " wickets: " + str(bowler.wkts))
        #rotate strike after an over
        player_on_strike = next((x for x in pair if x.onstrike == True), None)
        ind=pair.index(player_on_strike)
        if ind is 0:    alt_ind=1
        elif ind is 1:  alt_ind=0    
        pair[ind].onstrike = False
        pair[alt_ind].onstrike = True
    
    DisplayScore(batting_team)    
    for bowler in bowlers:
        print ("{0}\t{1}\t{2}\t{3}".format(bowler.name, str(bowler.balls_bowled), str(bowler.runs_given), str(bowler.wkts)))
        
