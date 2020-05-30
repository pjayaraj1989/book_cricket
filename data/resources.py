#venues
from functions.helper import Venue

#weightage for runs -1,0,1,2,3,4,5,6
venue_lords=Venue(name="Lords", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_mcg=Venue(name="The MCG", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_perth=Venue(name="The WACA, Perth", run_prob=[0.06, 0.33, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_mumbai=Venue(name="The Wankhede Stadium, Mumbai", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_colombo=Venue(name="R. Premadasa Stadium, Colombo", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_scg=Venue(name="The Sydney Cricket Ground", run_prob=[0.03, 0.22, 0.27, 0.18, 0.1, 0.05 , 0.11, 0.04])
venue_joburg=Venue(name="the Wanderers, Johannesburg", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_centurion=Venue(name="The Super Sport park, Centurion", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_barbados=Venue(name="The Kensington Oval, Bridgetown", run_prob=[0.05, 0.34, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_edgbaston=Venue(name="The Edgbaston", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_kolkata=Venue(name="The Eden Gardens, Kolkata", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])
venue_bangalore=Venue(name="M. Chinnaswamy Stadium, Bengaluru", run_prob=[0.03, 0.36, 0.27, 0.11, 0.1, 0.01 , 0.11, 0.01])

class resources():
    match_venues = [venue_lords,venue_barbados,venue_colombo,venue_joburg,venue_bangalore,
                    venue_centurion,venue_edgbaston, venue_mcg, venue_mumbai,venue_perth, venue_scg]

    runs_t20 = [0,0,6,0,0,3,1,1,6,1,4,1,-1,1,4,1,2,5]

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

    #fielders
    fields = {  4 : ['over first slip!',
                     'through the covers',
                     'punched off the backfoot',
                     'driven off the front foot',
                     'advances down the ground',
                     'driven through extra cover',
                     'reverse sweep',
                     'moved across the line and steers it through fine leg',
                     'lofted in the air',
                     'cut through point',
                     'flicks it towards the leg side',
                     'solidly played through extra cover',
                     'square cut over the point fielder',
                     'short ball punished through leg side',
                     'swept through fine leg!'],

                6: ['straight down the ground',
                    'smashes it over long-on',
                    'over long on',
                    'moves across the stumps and smashes it through leg side',
                    'blasted that through the covers',
                    'advances down the ground',
                    'smashed it over long off',
                    'cuts it hard over point',],

                "ground_shot" : ['runs past the slips',
                    'driven through the covers',
                    'drive through extra cover',
                    'worked that into the gap',
                    'sweetly timed into the gap',
                    'driven nicely through midwicket',
                    'hit that hard through point',
                    'steered it towards fine leg',
                    'runs it down the third man',],
    }



