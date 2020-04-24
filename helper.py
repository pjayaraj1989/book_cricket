class Player():
    def __init__(self,name, onstrike, runs, balls, status):
        self.onstrike=onstrike
        self.runs=runs
        self.balls=balls
        self.name=name
        self.status=status

class Match():
    def __init__(self, team1, team2, overs, result):
        self.team1=team1
        self.team2=team2
        self.overs=overs
        self.result=result

class Team():
    def __init__(self, team_array, total_score, innings_over, batting_second, target, name, wickets_fell, total_balls, opening_pair):
        self.team_array=team_array
        self.total_score=total_score
        self.innings_over=innings_over
        self.batting_second=batting_second
        self.target=target
        self.name=name
        self.wickets_fell=wickets_fell
        self.total_balls=total_balls
        self.opening_pair=opening_pair

class Result():
    def __init__(self, team1, team2, winner, result_str):
        self.team1=team1
        self.team2=team2
        self.winner=winner
        self.result_str=result_str