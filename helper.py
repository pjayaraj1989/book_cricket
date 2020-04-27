
#player attributes
class PlayerAttr():
    def __init__(self, **kwargs):
        #attribs should be int out of 10
        batting=bowling=iscaptain=iskeeper=None
        #init default
        self.batting=0
        self.bowling=0
        self.iskeeper=False
        self.iscaptain=False
        if kwargs is not None:
            for k,v in kwargs.items():
                if k=='batting':    self.batting=v
                if k=='bowling':    self.bowling=v
                if k=='iscaptain':  self.iscaptain=v
                if k=='iskeeper':   self.iskeeper=v

#player details
class Player():
    def __init__(self, **kwargs):
        attr=onstrike=runs=balls=name=status=wkts=balls_bowled=runs_given=dismissal=None
        self.attr=None
        self.onstrike=None
        self.runs=0
        self.balls=0
        self.wkts=0
        self.balls_bowled=0
        self.runs_given=0
        self.name=''
        self.status=True
        self.dismissal=""
        if kwargs is not None:
            for k,v in kwargs.items():
                if k=='onstrike':   self.onstrike=v
                if k=='runs':   self.runs=v
                if k=='balls':  self.balls=v
                if k=='name':   self.name=v
                if k=='status': self.status=v
                if k=='attr':   self.attr=v
                if k=='wkts':   self.wkts=v
                if k=='balls_bowled':   self.balls_bowled=v
                if k=='runs_given': self.runs_given=v
                if k=='dismissal':  self.dismissal=v

#match details
class Match():
    def __init__(self, **kwargs):
        team1=team2=overs=result=None
        #initialize default values
        self.overs=0
        self.result=None
        self.team1=None
        self.team2=None
        if kwargs is not None:
            for k,v in kwargs.items():
                if k=='team1':  self.team1=kwargs[k]                
                if k=='team2':  self.team2=kwargs[k]               
                if k=='overs':  self.overs=kwargs[k]                
                if k=='result': self.result=kwargs[k]       

#match details
class Team():
    def __init__(self, **kwargs):
        team_array=total_score=innings_over=batting_second=target=name=wickets_fell=total_balls=opening_pair=extras=None
        #initialize default values
        self.team_array=None
        self.total_score=0
        self.innings_over=False
        self.batting_second=False
        self.target=0
        self.name=""
        self.wickets_fell=0
        self.total_balls=0
        self.opening_pair=None
        self.extras=0
        if kwargs is not None:
            for k,v in kwargs.items():
                if k=='team_array':  self.team_array=kwargs[k]                
                if k=='total_score':  self.total_score=kwargs[k]               
                if k=='innings_over':  self.innings_over=kwargs[k]                
                if k=='batting_second': self.batting_second=kwargs[k]
                if k=='target': self.target=kwargs[k]
                if k=='name': self.name=kwargs[k]
                if k=='wickets_fell': self.wickets_fell=kwargs[k]
                if k=='total_balls': self.total_balls=kwargs[k]
                if k=='opening_pair': self.opening_pair=kwargs[k]
                if k=='extras': self.extras=kwargs[k]

#result details
class Result():
    def __init__(self, **kwargs):
        #default
        team1=team2=winner=result_str=most_runs=most_wkts=None
        self.team1=None
        self.team2=None
        self.winner=None
        self.result_str=''
        self.most_runs=None
        self.most_wkts=None
        if kwargs is not None:
            for k, v in kwargs.items():
                if k=='team1':  self.team1=v
                if k=='team2':  self.team2=v
                if k=='winner': self.winner=v
                if k=='result_str': self.result_str=v
                if k=='most_runs':  self.most_runs=v
                if k=='most_wkts:': self.most_wkts=v
