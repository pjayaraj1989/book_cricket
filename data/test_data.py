
from data.players import*
from colorama import Fore

#set teams here
ind_squad = [dhawan, rsharma, kohli, klrahul, hpandya, dhoni, jadeja, ashwin, bkumar, shami, bumrah]
team_ind=Team(team_array=ind_squad,color=Fore.LIGHTBLUE_EX,
                name="India",key='IND',captain=kohli,
                opening_pair=[ind_squad[0],ind_squad[1]])

#has to be odd numbered
aus_squad = [warner, finch, smarsh, ssmith, maxwell, stoinis, carey, cummins, starc, hazlewood, zampa]
team_aus=Team(team_array=aus_squad,color=Fore.YELLOW,
                    name="Australia",key='AUS', captain=finch,
                    opening_pair=[aus_squad[0],aus_squad[1]])

eng_squad = [roy, bairstow, root, morgan, stokes, buttler, moeen, woakes, plunkett, archer, wood]
team_eng=Team(team_array=eng_squad,color=Fore.CYAN,
                    name="England",key='ENG',captain=morgan,
                    opening_pair=[eng_squad[0],eng_squad[1]])

nz_squad = [guptill, munro, williamson, rtaylor, latham, neesham, dgrandhome, santner, henry, southee, boult]
team_nz=Team(team_array=nz_squad,color=Fore.LIGHTMAGENTA_EX,
                    name="New Zealand",key='NZ',captain=williamson,
                    opening_pair=[nz_squad[0],nz_squad[1]])

pak_squad = [imam, zaman, azam, hsohail, sarfraz, hafeez, imad, shadab, safridi, wahab, amir]
team_pak=Team(team_array=pak_squad,color=Fore.GREEN,
                    name="Pakistan",key='PAK',captain=sarfraz,
                    opening_pair=[pak_squad[0],pak_squad[1]])

wi_squad = [gayle, hope, dbravo, pooran, hetmeyer, russel, holder, brathwaite, nurse, cottrel, thomas]
team_wi=Team(team_array=wi_squad,color=Fore.MAGENTA,
                    name="West Indies",key='WI',captain=holder,
                    opening_pair=[wi_squad[0],wi_squad[1]])

sa_squad = [amla, dekock, markram, duplessis, vander, duminy, pretorius, phehlukwayo, rabada, steyn, tahir]
team_sa=Team(team_array=sa_squad,color=Fore.LIGHTGREEN_EX,
                    name="South Africa",key='SA',captain=duplessis,
                    opening_pair=[sa_squad[0],sa_squad[1]])

sl_squad = [dimuth, kperera, thirimanne, kmendis, mathews, milinda, tperera, dsilva, udana, malinga, pradeep]
team_sl=Team(team_array=sl_squad,color=Fore.LIGHTMAGENTA_EX,
                    name="Sri Lanka",key='SL',captain=dimuth,
                    opening_pair=[sl_squad[0],sl_squad[1]])

ban_squad = [tamim, soumya, shakib, rahim, liton, mahmudullah, sabbir, mehidy, mashrafe, rubel, mustafizur]
team_ban=Team(team_array=ban_squad,color=Fore.LIGHTBLACK_EX,
                    name="Bangladesh",key='BAN',captain=mashrafe,
                    opening_pair=[ban_squad[0],ban_squad[1]])

#classic teams
#set teams here
ind_classic = [sehwag, sachin, ganguly, dravid, yuvraj, kaif, mongia, harbhajan, agarkar, zaheer, nehra]
team_ind_classic=Team(team_array=ind_classic,color=Fore.BLUE,
                name="India-Legends",key='IND_CL',captain=ganguly,
                opening_pair=[ind_classic[0],ind_classic[1]])

#has to be odd numbered
aus_classic = [gilchrist, hayden, ponting, martyn, symonds, bevan, lehmann, bichel,hogg,lee, mcgrath]
team_aus_classic=Team(team_array=aus_classic,color=Fore.YELLOW,
                    name="Australia-Legends",key='AUS_CL', captain=ponting,
                    opening_pair=[aus_classic[0],aus_classic[1]])

pak_classic = [anwar, tumer, yousuf, younis, inzamam, afridi, razzaq, saqlain,akram,waqar,akhtar]
team_pak_classic=Team(team_array=pak_classic,color=Fore.GREEN,
                    name="Pakistan-Legends",key='PAK_CL', captain=waqar,
                    opening_pair=[pak_classic[0],pak_classic[1]])

eng_classic = [trescothik,knight,vaughan,hussain,stewart,collingwood,flintoff,giles,hoggard,caddick,anderson]
team_eng_classic = Team(team_array=eng_classic,color=Fore.LIGHTBLUE_EX,
                        name="England-Legends",key='ENG_CL',captain=hussain,
                        opening_pair=[trescothik,knight])

sri_classic = [atapattu,jayasuriya,adesilva,sangakkara,jayawardene,arnold,samaraweera,vaas,fernando,gunaratne,murali]
team_sri_classic = Team(team_array=sri_classic,color=Fore.MAGENTA,
                        name="SriLanka-Legends",key='SL_CL',captain=jayasuriya,
                        opening_pair=[jayasuriya,atapattu])

sa_classic = [gsmith,gibbs,kirsten,kallis,dippenaar,boucher,pollock,klusener,hall,ntini,donald]
team_sa_classic = Team(team_array=sa_classic,color=Fore.LIGHTGREEN_EX,
                       name="SouthAfrica-Legends",key='SA_CL',captain=pollock,
                       opening_pair=[gsmith,gibbs])

wi_classic = [gayle,hinds,lara,sarwan,chanderpaul,hooper,powell,jacobs,dillon,drakes,collins]
team_wi_classic = Team(team_array=wi_classic,color=Fore.LIGHTMAGENTA_EX,
                       name="WestIndies-Legends",key='WI_CL',captain=hooper,
                       opening_pair=[gayle,hinds])

nz_classic = [fleming,astle,mcmillan,styris,cairns,mccullum,harris,vettori,adams,tuffey,bond]
team_nz_classic = Team(team_array=nz_classic,color=Fore.CYAN,
                       name="NewZealand-Legends",key='NZ_CL',captain=fleming,
                       opening_pair=[fleming,astle])

#all time XI
sachin_xi = [hayden, sachin, lara, jayawardene, hooper, boucher, klusener, pollock, kumble, murali, mcgrath]
team_sachin_xi = Team(team_array = sachin_xi,color=Fore.CYAN, name="SachinXI",key='SACHIN',captain=sachin,opening_pair=[hayden, sachin])

ponting_xi = [ganguly, jayasuriya, gibbs, ponting, sangakkara, kallis, symonds, warne, zaheer, lee, donald]
team_ponting_xi = Team(team_array=ponting_xi,color=Fore.YELLOW, name="PontingXI",key='PONTING', captain=ponting, opening_pair=[ganguly, jayasuriya])

waugh_xi = [sehwag, gilchrist, chanderpaul, swaugh, bevan, flintoff, vettori, harbhajan, mjohnson, akram, akhtar]
team_waugh_xi = Team(team_array=waugh_xi,color=Fore.GREEN, name="WaughXI", key='WAUGH', captain=swaugh, opening_pair=[sehwag, gilchrist])

#LIST OF TEAMS
teams_int = [team_aus, team_ind, team_eng, team_nz, team_pak, team_sa, team_wi, team_sl, team_ban]
teams_classic = [team_aus_classic, team_pak_classic, team_ind_classic, team_eng_classic, team_sri_classic, team_sa_classic, team_wi_classic, team_nz_classic]
teams_all_time = [team_sachin_xi, team_ponting_xi, team_waugh_xi]