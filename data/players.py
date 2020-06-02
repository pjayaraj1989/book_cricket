#this is something like a player database
from functions.helper import *

extras = Player(name='Extra')

dhawan=Player(name='Shikhar Dhawan',attr=PlayerAttr(batting=8), no=42)
rsharma=Player(name='Rohit Sharma', attr=PlayerAttr(batting=8), no=45)
kohli=Player(name='Virat Kohli',attr=PlayerAttr(batting=8), no=18)
klrahul=Player(name='K.L. Rahul',attr=PlayerAttr(batting=7), no=1)
dkarthik=Player(name='Dinesh Karthik',attr=PlayerAttr(batting=6), no=19)
dhoni=Player(name='M.S. Dhoni',attr=PlayerAttr(batting=7,iskeeper=True), no=7)
hpandya=Player(name='Hardik Pandya',attr=PlayerAttr(bowling=7,batting=6), no=33)
ashwin=Player(name='Ravichandran Ashwin',attr=PlayerAttr(bowling=8,isspinner=True), no=99)
bkumar=Player(name='Bhuvneswar Kumar',attr=PlayerAttr(bowling=8, isopeningbowler=True), no=15)
shami=Player(name='Mohammad Shami',attr=PlayerAttr(bowling=8), no=11)
bumrah=Player(name='Jasprit Bumrah',attr=PlayerAttr(bowling=9), no=93)
jadeja=Player(name='Ravindra Jadeja',attr=PlayerAttr(bowling=7,batting=7), no=8)

warner=Player(name='David Warner',attr=PlayerAttr(batting=8), no=31)
finch=Player(name='Aaron Finch',attr=PlayerAttr(batting=7), no=5)
khawaja=Player(name='Usman Khawaja',attr=PlayerAttr(batting=7), no=1)
ssmith=Player(name='Steve Smith',attr=PlayerAttr(batting=8), no=49)
smarsh=Player(name='Shaun Marsh',attr=PlayerAttr(batting=8), no=9)
maxwell=Player(name='Glenn Maxwell',attr=PlayerAttr(batting=7,bowling=6, isspinner=True), no=32)
stoinis=Player(name='Marcus Stoinis',attr=PlayerAttr(bowling=6, batting=6), no=17)
carey=Player(name='Alex Carey', attr=PlayerAttr(batting=6, iskeeper=True), no=4)
cummins=Player(name='Pat Cummins',attr=PlayerAttr(bowling=8, isopeningbowler=True), no=31)
starc=Player(name='Mitchell Starc',attr=PlayerAttr(bowling=8, isopeningbowler=True), no=56)
bdorff=Player(name='Jason Behrendorff',attr=PlayerAttr(bowling=7), no=65)
hazlewood=Player(name='Josh Hazlewood',attr=PlayerAttr(bowling=8), no=30)
zampa=Player(name='Adam Zampa',attr=PlayerAttr(bowling=7, isspinner=True), no=88)

guptill=Player(name='Martin Guptill',attr=PlayerAttr(batting=8), no=31)
munro=Player(name='Colin Munro',attr=PlayerAttr(batting=7), no=82)
williamson=Player(name='Kane Williamson',attr=PlayerAttr(batting=8), no=22)
rtaylor=Player(name='Ross Taylor',attr=PlayerAttr(batting=8), no=3)
latham=Player(name='Tom Latham',attr=PlayerAttr(batting=7,iskeeper=True), no=23)
neesham=Player(name='Jimmy Neesham',attr=PlayerAttr(batting=6, bowling=7), no=83)
dgrandhome=Player(name='Colin deGrandhomme', attr=PlayerAttr(batting=6, bowling=7), no=76)
santner=Player(name='Mitchell Santner',attr=PlayerAttr(bowling=7, isspinner=True), no=32)
henry=Player(name='Matt Henry',attr=PlayerAttr(bowling=8), no=59)
southee=Player(name='Tim Southee',attr=PlayerAttr(bowling=8, isopeningbowler=True), no=38)
boult=Player(name='Trent Boult',attr=PlayerAttr(bowling=8, isopeningbowler=True), no=18)

roy=Player(name='Jason Roy',attr=PlayerAttr(batting=8), no=1)
bairstow=Player(name='Jonny Bairstow',attr=PlayerAttr(batting=7), no=2)
root=Player(name='Joe Root',attr=PlayerAttr(batting=8), no=3)
morgan=Player(name='Eoin Morgan',attr=PlayerAttr(batting=8), no=4)
stokes=Player(name='Ben Stokes',attr=PlayerAttr(batting=7, bowling=7), no=5)
buttler=Player(name='Jos Buttler',attr=PlayerAttr(batting=6, iskeeper=True), no=6)
woakes=Player(name='Chris Woakes', attr=PlayerAttr(batting=6, bowling=7,isopeningbowler=True), no=7)
plunkett=Player(name='Liam Plunkett',attr=PlayerAttr(bowling=7), no=8)
archer=Player(name='Joffra Archer',attr=PlayerAttr(bowling=8), no=9)
rashid=Player(name='Adil Rashid',attr=PlayerAttr(bowling=7, isspinner=True), no=10)
moeen=Player(name='Moeen Ali',attr=PlayerAttr(bowling=7, batting=7, isspinner=True), no=10)
wood=Player(name='Mark Wood',attr=PlayerAttr(bowling=8, isopeningbowler=True), no=11)

imam=Player(name='Imam Ul-Haq',attr=PlayerAttr(batting=8))
zaman=Player(name='Faqar Zaman',attr=PlayerAttr(batting=7))
azam=Player(name='Babar Azam',attr=PlayerAttr(batting=8))
hsohail=Player(name='Haris Sohail',attr=PlayerAttr(batting=8))
sarfraz=Player(name='Sarfraz Ahmed',attr=PlayerAttr(batting=7, iskeeper=True))
hafeez=Player(name='Mohammad Hafeez',attr=PlayerAttr(batting=6,bowling=6, isspinner=True))
imad=Player(name='Imad Wasim', attr=PlayerAttr(batting=6, bowling=7))
shadab=Player(name='Shadab Khan',attr=PlayerAttr(bowling=7, isspinner=True))
safridi=Player(name='Shaheen Afridi',attr=PlayerAttr(bowling=8))
wahab=Player(name='Wahab Riaz',attr=PlayerAttr(bowling=7, isopeningbowler=True))
amir=Player(name='Mohammad Amir',attr=PlayerAttr(bowling=8, isopeningbowler=True))

gayle=Player(name='Chris Gayle',attr=PlayerAttr(batting=8, bowling=6, isspinner=True))
hope=Player(name='Shai Hope',attr=PlayerAttr(batting=7, iskeeper=True))
dbravo=Player(name='Darren Bravo',attr=PlayerAttr(batting=8))
pooran=Player(name='Nicholas Pooran',attr=PlayerAttr(batting=8))
hetmeyer=Player(name='Shimron Hetmeyer',attr=PlayerAttr(batting=7))
russel=Player(name='Andre Russel',attr=PlayerAttr(batting=6,bowling=7))
holder=Player(name='Jason Holder', attr=PlayerAttr(batting=6, bowling=7))
brathwaite=Player(name='Carlos Brathwaite',attr=PlayerAttr(batting=7,bowling=7))
nurse=Player(name='Ashley Nurse',attr=PlayerAttr(bowling=8, isspinner=True))
cottrel=Player(name='Sheldon Cottrel',attr=PlayerAttr(bowling=7, isopeningbowler=True))
thomas=Player(name='Oshane Thomas',attr=PlayerAttr(bowling=8))

amla=Player(name='Hashim Amla',attr=PlayerAttr(batting=8))
dekock=Player(name='Quinton deKock',attr=PlayerAttr(batting=7, iskeeper=True))
markram=Player(name='Aiden Markram',attr=PlayerAttr(batting=8))
duplessis=Player(name='Faf duPlessis',attr=PlayerAttr(batting=8))
vander=Player(name='Rossie vanderDussen',attr=PlayerAttr(batting=7))
duminy=Player(name='J.P. Duminy',attr=PlayerAttr(batting=6,bowling=7, isspinner=True))
pretorius=Player(name='Dwayne Pretorius', attr=PlayerAttr(batting=6, bowling=7))
phehlukwayo=Player(name='Andile Phehlukwayo',attr=PlayerAttr(batting=7,bowling=7))
rabada=Player(name='Kagiso Rabada',attr=PlayerAttr(bowling=8, isopeningbowler=True))
steyn=Player(name='Dale Steyn',attr=PlayerAttr(bowling=8, isopeningbowler=True))
philander=Player(name='Vernon Philander',attr=PlayerAttr(bowling=7, isopeningbowler=True))
tahir=Player(name='Imran Tahir',attr=PlayerAttr(bowling=8, isspinner=True))

dimuth=Player(name='Dimuth Karunaratne',attr=PlayerAttr(batting=8))
kperera=Player(name='Kusal Perera',attr=PlayerAttr(batting=7, iskeeper=True))
thirimanne=Player(name='Lahiru Thirimanne',attr=PlayerAttr(batting=8))
kmendis=Player(name='Kusal Mendis',attr=PlayerAttr(batting=8))
mathews=Player(name='Angelo Mathews',attr=PlayerAttr(batting=7, bowling=7))
milinda=Player(name='Milinda Siriwardana',attr=PlayerAttr(batting=6))
tperera=Player(name='Tisara Perera', attr=PlayerAttr(batting=6, bowling=7))
dsilva=Player(name='Dhananjaya deSilva',attr=PlayerAttr(batting=7,bowling=7, isspinner=True))
udana=Player(name='Isuru Udana',attr=PlayerAttr(bowling=8))
malinga=Player(name='Lasith Malinga',attr=PlayerAttr(bowling=7, isopeningbowler=True))
pradeep=Player(name='Nuwan Pradeep',attr=PlayerAttr(bowling=8))

tamim=Player(name='Tamim Iqbal',attr=PlayerAttr(batting=8))
soumya=Player(name='Soumya Sarkar',attr=PlayerAttr(batting=7,bowling=7))
shakib=Player(name='Shakib Al-Hasan',attr=PlayerAttr(batting=8, bowling=7, isspinner=True))
rahim=Player(name='Mushfiqur Rahim',attr=PlayerAttr(batting=8, iskeeper=True))
liton=Player(name='Liton Das',attr=PlayerAttr(batting=7))
mahmudullah=Player(name='Rahim Mahmudullah',attr=PlayerAttr(batting=6))
sabbir=Player(name='Sabbir Rahman', attr=PlayerAttr(batting=6))
mehidy=Player(name='Mehidy Hasan',attr=PlayerAttr(batting=7,bowling=7, isspinner=True))
mashrafe=Player(name='Mashrafe Mortaza',attr=PlayerAttr(bowling=8))
rubel=Player(name='Rubel Hossain',attr=PlayerAttr(bowling=7, isopeningbowler=True))
mustafizur=Player(name='Mustafizur Rahman',attr=PlayerAttr(bowling=8))

#classic india
sehwag=Player(name='Virender Sehwag',attr=PlayerAttr(batting=8))
sachin=Player(name='Sachin Tendulkar', attr=PlayerAttr(batting=8, bowling=7, isspinner=True), no=10)
ganguly=Player(name='Sourav Ganguly',attr=PlayerAttr(batting=8, bowling=6))
dravid=Player(name='Rahul Dravid',attr=PlayerAttr(batting=8, iskeeper=True))
yuvraj=Player(name='Yuvraj Singh',attr=PlayerAttr(batting=7, bowling=7,isspinner=True))
kaif=Player(name='Mohammad Kaif',attr=PlayerAttr(batting=7))
laxman=Player(name='V.V.S. Laxman',attr=PlayerAttr(batting=7))
mongia=Player(name='Dinesh Mongia',attr=PlayerAttr(bowling=6,batting=6, isspinner=True))
harbhajan=Player(name='Harbhajan Singh',attr=PlayerAttr(bowling=8,isspinner=True))
zaheer=Player(name='Zaheer Khan',attr=PlayerAttr(bowling=8, isopeningbowler=True))
nehra=Player(name='Ashish Nehra',attr=PlayerAttr(bowling=8), no=64)
agarkar=Player(name='Ajit Agarkar',attr=PlayerAttr(bowling=8, isopeningbowler=False))
srinath=Player(name='Javagal Srinath',attr=PlayerAttr(bowling=9, isopeningbowler=True))
kumble = Player(name='Anil Kumble',attr=PlayerAttr(bowling=8,isspinner=True))

#classic aus
gilchrist=Player(name='Adam Gilchrist',attr=PlayerAttr(batting=8, iskeeper=True))
hayden=Player(name='Matthew Hayden', attr=PlayerAttr(batting=8))
ponting=Player(name='Ricky Ponting',attr=PlayerAttr(batting=8))
martyn=Player(name='Damien Martyn',attr=PlayerAttr(batting=8))
symonds=Player(name='Andrew Symonds',attr=PlayerAttr(batting=7, bowling=6,isspinner=True))
bevan=Player(name='Michael Bevan',attr=PlayerAttr(batting=7))
lehmann=Player(name='Darren Lehmann',attr=PlayerAttr(bowling=6,batting=6, isspinner=True))
hogg=Player(name='Brad Hogg',attr=PlayerAttr(bowling=8,isspinner=True))
warne=Player(name='Shane Warne',attr=PlayerAttr(bowling=8,isspinner=True))
bichel=Player(name='Andy Bichel',attr=PlayerAttr(bowling=8))
lee=Player(name='Brett Lee',attr=PlayerAttr(bowling=9))
mcgrath=Player(name='Glenn McGrath',attr=PlayerAttr(bowling=9, isopeningbowler=True))
swaugh=Player(name='Steve Waugh',attr=PlayerAttr(batting=6, bowling=8))
mjohnson=Player(name='Mitchell Johnson',attr=PlayerAttr(batting=7, bowling=8,isopeningbowler=True))


#classic pak
anwar=Player(name='Saeed Anwar',attr=PlayerAttr(batting=8))
tumer=Player(name='Toufeeq Umer', attr=PlayerAttr(batting=8, iskeeper=True))
moin=Player(name='Moin Khan', attr=PlayerAttr(batting=8, iskeeper=True))
yousuf=Player(name='Mohammad Yousuf',attr=PlayerAttr(batting=8))
younis=Player(name='Younis Khan',attr=PlayerAttr(batting=8))
inzamam=Player(name='Inzamam Ul-Haq',attr=PlayerAttr(batting=7))
afridi=Player(name='Shahid Afridi',attr=PlayerAttr(batting=7, bowling=7, isspinner=True))
razzaq=Player(name='Abdur Razzaq',attr=PlayerAttr(bowling=6,batting=6))
saqlain=Player(name='Saqlain Mushtaq',attr=PlayerAttr(batting=6,bowling=7,isspinner=True))
akram=Player(name='Wasim Akram',attr=PlayerAttr(bowling=8, isopeningbowler=True))
waqar=Player(name='Waqar Younis',attr=PlayerAttr(bowling=8, isopeningbowler=True))
akhtar=Player(name='Shoaib Akhtar',attr=PlayerAttr(bowling=9, isopeningbowler=True))

#classic england
trescothik=Player(name='Marcus Trescothick',attr=PlayerAttr(batting=8))
knight=Player(name='Nick Knight', attr=PlayerAttr(batting=8))
hussain=Player(name='Nasser Hussain',attr=PlayerAttr(batting=8))
vaughan=Player(name='Michael Vaughan',attr=PlayerAttr(batting=8))
stewart=Player(name='Alec Stewart',attr=PlayerAttr(batting=7, iskeeper=True))
collingwood=Player(name='Paul Collingwood',attr=PlayerAttr(batting=7, bowling=7))
flintoff=Player(name='Andrew Flintoff',attr=PlayerAttr(bowling=8,batting=6))
giles=Player(name='Ashley Giles',attr=PlayerAttr(batting=6,bowling=7, isspinner=True))
hoggard=Player(name='Matthew Hoggard',attr=PlayerAttr(bowling=8, isopeningbowler=True))
caddick=Player(name='Andy Caddick',attr=PlayerAttr(bowling=8, isopeningbowler=True))
anderson=Player(name='James Anderson',attr=PlayerAttr(bowling=9))

#classic srilanka
atapattu=Player(name='Marvan Atapattu',attr=PlayerAttr(batting=8))
jayasuriya=Player(name='Sanath Jayasuriya', attr=PlayerAttr(batting=8, bowling=7, isspinner=True))
adesilva=Player(name='Aravinda deSilva',attr=PlayerAttr(batting=8, bowling=7, isspinner=True))
sangakkara=Player(name='Kumar Sangakkara',attr=PlayerAttr(batting=8, iskeeper=True))
jayawardene=Player(name='Mahela Jayawardene',attr=PlayerAttr(batting=7))
arnold=Player(name='Russel Arnold',attr=PlayerAttr(batting=7, bowling=7, isspinner=True))
samaraweera=Player(name='Thilan Samaraweera',attr=PlayerAttr(bowling=6,batting=6, isspinner=True))
vaas=Player(name='Chaminda Vaas',attr=PlayerAttr(batting=6,bowling=9, isopeningbowler=True))
fernando=Player(name='Dilhara Fernando',attr=PlayerAttr(bowling=8))
gunaratne=Player(name='Pulasti Gunaratne',attr=PlayerAttr(bowling=8))
murali=Player(name='Muttiah Muralitharan',attr=PlayerAttr(bowling=8, isspinner=True))

#classic SA
gsmith=Player(name='Graeme Smith',attr=PlayerAttr(batting=8))
gibbs=Player(name='Herschelle Gibbs', attr=PlayerAttr(batting=8))
kirsten=Player(name='Gary Kirsten',attr=PlayerAttr(batting=8))
rhodes=Player(name='Jonty Rhodes',attr=PlayerAttr(batting=8))
kallis=Player(name='Jaques Kallis',attr=PlayerAttr(batting=8, bowling=8))
dippenaar=Player(name='Boeta Dippenaar',attr=PlayerAttr(batting=7))
boucher=Player(name='Mark Boucher',attr=PlayerAttr(batting=7, iskeeper=True))
pollock=Player(name='Shaun Pollock',attr=PlayerAttr(bowling=8,batting=6, isopeningbowler=True))
klusener=Player(name='Lance Klusener',attr=PlayerAttr(batting=7,bowling=7))
hall=Player(name='Andrew Hall',attr=PlayerAttr(bowling=8))
ntini=Player(name='Makhaya Ntini',attr=PlayerAttr(bowling=9, isopeningbowler=True))
donald=Player(name='Allan Donald',attr=PlayerAttr(bowling=9, isopeningbowler=True))

#classic WI
hinds=Player(name='Wavell Hinds', attr=PlayerAttr(batting=8))
lara=Player(name='Brian Lara',attr=PlayerAttr(batting=8))
chanderpaul=Player(name='Shivnarine Chanderpaul',attr=PlayerAttr(batting=8))
hooper=Player(name='Carl Hooper',attr=PlayerAttr(batting=7, bowling=7, isspinner=True))
powell=Player(name='Ricardo Powell',attr=PlayerAttr(batting=7, bowling=6, isspinner=True))
sarwan=Player(name='Ramnaresh Sarwan',attr=PlayerAttr(batting=7))
jacobs=Player(name='Ridley Jacobs',attr=PlayerAttr(batting=6,iskeeper=True))
dillon=Player(name='Mervyn Dillon',attr=PlayerAttr(bowling=8, isopeningbowler=True))
drakes=Player(name='Vasbert Drakes',attr=PlayerAttr(bowling=8))
collins=Player(name='Pedro Collins',attr=PlayerAttr(bowling=9, isopeningbowler=True))
ambrose=Player(name='Curtly Ambrose',attr=PlayerAttr(bowling=9, isopeningbowler=True))
walsh=Player(name='Courtney Walsh',attr=PlayerAttr(bowling=9, isopeningbowler=True))

#classic NZ
fleming=Player(name='Stephen Fleming', attr=PlayerAttr(batting=8))
astle=Player(name='Nathan Astle',attr=PlayerAttr(batting=8))
mcmillan=Player(name='Craig McMillan',attr=PlayerAttr(batting=8))
styris=Player(name='Scott Styris',attr=PlayerAttr(batting=7, bowling=7))
cairns=Player(name='Chris Cairns',attr=PlayerAttr(batting=7, bowling=6))
mccullum=Player(name='Brendon McCullum',attr=PlayerAttr(batting=7, iskeeper=True))
harris=Player(name='Chris Harris',attr=PlayerAttr(batting=6, bowling=7))
vettori=Player(name='Daniel Vettori',attr=PlayerAttr(bowling=8, isspinner=True))
adams=Player(name='Andre Adams',attr=PlayerAttr(bowling=8))
tuffey=Player(name='Daryll Tuffey',attr=PlayerAttr(bowling=9, isopeningbowler=False))
bond=Player(name='Shane Bond',attr=PlayerAttr(bowling=9, isopeningbowler=True))

#IPL2008 squads
ppatel=Player(name='Parthiv Patel', attr=PlayerAttr(batting=8, iskeeper=True))
sraina=Player(name='Suresh Raina',attr=PlayerAttr(batting=8, bowling=6, isspinner=True))
amorkel=Player(name='Albie Morkel',attr=PlayerAttr(batting=7, bowling=7))
lbalaji=Player(name='Lakshmipathy Balaji',attr=PlayerAttr(bowling=8, isopeningbowler=True))
mmorkel=Player(name='Morne Morkel',attr=PlayerAttr(bowling=8, isopeningbowler=True))
kakmal=Player(name='Kamran Akmal',attr=PlayerAttr(batting=8, iskeeper=True))
swatson=Player(name='Shane Watson',attr=PlayerAttr(batting=7, bowling=7))
ypathan=Player(name='Yousuf Pathan',attr=PlayerAttr(batting=7, bowling=6, isspinner=True))
swarne=Player(name='Shane Warne',attr=PlayerAttr(batting=7, bowling=9,isspinner=True))
stanvir=Player(name='Sohail Tanvir',attr=PlayerAttr(batting=6, bowling=7,isopeningbowler=True))
mpatel=Player(name='Munaf Patel',attr=PlayerAttr(bowling=8))
jhopes=Player(name='James Hopes', attr=PlayerAttr(batting=8, bowling=8))
ipathan=Player(name='Irfan Pathan',attr=PlayerAttr(batting=8, bowling=8,isopeningbowler=True))
pchawla=Player(name='Piyush Chawla',attr=PlayerAttr(batting=7, bowling=7,isspinner=True))
rpowar=Player(name='Ramesh Powar',attr=PlayerAttr(batting=7, bowling=6,isspinner=True))
sreesanth=Player(name='Santhakumaran Sreesanth',attr=PlayerAttr(bowling=7, isspinner=True))
ggambhir=Player(name='Gautam Gambhir', attr=PlayerAttr(batting=8))
tdilshan=Player(name='Tilakaratne Dilshan',attr=PlayerAttr(batting=8, bowling=8,isspinner=True))
fmaharoof=Player(name='Farveez Maharoof',attr=PlayerAttr(batting=7, bowling=7))
amishra=Player(name='Amit Mishra',attr=PlayerAttr(batting=7, bowling=6, isspinner=True))
masif=Player(name='Mohammad Asif',attr=PlayerAttr(batting=6, bowling=7,isopeningbowler=True))
misbah=Player(name='Misbah Ul-Haq',attr=PlayerAttr(batting=8))
cwhite=Player(name='Cameron White',attr=PlayerAttr(batting=8, bowling=7))
pkumar=Player(name='Praveen Kumar',attr=PlayerAttr(batting=7, bowling=6,isopeningbowler=True))
ruthappa=Player(name='Robin Uthappa', attr=PlayerAttr(batting=8))
dsmith=Player(name='Dwayne Smith',attr=PlayerAttr(batting=8))
rpsingh=Player(name='R.P. Singh',attr=PlayerAttr(batting=7, bowling=7))
mpandey=Player(name='Manish Pandey',attr=PlayerAttr(batting=7, bowling=7))