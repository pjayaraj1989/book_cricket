#! /usr/bin/env python3
from functions.functions import*

def PlayMatch():
    # input teams to play
    match = GetMatchInfo()
    # logging
    import os
    ScriptPath = os.path.dirname(os.path.abspath(__file__))
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
    Play(match, match.team1, match.team2, match.team1.opening_pair, match.team2.bowlers)
    DisplayScore(match, match.team1)
    DisplayBowlingStats(match, match.team2)
    # play second inns with target
    match.team2.target = match.team1.total_score + 1
    Play(match, match.team2, match.team1, match.team2.opening_pair, match.team1.bowlers)
    DisplayScore(match, match.team2)
    DisplayBowlingStats(match, match.team1)
    # show results
    result = CalculateResult(match)
    match.result = result
    MatchSummary(match)
    FindPlayerOfTheMatch(match)
    handler.close()

if __name__ == "__main__":
    PlayMatch()
    input("Thanks for playing, goodbye!")
