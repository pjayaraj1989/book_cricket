
from data.players import*
from colorama import Fore, Style, Back

#set teams here
ind_squad = [dhawan, rsharma, kohli, klrahul, dkarthik, dhoni, jadeja, ashwin, bkumar, shami, bumrah]
ind_squad[0].onstrike=True
team_ind=Team(team_array=ind_squad,color=Fore.BLUE,
                name="India",key='IND',captain=kohli,
                opening_pair=[ind_squad[0],ind_squad[1]])

#has to be odd numbered
aus_squad = [warner, finch, smarsh, ssmith, maxwell, stoinis, carey, cummins, starc, hazlewood, zampa]
aus_squad[0].onstrike=True
team_aus=Team(team_array=aus_squad,color=Fore.YELLOW,
                    name="Australia",key='AUS', captain=finch,
                    opening_pair=[aus_squad[0],aus_squad[1]])

eng_squad = [roy, bairstow, root, morgan, stokes, buttler, moeen, woakes, plunkett, archer, wood]
eng_squad[0].onstrike=True
team_eng=Team(team_array=eng_squad,color=Fore.CYAN,
                    name="England",key='ENG',captain=morgan,
                    opening_pair=[eng_squad[0],eng_squad[1]])

nz_squad = [guptill, munro, williamson, rtaylor, latham, neesham, dgrandhome, santner, henry, southee, boult]
nz_squad[0].onstrike=True
team_nz=Team(team_array=nz_squad,color=Fore.LIGHTMAGENTA_EX,
                    name="New Zealand",key='NZ',captain=williamson,
                    opening_pair=[nz_squad[0],nz_squad[1]])

pak_squad = [imam, zaman, azam, hsohail, sarfraz, hafeez, imad, shadab, afridi, wahab, amir]
pak_squad[0].onstrike=True
team_pak=Team(team_array=pak_squad,color=Fore.GREEN,
                    name="Pakistan",key='PAK',captain=sarfraz,
                    opening_pair=[pak_squad[0],pak_squad[1]])

wi_squad = [gayle, hope, dbravo, pooran, hetmeyer, russel, holder, brathwaite, nurse, cottrel, thomas]
wi_squad[0].onstrike=True
team_wi=Team(team_array=wi_squad,color=Fore.MAGENTA,
                    name="West Indies",key='WI',captain=holder,
                    opening_pair=[wi_squad[0],wi_squad[1]])

sa_squad = [amla, dekock, markram, duplessis, vander, duminy, pretorius, phehlukwayo, rabada, ngidi, tahir]
sa_squad[0].onstrike=True
team_sa=Team(team_array=sa_squad,color=Fore.LIGHTGREEN_EX,
                    name="South Africa",key='SA',captain=duplessis,
                    opening_pair=[sa_squad[0],sa_squad[1]])

sl_squad = [dimuth, kperera, thirimanne, kmendis, mathews, milinda, tperera, dsilva, udana, malinga, pradeep]
sl_squad[0].onstrike=True
team_sl=Team(team_array=sl_squad,color=Fore.LIGHTBLUE_EX,
                    name="Sri Lanka",key='SL',captain=dimuth,
                    opening_pair=[sl_squad[0],sl_squad[1]])

ban_squad = [tamim, soumya, shakib, rahim, liton, mahmudullah, sabbir, mehidy, mashrafe, rubel, mustafizur]
ban_squad[0].onstrike=True
team_ban=Team(team_array=ban_squad,color=Fore.LIGHTBLACK_EX,
                    name="Bangladesh",key='BAN',captain=mashrafe,
                    opening_pair=[ban_squad[0],ban_squad[1]])

#classic teams
#set teams here
ind_classic = [sehwag, sachin, ganguly, dravid, yuvraj, kaif, mongia, harbhajan, zaheer, nehra, srinath]
ind_classic[0].onstrike=True
team_ind_classic=Team(team_array=ind_classic,color=Fore.BLUE,
                name="India-Legends",key='IND_CL',captain=ganguly,
                opening_pair=[ind_classic[0],ind_classic[1]])

#has to be odd numbered
aus_classic = [gilchrist, hayden, ponting, martyn, symonds, bevan, lehmann, bichel,hogg,lee, mcgrath]
aus_classic[0].onstrike=True
team_aus_classic=Team(team_array=aus_classic,color=Fore.YELLOW,
                    name="Australia-Legends",key='AUS_CL', captain=ponting,
                    opening_pair=[aus_classic[0],aus_classic[1]])

list_of_teams = [team_aus, team_ind, team_eng, team_nz, team_pak, team_sa, team_wi, team_sl, team_ban, team_aus_classic, team_ind_classic]
team_keys=[l.key for l in list_of_teams]
