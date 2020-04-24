from Resources import*
from test_data import*
from helper import*

if __name__ == "__main__":
    teams=team_names
    t1=input('Select teams from : ' + ' / '.join(teams) + '\n')
    if t1 not in teams: Error_Exit('Invalid team')
    else:
        print ('Selected ' + t1)
        teams.remove(t1)
        t2=input('Select opponent team from : ' + ' / '.join(teams) + '\n')
        if not t2 in teams: Error_Exit('Invalid team')
        else:   print('Selected ' + t1 + ' and ' + t2)
    #find teams from user input
    for t in list_of_teams:
        if t.name == t1:    team1=t
        if t.name == t2:    team2=t
    
    t1=team1
    Play(t1, extras, t1.opening_pair, 300)
    target=0
    target = t1.total_score + 1        
    print("End of inns. Target: " + str(target))
    input()    
    #start innings
    t2=team2
    t2.batting_second=True
    t2.target=target
    extras.runs=0
    Play(t2, extras, t2.opening_pair, 300)
    #now check scores
    result = CalculateResult(t1, t2)
    PrintResult(result)
