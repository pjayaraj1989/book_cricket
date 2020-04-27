from Resources import*
from helper import*
from players import*

#set teams here
ind_squad = [dhawan, rsharma, kohli, klrahul, dkarthik, dhoni, hpandya, ashwin, bkumar, shami, bumrah]
ind_squad[0].onstrike=True
team_ind=Team(team_array=ind_squad,
                name="India",key='IND',
                opening_pair=[ind_squad[0],ind_squad[1]])

#has to be odd numbered
aus_squad = [warner, finch, khawaja, ssmith, maxwell, stoinis, carey, cummins, starc, bdorff, zampa]
aus_squad[0].onstrike=True
team_aus=Team(team_array=aus_squad,
                    name="Australia",key='AUS',
                    opening_pair=[aus_squad[0],aus_squad[1]])

eng_squad = [roy, bairstow, root, morgan, stokes, buttler, woakes, plunkett, archer, rashid, wood]
eng_squad[0].onstrike=True
team_eng=Team(team_array=eng_squad,
                    name="England",key='ENG',
                    opening_pair=[eng_squad[0],eng_squad[1]])

nz_squad = [guptill, munro, williamson, rtaylor, latham, neesham, dgrandhome, santner, henry, southee, boult]
nz_squad[0].onstrike=True
team_nz=Team(team_array=nz_squad,
                    name="New Zealand",key='NZ',
                    opening_pair=[nz_squad[0],nz_squad[1]])

list_of_teams = [team_aus, team_ind, team_eng, team_nz]
team_keys=[l.key for l in list_of_teams]
