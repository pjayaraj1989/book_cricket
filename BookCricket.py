from Resources import*
from test_data import*
from helper import*

if __name__ == "__main__":
    match=GetMatchInfo(team_keys)    
    overs=match.overs  
    t1=match.team1
    t2=match.team2
    
    bowlers_t1 = [plr for plr in t1.team_array if plr.attr.bowling >= 6]
    bowlers_t2 = [plr for plr in t2.team_array if plr.attr.bowling >= 6]

    Play(t1, t2, t1.opening_pair, overs, bowlers_t2)
    DisplayScore(t1) 
    DisplayBowlingStats(bowlers_t2)
    input()
    target=t1.total_score+1

    t2.target = target
    t2.batting_second=True
    Play(t2, t1, t2.opening_pair, overs, bowlers_t1)
    DisplayScore(t2)
    DisplayBowlingStats(bowlers_t1)

    result = CalculateResult(t1, t2, bowlers_t1, bowlers_t2)
    match.result = result
    PrintResult(match.result)
