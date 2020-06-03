#! /usr/bin/env python3
from functions.functions import*

if __name__ == "__main__":
    #input teams to play
    match=GetMatchInfo()

    #logging
    import os
    ScriptPath = os.path.dirname(os.path.abspath(__file__))
    log_file = 'log_{0}_v_{1}_{2}_{3}_ovrs.log'.format(match.team1.name,
                                                   match.team2.name,
                                                   match.venue.name,
                                                   str(match.overs))
    log = os.path.join(ScriptPath,'logs',log_file)
    if os.path.isfile(log): os.remove(log)
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log)
    logger.addHandler(handler)
    #add logger to match
    match.logger = logger

    #see if teams are valid
    ValidateMatchTeams(match)
    #toss, select who is batting first
    match=Toss(match)
    match.team1=match.batting_first
    match.team2=match.batting_second
    #play one inns
    Play(match, match.team1, match.team2, match.team1.opening_pair, match.team2.bowlers)
    DisplayScore(match, match.team1)
    DisplayBowlingStats(match, match.team2)
    #play second inns with target
    match.team2.target = match.team1.total_score+1
    Play(match, match.team2, match.team1, match.team2.opening_pair, match.team1.bowlers)
    DisplayScore(match, match.team2)
    DisplayBowlingStats(match, match.team1)
    #show results
    result = CalculateResult(match)
    match.result = result
    MatchSummary(match)
    FindPlayerOfTheMatch(match)
    handler.close()
    input('End of the Match.. Thanks for watching !!.. Press enter to exit')
