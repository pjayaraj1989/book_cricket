from Resources import*

if __name__ == "__main__":
    balls=10
    sachin=Player('Sachin',False, 0, 0, True)
    sehwag=Player('Sehwag',False, 0, 0, True)
    gambhir=Player('Gambhir',False, 0, 0, True)
    extras = Player('Extra',False,0,0,True)

    team = [sachin, sehwag, gambhir]

    #first member always on strike
    pair = [sachin, sehwag]
    sachin.onstrike=True

    Play(team,extras, pair)

