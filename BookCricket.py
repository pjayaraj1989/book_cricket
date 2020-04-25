from Resources import*
from test_data import*
from helper import*

if __name__ == "__main__":
    match=GetMatchInfo()    
    balls=int(match.overs)*6    
    t1=match.team1
    t2=match.team2
    #first innings
    Play(t1, extras, t1.opening_pair, balls, t2)
    target=0
    target = t1.total_score + 1        
    input('End of inns. Target: {0}'.format(str(target)))    
    #second innings
    t2.batting_second=True
    t2.target=target
    extras.runs=0
    Play(t2, extras, t2.opening_pair, balls, t1)    
    #now calc result
    result = CalculateResult(t1, t2)    
    #add result to match
    match.result = result
    PrintResult(match.result)
