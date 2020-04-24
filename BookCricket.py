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
    
    for t in list_of_teams:
        if t.name == t1:    team1=t
        if t.name == t2:    team2=t
    
    t1=team1
    Play(t1, extras_ind, t1.opening_pair, 300)
    print("End of 1st innings")
    target=0
    target = t1.total_score + 1        
    print("Target: " + str(target))
    input()
    
    #start innings
    t2=team2
    t2.batting_second=True
    t2.target=target
    Play(t2, extras_aus, t2.opening_pair, 300)
    #now check scores
    result = CalculateResult(t1, t2)
    print("Summary:")
    print(result.team1.name + " " + 
          str(result.team1.total_score) + "/" + 
          str(result.team1.wickets_fell) + "(" +
          str(result.team1.total_balls) + ")")
    print(result.team2.name + " " + 
          str(result.team2.total_score) + "/" + 
          str(result.team2.wickets_fell) + "(" +
          str(result.team2.total_balls) + ")")
    print(result.result_str)
