from Resources import*
from test_data import*
from helper import*

if __name__ == "__main__":
    match=GetMatchInfo(team_keys)    
    overs=match.overs  
    t1, t2=match.team1, match.team2
    
    ValidateMatchTeams(match)
    bowlers_t1, bowlers_t2=t1.bowlers, t2.bowlers

    Play(t1, t2, t1.opening_pair, overs, bowlers_t2)
    DisplayScore(t1) 
    bowlers_t2=DisplayBowlingStats(bowlers_t2)
    input()
    t2.target = t1.total_score+1
    t2.batting_second=True
    Play(t2, t1, t2.opening_pair, overs, bowlers_t1)
    DisplayScore(t2)
    bowlers_t1=DisplayBowlingStats(bowlers_t1)

    result = CalculateResult(t1, t2, bowlers_t1, bowlers_t2)
    match.result = result
    PrintResult(match.result)
