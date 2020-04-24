from Resources import*
from helper import*
from players import*

#set teams here
ind_squad = [sachin, sehwag, gambhir, kohli, yuvraj, dhoni, raina, ashwin, zaheer, nehra, sreesanth]
ind_squad[0].onstrike=True
opening_pair_ind = [ind_squad[0],ind_squad[1]]
team_ind=Team(ind_squad, 0, False, False, 0, "india", 0, 0, opening_pair_ind)

#has to be odd numbered
aus_squad = [hayden, gilchrist, ponting, clarke, hussey, watson, white, hogg, johnson, lee, tait]
aus_squad[0].onstrike=True
opening_pair_aus = [aus_squad[0], aus_squad[1]]
team_aus=Team(aus_squad, 0, False, False, 0, "australia", 0, 0, opening_pair_aus)

#has to be odd numbered
sl_squad = [tharanga, dilshan, sangakkara, jayawardene, samaraweera, kapugedera, kulashekara, perera, randiv, malinga, murali]
sl_squad[0].onstrike=True
opening_pair_sl = [sl_squad[0], sl_squad[1]]
team_sl=Team(sl_squad, 0, False, False, 0, "sri lanka", 0, 0, opening_pair_sl)

list_of_teams = [team_sl, team_aus, team_ind]
team_names=[l.name for l in list_of_teams]