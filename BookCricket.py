from Resources import*

if __name__ == "__main__":
    balls=10
    sachin=Player('Sachin',False, 0, 0, True)
    sehwag=Player('Sehwag',False, 0, 0, True)
    gambhir=Player('Gambhir',False, 0, 0, True)
    kohli=Player('Kohli',False, 0, 0, True)
    yuvraj=Player('Yuvraj',False, 0, 0, True)
    dhoni=Player('Dhoni',False, 0, 0, True)
    raina=Player('Raina',False, 0, 0, True)
    ashwin=Player('Ashwin',False, 0, 0, True)
    zaheer=Player('Zaheer',False, 0, 0, True)
    nehra=Player('Nehra',False, 0, 0, True)
    sreesanth=Player('Sreesanth',False, 0, 0, True)

    extras_ind = Player('Extra',False,0,0,True)

    #has to be odd numbered
    india_squad = [sachin, sehwag, gambhir, kohli, yuvraj, dhoni, raina, ashwin, zaheer, nehra, sreesanth]
    team_ind = Team(india_squad, 0, False, False, 0, "India", 0, 0)

    #first member always on strike
    opening_pair_ind = [sachin, sehwag]
    sachin.onstrike=True
    #start innings
    Play(team_ind, extras_ind, opening_pair_ind)

    target = team_ind.total_score + 1

    #now add next team, and 
    hayden=Player('hayden',False, 0, 0, True)
    gilchrist=Player('gilchrist',False, 0, 0, True)
    ponting=Player('ponting',False, 0, 0, True)
    clarke=Player('clarke',False, 0, 0, True)
    hussey=Player('hussey',False, 0, 0, True)
    watson=Player('watson',False, 0, 0, True)
    white=Player('white',False, 0, 0, True)
    hogg=Player('hogg',False, 0, 0, True)
    johnson=Player('johnson',False, 0, 0, True)
    lee=Player('lee',False, 0, 0, True)
    tait=Player('tait',False, 0, 0, True)

    #has to be odd numbered
    australia_squad = [hayden, gilchrist, ponting, clarke, hussey, watson, white, hogg, johnson, lee, tait]
    team_aus = Team(australia_squad, 0, False, True, target, "Australia", 0, 0)
    extras_aus = Player('Extra',False,0,0,True)

    #first member always on strike
    opening_pair_aus = [hayden, gilchrist]
    gilchrist.onstrike=True
    #start innings
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
