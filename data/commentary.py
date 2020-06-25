#all the commentary phrases are defined here

#commentary phrases
class commentary():
    intro_game = '*'*50 + '\n' + '*'*14 + 'Book Cricket Simulator' + '*'*14 + '\n' + '*' * 50

    intro_dialogues = ['Welcome everybody, here we are at ',
                        'Hello everyone, here we are at ',
                        'Hello and welcome everyone to ',
                        'Electrifying atmosphere here at ',
                        'Warm welcome to everybody to ']

    #Run rates
    commentary_less_req_rate = ['looks easily gettable for them',
                                'not a big task for them at all!',
                                'target looks easy but they are going to face some quality bowling attack!',
                                'looks like an easy target for them!']
    commentary_high_req_rate = ['reqd rate is really high for them!',
                                'this is gonna be a tough chase for them!',
                                'a big target and they will be facing a tough bowling attack too!',
                                'a himalayan task ahead for them! need to bat really well!',
                                'thats a big task ahead for them!']
    # comment situation based on Reqd RR
    commentary_situation_reqd_rate_low = ['they are well on course here!',
                                          'the reqd rate looks easily gettable!',
                                          'this chase looks easy for them!',
                                          'this chase is on!',
                                          'they are cruising here!',
                                          'they really know their target.. well on course!',
                                          'they are punishing the bowlers here! reqd rate is less than required',
                                          'they can get home without any hurdles with this scoring rate!',
                                          'they are chasing well here!',]

    commentary_situation_reqd_rate_high = ['required rate is high!.. they need to gear up!',
                                           'they need some big hits to boost up the run rate!',
                                           'singles and doubles wont take them home!',
                                           'need to boost up the run rate!',
                                           'required rate is going higher.. pressure building!',
                                           'bowlers are not giving them room to cope up with the reqd. rate!',
                                           'they will have to struggle to get home with this scoring rate!',
                                           'chase looks pretty sluggish!',
                                           'they need some hard hitters to stay alive in this chase!',
                                           'they really need to boost up the run rate here!']

    #comments for diff shots
    commentary_six = ['thats in the stands! ',
                      'he goes bang ! Thats a big one!',
                      'smashed it out of the park!',
                      'where do you set fielders for this man!',
                      'oh what a shot! That is been smashed out of the ground!',
                      'stand and deliver!',
                      'picked up the slow ball well and hit really hard!',
                      'he has blazed that one! go fetch that!',
                      'thats gone miles in the air!',
                      'he is dealing in sixes here!',
                      'loose delivery and punished hard!',
                      'what a biggie! it has gone into the trees!',
                      'the batsman has decided that tonights gonna be his night!',
                      'fielder in the deep will just watch it sail over the fence!',
                      'will this be taken in the deep.. no its 6!',
                      'thats a powerful shot.. will be a one bounce.. not its gone all the way for 6!',
                      'thats one of the biggest sixes ever!',
                      'that is gone, and forgotten! what a hit!',
                      'thats a flat six! beautifully hit!',
                      'thats big and the crowd will catch it! ',
                      'boy what a hit!',
                      'thats huge, its out of here!',]
    commentary_four = ['what a shot!.. that will find the fence!',
                       'oh will this be taken in the deep, oh he has dropped it.. and its 4!',
                        'the crowd is loving this!',
                       'beautiful drive and the fielder has given up the chase!',
                       'into the gap for four!',
                       'smashed through the gap!',
                       'poor delivery and deserved to be hit!',
                       'long chase for the fielder... and the ball wins the race!',
                        'how do you set fields for this batsman!',
                        'bad ball and punished!..',
                       'bad delivery.. it had 4 written all over it!',
                        'well connected!.. that will go to the boundary',
                        'Great shot! Abssollutely magnificent!. And the batsman has not moved an inch!',
                        'that will find the fence!',
                        'magnificent shot!.. ',
                        'oh unbelievable timing!',
                        'Beautiful shot.. oh sloppy fielding in the deep!',
                        'When He Hits It, It Stays Hit !',
                        'he is getting warmed up here!',
                        'boy what a shot!',
                        'right out of the middle of the bat!',
                        'what a smash!',
                        'He\'s a better player Than His statistics suggest',
                        'thats a great lesson for any youngster watching !',
                        'Terrific batting this.. what would be the reply from the bowler?',
                        'Another one of those, and there will be a chat between the bowler and his captain!',
                        'he goes bang!']
    commentary_ground_shot = ['not timed well but will get some runs',
                        'found the gap well',
                        'good ball ! but well played into the gap',
                        'into the gap',
                        'good delivery and somehow the batsman manages to get some runs out of it',
                        'very quick running',
                        'he has to hurry!',
                        'well played into the gap',
                        'edged and dropped!!! oh what a miss',
                        'in the air, dropped! batsman will get some runs too!',
                        'poor fielding, thats gifting singles and doubles to the batsman!',
                        'sloppy fielding, useful singles and doubles for the batsman',
                        'Oooh! direct hit and he wouldve gone!',
                        'thats quick running!',
                        'not timed well but lazy fielding, bowler is not happy!',
                        'singles and doubles will surely irritate the fielding captain']
    #four first  ball
    commentary_firstball_four = ['what a way to start the innings!',
                                 'glorious start to the innings!',
                                 'he starts with a bang! no pressure at all!',
                                 'explosive start! bowler is stunned!',
                                 'bowler feels the pressure now! first ball has been smoked!',
                                 'well what a start! the first ball has been goes for a boundary',
                                 'thats how you start an innings! pressure straightway on the bowler now!']
    commentary_firstball_six = ['six of the first ball!',
                                'would you believe it! six of the first ball!',
                                'explosive start! bowler is stunned!',
                                'bowler looks shell shocked! first ball has been smashed!',
                                'first ball and its dispatched! Beware bowlers!',
                                'bang! he has smashed the first ball out of here!',
                                'thats how you start an innings! pressure straightway on the bowler now!'
                                'thats hit off the first ball!.. ']

    #captain next:
    commentary_captain_to_bat_next = ['the captain walking out to the middle!',
                                      'the skipper to bat next!',
                                      'and now we have the captain at the crease',
                                      'the captain now has a job to do!',
                                      'crowd cheering as the captain walks out to bat',
                                      'the skipper, to walk into the ground now',
                                      'huge applause as the captain is going into the middle']

    #captain out
    commentary_captain_out = ['got rid of the skipper!',
                              'the captain goes!',
                              'got the skipper!',
                              'thats the end of the captain!',
                              'yes! the skippers is gone!']
    #captain leading
    commentary_captain_leading = ['captain leading from the front',
                                  'captain courageous!',
                                  'thats how you lead your team! bravo skipper!',
                                  'he is a perfect example of a brave leader!',
                                  'the skipper leading from the front here']

    #comments for wkts
    commentary_one_down = ['they draw first blood!',
                           'the opening stand is broken!',
                           'first one down!',
                           'the bowling team draw first blood!',
                           'one down!']

    #half the side is down
    commentary_five_down = ['half the side is back in the pavilion!',
                            'job half done!.. 5 wkts down!',
                            '5 down and i am afraid the flood gates have opened!',
                            'half down and the tail is exposed!']

    #commentary last man
    commentary_lastman = ['last man coming out to bat!',
                          '9 down, last wicket coming out to bat',
                          'now they will be trying to mop up the tail!',
                          'tail ender coming out into the middle!']

    #diff types of dismissals
    commentary_hit_wkt = ['gone! he has hit the stumps!']
    commentary_bowled = ['full and straight what a ball',
                        'what a yorker! he is on fire!',
                        'bowled himm!',
                         'got him! and the bowler lets out a roar!',
                         'perfect length, that has hit the top of off-stump!',
                        'Middle stump out of here',
                        'inside edge and bowled!',
                        'dragged on to the stumps',
                        'done him and shattered the stumps!',
                        'he has made an awful mess of the stumps!',
                        'knocked him over with a ripper!',
                        'oh hes played it on!.. Batsman would be so dissapointed',
                        'oh what a delivery!.. Perfect line and length!',
                        'Bowled him!! comprehensively bowled!',
                        'knocked his stumps over!',
                        'off stump out of the ground!',
                        'bowled him! You beauty!',
                         'done him! peach of a delivery!',
                        'Knocked his middle stump out!... And there is a stare at the batsman!',
                        'Bowled him! And he is showing the batsman the way to the dressing room!',
                        'done him with a toe crushing yorker!',
                        'oh bowledimm!, an unplayable delivery!',]
    commentary_in_a_row = ['thats 3 in a row!',
                            'three in a row now!, bowler is clueless here',
                            'three in a row!']
    commentary_reverse = ['Oh thats reversed!',
                          'the ball has reversed!',
                          'he gets it to reverse!',
                          'oh yes he gets it to reverse!',
                          'reverse swinging delivery !',
                          'magnificent reverse swinging delivery!',
                          'brilliant reverse swinger this!']
    commentary_swing = ['Terrific inswinger!',
                        'superb inswinger!',
                        'outswinging delivery!',
                        'wild swinging delivery!',
                        'what a peach! that swung inside! ',
                        'beautiful seam position.. swinging in!',
                        'he has this ability to swing the ball both ways!',
                        'thats quick and it swung a long way!!',
                        'oh that swung a long way!',
                        'brilliant outswinger!',
                        'unbelievable swing!']
    commentary_turn = ['that ball turned a long way!',
                       'oh that spun a long way!',
                       'terrific spin bowling this!',
                       'terrific spin! the batsman cant believe it!',
                       'oh it turned a long way! surprised even the bowler!',
                       'what a turn! the batsman is stunned!',
                       'that spun like never before!',
                       'deceived by the googly!',
                       'that was the one which didnt turn!,, batsman is fooled!',
                       'that ball turned so sharp!!',
                       'that was the wrong-un!',
                       'beautiful top spinner!',
                       'what a delivery!.. terrific spin!',
                       'oh what a turn! and the batsman is fooled completely!',
                       'what a turn! it has stunned the batsman!',]
    commentary_runout = ['what a terrible mix up!',
                            'this is bizzare!.. terrible miscommunication',
                            'dead accurate throw from the fielder!',
                            'this is poor running! that was a wrong call!',
                            'magnificent fielding.. brilliant throw!',
                            'he is coming back for the second.. direct hit and gone!',
                            'that was a horrible call!',
                            'there was absolutely no run there! poor running between the wkts!',
                            'that is horrific! where was the run there?',
                            'lazy running between the wickets at this stage of the match!',
                            'horrible running between the wickets!',
                            'magnificent throw and the batsman knows it! good fielding!',
                            'brilliant throw and good collection! umpire need not review this!',
                            'there was no run there! this is bizzare!',
                            'rocket arm from the fielder! what a throw!',
                            'direct hit and gone!',
                            'thats gone.. runout!! never run off a mis-field!',
                            'what was the batsman thinking!?']
    commentary_stumped = ['swift work by the keeper!',
                            'thats out! stumped!',
                            'batsman misses it and swift work behind the stumps!',
                            'stumped, no need to refer it!',
                            'fast hands behind the stumps!',
                            'very quick piece of stumping!',
                            'terrific stumping!',
                            'quick stumping! keeper appeals, umpire says out!',
                            'lightning quick behind the stumps']
    commentary_caught = ['in the air.. and taken!',
                            'thats straight up in the air.. taken!',
                            'bad shot.. leading edge and gone!',
                            'outside edge and a magnificent catch!',
                            'thats not timed well and oh what a catch!',
                            'in the air thats taken! what a blinder!',
                            'brilliant catch! he is a supreme athelete!',
                            'oh man! what a catch! one of the best catches ever!',
                            'thats in the air, has he dropped it, no he hasnt! what a catch!',
                            'thats hit straight down the fielders throat!',
                            'hit in the air and what a catch!...unbelievable catch!',
                            'straight up in the air.. fielder says mine.. takes it in the end!',
                            'hit very hard but straight to the fielder.. batsman cant believe what he has done!',
                            'magnificent catch..! ..diving in the air!',
                            'in the air and taken! batsman looks shell shocked! what a catch!',
                            'hit in the air...brilliant dive! what a take! batsman looks stunned!',
                            'up in the air and oh what a catch! one handed!',
                            'hit hard to the fielder and he takes it!',
                            'hit straight down the fielder\'s throat!',
                            'in the air and oh! has he taken that? He has! what a catch!']

    #modify this as per DRS
    commentary_lbw_umpire = ['big appeal.. and the finger goes up!',
                             'that looks in line and umpire says out!',
                             'looks plumb, and the finger raises!',
                             'hit on the pads! and given out!',
                             'looks dead straight to me... and umpire says out!',
                             'thats a big appeal.. and finally given lbw!!',
                             'big appeal.. and umpire says out! oh that looks like a harsh decision!',]
    commentary_lbw_drs_taken = ['batsman looks confused.. long chat with his partner.. and finally takes it upstairs!',
                                'long discussion with his partner.. and finally decides to go for the DRS',
                                'Oh they are going with the DRS.. looks like a review wasted?',
                                'He is having a chat with the non striker.. and decides to opt for the DRS',
                                'This is a tough call.. Will they waste a DRS chance here?',
                                'well, he hasnt even discussed with the non-striker, has gone upstairs instantly!',
                                'well he has gone for the review instantly!']
    commentary_lbw_drs_not_taken = ['long chat with the non striker.. and finally he is walking off..',
                                    'it looked close to me, they will not be wasting a DRS chance here',
                                    'Will he go upstairs, dont think so.. he is walking off the field',
                                    'are they going for the DRS here? I dont think so..']
    commentary_lbw_decision_stays = ['Well it shows that the ball will be hitting the top of off!. Decision stays!',
                                     'Pitching in line, impact in line.. hitting middle!',
                                     'missing leg? No! thats out',
                                     'Its pitching in-line! Hitting middle and leg.. Decision stays! He has to go!']
    commentary_lbw_overturned = ['It shows the ball missing the stumps by an inch! not out!',
                                 'Impact in line, but wickets missing!',
                                 'pitching in line, impact in line, wkts.. missing! good review!',
                                'Oh thats missing the top of off by inches!.. decision will be overturned!']
    commentary_lbw_edged_outside = ['DRS says there is bat involved! Overturned!.. well that saves them a review',
                                    'impact outside leg!.. this will be overturned',
                                    'impact outside off!...',
                                    'pitching outside off.. impact outside off!',
                                    'DRS says thats pitching outside leg! Not out!',
                                    'there is a slight nick!.. ',
                                    'Oh there is an inside edge...? This will be given not out!',]
    commentary_lbw = [ 'trapped him in front! ',
                        'given out, batsman is not happy at all',
                        'the batsman doesnt look happy! he is shaking his head!',
                        'batsman shakes his head',
                        'batsman looks unhappy, he thinks it was outside the line',]
    commentary_lbw_nomore_drs = ['they donot have any more DRS reviews left!',
                                 'they have used all their review chances!',
                                 'No more reviews left!']

    commentary_return_catch = ['beautiful return catch!',
                               'oh what a return catch!',
                               'oh he has dropped.. no he hasnt! what a catch!',
                               'thats out, caught n bowled!',
                               'caught and bowled! what a reflex!',
                               'what kind of reflexes by the bowler! Thats taken!',
                               'hit it hard but taken by the bowler himself!']

    commentary_dot_ball_pacer = ['swing and a miss.. no run!',
                                 'its a short one and hit him on the shoulder!',
                                 'oh thats a nasty bouncer! hit the batsman!',
                                 'ooh it bounced and hit the batsman!',
                                 'oh that has hit the batsman on the helmet!',
                                 'oh thats a quick delivery!',
                                 'its fast and swinging dangerously.. missed the off stump!',
                                 'dangerous delivery! batsman had no clue about it',
                                 'that bounced too much.. batsman had no clue.. and well taken by the keeper too!',
                                 'dangerous short ball.. !',]

    commentary_dot_ball = ['beautiful delivery, missed the stumps by inches!',
                            'thats well defended!',
                            'thats a solid defence',
                            'thats a textbook defence!',
                            'big big appeal ... but umpire shakes his head!',
                            'He\'s Bowling a Good Line and Length',
                            'edged and dropped at first slip!.. oh dear!',
                            'swings and misses.. batsman living dangerously!',
                            'in the air and oh.. ! put down!',
                            'in the air but drops safe..!',
                            'deceived the batsman.. and the bowler gives him a stare!',
                            'big appeal.. but umpire says not out!',
                            'that looks close, but not out says the umpire!',
                            'missed it, there is a stare from the bowler',
                            'oh swing and a miss!.. batsman is looking nervous!',
                            'hit well but straight to the man at short extra cover!.. well fielded!',
                            'magnificent delivery.. just above the bails to the keeper!',
                            'oh tantalizingly close to the stumps... a near miss!',
                            'bowler thinks there is an edge..? keeper is appealing.. but the umpire shakes his head!',
                            'thats in the air but put down by the keeper! oh what a miss!',
                            'decieved the batsman and nearly missed the offstump',
                            'thats in the air and chance goes down! goodness me! catches win matches',
                            'in the air and this should be out. oh dropped! goodness me!',
                            'straight up in the air, oh he has dropped it!',
                            'oh that was perilously close to the off stump!, batsman looking nervous here!',
                            'outside off and he misses that!',
                            'oh that was a quick one!',
                            'mistimed. should be taken.. and dropped!.. dear o dear!',
                            'beautiful slow ball.. fooled the batsman!',
                            'thats straight up in the air, keeper says mine.. oh and put down!',
                            'thats in the air but falls in no mans land',
                            'driven nicely but the fielder was lightning quick! saved a certain boundary!',
                            'played well but straight to the fielder!',
                            'slower ball and he misses it!']

    #MILESTONES
    commentary_partnership_milestone = ['this has been a terrific partnership!',
                                        'what a partnership this has been!',
                                        'what a useful partnership!',
                                        'this was a magnificent partnership!',
                                        'one of the best partnerships ever!',
                                        'ends a terrific partnership between these two!']

    commentary_out_first_ball = ['Out first ball!',
                                    'gone without tickling the scoreboard!',
                                    'gone... first ball wicket!',
                                    'Disappointment for the batsman! gone for a duck!',
                                    'Thats a slow walk back when youre out first ball!',
                                    'He is out without disturbing the scoreboard!',]

    commentary_nineties = ['Oh he will be so disappointed! Gone in the nervous nineties!',
                           'oh what a shame! missed a deserving century!',
                           'gone in the nervous nineties! he will be so disappointed here!',
                           'needless shot! lost a brilliant century!',
                           'oh gone in the nineties.. the batsman will be kicking himself!',
                           'unlucky! gone in the nineties!',
                           'oh missed a well deserving ton!']

    commentary_out_duck = ['The batsman will be so disappointed.. he is gone for nothing!',
                           'gone for a duck! His nightmare continues!',
                           'thats his second duck in a row in this season!',
                           'slow walk back when youre gone for a duck!',
                           'out for nothing!',
                           'gone for none! The scoreboard is undisturbed by him!',
                           'gone for zero.. disappointment for the batsman!',
                           'he hasnt troubled the scoreboard!']

    commentary_out_fifty = ['what a valuable innings!',
                            'useful innings comes to a close!',
                            'he is out but the damage is done!',
                            'big applause from the crowd!',
                            'standing ovation for this !',
                            'the crowd acknowledge this innings! brilliant!',
                            'the party is over, the crowd loved the innings!',
                            'take a bow, what an innings it was!',
                            'terrific knock comes to an end!',
                            'end of a brilliant innings']

    commentary_wide = ['he has lost his line completely!',
                            'oh thats a harsh call from the umpire!',
                            'not good bowling from him!',
                            'this will irritate the captain!',
                            'he is leaking runs here!',
                            'leg side.. umpire says wide!',
                            'he has lost his line!',
                            'poor bowling, wide delivery!',
                            'oh big appeal from the keeper but Wide says the umpire!',
                            'bowler under pressure here!',]

    commentary_no_ball = ['good delivery , batsman misses it.. but No ball called!',
                          'well bowled.. but no ball!',
                          'lost his run up !',
                          'oh thats a dangerous beamer! no ball called!',
                          'bowler tries a full toss but thats way above waist height!',
                          'bowler loses his rhythm! no ball called',
                          'bowled him! but oh thats a no ball!',
                          'in the air and taken!. but no ball called!!',
                          'oh thats a high full toss! no ball called!']

    commentary_milestone = ['Its been a terrific knock..!',
                                'what a performance...!',
                                'Take a bow! What a knock!',
                                'Absolutely magnificent innings!',
                                'he is playing a gem of an innings!',
                                'this man is on fire today!',
                                'he decides tonight is going to be his night!',
                                'Thats it! A brilliant knock under pressure!',
                                'he is on absolute fire here !']

    commentary_goingtolose = ['surely its all over now!',
                              'its literally impossible to win now!',
                              'that, I am sure, is the final nail on the coffin!',
                              'thats the end of all hopes for them now!',
                              'its surely all over..!',
                              'they need some miracle to win this match!',
                              'one by one they are going down the drain!',
                              'now, the bowling captain eyes victory for sure!',]

    commentary_fifer = ['what a bowler he is!',
                        'he has totally rattled this batting team!',
                        'he is on absolute fire!',
                        'he has been on fire with the ball today!',
                        'thats a fantastic five-fer!',
                        'he has intimidated every batsmen today!',
                        'he has made an aweful mess of this innings!',]

    commentary_hattrick = ['thats it! thats a hattrick !!',
                           'Hattrick for the bowler!',
                           '3 in 3! This man is on absolllute fire!',
                           'hattrick for the bowler! what a performance from him!',]

    commentary_keeper_catch = ['edged.. and taken!',
                                'there is an edge and what a catch by the keeper!',
                                'thin edge, big appeal behind the stumps! given!',
                                'is there an edge? Yes it is!',
                                'edged and brilliant dive from the keeper!',
                                'ooh there is an edge? Keeper appeals, bowler appeals...given!',
                                'outside edge and brilliantly taken by the keeper!',
                                'oh is there a nick!? Batsman is walking...!',
                                'straight up in the air, keeper says mine and takes it!',]

    commentary_match_won = ['thats it, thats the end of the match!',
                            'thats it, they have won the match!',
                            'thats the end of the match!']

    commentary_all_out = ['thats it! they have been bowled out!',
                          'terrific bowling performance, they have been bowled out!',
                          'its all over for them!',
                          'done ! all out!']

    #LAST OVER/MATCH/INNS
    # LAST BALL OF THE MATCH
    commentary_last_ball_match = ['this is it.. the last ball of the match!',
                                  'we are down to the last ball of the match',
                                  'last ball of this match coming up!']

    commentary_last_ball_innings = ['last ball of this innings !']

    commentary_last_over_match = ['last over of the match!',
                                  'last over! the crowd on their feet!',
                                  'we are all set to witness a last over thriller!',
                                  'here we go! last over of this match!',
                                  'this is what it has come down to! the last over!']

    commentary_last_over_innings = ['last over of this innings coming up',
                                    'we are down to the last over!',
                                    'last over of the innings!']

    #chasing and lost
    commentary_lost_chasing = ['end of the match.. end of the chase!!',
                               'afraid to say thats the end of the chase',
                               'they have failed in this chase!',
                               'they fought well, but the bowlers dominated today!',
                               'the pressure was too much for them!',
                               'the bowling team was too good for them!',
                               'they were totally outsmarted by the bowling team!',
                               'they have succumbed to pressure!']

    #maiden
    commentary_expensive_over=['what an expensive over!',
                               'a costly over.. they will have to pay for this!',
                               'an expensive over! this could turn the course of the match!',
                               'costly over.. this could change the match!',
                               'expensive over.. the bowler is shattered!',
                               'poor bowling.. expensive over!',
                               'thats an expensive over from the bowler!',]

    #good over
    commentary_economical_over = ['what an over.. very economical!',
                                  'magnificent over.. ',
                                  'superb over .. very disciplined!',
                                  'very economical bowling!',
                                  'an economical over !']

    #bowler's last over
    commentary_bowler_last_over = ['this is the last of his allotted overs!',
                                   'bowling his last over!',
                                   'he is going to bowl the last of his allotted overs',
                                   'bowler with his last over!',
                                   'he is gonna bowl his last over!']

    #check if bowler had a good spell
    commentary_bowler_good_spell = ['he had a terrific spell so far!',
                                    'he was in good form today!',
                                    'he bowled really well today!',
                                    'he had a nice spell so far!',
                                    'he had a good day with the ball!',]

    commentary_bowler_bad_spell = ['he didnt have a good day so far!',
                                   'he was very expensive today!',
                                   'he was not in form today!.. too expensive',
                                   'he was not in good touch today!',
                                   'he didnt have a good day with the ball',]

    #check if bowler is spinner
    commentary_spinner_into_attack = ['the spinner, to start the over!',
                                      'spinner into the attack!.. lets see if he gets the ball to turn!',
                                      'we have a spin bowler into the attack',
                                      'the spinner to start his over',
                                      'we have a spinner to bowl this over',
                                      'the spin bowler to start the over',]

    commentary_pacer_into_attack = ['a pacer into the attack now!',
                                    'a pacer into the attack!.. lets see if he can get some swing',
                                    'seamer to start a new over',
                                    'a fast bowler to start a new over!',
                                    'a quick bowler into the attack here',
                                    'the seamer to begin a new over.. ',
                                    'we have a fast bowler into the attack',]

    commentary_medium_into_attack = ['medium pacer into the attack',
                                     'a medium pacer, to start a new over',
                                     'the medium pacer to start the over.. lets see if he can induce a wicket',
                                     'we have a medium bowler into the attack',]

    #check if bowler is captain
    commentary_captain_to_bowl = ['skipper to bowl a new over',
                                  'captain to start a new over here!',
                                  'skipper, to begin a new over',
                                  'captain to bowl now!',
                                  'lets see if the captain can make an impact!',
                                  'captain is going to try an over now!',
                                  'captain coming on to bowl this over!']

    commentary_maiden_over = ['what a bowler.. thats a maiden over!',
                              'maiden over!!!.. brilliant!',
                              'thats it.. its a maiden over.. brilliant!']

    #rain
    commentary_rain_cloudy = ['well it looks cloudy and looks like it might rain..',
                              'oops.. there are some rain clouds above us.. ',
                              'weather doesnt look good.. can see the rain clouds developing....']

    commentary_rain_drizzling = ['this is not looking good, a slight drizzle.. we can see raincoats among the crowd',
                                 'it started drizzling a little now..  tougher for the players',
                                 'slight drizzle, and fielding is getting tougher!.. we could see the spectators getting their coats']

    commentary_rain_heavy = ['this is bad.. it started pouring!.. Umpires looking concerned',
                             'oops it has started pouring!.. Umpires are having a chat with the players',
                             'Its raining.. !!']

    commentary_rain_interrupt = ['heavy rain I am afraid to say the match might have to be called off!',
                                 'this is an unfortunate end ! Rain has forced to call off the match',
                                 'heavy rains and the umpires and the match referee have decided to call off the match']