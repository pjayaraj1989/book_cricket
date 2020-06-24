#functions to initiate the game

#read venue data
import json

import numpy

from data.resources import*
from data.commentary import*
from functions.DisplayScores import DisplayPlayingXI
from functions.helper import Venue, Team, Player, Match
from functions.utilities import ChooseFromOptions, PrintInColor, Randomize, Error_Exit
import random
from numpy.random import choice
from colorama import Fore, Style

def GetVenue(venue_data):
    venue_obj = None
    f=open(venue_data)
    data = json.load(f)
    countries = {}
    if data is not None:    countries = data['Venues']
    #now get venues for each countries
    country = ChooseFromOptions(list(countries.keys()), "Select Venue", 5)
    #now get venues in this
    venue = random.choice(countries[country]['places'])
    print ("Selected Stadium: " + venue['name'])
    venue_obj = Venue(name=venue['name'], run_prob=venue['run_prob'])
    #populate run_prob_t20
    run_prob_t20 = data['run_prob_t20']
    venue_obj.run_prob_t20 = run_prob_t20
    #choose weather
    weather = choice(list(resources.weathers.keys()), 1, p=resources.weather_prob, replace=False)[0]
    venue_obj.weather = weather
    PrintInColor(resources.weathers[weather], Style.BRIGHT)
    return venue_obj

#read teams and
def ReadTeams(json_file):
    Teams_List = []
    f=open(json_file)
    data = json.load(f)
    if data is not None:
        #read values for the key 'teams'
        teams = data['Teams']
        for k,v in teams.items():
            #create teams
            t = Team(name=k)
            #now create team array from the array of values
            for plr in v['players']:
                p = Player(name=plr['name'])
                if 'batting' in plr:    p.attr.batting = plr['batting']
                if 'bowling' in plr:    p.attr.bowling = plr['bowling']
                if 'spinner' in plr and plr['spinner'] == 1:    p.attr.isspinner = True
                if 'pacer' in plr and plr['pacer'] == 1:  p.attr.ispacer = True
                if 'keeper' in plr and plr['keeper'] == 1:    p.attr.iskeeper = True
                if 'openingbowler' in plr and plr['openingbowler'] == 1:    p.attr.isopeningbowler = True
                t.team_array.append(p)
                if 'captain' in plr and plr['captain'] == 1: t.captain = p
            t.key = v["key"]
            t.opening_pair = [t.team_array[0], t.team_array[1]]
            #color
            t.color = resources.color_map[v["color"]]
            Teams_List.append(t)
    return (Teams_List)

#get match info
def GetMatchInfo(list_of_teams, venue):
    match=None
    intro=Randomize(commentary.intro_dialogues)
    commentator = random.sample(set(resources.commentators), 2)
    umpire = Randomize(resources.umpires)

    teams = [l.key for l in list_of_teams]
    #select overs
    overs=input('Select overs (multiple of 5)\n')
    if (overs.isdigit() == False) or \
            (int(overs)%5 != 0) or \
            (int(overs) > 50) or \
            (int(overs) <= 0):
        overs = 5
        print("Invalid entry, default {0} overs selected".format(overs))

    overs=int(overs)
    #max overs alloted for each bowler
    bowler_max_overs = overs / 5

    #input teams
    t1 = ChooseFromOptions(teams, "Select your team", 5)
    teams.remove(t1)
    t2 = ChooseFromOptions(teams, 'Select opponent', 5)
    print('Selected {0} and {1}'.format(t1,t2))
    #find teams from user input
    for t in list_of_teams:
        if t.key == t1:    team1=t
        if t.key == t2:    team2=t

    #initialize match with teams, overs
    match=Match(team1=team1, team2=team2, overs=overs, result=None)
    if overs == 50: temp = 'ODI'
    elif overs == 20:   temp = 'T20'
    else:   temp = str(overs) + ' over'
    PrintInColor('{4}, {0}, for the exciting {1} match between {2} and {3}'.format(venue.name,
                                                        temp,
                                                        team1.name,
                                                        team2.name,
                                                       intro), Fore.LIGHTCYAN_EX)
    print ('In the commentary box, myself {0} with {1}'.format(commentator[0],commentator[1]))
    print ('Umpire: {0}'.format(umpire))
    input('press enter to continue..')

    #assign match properties
    match.venue = venue
    match.umpire = umpire
    match.bowler_max_overs = bowler_max_overs

    #set overs to team also
    for t in [match.team1,match.team2]:
        t.total_overs = match.overs

    #display squad
    DisplayPlayingXI(match)
    #Want to skip balls?
    opt=ChooseFromOptions(['y','n'], "Do you want to play only highlights? y/n?", 5)
    if opt.lower() == 'y':
        match.autoplay=True
    return match

#toss
def Toss (match):
    logger = match.logger
    print('Toss..')
    if match.team1.captain is None or match.team2.captain is None:
        Error_Exit('No captains assigned!')
    print ('We have the captains {0}({1}) and {2}({3}) in the middle'.format(match.team1.captain.name,
                                                                                match.team1.name,
                                                                                match.team2.captain.name,
                                                                                match.team2.name))
    #assign captain attribute to the players
    match.team1.captain.attr.iscaptain = True
    match.team2.captain.attr.iscaptain = True

    print ('{0} is gonna flip the coin'.format(match.team2.captain.name))
    opts = ['1','2']
    call=input('{0}, Heads or tails? 1.Heads 2.Tails\n'.format(match.team1.captain.name))
    if call == '' or call not in opts:
        call = Randomize(opts)
        print("Invalid choice!..autoselected")
    call=int(call)
    coin=Randomize([1,2])
    coin=int(coin)
    if coin == call:
        msg = '{0} won the toss, elected to bat first'.format(match.team1.captain.name)
        PrintInColor(msg, match.team1.color)
        logger.info(msg)
        match.team1.batting_second=False
        match.team2.batting_second=True
    else:
        msg = '{0} won the toss, elected to bat first'.format(match.team2.captain.name)
        PrintInColor(msg, match.team2.color)
        logger.info(msg)
        match.team2.batting_second=False
        match.team1.batting_second=True
    #now find out who is batting first
    batting_first = next((x for x in [match.team1, match.team2] if x.batting_second == False), None)
    batting_second = next((x for x in [match.team1, match.team2] if x.batting_second == True), None)
    match.batting_first = batting_first
    match.batting_second = batting_second
    return match

#validate teams
def ValidateMatchTeams(match):
    if match.team1 is None or match.team2 is None:
        Error_Exit('No teams found!')
    for t in [match.team1, match.team2]:
        #check if 11 players
        if len(t.team_array) != 11:
            Error_Exit('Only {0} members in team {1}'.format(len(t.team_array), t.name))
        #check if they have keeper
        if [plr for plr in t.team_array if plr.attr.iskeeper == True] is None or []:
            Error_Exit('No keeper found in team {0}'.format(t.name))
        #get bowlers who has bowling attribute
        bowlers = [plr for plr in t.team_array if plr.attr.bowling > 0]
        if len(bowlers) < 6:
            Error_Exit('Team {0} should have 6 bowlers in the playing XI'.format(t.name) )
        else:
            t.bowlers = bowlers
            #assign max overs for bowlers
            for bowler in t.bowlers:
                bowler.max_overs = match.bowler_max_overs
    #ensure no common members in the teams
    common_players=list(set(match.team1.team_array).intersection(match.team2.team_array))
    if common_players != []:
        Error_Exit("Common players in teams found! : {0}".format(','.join([p.name for p in common_players])))

    #make first batsman on strike
    for t in [match.team1, match.team2]:
        t.opening_pair[0].onstrike=True
        t.opening_pair[0].onfield=True
        t.opening_pair[1].onstrike=False
        t.opening_pair[1].onfield=True

    #check if players have numbers, else assign randomly
    for t in [match.team1, match.team2]:
        for player in t.team_array:
            if player.no == None:
                player.no = random.choice(list(range(100)))

    PrintInColor('Validated teams', Style.BRIGHT)
