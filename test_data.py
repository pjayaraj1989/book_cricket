from Resources import*

sachin=Player('Sachin',False, 0, 0, True)
sehwag=Player('Sehwag',False, 0, 0, True)
gambhir=Player('Gambhir',False, 0, 0, True)
kohli=Player('Kohli',False, 0, 0, True)
yuvraj=Player('Yuvraj',False, 0, 0, True)
dhoni=Player('Dhoni',False, 0, 0, True)
raina=Player('Raina',False, 0, 0, True)
ashwin=Player('Ashwin',False, 0, 0, True)
zaheer=Player('Zaheer',False, 0, 0, True)
nehra=Player('Nehra',False, 0, 0, True)
sreesanth=Player('Sreesanth',False, 0, 0, True)
extras_ind = Player('Extra',False,0,0,True)
#has to be odd numbered
india_squad = [sachin, sehwag, gambhir, kohli, yuvraj, dhoni, raina, ashwin, zaheer, nehra, sreesanth]
opening_pair_ind = [sachin, sehwag]
sachin.onstrike=True

#now add next team, and 
hayden=Player('hayden',False, 0, 0, True)
gilchrist=Player('gilchrist',False, 0, 0, True)
ponting=Player('ponting',False, 0, 0, True)
clarke=Player('clarke',False, 0, 0, True)
hussey=Player('hussey',False, 0, 0, True)
watson=Player('watson',False, 0, 0, True)
white=Player('white',False, 0, 0, True)
hogg=Player('hogg',False, 0, 0, True)
johnson=Player('johnson',False, 0, 0, True)
lee=Player('lee',False, 0, 0, True)
tait=Player('tait',False, 0, 0, True)
extras_aus = Player('Extra',False,0,0,True)
#has to be odd numbered
australia_squad = [hayden, gilchrist, ponting, clarke, hussey, watson, white, hogg, johnson, lee, tait]
opening_pair_aus = [hayden, gilchrist]
gilchrist.onstrike=True
