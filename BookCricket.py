from Resources import*
from test_data import*
from helper import*

if __name__ == "__main__":
    teams=team_names
    overs=input('Select overs\n')
    overs=int(overs)
    if overs > 50 or overs <= 0: Error_Exit('Invalid overs')    
    balls=overs*6
    
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
    
    t1=team1
    Play(t1, extras, t1.opening_pair, balls)
    target=0
    target = t1.total_score + 1        
    input('End of inns. Target: {0}'.format(str(target)))
    
    #second innings
    t2=team2
    t2.batting_second=True
    t2.target=target
    extras.runs=0
    Play(t2, extras, t2.opening_pair, balls)
    
    #now calc result
    result = CalculateResult(t1, t2)
    PrintResult(result)
