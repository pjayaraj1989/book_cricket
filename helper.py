#venues
venues = ['Lords','The MCG','The Chinnaswamy Stadium,Bengaluru','SuperSport Park Centurion','The Sydney Cricket Ground','The Wankhede, Mumbai',
            'Edgbaston', 'The WACA, Perth', 'The Eden Gardens, Kolkata', 'Johannesburg', 'R.Premadasa Stadium, Colombo']

intro_dialogues = ['welcome everybody, here we are','hello everyone, here we are','warm welcome to everyone to ']

commentators = ['Harsha Bhogle','Sourav Ganguly','Tony Greig','Ian Smith','Ravi Shastri','Michael Clarke','Pommie Mbangwa','Rahul Dravid','Michael Hussey']

umpires = ['Kumar Dharmasena','Ian Gould','Asad Rauf','Aleem Dar','Nitin Menon','Marais Erasmus','Richard Kettleborough','Nigel Llong','Paul Reiffel',
                'Richard Illingworth','Simon Tauffel','S Ravi','Billy Bowden',]

#random array for runs
run_array = [-1,0,0,0,0,0,3,1,1,6,-1,1,1,4,4,1,1,1,1,2,3,4,5]    #select random bowler for this over

#fielders
field_positions = ['past slips','through first slip','through fine leg', 'through cover', 'through point',
                    'straight down the ground', 'through mid-on','through mid-off',
                    'through extra cover']
#commentary
commentary_big_shot = ['what a shot!','bad ball and punished','well connected','that will find the fence!',
                        'magnificent shot!','stand and deliver!','oh unbelievable timing!','Beautiful shot!'
                        'he is getting warmed up here!','boy what a shot!','right out of the middle of the bat!']
commentary_ground_shot = ['not timed well', 'found the gap well', 'good ball ! but well played into the gap','into the gap']
commentary_bowled = ['full and straight what a ball','what a yorker! he is on fire!','bowled himm!', 'Middle stump out of here',
                            'done him and shattered the stumps!','he has made an awful mess of the stumps!','knocked him over with a ripper!',
                            'knocked his stumps over!','off stump out of the ground!','bowled him! You beauty!','oh bowledim, an unplayable delivery!']
commentary_runout = ['what a terrible mix up!','this is bizzare!','he is coming back for the double, gone!','that was a horrible call!',
                        'direct hit and gone!','what was the batsman thinking!?']
commentary_stumped = ['swift work by the keeper!', 'thats out stumped!','stumped, no need to refer it!','fast hands behind the stumps!','lightning quick behind the stumps']
commentary_caught = ['in the air and taken!','thats straight up in the air.. taken!','leading edge and gone!','oh what a catch!','what a blinder!','unbelievable catch!','has he taken that? He has!']
commentary_lbw = ['big appeal.. and the finger goes up!','thats in line and umpire says out','missing leg? No! thats out','oh thats a harsh decision',
                        'given out, batsman is not happy at all','thats dead, dont look at the umpire!','thats a long appeal and finally the finger is raised!']
commentary_dot_ball = ['beautiful delivery, missed the stumps by inches!','well defended!','solid defence','swings and misses',
                        'big appeal.. but umpire says not out!', 'that looks close, but not out says the umpire!','missed it, there is a stare from the bowler',
                        'swing and a miss!',
                            'outside off and he misses that!','dangerous delivery! batsman had no clue about it','slower ball and he misses it!']

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
        team1=team2=overs=result=venue=None
        #initialize default values
        self.overs=0
        self.result=None
        self.team1=None
        self.team2=None
        self.venue=None
        self.umpire=None
        if kwargs is not None:
            for k,v in kwargs.items():
                if k=='team1':  self.team1=kwargs[k]                
                if k=='team2':  self.team2=kwargs[k]               
                if k=='overs':  self.overs=kwargs[k]                
                if k=='result': self.result=kwargs[k]
                if k=='venue':  self.venue=kwargs[k]     
                if k=='umpire': self.umpire=kwargs[k]
                
#match details
class Team():
    def __init__(self, **kwargs):
        team_array=total_score=innings_over=batting_second=target=name=wickets_fell=total_balls=opening_pair=extras=key=last_bowler=bowlers=fow=captain=nrr=None
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
