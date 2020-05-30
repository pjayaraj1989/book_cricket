
from data.test_data import*
from data.resources import*
from data.commentary import*
from data.players import *
from colorama import Fore,Style
from functions.utilities import *

#get match info
def GetMatchInfo(team_keys):
    match=None
    #get venue randomly
    #check venues are valid run probs
    for venue in resources.match_venues:
        if sum(venue.run_prob) != 1:
            Error_Exit("Error in venue! " + venue.name + " " + str(sum(venue.run_prob)))
    venue=Randomize(resources.match_venues)
    intro=Randomize(commentary.intro_dialogues)
    import random
    commentator = random.sample(set(resources.commentators), 2)
    umpire = Randomize(resources.umpires)
    
    teams=team_keys

    #welcome text
    PrintInColor(commentary.intro_game, Style.BRIGHT)

    overs=input('Select overs\n')
    overs=int(overs)
    if overs > 50 or overs <= 0: Error_Exit('Invalid overs') 
    #has to be a multiple of 5
    if overs%5 != 0:    Error_Exit('Overs should be a multiple of 5')

    #max overs alloted for each bowler
    bowler_max_overs = overs / 5

    #input teams
    t1=input('Select your team from : {0}\n'.format('/'.join(teams)))    
    t1=t1.upper()
    if t1 not in teams: Error_Exit('Invalid team')
    else:
        print ('Selected ' + t1)
        teams.remove(t1)
        t2=input('Select opponent team from : {0}\n'.format('/'.join(teams)))
        t2=t2.upper()
        if not t2 in teams: Error_Exit('Invalid team')
        else:   print('Selected {0} and {1}'.format(t1,t2))
    #find teams from user input
    for t in list_of_teams:
        if t.key == t1:    team1=t
        if t.key == t2:    team2=t
    match=Match(team1=team1, team2=team2, overs=overs, result=None)
    PrintInColor('{4}, {0}, for the exciting {1} over match between {2} and {3}'.format(venue.name,
                                                        str(overs),
                                                        team1.name,
                                                        team2.name,
                                                       intro), Fore.CYAN)
    print ('In the commentary box, myself {0} with {1}'.format(commentator[0],commentator[1]))
    print ('Umpire: {0}'.format(umpire))
    input('press enter to continue..')
    match.venue = venue
    match.umpire = umpire
    match.bowler_max_overs = bowler_max_overs

    #Want to skip balls?
    opt = input('Do you want to play only highlights? Choose y for highlights, n for full match')
    if opt.lower() == 'y':
        match.autoplay=True
    return match

#toss
def Toss (match):
    print('Toss..')
    if match.team1.captain is None or match.team2.captain is None:
        Error_Exit('No captains assigned!')
    print ('We have the captains {0}({1}) and {2}({3}) in the middle'.format(match.team1.captain.name,
                                                                            match.team1.name,
                                                                        match.team2.captain.name,
                                                                        match.team2.name))
    #assign captain attribute to the players
    match.team1.captain.attr.iscaptain = True
    match.team2.captain.attr.iscaptain = True

    print ('{0} is gonna flip the coin'.format(match.team2.captain.name))
    call=input('{0}, Heads or tails? 1.Heads 2.Tails\n'.format(match.team1.captain.name))
    if call == '' or None:
        Error_Exit("Invalid choice!")
    call=int(call)
    coin=Randomize([1,2])
    coin=int(coin)
    if coin == call:
        PrintInColor('{0} won the toss, batting first'.format(match.team1.captain.name), match.team1.color)
        match.team1.batting_second=False
        match.team2.batting_second=True
    else:
        PrintInColor('{0} won the toss, batting first'.format(match.team2.captain.name), match.team2.color)
        match.team2.batting_second=False
        match.team1.batting_second=True
    #now find out who is batting first
    batting_first = next((x for x in [match.team1, match.team2] if x.batting_second == False), None)
    batting_second = next((x for x in [match.team1, match.team2] if x.batting_second == True), None)

    match.batting_first = batting_first
    match.batting_second = batting_second
    return match

#validate teams
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
        if len(bowlers) < 6:
            Error_Exit('Team {0} should have 6 bowlers in the playing XI'.format(t.name) )
        else:
            t.bowlers = bowlers
            #assign max overs for bowlers
            for bowler in t.bowlers:
                bowler.max_overs = match.bowler_max_overs
    #ensure no common members in the teams
    common_players=list(set(match.team1.team_array).intersection(match.team2.team_array))
    if common_players != []:
        Error_Exit("Common players in teams found! : {0}".format(','.join([p.name for p in common_players])))
    PrintInColor('Validated teams', Style.BRIGHT)

#calculate match result
def CalculateResult(match):
    team1=match.team1
    team2=match.team2
    bowlers_t1=match.team1.bowlers
    bowlers_t2=match.team2.bowlers

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
            if win_margin != 0:
                result.result_str += " by {0} wickets".format(str(win_margin))
        elif result.winner.batting_second == False:
            win_margin = abs(result.winner.total_score - loser.total_score)
            if win_margin != 0:
                result.result_str += " by {0} runs".format(str(win_margin))
    #only bowlers who bowled
    bowlers_list = bowlers_t1 + bowlers_t2
    result=FindBestPlayers(result, bowlers_list)
    return result

#find best player
def FindBestPlayers(result, bowlers_list):
    total_players = result.team1.team_array + result.team2.team_array
    #find best batsman
    most_runs = sorted(total_players, key=lambda x: x.runs, reverse=True)
    if len(most_runs) >= 3:
        most_runs = most_runs[:3]    #we need only top 3 scorers
    result.most_runs = most_runs
    
    #find most wkts
    most_wkts = sorted(bowlers_list, key=lambda x: x.wkts, reverse=True)
    if len(most_wkts) >= 3:
        most_wkts = most_wkts[:3]    #we need only top 3 scorers
    result.most_wkts = most_wkts

    #find best eco bowler
    best_eco = sorted(bowlers_list, key=lambda x: x.eco, reverse=False)
    if len(best_eco) >= 3:
        best_eco = best_eco[:3]    #we need only top 3 scorers
    result.besteco = best_eco
    return result

#Man of the match
def FindPlayerOfTheMatch(match):
    #find which team won
    from operator import attrgetter
    team_won = max([match.team1,match.team2], key=attrgetter('total_score'))
    team_lost = min([match.team1,match.team2], key=attrgetter('total_score'))    
    best_player = None
    #if scores tied, select randomly
    if team_won.total_score == team_lost.total_score:
        best_player = max(team_won.team_array, key=attrgetter('runs'))
        comment_to_print = 'took {0} ({1})'.format(str(best_player.runs), str(best_player.balls))
    #check if win margin is >50% , if so, give credit to bowlers, else batsmen
    elif (float(team_won.total_score / team_lost.total_score)  >= 1.6):
        best_player = max(team_won.team_array, key=attrgetter('wkts'))
        comment_to_print = 'took {0} wkts'.format(str(best_player.wkts))
    else:
        best_player = max(team_won.team_array, key=attrgetter('runs'))
        comment_to_print = 'took {0} ({1})'.format(str(best_player.runs), str(best_player.balls))

    match.result.mom = best_player
    PrintInColor("Player of the match: {0}: {1}".format(best_player.name, comment_to_print), team_won.color)

#a pair face a delivery
def PairFaceBall(pair, run):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:   Error_Exit("Error! both cant be on strike!")  
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    if ind == 0:    alt_ind=1
    elif ind == 1:  alt_ind=0        
    pair[ind].runs += run
    pair[ind].balls += 1
    #now if runs is 1/3
    if (run % 2 != 0):
        pair[ind].onstrike = False
        pair[alt_ind].onstrike = True
    return pair

#calculate required rr at a point
def GetRequiredRate(totalovers, team):
    nrr=0.0
    #if chasing, calc net nrr
    balls_remaining=totalovers*6 - team.total_balls
    overs_remaining=BallsToOvers(balls_remaining)
    towin = team.target - team.total_score
    nrr = float(towin / overs_remaining)
    nrr = round(nrr,2)
    return nrr

#batting summary - scoreboard
def DisplayScore(team):
    ch='-'
    print(ch*45)
    PrintInColor(ch*15 + 'Batting Summary' + ch*15, team.color)
    print (ch*45)
    for p in team.team_array:
        name = p.name
        if p.attr.iscaptain == True:    name = name + '(c)'
        if p.attr.iskeeper == True: name = name + '(wk)'
        if p.status is True:    #* if not out
            if p.balls == 0 and p.runs == 0:
                print("{0}\tDNB".format(name))
            else:
                print ('{0}\t{1}\t{2}* ({3})'.format(name, "not out", str(p.runs), str(p.balls)))
        else:
            print ('{0}\t{1}\t{2} ({3})'.format(name, p.dismissal, str(p.runs), str(p.balls)))
    print ("Extras: " + str(team.extras))
    print (' ')
    PrintInColor('{0} {1}/{2} from ({3} overs)'.format(team.name.upper(), str(team.total_score), str(team.wickets_fell), str(BallsToOvers(team.total_balls))), team.color)
    #show FOW
    if team.wickets_fell != 0:
        PrintInColor('FOW:', Style.BRIGHT)
        #get fow_array
        fow_array = []
        for f in team.fow:
            fow_array.append('{0}/{1} {2}({3})'.format(str(f.runs),
                                                       str(f.wkt),
                                                       f.player_dismissed.name,
                                                      str(BallsToOvers(f.total_balls))))
        fow_str = ', '.join(fow_array)
        PrintInColor(fow_str, team.color)
    #partnerships
    PrintInColor("Partnerships:", Style.BRIGHT)
    for p in team.partnerships:
        print('{0} - {1} :\t{2}'.format(p.batsman_onstrike.name, p.batsman_dismissed.name, str(p.runs)))

    print (ch*45)

#match summary
def MatchSummary(match):
    result = match.result
    PrintInColor('-'*10 + 'Match Summary' + '-'*10, Style.BRIGHT)
    print('{0} vs {1}, at {2}'.format(result.team1.name, result.team2.name, match.venue.name))
    print(result.team1.name + " " +
          str(result.team1.total_score) + "/" +
          str(result.team1.wickets_fell) + "(" +
          str(BallsToOvers(result.team1.total_balls)) + ")")
    #see who all bowled
    bowlers1 = [plr for plr in result.team1.team_array if plr.attr.bowling >= 6]
    bowlers2 = [plr for plr in result.team2.team_array if plr.attr.bowling >= 6]
    #print first three top scorers
    most_runs = sorted(result.team1.team_array, key=lambda x: x.runs, reverse=True)
    most_runs = most_runs[:2]
    best_bowlers = sorted(bowlers2, key=lambda x: x.wkts, reverse=True)
    best_bowlers = best_bowlers[:2]
    for x in range(2):
        if most_runs[x].status == True: runs = str(most_runs[x].runs) + '*'
        else:   runs = str(most_runs[x].runs)
        PrintInColor('{0} {1} ({2})\t{3} {4}/{5}'.format(most_runs[x].name, most_runs[x].runs, most_runs[x].balls,
                                                              best_bowlers[x].name, best_bowlers[x].runs_given, best_bowlers[x].wkts),
                        Style.BRIGHT)

    print(result.team2.name + " " +
          str(result.team2.total_score) + "/" +
          str(result.team2.wickets_fell) + "(" +
          str(BallsToOvers(result.team2.total_balls)) + ")")
    most_runs = sorted(result.team2.team_array, key=lambda x: x.runs, reverse=True)
    most_runs = most_runs[:2]
    best_bowlers = sorted(bowlers1, key=lambda x: x.wkts, reverse=True)
    best_bowlers = best_bowlers[:2]
    for x in range(2):
        if most_runs[x].status == True: runs = str(most_runs[x].runs) + '*'
        else:   runs = str(most_runs[x].runs)
        PrintInColor('{0} {1} ({2})\t{3} {4}/{5}'.format(most_runs[x].name, runs, most_runs[x].balls,
                                                              best_bowlers[x].name, best_bowlers[x].runs_given, best_bowlers[x].wkts),
                        Style.BRIGHT)
    print('-' * 43)
    input('Press any key to exit..')

#batsman out
def BatsmanOut(pair, dismissal):
    #find out who is on strike
    if pair[0].onstrike is True and pair[1].onstrike is True:
        Error_Exit("Error! both cant be on strike!")
    player_on_strike = next((x for x in pair if x.onstrike == True), None)
    ind=pair.index(player_on_strike)
    if ind == 0:    alt_ind=1
    elif ind == 1:  alt_ind=0
    #bastman dismissed
    pair[ind].status = False
    pair[ind].balls += 1
    pair[ind].strikerate = float((pair[ind].runs / pair[ind].balls)*100)
    pair[ind].strikerate = round(pair[ind].strikerate, 2)
    #update dismissal mode
    pair[ind].dismissal = dismissal
    return pair

#randomly select a mode of dismissals
def GenerateDismissal(bowler, bowling_team):
    dismissal_str=None
    keeper = next((x for x in bowling_team.team_array if x.attr.iskeeper == True), None)
    #now get a list without keeper and bolwer
    fielders = [x for x in bowling_team.team_array if x != bowler and x != keeper]
    fielder=Randomize(fielders)

    #list of mode of dismissals
    #stumped only for a spinner
    if bowler.attr.isspinner == True:
        dismissal_types = ['c','st','runout','lbw','b', 'c&b']
    else:
        dismissal_types = ['c','runout','lbw','b','c&b']
    dismissal=Randomize(dismissal_types)
    if dismissal == 'lbw' or dismissal == 'b':
        dismissal_str = '{0} {1}'.format(dismissal,bowler.name)
    elif dismissal == 'c&b':
        dismissal_str = '{0} {1}'.format(dismissal, bowler.name)
    elif dismissal == 'st':
        dismissal_str = 'st {0} b {1}'.format(keeper.name, bowler.name)
    elif dismissal == 'c':
        fielders = fielders + [keeper]
        fielder=Randomize(fielders)
        dismissal_str = '{0} {1} b {2}'.format(dismissal, fielder.name, bowler.name)
    elif dismissal == 'runout':
        fielder=Randomize(fielders)
        dismissal_str = 'runout {0}'.format(fielder.name)
    else:
        None
    return dismissal_str

#display temporary stat
def ShowHighlights(batting_team):
    PrintInColor('{0} {1} / {2} ({3} Overs)'.format(batting_team.name,
                                               str(batting_team.total_score), 
                                               str(batting_team.wickets_fell), 
                                               str( BallsToOvers(batting_team.total_balls))), Style.BRIGHT)

#check for N consecutive elements in a list
def CheckForConsecutiveBalls(bowler, element):
    result=False
    #check array bowler.ball_history[] without extras!
    arr=[x for x in bowler.ball_history if x != 'WD']
    total_balls_bowled = len(arr)
    for i in range(2, total_balls_bowled):
        if arr[i] == arr[i-1] == arr[i-2] == element:
            result = True
            break
    return result

#play a ball
def Ball(run, pair, bowler, batting_team, bowling_team):
    #get keeper
    keeper = next((x for x in bowling_team.team_array if x.attr.iskeeper == True), None)
    #get who is on strike   
    on_strike = next((x for x in pair if x.onstrike == True), None)
    #if out
    if run == -1:
            dismissal = GenerateDismissal(bowler, bowling_team)
            if not 'runout' in dismissal:
                # add this to bowlers history
                bowler.ball_history.append('Wkt')
                bowler.wkts += 1
            elif 'runout' in dismissal:
                bowler.ball_history.append('RO')

            #update wkts, balls, etc
            bowler.balls_bowled += 1
            batting_team.wickets_fell += 1
            batting_team.total_balls += 1

            pair=BatsmanOut(pair, dismissal)

            player_dismissed = next((x for x in pair if x.status == False), None)
            #check if player dismissed is captain
            if player_dismissed.attr.iscaptain == True:
                PrintInColor(Randomize(commentary.commentary_captain_out), bowling_team.color)

            player_onstrike = next((x for x in pair if x.status == True), None)
            PrintInColor ("OUT ! {0} {1} {2} ({3}) SR: {4}".format(player_dismissed.name, 
                                               player_dismissed.dismissal, 
                                               str(player_dismissed.runs), 
                                               str(player_dismissed.balls),
                                               str(player_dismissed.strikerate)), Fore.RED)

            #detect a hat-trick!
            isHattrick = CheckForConsecutiveBalls(bowler, 'Wkt')
            if isHattrick == True:
                bowler.hattricks += 1
                PrintInColor(Randomize(commentary.commentary_hattrick), bowling_team.color)

            #check if bowler got 5 wkts
            if bowler.wkts == 5:
                PrintInColor('Thats 5 Wickets for {0} !'.format(bowler.name), bowling_team.color)
                PrintInColor(Randomize(commentary.commentary_fifer), bowling_team.color)
                input('press enter to continue..')

            #update fall of wicket
            fow_info = Fow(wkt=batting_team.wickets_fell,
                           runs=batting_team.total_score,
                           total_balls=batting_team.total_balls,
                           player_onstrike=player_onstrike,
                           player_dismissed=player_dismissed,)
            batting_team.fow.append(fow_info)

            #check if 5 wkts gone
            if batting_team.wickets_fell == 5:
                PrintInColor(Randomize(commentary.commentary_five_down), bowling_team.color)

            #get partnership details
            #1st wkt partnership
            if batting_team.wickets_fell == 1:
                partnership_runs = batting_team.fow[0].runs
            else:
                partnership_runs = batting_team.fow[batting_team.wickets_fell-1].runs - batting_team.fow[batting_team.wickets_fell - 2].runs

            partnership = Partnership(batsman_dismissed=fow_info.player_dismissed,
                                      batsman_onstrike=fow_info.player_onstrike,
                                      runs=partnership_runs)
            #update batting team partnership details
            batting_team.partnerships.append(partnership)

            #commentary            
            if 'runout' in dismissal:
                comment = Randomize(commentary.commentary_runout)
            elif 'st ' in dismissal:
                comment = Randomize(commentary.commentary_stumped)
            # if bowler is the catcher
            elif 'c&b' in dismissal:
                comment = Randomize(commentary.commentary_return_catch)
            elif 'c ' in dismissal and ' b ' in dismissal:
                #see if the catcher is the keeper
                if keeper.name in dismissal:
                    comment = Randomize(commentary.commentary_keeper_catch)
                else:
                    comment = Randomize(commentary.commentary_caught)
            elif 'b ' or 'lbw' in dismissal:
                #reverse swing if > 30 overs
                if 150 <= batting_team.total_balls <= 240 and bowler.attr.isspinner==False:
                    PrintInColor(Randomize(commentary.commentary_reverse), Style.BRIGHT)
                #initial swing
                if batting_team.total_balls < 24 and bowler.attr.isspinner==False:
                    PrintInColor(Randomize(commentary.commentary_swing), Style.BRIGHT)
                #turn
                if bowler.attr.isspinner==True:
                    PrintInColor(Randomize(commentary.commentary_turn), Style.BRIGHT)
                #if lbw
                if 'lbw' in dismissal:  comment = Randomize(commentary.commentary_lbw)
                else:   comment = Randomize(commentary.commentary_bowled)
            else:
                None

            #comment dismissal
            PrintInColor(comment, Style.BRIGHT)

            #if its a great knock, say this
            if player_dismissed.runs > 50:
                PrintInColor(Randomize(commentary.commentary_out_fifty), Style.BRIGHT)
            #if duck
            if player_dismissed.runs == 0:
                PrintInColor(Randomize(commentary.commentary_out_duck), Style.BRIGHT)
            #out first ball
            if player_dismissed.balls == 1:
                PrintInColor (Randomize(commentary.commentary_out_first_ball), Style.BRIGHT)
            # if partnership is great
            if partnership.runs > 50:
                PrintInColor(Randomize(commentary.commentary_partnership_milestone), Style.BRIGHT)

            # calculate the situation
            towin = batting_team.target - batting_team.total_score
            if batting_team.batting_second and batting_team.wickets_fell >= 8:
                PrintInColor(Randomize(commentary.commentary_goingtolose), Style.BRIGHT)

            #show score
            ShowHighlights(batting_team)
            
            input('press enter to continue..')

            if batting_team.wickets_fell < 10:
                ind=pair.index(player_dismissed)
                pair[ind] = batting_team.team_array[batting_team.wickets_fell + 1]
                pair[ind].onstrike=True
                PrintInColor ("New Batsman: " + pair[ind].name, batting_team.color)        
    else:
            #appropriate commentary for 4s and 6s
            if run == 4:
                field = Randomize(resources.fields[4])
                comment=Randomize(commentary.commentary_four)
                PrintInColor (field + " FOUR! " + comment, Fore.GREEN)
                #check if first ball hit for a boundary
                if on_strike.balls == 0:
                    PrintInColor(Randomize(commentary.commentary_firstball_four), Fore.GREEN)
                if CheckForConsecutiveBalls(bowler, 4) == True:
                    PrintInColor(Randomize(commentary.commentary_in_a_row), Fore.GREEN)
            elif run == 6:
                #check uf furst ball is hit
                if on_strike.balls == 0:
                    PrintInColor(Randomize(commentary.commentary_firstball_six), Fore.GREEN)
                if CheckForConsecutiveBalls(bowler, 6) == True:
                    PrintInColor(Randomize(commentary.commentary_in_a_row), Fore.GREEN)
                field = Randomize(resources.fields[6])
                comment=Randomize(commentary.commentary_six)
                PrintInColor (field + " SIX! " + comment, Fore.GREEN)
            elif run == 0:
                comment=Randomize(commentary.commentary_dot_ball)
                print ('{0}, No Run'.format(comment))
            else:
                field = Randomize(resources.fields["ground_shot"])
                comment=Randomize(commentary.commentary_ground_shot)
                print ('{0},{1} {2} run'.format(comment, field, str(run)))

            bowler.balls_bowled += 1
            bowler.runs_given += run
            PairFaceBall(pair, run)
            batting_team.total_balls += 1
            batting_team.total_score += run

            # add this to bowlers history
            bowler.ball_history.append(run)

            #check for milestones
            CheckMilestone(pair, batting_team)

#print bowlers stats
def DisplayBowlingStats(team):
    bowlers=team.bowlers
    #here, remove the bowlers who didnt bowl
    bowlers_updated=[]
    char='-'
    print (char*45)
    PrintInColor (char*15 + '-Bowling Stats-' + char*15, Style.BRIGHT)
    print (char*45)
    eco=0.0
    for bowler in bowlers:
        #dont print if he hasnt bowled
        if bowler.balls_bowled != 0:
            bowlers_updated.append(bowler)
            balls=bowler.balls_bowled
            overs=BallsToOvers(balls)
            eco = float(bowler.runs_given / overs)
            eco = round(eco,2)
            bowler.eco = eco
            print ("{0}\tOvr:{1} Mdn:{5} {2}/{3} Eco: {4}".format(bowler.name,
                                           str(overs),
                                           str(bowler.runs_given), 
                                           str(bowler.wkts),
                                           str(bowler.eco),
                                           str(bowler.maidens)))
    print (char*45)
    input('press enter to continue..')
    team.bowlers = bowlers_updated

#update last partnership
def UpdateLastPartnership(batting_team,pair):
    # update last partnership
    if batting_team.wickets_fell > 0:
        last_fow = batting_team.fow[-1].runs
        last_partnership_runs = batting_team.total_score - last_fow
        last_partnership = Partnership(batsman_dismissed=pair[0],
                                       batsman_onstrike=pair[1],
                                       runs=last_partnership_runs)
        batting_team.partnerships.append(last_partnership)
    #if no wkt fell
    elif batting_team.wickets_fell == 0:
        last_partnership_runs = batting_team.total_score
        last_partnership = Partnership(batsman_dismissed=pair[0],
                                       batsman_onstrike=pair[1],
                                       runs=last_partnership_runs)
        batting_team.partnerships.append(last_partnership)
    else:
        None

#play an over
def PlayOver(over, overs, batting_team, bowling_team, pair, bowlers, match):
    match_status = True
    import random
    #if first over, opening bowler does it
    if bowling_team.last_bowler is None:
        bowler = next((x for x in bowlers if x.attr.isopeningbowler == True), None)
    else:
        if bowling_team.last_bowler in bowlers:
            #bowling list except the bowler who did last over and bowlers who finished their allotted overs
            temp = [x for x in bowlers if (x != bowling_team.last_bowler and x.balls_bowled < x.max_overs*6)]

        #if autoplay, let bowlers be chosen randomly
        if match.autoplay == True:
            bowler = Randomize(temp)
        #esle pick bowler
        else:
            choice = input('Choose next bowler from: {0} [Press Enter to auto-select]'.format(' / '.join([x.name for x in temp])))            
            bowler = next((x for x in temp if choice.lower() in x.name.lower()), None)
            if bowler is None:
                bowler = Randomize(temp)

    PrintInColor("New bowler: {0} {1}/{2} ({3})".format(bowler.name,
                                                        str(bowler.runs_given),
                                                        str(bowler.wkts),
                                                        str(BallsToOvers(bowler.balls_bowled))),
                                bowling_team.color)

    ball=1
    bowling_team.last_bowler=bowler
    ismaiden=True
    while(ball <= 6):
        #towards the death overs, show a highlights
        towin=batting_team.target - batting_team.total_score 
        #calculate if score is close        
        if batting_team.batting_second and towin <= 20:
            ShowHighlights(batting_team)
            PrintInColor ('To win: {0} from {1}'.format(str(towin),
                                                    str(overs*6 - batting_team.total_balls)), Style.BRIGHT)
            input('press enter to continue...')

        print ("Over: {0}.{1}".format(str(over),str(ball)))
        player_on_strike = next((x for x in pair if x.onstrike == True), None)
        print ('{0} to {1}'.format(bowler.name, player_on_strike.name))
        if match.autoplay == True:
            import time
            time.sleep(2)
        else:
            input('press enter to continue..')

        #generate run
        #if odi
        if match.overs == 50:
            from numpy.random import choice
            run = choice([-1,0,1,2,3,4,5,6], 1, p=match.venue.run_prob, replace=False)[0]
        else:
            #t20
            run = Randomize(resources.runs_t20)

        #check if maiden or not
        if run != 0 or run != -1:
            ismaiden=False 
        #check if extra
        if run == 5:
            # add this to bowlers history
            bowler.ball_history.append('WD')
            ismaiden=False
            comment = Randomize(commentary.commentary_wide)
            PrintInColor ("WIDE...!", Style.BRIGHT)
            PrintInColor (comment, Style.BRIGHT)
            bowler.runs_given += 1
            batting_team.extras += 1
            batting_team.total_score += 1
        else:
            Ball(run, pair, bowler, batting_team, bowling_team)
            ball += 1
            # check if 1st innings over
            if batting_team.batting_second is False and batting_team.total_balls == (match.overs * 6):
                PrintInColor("End of innings", Style.BRIGHT)
                #update last partnership
                if batting_team.wickets_fell > 0:
                    last_fow = batting_team.fow[-1].runs
                    last_partnership_runs = batting_team.total_score - last_fow
                    last_partnership = Partnership(batsman_dismissed=pair[0],
                                          batsman_onstrike=pair[1],
                                          runs=last_partnership_runs)
                    batting_team.partnerships.append(last_partnership)
                input('press enter to continue')
                break

            #batting second
            # if chasing and lost
            if batting_team.batting_second is True and batting_team.total_balls >= (match.overs * 6):
                # update last partnership
                UpdateLastPartnership(batting_team, pair)
                match_status = False
                PrintInColor("End of innings", Style.BRIGHT)
                input('press enter to continue...')
                break

            # check if target achieved chasing
            if batting_team.batting_second is True and (batting_team.total_score >= batting_team.target):
                PrintInColor("Match won!", Fore.GREEN)
                match_status = False
                UpdateLastPartnership(batting_team, pair)
                input('press enter to continue...')
                break
            # if all out
            if batting_team.wickets_fell == 10:
                PrintInColor("All out!", Fore.RED)
                match_status = False
                input('press enter to continue...')
                break

    if ismaiden == True:
        bowler.maidens += 1
    return match_status

#check for milestones
def CheckMilestone(pair, batting_team):
    import random
    for p in pair:
        #first fifty
        if p.runs >= 50 and p.fifty == 0:
            comment=Randomize(commentary.commentary_milestone)
            p.fifty += 1
            PrintInColor("50 for {0}!".format(p.name), batting_team.color)
            #check if captain
            if p.attr.iscaptain == True:
                PrintInColor(Randomize(commentary.commentary_captain_leading), batting_team.color)
            PrintInColor(comment, batting_team.color)
            input('press enter to continue..')
        elif p.runs >= 100 and (p.fifty == 1 and p.hundred == 0):
            #after first fifty is done
            comment=Randomize(commentary.commentary_milestone)
            p.hundred += 1
            p.fifty += 1
            PrintInColor("100 for {0}!".format(p.name),  batting_team.color)
            #check if captain
            if p.attr.iscaptain == True:
                PrintInColor(Randomize(commentary.commentary_captain_leading), batting_team.color)
            PrintInColor(comment, batting_team.color)
            input('press enter to continue..')
        elif p.runs >= 200 and (p.hundred == 1):
            #after first fifty is done
            comment=Randomize(commentary.commentary_milestone)
            p.hundred += 1
            PrintInColor("200 for {0}! What a superman!".format(p.name),  batting_team.color)
            #check if captain
            if p.attr.iscaptain == True:
                PrintInColor(Randomize(commentary.commentary_captain_leading), batting_team.color)
            PrintInColor(comment, batting_team.color)
            input('press enter to continue..')
        else:
            None

#play!
def Play(match, batting_team, bowling_team, pair, bowlers):
    overs=match.overs
    if batting_team.batting_second is True:
        PrintInColor('Target for {0}: {1} from {2} overs'.format(batting_team.name,
                                                                 str(batting_team.target),
                                                                 str(overs)), batting_team.color)
    #now run for each over
    for over in range(0,overs):
        #show net rr required if batting second
        if batting_team.batting_second is True:
            nrr=GetRequiredRate(overs, batting_team)
            PrintInColor('Reqd Run Rate: {0} per over'.format(str(nrr)), Style.BRIGHT)

        #play an over      
        status=PlayOver(over, overs, batting_team, bowling_team, pair, bowlers, match)
        #show batting stats
        for p in pair:
            PrintInColor('{0} {1} ({2})'.format(p.name, str(p.runs), str(p.balls)), Style.BRIGHT)
        ShowHighlights(batting_team)
        if status is False:
            break
        #rotate strike after an over
        player_on_strike = next((x for x in pair if x.onstrike == True), None)
        ind=pair.index(player_on_strike)
        if ind == 0:    alt_ind=1
        elif ind == 1:  alt_ind=0    
        pair[ind].onstrike = False
        pair[alt_ind].onstrike = True  
