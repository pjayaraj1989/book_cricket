from Resources import*
from test_data import*
from helper import*

if __name__ == "__main__":
    match=GetMatchInfo()    
    balls=int(match.overs)*6    
    t1=match.team1
    t2=match.team2
    
    Play(t1, t2, t1.opening_pair, balls)
    DisplayScore(t1) 
    input()
    target=t1.total_score+1

    t2.target = target
    t2.batting_second=True
    Play(t2, t1, t2.opening_pair, balls)
    DisplayScore(t2)
    
    result = CalculateResult(t1, t2)
    match.result = result
    PrintResult(match.result)
