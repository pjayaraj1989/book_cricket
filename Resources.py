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

def PairFaceBall(pair, run, ball):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:   Error_Exit("Error! both cant be on strike!")  
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    if ind is 0:    alt_ind=1
    elif ind is 1:  alt_ind=0        
    pair[ind].runs += run
    pair[ind].balls += 1
    print("On strike: {0} on {1}({2})".format(pair[ind].name, str(pair[ind].runs), str(pair[ind].balls)))        
    #now if runs is 1/3, or if ball is a mul of 6 rotate strike
    if (run % 2 != 0) or (ball % 6 ==0):
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

def DisplayScore(team, extras, wkts_fell):
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
    team.wickets_fell = wkts_fell

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

def Play(team, extras, pair, num_of_balls, team2):
    team_list=team.team_array
    total_wkts = len(team_list)-1
    wkts_fell = 0
    
    #get opp bowlers if their bowling strength is >5
    fielding_team_members = [plr for plr in team2.team_array]
    bowlers = [plr for plr in team2.team_array if plr.attr.bowling > 5]    
    keeper = [plr for plr in team2.team_array if plr.attr.iskeeper==True] 
    
    for ball in range(1,num_of_balls+1):
        if team.batting_second is True and team.total_score > team.target:
            print ("Match won!")
            break
        #input()
        print("Ball: " + str(ball))
        if wkts_fell == total_wkts:
            print("All out!")
            break
        #this is the main guy who generates runs
        import random
        run_array = [-1,0,0,0,0,0,1,1,1,1,1,1,1,1,2,3,4,5,6]
        run = random.choice(run_array)
        #if run is 5, treat as a wide dont count ball, incr extras
        if run is 5:
            extras.runs += 1
            print("Wide, total extras: " + str(extras.runs))
        #-1 ==> out!
        elif run is -1:
            #randomly get bowler
            wicket_taker=random.choice(bowlers)
            catcher = random.choice(fielding_team_members)
            dismissal_mode=random.choice(['B','C','runout','LBW'])
            if dismissal_mode == 'C':
                dismissal = 'c {0} b {1}'.format(catcher.name, wicket_taker.name)
            elif dismissal_mode == 'B' or 'LBW':
                dismissal = '{0} {1}'.format(dismissal_mode,wicket_taker.name)
            else:
                dismissal = ' runout {0}'.format(random.choice(fielding_team_members))
                
            ball += 1
            pair=BatsmanOut(pair)
            player_dismissed = next((x for x in pair if x.status == False), None)
            ind=pair.index(player_dismissed)
            
            print("OUT! {0} {1} {2} ({3})".format(player_dismissed.name, 
                                dismissal, 
                                str(player_dismissed.runs),
                                str(player_dismissed.balls)))
            input()            
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
            
        UpdateScore(team, extras, wkts_fell, ball)
    #print scorecard
    DisplayScore(team, extras, wkts_fell)

def PrintResult(result):
    print("Match Summary")
    print(result.team1.name + " " + 
          str(result.team1.total_score) + "/" + 
          str(result.team1.wickets_fell) + "(" +
          str(result.team1.total_balls) + ")")
    print(result.team2.name + " " + 
          str(result.team2.total_score) + "/" + 
          str(result.team2.wickets_fell) + "(" +
          str(result.team2.total_balls) + ")")
    print(result.result_str)
