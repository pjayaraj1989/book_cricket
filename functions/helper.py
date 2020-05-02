
#player attributes
class PlayerAttr():
    def __init__(self, **kwargs):
        batting=bowling=iscaptain=iskeeper=isopeningbowler=isspinner=ispacer=None
        #init default
        self.batting=0
        self.bowling=0
        self.iskeeper=False
        self.iscaptain=False
        self.isopeningbowler=False
        self.isspinner=False
        self.ispacer=False
        if kwargs is not None:
            for k,v in kwargs.items():
                if k=='batting':    self.batting=v
                if k=='bowling':    self.bowling=v
                if k=='iscaptain':  self.iscaptain=v
                if k=='iskeeper':   self.iskeeper=v
                if k=='isopeningbowler':    self.isopeningbowler=v
                if k=='isspinner':  self.isspinner=v
                if k=='ispacer':    self.ispacer=v

#player details
class Player():
    def __init__(self, **kwargs):
        attr=onstrike=runs=balls=name=status=wkts=balls_bowled=runs_given=dismissal=maidens=eco=fifty=hundred=strikerate=max_overs=None
        self.attr=None
        self.onstrike=None
        self.runs=0
        self.balls=0
        self.wkts=0
        self.balls_bowled=0
        self.runs_given=0
        self.maidens=0
        self.name=''
        self.status=True
        self.dismissal=""
        self.eco=0.0
        self.fifty=0
        self.hundred=0
        self.strikerate=0.0
        self.max_overs=0
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
                if k=='maidens':    self.maidens=v
                if k=='eco':    self.eco=v
                if k=='fifty':  self.eco=v
                if k=='hundred':    self.hundred=v
                if k=='strikerate': self.strikerate=v
                if k=='max_overs':    self.max_overs=v

#match details
class Match():
    def __init__(self, **kwargs):
        team1=team2=overs=result=venue=batting_first=batting_second=bowler_max_overs=autoplay=None
        #initialize default values
        self.overs=0
        self.result=None
        self.team1=None
        self.team2=None
        self.venue=None
        self.umpire=None
        self.batting_first=None
        self.batting_second=None
        self.won=False
        self.bowler_max_overs=0
        self.autoplay=False
        if kwargs is not None:
            for k,v in kwargs.items():
                if k=='team1':  self.team1=kwargs[k]                
                if k=='team2':  self.team2=kwargs[k]               
                if k=='overs':  self.overs=kwargs[k]                
                if k=='result': self.result=kwargs[k]
                if k=='venue':  self.venue=kwargs[k]     
                if k=='umpire': self.umpire=kwargs[k]
                if k=='batting_first':  self.batting_first=kwargs[k]
                if k=='batting_second': self.batting_second=kwargs[k]
                if k=='won':    self.won=kwargs[k]
                if k=='bowler_max_overs':   self.bowler_max_overs=kwargs[k]
                if k=='autoplay':   self.autoplay=kwargs[k]

#match details
class Team():
    def __init__(self, **kwargs):
        team_array=total_score=innings_over=won=batting_second=target=name=wickets_fell=total_balls=opening_pair=extras=key=last_bowler=bowlers=fow=captain=nrr=color=None
        #initialize default values
        self.team_array=None
        self.total_score=0
        self.innings_over=False
        self.batting_second=False
        self.target=0
        self.name=""
        self.key=""
        self.wickets_fell=0
        self.total_balls=0
        self.opening_pair=None
        self.extras=0
        self.last_bowler=None
        self.bowlers=None
        self.fow=[]
        self.captain=None
        self.nrr=0.0
        self.color=None
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
                if k=='key':    self.key=kwargs[k]
                if k=='last_bowler':    self.last_bowler=kwargs[k]
                if k=='bowlers':    self.bowlers=kwargs[k]
                if k=='fow':    self.fow=kwargs[k]
                if k=='captain':    self.captain=kwargs[k]
                if k=='nrr':    self.nrr=kwargs[k]
                if k=='color':  self.color=kwargs[k]

#result details
class Result():
    def __init__(self, **kwargs):
        #default
        team1=team2=winner=result_str=most_runs=most_wkts=besteco=mom=None
        self.team1=None
        self.team2=None
        self.winner=None
        self.result_str=''
        self.most_runs=None
        self.most_wkts=None
        self.besteco=None
        self.mom=None
        if kwargs is not None:
            for k, v in kwargs.items():
                if k=='team1':  self.team1=v
                if k=='team2':  self.team2=v
                if k=='winner': self.winner=v
                if k=='result_str': self.result_str=v
                if k=='most_runs':  self.most_runs=v
                if k=='most_wkts:': self.most_wkts=v
                if k=='besteco':    self.besteco=v
                if k=='mom':    self.mom=v
