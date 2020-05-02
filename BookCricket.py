
from functions.functions import*

if __name__ == "__main__":
    #input teams to play
    match=GetMatchInfo(team_keys)

    #see if teams are valid
    ValidateMatchTeams(match)

    #toss, select who is batting first
    match=Toss(match)
    match.team1=match.batting_first
    match.team2=match.batting_second
    
    #play one inns
    Play(match, match.team1, match.team2, match.team1.opening_pair, match.team2.bowlers)
    DisplayScore(match.team1) 
    DisplayBowlingStats(match.team2)
    
    #play second inns with target
    match.team2.target = match.team1.total_score+1
    Play(match, match.team2, match.team1, match.team2.opening_pair, match.team1.bowlers)
    DisplayScore(match.team2)
    DisplayBowlingStats(match.team1)

    #show results
    result = CalculateResult(match)
    match.result = result
    PrintResult(match.result)

    FindPlayerOfTheMatch(match)
    input('End of the Match.. Thanks for watching !!.. Press enter to exit')