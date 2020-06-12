#! /usr/bin/env python3
from functions.functions import*

def PlayMatch():
    import os
    ScriptPath = os.path.dirname(os.path.abspath(__file__))
    # input teams to play
    data_path = os.path.join(ScriptPath,'data')
    #now get the json files available
    json_files = [f for f in os.listdir(data_path) if (f.startswith('teams_') and f.endswith('.json') == True)]
    leagues = [l.lstrip('teams_').strip('.json') for l in json_files]
    league = ChooseFromOptions(leagues, "Choose league")
    data_file = [l for l in json_files if league in l][0]
    team_data = os.path.join(data_path,data_file)
    teams = ReadTeams(team_data)

    #now read venue data
    venue_data = os.path.join(data_path,'venue_data.json')
    venue = GetVenue(venue_data)

    match = GetMatchInfo(teams, venue)
    # logging
    log_file = 'log_{0}_v_{1}_{2}_{3}_ovrs.log'.format(match.team1.name,
                                                       match.team2.name,
                                                       match.venue.name.replace(' ', '_'),
                                                       str(match.overs))
    log_folder = os.path.join(ScriptPath, 'logs')
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log = os.path.join(log_folder,log_file)
    if os.path.isfile(log): os.remove(log)
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log)
    logger.addHandler(handler)
    # add logger to match
    match.logger = logger
    # see if teams are valid
    ValidateMatchTeams(match)
    # toss, select who is batting first
    match = Toss(match)
    match.team1 = match.batting_first
    match.team2 = match.batting_second
    # play one inns
    Play(match, match.team1, match.team2)
    DisplayScore(match, match.team1)
    DisplayBowlingStats(match, match.team2)
    # play second inns with target
    match.team2.target = match.team1.total_score + 1
    Play(match, match.team2, match.team1)
    DisplayScore(match, match.team2)
    DisplayBowlingStats(match, match.team1)
    # show results
    CalculateResult(match)
    MatchSummary(match)
    FindPlayerOfTheMatch(match)
    handler.close()

if __name__ == "__main__":
    PlayMatch()
    input("Thanks for playing, goodbye!")
