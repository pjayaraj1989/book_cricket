#routines to display scores, etc
#display temporary stats
from functions.utilities import PrintInColor, BallsToOvers, GetShortName, PrintListFormatted
from colorama import Style

#get current rate
def GetCurrentRate(team):
    crr = 0.0
    if team.total_balls > 0:
        crr = team.total_score / BallsToOvers(team.total_balls)
    crr = round(crr, 2)
    return crr

def GetRequiredRate(team):
    nrr=0.0
    #if chasing, calc net nrr
    balls_remaining=(team.total_overs)*6 - team.total_balls
    if balls_remaining > 0:
        overs_remaining=BallsToOvers(balls_remaining)
        towin = team.target - team.total_score
        nrr = float(towin / overs_remaining)
        nrr = round(nrr, 2)
    return nrr

def ShowHighlights(batting_team):
    reqd_rate=0.0
    crr = GetCurrentRate(batting_team)
    if batting_team.batting_second == True:
        if batting_team.total_balls <= batting_team.total_overs * 6 or batting_team.total_score <= batting_team.target:
            reqd_rate = GetRequiredRate(batting_team)
    #default msg
    msg = '{0} {1} / {2} ({3} Overs)'.format(batting_team.name,
                                               str(batting_team.total_score),
                                               str(batting_team.wickets_fell),
                                               str(BallsToOvers(batting_team.total_balls)))
    #if overs done, dont print Runrate
    if batting_team.total_balls <= batting_team.total_overs*6:
        msg += ', Current RR: {0}'.format(str(crr))
    #if second innings
    if batting_team.batting_second == True:
        #if overs done, dont print this
        if batting_team.total_balls <= batting_team.total_overs*6 or batting_team.total_score <= batting_team.target:
            msg += ", Reqd. Rate: {0}".format(str(reqd_rate))
    PrintInColor(msg, Style.BRIGHT)

#batting summary - scoreboard
def DisplayScore(match, team):
    logger=match.logger
    ch = '-'
    print(ch*45)
    logger.info(ch*45)

    msg = ch*15 + 'Batting Summary' + ch*15
    PrintInColor(msg, team.color)
    logger.info(msg)
    print(ch*45)
    logger.info(ch*45)

    #this should be a nested list of 3 elements
    data_to_print = []
    for p in team.team_array:
        name = GetShortName(p.name)
        if p.attr.iscaptain == True:    name = name + '(c)'
        if p.attr.iskeeper == True: name = name + '(wk)'
        if p.status is True:    #* if not out
            if p.onfield == False:
                data_to_print.append([name, 'DNB', ''])
            else:
                data_to_print.append([name, "not out", "{0}* ({1})".format(str(p.runs), str(p.balls))])
        else:
            data_to_print.append([name, p.dismissal, "{0} ({1})".format(str(p.runs), str(p.balls))])

    PrintListFormatted(data_to_print, 0.01, logger)

    msg = "Extras: " + str(team.extras)
    print(msg)
    logger.info (msg)
    print (' ')
    logger.info(' ')

    msg = '{0} {1}/{2} from ({3} overs)'.format(team.name.upper(),
                                                       str(team.total_score),
                                                       str(team.wickets_fell),
                                                       str(BallsToOvers(team.total_balls)))
    PrintInColor(msg, team.color)
    logger.info(msg)

    #show RR
    crr=GetCurrentRate(team)
    msg = "RunRate: {0}".format(str(crr))
    print (msg)
    logger.info(msg)
    print(' ')
    logger.info(' ')

    #show FOW
    if team.wickets_fell != 0:
        PrintInColor('FOW:', Style.BRIGHT)
        logger.info('FOW:')
        #get fow_array
        fow_array = []
        for f in team.fow:
            fow_array.append('{0}/{1} {2}({3})'.format(str(f.runs),
                                                       str(f.wkt),
                                                       GetShortName(f.player_dismissed.name),
                                                      str(BallsToOvers(f.total_balls))))
        fow_str = ', '.join(fow_array)
        PrintInColor(fow_str, team.color)
        logger.info(fow_str)

    #partnerships
    msg = "Partnerships:"
    PrintInColor(msg, Style.BRIGHT)
    logger.info(msg)
    for p in team.partnerships:
        msg = '{0} - {1} :\t{2}'.format(GetShortName(p.batsman_onstrike.name),
                                        GetShortName(p.batsman_dismissed.name),
                                        str(p.runs))
        print(msg)
        logger.info(msg)

    print (ch*45)
    logger.info(ch*45)

#match summary
def MatchSummary(match):
    logger=match.logger
    ch='-'
    result = match.result

    msg = ch*10 + 'Match Summary' + ch*10
    PrintInColor(msg, Style.BRIGHT)
    logger.info(msg)

    msg = '{0} vs {1}, at {2}'.format(result.team1.name, result.team2.name, match.venue.name)
    PrintInColor(msg, Style.BRIGHT)
    logger.info(msg)

    msg = ch*45
    print(ch*45)
    logger.info(msg)

    msg = result.result_str
    PrintInColor(msg, Style.BRIGHT)
    logger.info(msg)

    print(ch*45)
    logger.info(ch*45)

    msg = '{0} {1}/{2} ({3})'.format(result.team1.key,
                                            str(result.team1.total_score),
                                            str(result.team1.wickets_fell),
                                            str(BallsToOvers(result.team1.total_balls)))
    PrintInColor(msg, Style.BRIGHT)
    logger.info(msg)

    #see who all bowled
    bowlers1 = [plr for plr in result.team1.team_array if plr.balls_bowled > 0]
    bowlers2 = [plr for plr in result.team2.team_array if plr.balls_bowled > 0]
    #print first three top scorers
    most_runs = sorted(result.team1.team_array, key=lambda x: x.runs, reverse=True)
    most_runs = most_runs[:2]
    best_bowlers = sorted(bowlers2, key=lambda x: x.wkts, reverse=True)
    best_bowlers = best_bowlers[:2]
    # must be a nested list of fixed size elements
    data_to_print = []
    for x in range(2):
        if most_runs[x].status == True: runs = str(most_runs[x].runs) + '*'
        else:   runs = str(most_runs[x].runs)
        #print
        data_to_print.append([GetShortName(most_runs[x].name),
                              '{0}({1})'.format(runs, most_runs[x].balls),
                              GetShortName(best_bowlers[x].name),
                              '{0}/{1}'.format(best_bowlers[x].runs_given, best_bowlers[x].wkts)])

    #print
    PrintListFormatted(data_to_print, 0.01, logger)

    data_to_print = []
    print(ch*45)
    logger.info(ch*45)

    msg = '{0} {1}/{2} ({3})'.format(result.team2.key,
                                            str(result.team2.total_score),
                                            str(result.team2.wickets_fell),
                                            str(BallsToOvers(result.team2.total_balls)))
    PrintInColor(msg, Style.BRIGHT)
    logger.info(msg)

    most_runs = sorted(result.team2.team_array, key=lambda x: x.runs, reverse=True)
    most_runs = most_runs[:2]
    best_bowlers = sorted(bowlers1, key=lambda x: x.wkts, reverse=True)
    best_bowlers = best_bowlers[:2]
    for x in range(2):
        if most_runs[x].status == True: runs = str(most_runs[x].runs) + '*'
        else:   runs = str(most_runs[x].runs)

        #print
        data_to_print.append([GetShortName(most_runs[x].name),
                              '{0}({1})'.format(runs, most_runs[x].balls),
                              GetShortName(best_bowlers[x].name),
                              '{0}/{1}'.format(best_bowlers[x].runs_given, best_bowlers[x].wkts)])

    PrintListFormatted(data_to_print, 0.01, logger)
    print('-' * 43)
    logger.info('-' * 43)
    input('Press Enter to continue..')

#print bowlers stats
def DisplayBowlingStats(match, team):
    logger = match.logger
    bowlers=team.bowlers
    #here, remove the bowlers who didnt bowl
    bowlers_updated=[]
    char='-'
    print (char*45)
    logger.info(char*45)

    msg = char*15 + '-Bowling Stats-' + char*15
    PrintInColor (msg, Style.BRIGHT)
    logger.info(msg)
    print (char*45)
    logger.info(char*45)
    #nested list of fixed size elements
    data_to_print=[['Bowler', 'Ovrs', 'Mdns', 'Runs', 'Wkts', 'Eco']]
    for bowler in bowlers:
        #dont print if he hasnt bowled
        if bowler.balls_bowled != 0:
            bowlers_updated.append(bowler)
            balls=bowler.balls_bowled
            overs=BallsToOvers(balls)
            eco = float(bowler.runs_given / overs)
            eco = round(eco,2)
            bowler.eco = eco
            data_to_print.append([GetShortName(bowler.name),
                                  str(overs),
                                  str(bowler.maidens),
                                  str(bowler.runs_given),
                                  str(bowler.wkts),
                                  str(bowler.eco)])

    PrintListFormatted(data_to_print, 0.01, logger)
    print (char*45)
    logger.info(char*45)
    input('press enter to continue..')
    team.bowlers = bowlers_updated

#print playing XI
def DisplayPlayingXI(match):
    t1,t2=match.team1, match.team2
    #assign captain roles
    for t in [t1,t2]:
        for player in t.team_array:
            if player == t.captain:
                player.attr.iscaptain=True
    # print the playing XI
    print('Playing XI:')
    data_to_print = []
    data_to_print.append([t1.name,t2.name])
    data_to_print.append([' ', ' '])
    for x in range(11):
        name1 = t1.team_array[x].name
        name2 = t2.team_array[x].name
        if t1.team_array[x].attr.iscaptain == True:
            name1 = name1 + '(c)'
        if t1.team_array[x].attr.iskeeper == True:
            name1 = name1 + '(wk)'
        if t2.team_array[x].attr.iscaptain == True:
            name2 = name2 + '(c)'
        if t2.team_array[x].attr.iskeeper == True:
            name2 = name2 + '(wk)'
        data_to_print.append([name1, name2])
    #now print it
    PrintListFormatted(data_to_print, 0.1, None)