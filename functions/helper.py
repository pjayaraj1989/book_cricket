#venues
venues = ['Lords',
            'The MCG',
            'The Chinnaswamy Stadium,Bengaluru',
            'SuperSport Park Centurion',
            'The Sydney Cricket Ground',
            'The Wankhede, Mumbai',
            'Edgbaston',
            'The WACA, Perth',
            'The Eden Gardens, Kolkata',
            'Johannesburg',
            'R.Premadasa Stadium, Colombo']

intro_dialogues = ['Welcome everybody, here we are at',
                    'Hello everyone, here we are at',
                    'Lovely evening here at ',
                    'Electrifying atmosphere here at',
                    'Warm welcome to everybody to ']

commentators = ['Harsha Bhogle',
                'Ramiz Raja',
                'Tony Greig',
                'Ian Smith',
                'Sunil Gavaskar',
                'Sanjay Manjrekar',
                'Ravi Shastri',
                'Richie Benaud',
                'Phil Tufnel',
                'Pommie Mbangwa',
                'Nasser Hussain']

umpires = ['Kumar Dharmasena',
                'Ian Gould',
                'Asad Rauf',
                'Aleem Dar',
                'Nitin Menon',
                'Marais Erasmus',
                'Richard Kettleborough',
                'Nigel Llong',
                'Paul Reiffel',
                'Richard Illingworth',
                'Simon Tauffel',
                'S Ravi',
                'Billy Bowden',]

#random array for runs
run_array = [0,0,0,0,0,3,1,1,1,1,4,4,1,-1,1,1,1,2,3,4,5]    #select random bowler for this over

#fielders
field_positions = ['past slips',
                    'through first slip',
                    'through leg side',
                    'through cover',
                    'through point',
                    'straight down the ground',
                    'through mid-on',
                    'through mid-off',
                    'through extra cover',
                    'through the gully']

#commentary
commentary_big_shot = ['what a shot!',
                        'the crowd is loving this!',
                        'how do you set fields for this batsman!',
                        'bad ball and punished!',
                        'well connected!',
                        'Great shot! Abssollutely magnificent!. And the batsman has not moved an inch!',
                        'that will find the fence!',
                        'magnificent shot!',
                        'stand and deliver!',
                        'oh unbelievable timing!',
                        'Beautiful shot!',
                        'he is getting warmed up here!',
                        'boy what a shot!',
                        'right out of the middle of the bat!',
                        'what a smash!',
                        'Terrific batting this.. what would be the reply from the bowler?',
                        'Another one of those, and there will be a chat between the bowler and his captain!',
                        'he goes bang!']
                        
commentary_ground_shot = ['not timed well',
                        'found the gap well',
                        'good ball ! but well played into the gap',
                        'into the gap',
                        'very quick running',
                        'he has to hurry!',
                        'Oooh! direct hit and he wouldve gone!',
                        'singles and doubles will surely irritate the fielding captain']
                        
commentary_bowled = ['full and straight what a ball',
                        'what a yorker! he is on fire!',
                        'bowled himm!',
                        'Middle stump out of here',
                        'inside edge and bowled!',
                        'dragged on to the stumps',
                        'done him and shattered the stumps!',
                        'he has made an awful mess of the stumps!',
                        'knocked him over with a ripper!',
                        'oh hes played it on!.. Batsman would be so dissapointed',
                        'oh what a delivery!.. Perfect line and length!',
                        'Bowled him!! comprehensively bowled!',
                        'knocked his stumps over!',
                        'off stump out of the ground!',
                        'bowled him! You beauty!',
                        'Kocked his middle stump out!... And there is a stare at the batsman!',
                        'Bowled him! And he is showing the batsman the way to the dressing room!',
                        'done him with a toe crushing yorker!',
                        'oh bowledimm!, an unplayable delivery!',]

commentary_runout = ['what a terrible mix up!',
                        'this is bizzare!',
                        'he is coming back for the second, direct hit and gone!',
                        'that was a horrible call!',
                        'direct hit and gone!','what was the batsman thinking!?']

commentary_stumped = ['swift work by the keeper!',
                        'thats out stumped!',
                        'stumped, no need to refer it!',
                        'fast hands behind the stumps!',
                        'lightning quick behind the stumps']

commentary_caught = ['in the air.. and taken!',
                        'thats straight up in the air.. taken!',
                        'leading edge and gone!',
                        'outside edge and a magnificent catch!',
                        'oh what a catch!',
                        'what a blinder!',
                        'unbelievable catch!',
                        'has he taken that? He has! what a catch!']

commentary_lbw = ['big appeal.. and the finger goes up!',
                'thats in line and umpire says out',
                'missing leg? No! thats out',
                'oh thats a harsh decision',
                'given out, batsman is not happy at all',
                'thats dead, dont look at the umpire!',
                'thats a long appeal and... finally the finger is raised!']

commentary_dot_ball = ['beautiful delivery, missed the stumps by inches!',
                        'well defended!',
                        'solid defence',
                        'edged and dropped at first slip!.. oh dear!',
                        'swings and misses',
                        'in the air but drops safe..!',
                        'big appeal.. but umpire says not out!',
                        'that looks close, but not out says the umpire!',
                        'missed it, there is a stare from the bowler',
                        'swing and a miss!',
                        'oh that was perilously close to the off stump!, batsman looking nervous here!',
                        'outside off and he misses that!',
                        'dangerous delivery! batsman had no clue about it',
                        'oh that was a quick one!',
                        'beautiful slow ball!',
                        'driven nicely but the fielder was lightning quick! saved a certain boundary!',
                        'played well but straight to the fielder!',
                        'slower ball and he misses it!']

commentary_wide = ['he has lost his line completely!',
                    'oh thats a harsh call from the umpire!',
                    'not good bowling from him!',
                    'this will irritate the captain!',
                    'he is leaking runs here!',
                    'bowler under pressure here!',
                    ]

commentary_milestone = ['Its been a terrific knock..!',
                    'what a performance...!',
                    'Absolutely magnificent innings!',
                    'Thats it! A brilliant knock under pressure!',
                    'he is on absolute fire here !']

commentary_keeper_catch = ['edged.. and taken!',
                            'thin edge, big appeal from behind the stumps! given!',
                            'is there an edge? Yes it is!',
                            'oh is there a nick!? Batsman is walking...!',
                            'straight up in the air, keeper says mine and takes it!',
                            ]

#color codes90
color_map = {
    'red' : "\033[1;31m",
    'green' : "\033[0;32m",
    'reset' : "\033[0;0m",
    'bold' : "\033[;1m",
    'cyan' : "\033[1;36m",
    'blue' : "\033[1;34m",
    'purple'   :   "\033[1;35m",
    'gray': "\033[1;37m",
    'lightblue':    "\033[1;34m",
    'lightgreen':   "\033[1;32m",
    'brown':    "\033[1;33m",
    'yellow':  "\033[1;93m",
    'magenta':  "\033[1;45m"
    }

#player attributes
class PlayerAttr():
    def __init__(self, **kwargs):
        #attribs should be int out of 10
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
        attr=onstrike=runs=balls=name=status=wkts=balls_bowled=runs_given=dismissal=maidens=eco=fifty=hundred=None
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
        team_array=total_score=innings_over=batting_second=target=name=wickets_fell=total_balls=opening_pair=extras=key=last_bowler=bowlers=fow=captain=nrr=color=None
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
