from Resources import*
from test_data import*
from helper import*

if __name__ == "__main__": 
    #start innings
    t1 = Team(india_squad, 0, False, False, 0, "India", 0, 0)   
    Play(t1, extras_ind, opening_pair_ind, 300)
    print("End of 1st innings")
    target=0
    target = t1.total_score + 1        
    print("Target: " + str(target))
    input()
    #start innings
    t2 = Team(australia_squad, 0, False, True, target, "Australia", 0, 0)    
    Play(t2, extras_aus, opening_pair_aus, 300)
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
