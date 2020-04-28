
#random array for runs
run_array = [-1,0,0,0,0,0,3,1,1,6,-1,1,1,4,4,1,1,1,1,2,3,4,5]    #select random bowler for this over

#fielders
field_positions = ['past slips', 'through fine leg', 'through cover', 'through point',
                    'straight down the ground', 'through mid-on','through mid-off',
                    'through extra cover']
#commentary
commentary_big_shot = ['what a shot!','bad ball and punished','well connected', 'that will find the fence!','magnificent shot!','stand and deliver!']
commentary_ground_shot = ['not timed well', 'found the gap well', 'good ball ! but well played into the gap','into the gap']
commentary_bowled = ['full and straight what a ball','bowledim!', 'Middle stump out of here','knocked him over with a ripper!','knocked his stumps over!']
commentary_runout = ['what a terrible mix up!', 'this is bizzare!']
commentary_stumped = ['swift work by the keeper!', 'thats out stumped!', 'fast hands by the keeper','lightning quick behind the stumps']
commentary_caught = ['in the air and taken!','thats straight up in the air', 'oh what a catch','what a blinder!','unbelievable catch!']
commentary_lbw = ['the finger goes up!','thats in line and umpire says out','missing leg? No! thats out','oh thats a harsh decision']
commentary_dot_ball = ['beautiful delivery, missed the stumps by inches!',  'well defended!','solid defence'
                        'big appeal.. but umpire says not out!', 'that looks close, but not out says the umpire!'
                            'outside off and he misses that!','dangerous delivery batsman had no clue about it']

#player attributes
class PlayerAttr():
    def __init__(self, **kwargs):
        #attribs should be int out of 10
        batting=bowling=iscaptain=iskeeper=isopeningbowler=None
        #init default
        self.batting=0
        self.bowling=0
        self.iskeeper=False
        self.iscaptain=False
        self.isopeningbowler=False
        if kwargs is not None:
            for k,v in kwargs.items():
                if k=='batting':    self.batting=v
                if k=='bowling':    self.bowling=v
                if k=='iscaptain':  self.iscaptain=v
                if k=='iskeeper':   self.iskeeper=v
                if k=='isopeningbowler':    self.isopeningbowler=v

#player details
class Player():
    def __init__(self, **kwargs):
        attr=onstrike=runs=balls=name=status=wkts=balls_bowled=runs_given=dismissal=maidens=eco=None
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
        team_array=total_score=innings_over=batting_second=target=name=wickets_fell=total_balls=opening_pair=extras=key=last_bowler=bowlers=None
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

#result details
class Result():
    def __init__(self, **kwargs):
        #default
        team1=team2=winner=result_str=most_runs=most_wkts=besteco=None
        self.team1=None
        self.team2=None
        self.winner=None
        self.result_str=''
        self.most_runs=None
        self.most_wkts=None
        self.besteco=None
        if kwargs is not None:
            for k, v in kwargs.items():
                if k=='team1':  self.team1=v
                if k=='team2':  self.team2=v
                if k=='winner': self.winner=v
                if k=='result_str': self.result_str=v
                if k=='most_runs':  self.most_runs=v
                if k=='most_wkts:': self.most_wkts=v
                if k=='besteco':    self.besteco=v
