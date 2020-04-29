import sys
sys.path.append('data')
sys.path.append('functions')
from Resources import*
from test_data import*
from helper import*

if __name__ == "__main__":
    #input teams
    match=GetMatchInfo(team_keys)    
    overs=match.overs  
    #see if teams are valid
    ValidateMatchTeams(match)
    #toss
    match=Toss(match)
    #now find out who is batting first
    batting_first = next((x for x in [match.team1, match.team2] if x.batting_second == False), None)
    batting_second = next((x for x in [match.team1, match.team2] if x.batting_second == True), None)    
    match.team1=batting_first
    match.team2=batting_second
    #get list of bowlers 
    bowlers_t1, bowlers_t2=match.team1.bowlers, match.team2.bowlers
    #play one inns
    Play(match.team1, match.team2, match.team1.opening_pair, overs, bowlers_t2)
    DisplayScore(match.team1) 
    bowlers_t2=DisplayBowlingStats(bowlers_t2)
    
    #play second inns
    match.team2.target = match.team1.total_score+1
    match.team2.batting_second=True
    Play(match.team2, match.team1, match.team2.opening_pair, overs, bowlers_t1)
    DisplayScore(match.team2)
    bowlers_t1=DisplayBowlingStats(bowlers_t1)

    #show results
    result = CalculateResult(match.team1, match.team2, bowlers_t1, bowlers_t2)
    match.result = result
    PrintResult(match.result)
