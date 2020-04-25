from Resources import*
from helper import*
from players import*

#set teams here
ind_squad = [sachin, sehwag, gambhir, kohli, yuvraj, dhoni, raina, ashwin, zaheer, nehra, sreesanth]
ind_squad[0].onstrike=True
team_ind=Team(team_array=ind_squad,
                name="India", 
                opening_pair=[ind_squad[0],ind_squad[1]])

#has to be odd numbered
aus_squad = [hayden, gilchrist, ponting, clarke, hussey, watson, white, hogg, johnson, lee, tait]
aus_squad[0].onstrike=True
team_aus=Team(team_array=aus_squad,
                    name="Australia",
                    opening_pair=[aus_squad[0],aus_squad[1]])

list_of_teams = [team_aus, team_ind,]
team_names=[l.name for l in list_of_teams]
