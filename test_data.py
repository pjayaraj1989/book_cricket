from Resources import*
from helper import*
from players import*

#set teams here
ind_squad = [sachin, sehwag, gambhir, kohli, yuvraj, dhoni, raina, ashwin, zaheer, nehra, sreesanth]
ind_squad[0].onstrike=True
team_ind=Team(ind_squad, 0, False, False, 0, "india", 0, 0, [ind_squad[0],ind_squad[1]])

#has to be odd numbered
aus_squad = [hayden, gilchrist, ponting, clarke, hussey, watson, white, hogg, johnson, lee, tait]
aus_squad[0].onstrike=True
team_aus=Team(aus_squad, 0, False, False, 0, "australia", 0, 0, [aus_squad[0], aus_squad[1]])

#has to be odd numbered
sl_squad = [tharanga, dilshan, sangakkara, jayawardene, samaraweera, kapugedera, kulashekara, perera, randiv, malinga, murali]
sl_squad[0].onstrike=True
team_sl=Team(sl_squad, 0, False, False, 0, "sri lanka", 0, 0, [sl_squad[0], sl_squad[1]])

#rsa
sa_squad = [smith,amla,kallis,devilliers,duminy,duplessis,vanvyk,botha,peterson,morkel,steyn]
sa_squad[0].onstrike=True
team_sa=Team(sa_squad, 0, False, False, 0, "south africa", 0, 0, [sa_squad[0],sa_squad[1]])

#nz
nz_squad = [guptill,bmccullum,how,taylor,franklin,styris,nmccullum,oram,mills,vettori,southee]
nz_squad[0].onstrike=True
team_nz=Team(nz_squad, 0, False, False, 0, "new zealand", 0, 0, [nz_squad[0],nz_squad[1]])

list_of_teams = [team_sl, team_aus, team_ind, team_sa, team_nz]
team_names=[l.name for l in list_of_teams]