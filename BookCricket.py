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

    extras = Player('Extra',False,0,0,True)

    #has to be odd numbered
    india_squad = [sachin, sehwag, gambhir, kohli, yuvraj, dhoni, raina, ashwin, zaheer, nehra, sreesanth]
    team_ind = Team(india_squad, 0, False)

    #first member always on strike
    opening_pair = [sachin, sehwag]
    sachin.onstrike=True
    #start innings
    Play(team_ind, extras, opening_pair)

    team_ind=team_ind

