from helper import*
from test_data import*

def Error_Exit(msg):
    print("Error: " + msg)
    exit(0)

def GetMatchInfo(team_keys):
    match=None
    teams=team_keys
    overs=input('Select overs\n')
    overs=int(overs)
    if overs > 50 or overs <= 0: Error_Exit('Invalid overs')    
    
    t1=input('Select teams from : {0}\n'.format('/'.join(teams)))
    t1=t1.upper()
    if t1 not in teams: Error_Exit('Invalid team')
    else:
        print ('Selected ' + t1)
        teams.remove(t1)
        t2=input('Select teams from : {0}\n'.format('/'.join(teams)))
        t2=t2.upper()
        if not t2 in teams: Error_Exit('Invalid team')
        else:   print('Selected {0} and {1}'.format(t1,t2))
    #find teams from user input
    for t in list_of_teams:
        if t.key == t1:    team1=t
        if t.key == t2:    team2=t
    match=Match(team1=team1, team2=team2, overs=overs, result=None)
    return match

def ValidateMatchTeams(match):
    if match.team1 is None or match.team2 is None:
        Error_Exit('No teams found!')
    for t in [match.team1, match.team2]:
        #check if 11 players
        if len(t.team_array) != 11:
            Error_Exit('Only {0} members in team {1}'.format(len(t.team_array), t.name))
        #check if they have keeper
        if [plr for plr in t.team_array if plr.attr.iskeeper == True] is None or []:
            Error_Exit('No keeper found in team {0}'.format(t.name))
        #get bowlers must be at least 5 of them
        bowlers = [plr for plr in t.team_array if plr.attr.bowling >= 6]
        if len(bowlers) < 5:
            Error_Exit('Team {0} should have 5 bowlers in the playing XI'.format(t.name) )
        else:
            t.bowlers = bowlers
    print('Validated teams')

def CalculateResult(team1, team2, bowlers_t1, bowlers_t2):
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
    #calculate MOM and best bowler
    #onlt bowlers who bowled
    bowlers_list = bowlers_t1 + bowlers_t2
    result=FindBestPlayers(result, bowlers_list)
    return result

#find best player
def FindBestPlayers(result, bowlers_list):
    best_batter=None
    best_bowler=None
    best_eco_bowler=None
    total_players = result.team1.team_array + result.team2.team_array
    from operator import attrgetter
    #find best batsman
    best_batter = max(total_players, key=attrgetter('runs'))
    result.best_batsman = best_batter
    #find most wkts
    best_bowler = max(bowlers_list, key=attrgetter('wkts'))
    result.best_bowler = best_bowler
    #find best eco bowler
    best_eco_bowler = min(bowlers_list, key=attrgetter('eco'))
    result.besteco = best_eco_bowler
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
    #now if runs is 1/3
    if (run % 2 != 0):
        pair[ind].onstrike = False
        pair[alt_ind].onstrike = True
    return pair

#batting summary - scoreboard
def DisplayScore(team):
    ch='-'
    print(ch*45)
    print(ch*15 + 'Batting Summary' + ch*15)
    print (ch*45)
    for p in team.team_array:
        if p.status is True:    #* if not out
            if p.balls == 0 and p.runs == 0:
                print("{0}: DNB".format(p.name))
            else:
                print ('{0} {1} {2}* ({3})'.format(p.name, p.dismissal, str(p.runs), str(p.balls)))
        else:
            print ('{0} {1} {2} ({3})'.format(p.name, p.dismissal, str(p.runs), str(p.balls)))
    print ("Extras: " + str(team.extras))
    print (' ')
    print('{0} {1}/{2} ({3})'.format(team.name.upper(), str(team.total_score), str(team.wickets_fell), str(team.total_balls)))
    print (ch*45)

def PrintResult(result):
    print('-'*10 + 'Match Summary' + '-'*10)
    print(result.team1.name + " " + 
          str(result.team1.total_score) + "/" + 
          str(result.team1.wickets_fell) + "(" +
          str(result.team1.total_balls) + ")")
    print(result.team2.name + " " + 
          str(result.team2.total_score) + "/" + 
          str(result.team2.wickets_fell) + "(" +
          str(result.team2.total_balls) + ")")
    print(result.result_str)
    print ('Most runs: {0} {1} ({2})'.format(result.best_batsman.name,
                                        str(result.best_batsman.runs),
                                        str(result.best_batsman.balls)))
    print ('Best bowler: {0} {1}/{2}'.format(result.best_bowler.name,
                                        str(result.best_bowler.runs_given),
                                        str(result.best_bowler.wkts)))
    print ('Best economy: {0} {1}'.format(result.besteco.name,
                                        str(result.besteco.eco)))
    print('-'*43)

def BatsmanOut(pair, dismissal):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:
        Error_Exit("Error! both cant be on strike!")
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    if ind is 0:    alt_ind=1
    elif ind is 1:  alt_ind=0
    #bastman dismissed
    pair[ind].status = False
    pair[ind].balls += 1
    #update dismissal mode
    pair[ind].dismissal = dismissal
    return pair

#randomly select a mode of dismissals
def GenerateDismissal(bowler, bowling_team):
    dismissal_str=None
    keeper = next((x for x in bowling_team.team_array if x.attr.iskeeper == True), None)
    #now get a list without keeper and bolwer
    fielders = [x for x in bowling_team.team_array if x != bowler and x != keeper]
    import random
    fielder=random.choice(fielders)
    #list of mode of dismissals
    dismissal_types = ['c','st','runout','lbw','b']
    dismissal=random.choice(dismissal_types)
    if dismissal == 'lbw' or dismissal == 'b':
        dismissal_str = '{0} {1}'.format(dismissal,bowler.name)
    elif dismissal == 'st':
        dismissal_str = 'st {0} b {1}'.format(keeper.name, bowler.name)
    elif dismissal == 'c':
        fielders = fielders + [keeper]
        fielder=random.choice(fielders)
        dismissal_str = '{0} {1} b {2}'.format(dismissal, fielder.name, bowler.name)
    elif dismissal == 'runout':
        fielder=random.choice(fielders)
        dismissal_str = 'runout {0}'.format(fielder.name)
    else:
        None
    return dismissal_str

#display temporary stat
def ShowHighlights(batting_team):
    print('{0} {1} / {2} ({3})'.format(batting_team.name,
                                               str(batting_team.total_score), 
                                               str(batting_team.wickets_fell), 
                                               str(batting_team.total_balls)))
#play a ball
def Ball(run, pair, bowler, batting_team, bowling_team):    
    on_strike = next((x for x in pair if x.onstrike == True), None) 
    #if out
    if run is -1:
            dismissal = GenerateDismissal(bowler, bowling_team)
            if not 'runout' in dismissal:
                bowler.wkts += 1
            bowler.balls_bowled += 1
            batting_team.wickets_fell += 1
            batting_team.total_balls += 1
            pair=BatsmanOut(pair, dismissal)           
            player_dismissed = next((x for x in pair if x.status == False), None)
            print ("OUT ! {0} {1} {2} ({3})".format(player_dismissed.name, 
                                               player_dismissed.dismissal, 
                                               str(player_dismissed.runs), 
                                               str(player_dismissed.balls)))
            #commentary
            import random
            if 'runout' in dismissal:
                comment = random.choice(commentary_runout)
            elif 'st ' in dismissal:
                comment = random.choice(commentary_stumped)
            elif 'c ' in dismissal and ' b ' in dismissal:
                comment = random.choice(commentary_caught)
            elif 'lbw' in dismissal:
                comment = random.choice(commentary_lbw)
            elif 'b ' in dismissal:
                comment = random.choice(commentary_bowled)
            else:
                None

            if player_dismissed.balls is 1:
                print ('Out first ball!!')
            print (comment)

            #show score
            ShowHighlights(batting_team)
            
            input('press any key to continue..')

            if batting_team.wickets_fell < 10:
                ind=pair.index(player_dismissed)
                pair[ind] = batting_team.team_array[batting_team.wickets_fell + 1]
                pair[ind].onstrike=True
                print ("New Batsman: " + pair[ind].name)        
    else:
            #appropriate commentary for 4s and 6s
            import random
            field=random.choice(field_positions)
            if run == 4:
                comment=random.choice(commentary_big_shot)
                print (field + " FOUR! " + comment)
            elif run == 6:
                comment=random.choice(commentary_big_shot)
                print (field + " SIX! " + comment)
            elif run == 0:
                comment=random.choice(commentary_dot_ball)
                print ('{0}, No Run'.format(comment))
            else:
                comment=random.choice(commentary_ground_shot)
                print ('{0},{1} {2} run'.format(comment, field, str(run)))

            bowler.balls_bowled += 1
            bowler.runs_given += run
            PairFaceBall(pair, run)
            batting_team.total_balls += 1
            batting_team.total_score += run

#print bowlers stats
def DisplayBowlingStats(bowlers):
    #here, remove the bowlers who didnt bowl
    bowlers_updated=[]
    char='-'
    print (char*45)
    print (char*15 + '-Bowling Stats-' + char*15)
    print (char*45)
    eco=0.0
    for bowler in bowlers:
        #dont print if he hasnt bowled
        if bowler.balls_bowled is not 0:
            bowlers_updated.append(bowler)
            balls=bowler.balls_bowled
            overs=str(int(balls/6)) + '.' + str(balls%6)
            eco = float(bowler.runs_given / float(overs))
            eco = round(eco,2)
            bowler.eco = eco
            print ("{0} Overs:{1} Maidens:{5} Runs:{2} Wkts:{3} Eco: {4}".format(bowler.name, 
                                           overs, 
                                           str(bowler.runs_given), 
                                           str(bowler.wkts),
                                           str(bowler.eco),
                                           str(bowler.maidens)))
    print (char*45)
    return bowlers_updated

#play an over
def PlayOver(over, overs, batting_team, bowling_team, pair, bowlers):
    match_status = True
    import random
    if bowling_team.last_bowler is None:
        #if first over, opening bowler does it
        bowler = next((x for x in bowlers if x.attr.isopeningbowler == True), None)
    else:
        if bowling_team.last_bowler in bowlers:
            temp = [x for x in bowlers if x != bowling_team.last_bowler]
        bowler = random.choice(temp)
    print ("New Bowler: " + bowler.name)
    ball=1
    bowling_team.last_bowler=bowler
    ismaiden=True
    while(ball <= 6):
        #check if target achieved
        if batting_team.batting_second is True and (batting_team.total_score >= batting_team.target):
            print ("Match won!")
            match_status=False
            input('press any key to continue...')
            break
        if batting_team.wickets_fell == 10:
            print("All out!")
            match_status=False
            input ('press any key to continue...')
            break

        #towards the death overs, show a highlights
        towin=batting_team.target - batting_team.total_score 
        #calculate if score is close        
        if batting_team.batting_second and towin <= 20:
            ShowHighlights(batting_team)
            print ('To win: {0} from {1}'.format(str(towin),
                                                    str(overs*6 - batting_team.total_balls)))
            input('press any key to continue...')

        print ("Over: {0}.{1}".format(str(over),str(ball)))
        player_on_strike = next((x for x in pair if x.onstrike == True), None)
        print ('{0} to {1}'.format(bowler.name, player_on_strike.name))
        input('press any key to continue..')
        run = random.choice(run_array)
        #check if maiden or not
        if run is not 0 or -1:
            ismaiden=False 
        #check if extra
        if run is 5:
            ismaiden=False
            print ("WIDE...!")
            bowler.runs_given += 1
            batting_team.extras += 1
            batting_team.total_score += 1
        else:
            Ball(run, pair, bowler, batting_team, bowling_team)
            ball += 1
    if ismaiden == True:
        bowler.maidens += 1
    return match_status

#play!
def Play(batting_team, bowling_team, pair, overs, bowlers):
    if batting_team.batting_second is True:
        print('Target for {0}: {1} from {2} overs'.format(batting_team.name,
                                                                 str(batting_team.target),
                                                                 str(overs)))
    #now run for each over
    for over in range(0,overs):
        #play an over      
        status=PlayOver(over, overs, batting_team, bowling_team, pair, bowlers)
        #show batting stats
        for p in pair:
            print('{0} {1} ({2})'.format(p.name, str(p.runs), str(p.balls)))

        ShowHighlights(batting_team)

        if status is False:
            break
        #rotate strike after an over
        player_on_strike = next((x for x in pair if x.onstrike == True), None)
        ind=pair.index(player_on_strike)
        if ind is 0:    alt_ind=1
        elif ind is 1:  alt_ind=0    
        pair[ind].onstrike = False
        pair[alt_ind].onstrike = True  
