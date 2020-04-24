from Resources import*
from test_data import*

if __name__ == "__main__": 
    #start innings
    team_ind = Team(india_squad, 0, False, False, 0, "India", 0, 0)
    #first member always on strike
    opening_pair_ind = [sachin, sehwag]
    sachin.onstrike=True
    Play(team_ind, extras_ind, opening_pair_ind)
    target=0
    target = team_ind.total_score + 1        
    
    #start innings
    team_aus = Team(australia_squad, 0, False, True, target, "Australia", 0, 0)
    #first member always on strike
    opening_pair_aus = [hayden, gilchrist]
    gilchrist.onstrike=True
    Play(team_aus, extras_aus, opening_pair_aus)

    #now check scores
    result = CalculateResult(team_ind, team_aus)

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
