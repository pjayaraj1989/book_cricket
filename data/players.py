#this is something like a player database
from functions.helper import *

extras = Player(name='Extra')

dhawan=Player(name='S. Dhawan',attr=PlayerAttr(batting=8))
rsharma=Player(name='R. Sharma', attr=PlayerAttr(batting=8))
kohli=Player(name='V. Kohli',attr=PlayerAttr(batting=8))
klrahul=Player(name='K.L. Rahul',attr=PlayerAttr(batting=7))
dkarthik=Player(name='D. Karthik',attr=PlayerAttr(batting=6))
dhoni=Player(name='M.S. Dhoni',attr=PlayerAttr(batting=7,iskeeper=True))
hpandya=Player(name='H. Pandya',attr=PlayerAttr(bowling=6,batting=6))
ashwin=Player(name='R. Ashwin',attr=PlayerAttr(bowling=8,isspinner=True))
bkumar=Player(name='B. Kumar',attr=PlayerAttr(bowling=8, isopeningbowler=True))
shami=Player(name='M. Shami',attr=PlayerAttr(bowling=8))
bumrah=Player(name='J. Bumrah',attr=PlayerAttr(bowling=9))
jadeja=Player(name='R. Jadeja',attr=PlayerAttr(bowling=7,batting=7))

warner=Player(name='D. Warner',attr=PlayerAttr(batting=8))
finch=Player(name='A. Finch',attr=PlayerAttr(batting=7))
khawaja=Player(name='U. Khawaja',attr=PlayerAttr(batting=7))
ssmith=Player(name='S. Smith',attr=PlayerAttr(batting=8))
smarsh=Player(name='S. Marsh',attr=PlayerAttr(batting=8))
maxwell=Player(name='G. Maxwell',attr=PlayerAttr(batting=7,bowling=6, isspinner=True))
stoinis=Player(name='M. Stoinis',attr=PlayerAttr(bowling=6, batting=6))
carey=Player(name='A. Carey', attr=PlayerAttr(batting=6, iskeeper=True))
cummins=Player(name='P. Cummins',attr=PlayerAttr(bowling=8, isopeningbowler=True))
starc=Player(name='M. Starc',attr=PlayerAttr(bowling=8, isopeningbowler=True))
bdorff=Player(name='J. Behrendorff',attr=PlayerAttr(bowling=7))
hazlewood=Player(name='J. Hazlewood',attr=PlayerAttr(bowling=7))
zampa=Player(name='A. Zampa',attr=PlayerAttr(bowling=7, isspinner=True))

guptill=Player(name='M. Guptill',attr=PlayerAttr(batting=8))
munro=Player(name='C. Munro',attr=PlayerAttr(batting=7))
williamson=Player(name='K. Williamson',attr=PlayerAttr(batting=8))
rtaylor=Player(name='R. Taylor',attr=PlayerAttr(batting=8))
latham=Player(name='T. Latham',attr=PlayerAttr(batting=7,iskeeper=True))
neesham=Player(name='J. Neesham',attr=PlayerAttr(batting=6, bowling=7))
dgrandhome=Player(name='C. de Grandhomme', attr=PlayerAttr(batting=6, bowling=7))
santner=Player(name='M. Santner',attr=PlayerAttr(bowling=7, isspinner=True))
henry=Player(name='M. Henry',attr=PlayerAttr(bowling=8))
southee=Player(name='T. Southee',attr=PlayerAttr(bowling=8, isopeningbowler=True))
boult=Player(name='T. Boult',attr=PlayerAttr(bowling=8, isopeningbowler=True))

roy=Player(name='J. Roy',attr=PlayerAttr(batting=8))
bairstow=Player(name='J. Bairstow',attr=PlayerAttr(batting=7))
root=Player(name='J. Root',attr=PlayerAttr(batting=8))
morgan=Player(name='E. Morgan',attr=PlayerAttr(batting=8))
stokes=Player(name='B. Stokes',attr=PlayerAttr(batting=7, bowling=7))
buttler=Player(name='J. Buttler',attr=PlayerAttr(batting=6, iskeeper=True))
woakes=Player(name='C. Woakes', attr=PlayerAttr(batting=6, bowling=7,isopeningbowler=True))
plunkett=Player(name='L. Plunkett',attr=PlayerAttr(bowling=7))
archer=Player(name='J. Archer',attr=PlayerAttr(bowling=8))
rashid=Player(name='A. Rashid',attr=PlayerAttr(bowling=7, isspinner=True))
moeen=Player(name='M. Ali',attr=PlayerAttr(bowling=7, batting=7, isspinner=True))
wood=Player(name='M. Wood',attr=PlayerAttr(bowling=8, isopeningbowler=True))

imam=Player(name='I. Ul Haq',attr=PlayerAttr(batting=8))
zaman=Player(name='F. Zaman',attr=PlayerAttr(batting=7))
azam=Player(name='B. Azam',attr=PlayerAttr(batting=8))
hsohail=Player(name='H. Sohail',attr=PlayerAttr(batting=8))
sarfraz=Player(name='S. Ahmed',attr=PlayerAttr(batting=7, iskeeper=True))
hafeez=Player(name='M. Hafeez',attr=PlayerAttr(batting=6,bowling=6, isspinner=True))
imad=Player(name='I. Wasim', attr=PlayerAttr(batting=6, bowling=7))
shadab=Player(name='S. Khan',attr=PlayerAttr(bowling=7, isspinner=True))
safridi=Player(name='S. Afridi',attr=PlayerAttr(bowling=8))
wahab=Player(name='W. Riaz',attr=PlayerAttr(bowling=7, isopeningbowler=True))
amir=Player(name='M. Amir',attr=PlayerAttr(bowling=8, isopeningbowler=True))

gayle=Player(name='C. Gayle',attr=PlayerAttr(batting=8, bowling=6, isspinner=True))
hope=Player(name='S. Hope',attr=PlayerAttr(batting=7, iskeeper=True))
dbravo=Player(name='D. Bravo',attr=PlayerAttr(batting=8))
pooran=Player(name='N. Pooran',attr=PlayerAttr(batting=8))
hetmeyer=Player(name='S. Hetmeyer',attr=PlayerAttr(batting=7))
russel=Player(name='A. Russel',attr=PlayerAttr(batting=6,bowling=7))
holder=Player(name='J. Holder', attr=PlayerAttr(batting=6, bowling=7))
brathwaite=Player(name='C. Brathwaite',attr=PlayerAttr(batting=7,bowling=7))
nurse=Player(name='A. Nurse',attr=PlayerAttr(bowling=8, isspinner=True))
cottrel=Player(name='S. Cottrel',attr=PlayerAttr(bowling=7, isopeningbowler=True))
thomas=Player(name='O. Thomas',attr=PlayerAttr(bowling=8))

amla=Player(name='H. Amla',attr=PlayerAttr(batting=8))
dekock=Player(name='Q. de Kock',attr=PlayerAttr(batting=7, iskeeper=True))
markram=Player(name='A. Markram',attr=PlayerAttr(batting=8))
duplessis=Player(name='F. du Plessis',attr=PlayerAttr(batting=8))
vander=Player(name='R. van der Dussen',attr=PlayerAttr(batting=7))
duminy=Player(name='J.P. Duminy',attr=PlayerAttr(batting=6,bowling=7, isspinner=True))
pretorius=Player(name='D. Pretorius', attr=PlayerAttr(batting=6, bowling=7))
phehlukwayo=Player(name='A. Phehlukwayo',attr=PlayerAttr(batting=7,bowling=7))
rabada=Player(name='K. Rabada',attr=PlayerAttr(bowling=8, isopeningbowler=True))
steyn=Player(name='D. Steyn',attr=PlayerAttr(bowling=8, isopeningbowler=True))
philander=Player(name='V. Philander',attr=PlayerAttr(bowling=7, isopeningbowler=True))
tahir=Player(name='I. Tahir',attr=PlayerAttr(bowling=8, isspinner=True))

dimuth=Player(name='D. Karunaratne',attr=PlayerAttr(batting=8))
kperera=Player(name='K. Perera',attr=PlayerAttr(batting=7, iskeeper=True))
thirimanne=Player(name='L. Thirimanne',attr=PlayerAttr(batting=8))
kmendis=Player(name='K. Mendis',attr=PlayerAttr(batting=8))
mathews=Player(name='A. Mathews',attr=PlayerAttr(batting=7, bowling=7))
milinda=Player(name='M. Siriwardana',attr=PlayerAttr(batting=6))
tperera=Player(name='T. Perera', attr=PlayerAttr(batting=6, bowling=7))
dsilva=Player(name='D. de Silva',attr=PlayerAttr(batting=7,bowling=7, isspinner=True))
udana=Player(name='I. Udana',attr=PlayerAttr(bowling=8))
malinga=Player(name='L. Malinga',attr=PlayerAttr(bowling=7, isopeningbowler=True))
pradeep=Player(name='N. Pradeep',attr=PlayerAttr(bowling=8))

tamim=Player(name='T. Iqbal',attr=PlayerAttr(batting=8))
soumya=Player(name='S. Sarkar',attr=PlayerAttr(batting=7,bowling=7))
shakib=Player(name='S. Al Hasan',attr=PlayerAttr(batting=8, bowling=7, isspinner=True))
rahim=Player(name='M. Rahim',attr=PlayerAttr(batting=8, iskeeper=True))
liton=Player(name='L. Das',attr=PlayerAttr(batting=7))
mahmudullah=Player(name='R. Mahmudullah',attr=PlayerAttr(batting=6))
sabbir=Player(name='S. Rahman', attr=PlayerAttr(batting=6))
mehidy=Player(name='M. Hasan',attr=PlayerAttr(batting=7,bowling=7, isspinner=True))
mashrafe=Player(name='M. Mortaza',attr=PlayerAttr(bowling=8))
rubel=Player(name='R. Hossain',attr=PlayerAttr(bowling=7, isopeningbowler=True))
mustafizur=Player(name='M. Rahman',attr=PlayerAttr(bowling=8))

#classic india
sehwag=Player(name='V. Sehwag',attr=PlayerAttr(batting=8))
sachin=Player(name='S. Tendulkar', attr=PlayerAttr(batting=8, bowling=7, isspinner=True))
ganguly=Player(name='S. Ganguly',attr=PlayerAttr(batting=8, bowling=6))
dravid=Player(name='R. Dravid',attr=PlayerAttr(batting=8, iskeeper=True))
yuvraj=Player(name='Y. Singh',attr=PlayerAttr(batting=7, bowling=8,isspinner=True))
kaif=Player(name='M. Kaif',attr=PlayerAttr(batting=7))
laxman=Player(name='V.V.S. Laxman',attr=PlayerAttr(batting=7))
mongia=Player(name='D. Mongia',attr=PlayerAttr(bowling=6,batting=6, isspinner=True))
harbhajan=Player(name='H. Singh',attr=PlayerAttr(bowling=8,isspinner=True))
zaheer=Player(name='Z. Khan',attr=PlayerAttr(bowling=8, isopeningbowler=True))
nehra=Player(name='A. Nehra',attr=PlayerAttr(bowling=8))
agarkar=Player(name='A. Agarkar',attr=PlayerAttr(bowling=8, isopeningbowler=False))
srinath=Player(name='J. Srinath',attr=PlayerAttr(bowling=9, isopeningbowler=True))
kumble = Player(name='A. Kumble',attr=PlayerAttr(bowling=8,isspinner=True))

#classic aus
gilchrist=Player(name='A. Gilchrist',attr=PlayerAttr(batting=8, iskeeper=True))
hayden=Player(name='M. Hayden', attr=PlayerAttr(batting=8))
ponting=Player(name='R. Ponting',attr=PlayerAttr(batting=8))
martyn=Player(name='R. Martyn',attr=PlayerAttr(batting=8))
symonds=Player(name='A. Symonds',attr=PlayerAttr(batting=7, bowling=8,isspinner=True))
bevan=Player(name='M. Bevan',attr=PlayerAttr(batting=7))
lehmann=Player(name='D. Lehmann',attr=PlayerAttr(bowling=6,batting=6, isspinner=True))
hogg=Player(name='B. Hogg',attr=PlayerAttr(bowling=8,isspinner=True))
warne=Player(name='S. Warne',attr=PlayerAttr(bowling=8,isspinner=True))
bichel=Player(name='A. Bichel',attr=PlayerAttr(bowling=8))
lee=Player(name='B. Lee',attr=PlayerAttr(bowling=8))
mcgrath=Player(name='G. McGrath',attr=PlayerAttr(bowling=9, isopeningbowler=True))
swaugh=Player(name='S. Waugh',attr=PlayerAttr(batting=7, bowling=8))
mjohnson=Player(name='M. Johnson',attr=PlayerAttr(batting=7, bowling=8,isopeningbowler=True))


#classic pak
anwar=Player(name='S. Anwar',attr=PlayerAttr(batting=8))
tumer=Player(name='T. Umer', attr=PlayerAttr(batting=8, iskeeper=True))
moin=Player(name='M. Khan', attr=PlayerAttr(batting=8, iskeeper=True))
yousuf=Player(name='M. Yousuf',attr=PlayerAttr(batting=8))
younis=Player(name='Y. Khan',attr=PlayerAttr(batting=8))
inzamam=Player(name='I. Ul-Haq',attr=PlayerAttr(batting=7))
afridi=Player(name='S. Afridi',attr=PlayerAttr(batting=7, bowling=7, isspinner=True))
razzaq=Player(name='A. Razzaq',attr=PlayerAttr(bowling=6,batting=6))
saqlain=Player(name='S. Mushtaq',attr=PlayerAttr(batting=6,bowling=7,isspinner=True))
akram=Player(name='W. Akram',attr=PlayerAttr(bowling=8, isopeningbowler=True))
waqar=Player(name='W. Younis',attr=PlayerAttr(bowling=8, isopeningbowler=True))
akhtar=Player(name='S. Akhtar',attr=PlayerAttr(bowling=9, isopeningbowler=True))

#classic england
trescothik=Player(name='M. Trescothick',attr=PlayerAttr(batting=8))
knight=Player(name='N. Knight', attr=PlayerAttr(batting=8))
hussain=Player(name='N. Hussain',attr=PlayerAttr(batting=8))
vaughan=Player(name='M. Vaughan',attr=PlayerAttr(batting=8))
stewart=Player(name='A. Stewart',attr=PlayerAttr(batting=7, iskeeper=True))
collingwood=Player(name='P. Collingwood',attr=PlayerAttr(batting=7, bowling=7))
flintoff=Player(name='A. Flintoff',attr=PlayerAttr(bowling=7,batting=6))
giles=Player(name='A. Giles',attr=PlayerAttr(batting=6,bowling=7, isspinner=True))
hoggard=Player(name='M. Hoggard',attr=PlayerAttr(bowling=8, isopeningbowler=True))
caddick=Player(name='A. Caddick',attr=PlayerAttr(bowling=8, isopeningbowler=True))
anderson=Player(name='J. Anderson',attr=PlayerAttr(bowling=9))

#classic srilanka
atapattu=Player(name='M. Atapattu',attr=PlayerAttr(batting=8))
jayasuriya=Player(name='S. Jayasuriya', attr=PlayerAttr(batting=8, bowling=6, isspinner=True))
adesilva=Player(name='A. de Silva',attr=PlayerAttr(batting=8, bowling=6, isspinner=True))
sangakkara=Player(name='K. Sangakkara',attr=PlayerAttr(batting=8, iskeeper=True))
jayawardene=Player(name='M. Jayawardene',attr=PlayerAttr(batting=7))
arnold=Player(name='R. Arnold',attr=PlayerAttr(batting=7, bowling=7, isspinner=True))
samaraweera=Player(name='T. Samaraweera',attr=PlayerAttr(bowling=7,batting=6, isspinner=True))
vaas=Player(name='C. Vaas',attr=PlayerAttr(batting=6,bowling=7, isopeningbowler=True))
fernando=Player(name='D. Fernando',attr=PlayerAttr(bowling=8))
gunaratne=Player(name='P. Gunaratne',attr=PlayerAttr(bowling=8))
murali=Player(name='M. Muralitharan',attr=PlayerAttr(bowling=9, isspinner=True))

#classic SA
gsmith=Player(name='G. Smith',attr=PlayerAttr(batting=8))
gibbs=Player(name='H. Gibbs', attr=PlayerAttr(batting=8))
kirsten=Player(name='G. Kirsten',attr=PlayerAttr(batting=8))
rhodes=Player(name='J.Rhodes',attr=PlayerAttr(batting=8))
kallis=Player(name='J. Kallis',attr=PlayerAttr(batting=8, bowling=7))
dippenaar=Player(name='B. Dippenaar',attr=PlayerAttr(batting=7))
boucher=Player(name='M. Boucher',attr=PlayerAttr(batting=7, iskeeper=True))
pollock=Player(name='S. Pollock',attr=PlayerAttr(bowling=7,batting=6, isopeningbowler=True))
klusener=Player(name='L. Klusener',attr=PlayerAttr(batting=6,bowling=7))
hall=Player(name='A. Hall',attr=PlayerAttr(bowling=8))
ntini=Player(name='M. Ntini',attr=PlayerAttr(bowling=8, isopeningbowler=True))
donald=Player(name='A. Donald',attr=PlayerAttr(bowling=9, isopeningbowler=True))

#classic WI
hinds=Player(name='W. Hinds', attr=PlayerAttr(batting=8))
lara=Player(name='B. Lara',attr=PlayerAttr(batting=8))
chanderpaul=Player(name='S. Chanderpaul',attr=PlayerAttr(batting=8))
hooper=Player(name='C. Hooper',attr=PlayerAttr(batting=7, bowling=7, isspinner=True))
powell=Player(name='R. Powell',attr=PlayerAttr(batting=7, bowling=6, isspinner=True))
sarwan=Player(name='R. Sarwan',attr=PlayerAttr(batting=7))
jacobs=Player(name='R. Jacobs',attr=PlayerAttr(batting=6,iskeeper=True))
dillon=Player(name='M. Dillon',attr=PlayerAttr(bowling=8, isopeningbowler=True))
drakes=Player(name='V. Drakes',attr=PlayerAttr(bowling=8))
collins=Player(name='P. Collins',attr=PlayerAttr(bowling=9, isopeningbowler=True))
ambrose=Player(name='C. Ambrose',attr=PlayerAttr(bowling=9, isopeningbowler=True))
walsh=Player(name='C. Walsh',attr=PlayerAttr(bowling=9, isopeningbowler=True))


#classic NZ
fleming=Player(name='S. Fleming', attr=PlayerAttr(batting=8))
astle=Player(name='N. Astle',attr=PlayerAttr(batting=8))
mcmillan=Player(name='C. McMillan',attr=PlayerAttr(batting=8))
styris=Player(name='S. Styris',attr=PlayerAttr(batting=7, bowling=7))
cairns=Player(name='C. Cairns',attr=PlayerAttr(batting=7, bowling=6))
mccullum=Player(name='B. McCullum',attr=PlayerAttr(batting=7, iskeeper=True))
harris=Player(name='C. Harris',attr=PlayerAttr(batting=6, bowling=7))
vettori=Player(name='D. Vettori',attr=PlayerAttr(bowling=8, isspinner=True))
adams=Player(name='A. Adams',attr=PlayerAttr(bowling=8))
tuffey=Player(name='D. Tuffey',attr=PlayerAttr(bowling=9, isopeningbowler=False))
bond=Player(name='S. Bond',attr=PlayerAttr(bowling=9, isopeningbowler=True))

#IPL2008 squads
ppatel=Player(name='P. Patel', attr=PlayerAttr(batting=8, iskeeper=True))
sraina=Player(name='S. Raina',attr=PlayerAttr(batting=8, bowling=6, isspinner=True))
amorkel=Player(name='A. Morkel',attr=PlayerAttr(batting=7, bowling=7))
lbalaji=Player(name='L. Balaji',attr=PlayerAttr(bowling=8, isopeningbowler=True))
mmorkel=Player(name='M. Morkel',attr=PlayerAttr(bowling=8, isopeningbowler=True))
kakmal=Player(name='K. Akmal',attr=PlayerAttr(batting=8, iskeeper=True))
swatson=Player(name='S. Watson',attr=PlayerAttr(batting=7, bowling=7))
ypathan=Player(name='Y. Pathan',attr=PlayerAttr(batting=7, bowling=6, isspinner=True))
swarne=Player(name='S. Warne',attr=PlayerAttr(batting=7, bowling=9,isspinner=True))
stanvir=Player(name='S. Tanvir',attr=PlayerAttr(batting=6, bowling=7,isopeningbowler=True))
mpatel=Player(name='M. Patel',attr=PlayerAttr(bowling=8))
jhopes=Player(name='J. Hopes', attr=PlayerAttr(batting=8, bowling=8))
ipathan=Player(name='I. Pathan',attr=PlayerAttr(batting=8, bowling=8,isopeningbowler=True))
pchawla=Player(name='P. Chawla',attr=PlayerAttr(batting=7, bowling=7,isspinner=True))
rpowar=Player(name='R. Powar',attr=PlayerAttr(batting=7, bowling=6,isspinner=True))
sreesanth=Player(name='S. Sreesanth',attr=PlayerAttr(bowling=7, isspinner=True))
ggambhir=Player(name='G. Gambhir', attr=PlayerAttr(batting=8))
tdilshan=Player(name='T. Dilshan',attr=PlayerAttr(batting=8, bowling=8,isspinner=True))
fmaharoof=Player(name='F. Maharoof',attr=PlayerAttr(batting=7, bowling=7))
amishra=Player(name='A. Mishra',attr=PlayerAttr(batting=7, bowling=6, isspinner=True))
masif=Player(name='M. Asif',attr=PlayerAttr(batting=6, bowling=7,isopeningbowler=True))
misbah=Player(name='M. Ul Haq',attr=PlayerAttr(batting=8))
cwhite=Player(name='C. White',attr=PlayerAttr(batting=8, bowling=7))
pkumar=Player(name='P. Kumar',attr=PlayerAttr(batting=7, bowling=6,isopeningbowler=True))
ruthappa=Player(name='R. Uthappa', attr=PlayerAttr(batting=8))
dsmith=Player(name='D. Smith',attr=PlayerAttr(batting=8))
rpsingh=Player(name='R.P. Singh',attr=PlayerAttr(batting=7, bowling=7))
mpandey=Player(name='M. Pandey',attr=PlayerAttr(batting=7, bowling=7))








