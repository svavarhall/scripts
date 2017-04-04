#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os

overwatch = """

             `.-:://////::-.`            
        `-://////////////////:-`        
      -`://////////////////////:`-      
    :yhs..///:.``      ``.:///..shy:    
  `ohhhhh+`.                .`+hhhhho`  
 `shhhhhy-         ```        -yhhhhhs` 
 shhhhho          o-.s          ohhhhhs 
:hhhhhs          oh-.ho          shhhhh:
shhhhh.         +hh-.hho         .hhhhhs
hhhhhy         /hhh-.hhh+         yhhhhh
hhhhhy       /yhhhh-.hhhhy/`      yhhhhh
yhhhhh.    /yhhhhhh-.hhhhhhh/`   .hhhhhs
:hhhhhs `/yhhhhhhs-  -shhhhhhh/` shhhhh:
 shhhhhshhhhhhhs-      -ohhhhhhhshhhhhs 
 `shhhhhhhhhhs-          .ohhhhhhhhhhs` 
  `ohhhhhhhy.              .yhhhhhhho`  
    :yhhhhhhho/-.     `.-/ohhhhhhhy:    
      :yhhhhhhhhhhhyyhhhhhhhhhhhs:      
        ./shhhhhhhhhhhhhhhhhhs/.        
           `-/osyhhhhhhyso/-`           

"""

skeleton = """

            ,--. 
            ([ oo] 
            `- ^\\
            _  I`-'
        ,o(`-V' 
        |( `-H-'
        |(`--A-'
        |(`-/_\'\\
        O `'I ``\\ 
        (\  I    |\,
         \\-T-"`, |H
    
"""

giraf = """

                ._ o o
                \_`-)|_
                ,""       \ 
            ,"  ## |   ಠ ಠ. 
            ," ##   ,-\__    `.
        ,"       /     `--._;)
        ,"     ## /
    ,"   ##    /

"""

batman = """

             .  .
             |\_|\\
             | a_a\\
             | | "]
         ____| '-\___
        /.----.___.-'\\
       //        _    \\
      //   .-. (~v~) /|
     |'|  /\:  .--  / \\
    // |-/  \_/____/\/~|
   |/  \ |  []_|_|_] \ |
   | \  | \ |___   _\ ]_}
   | |  '-' /   '.'  |
   | |     /    /|:  |
   | |     |   / |:  /\\
   | |     /  /  |  /  \\
   | |    |  /  /  |    \\
   \ |    |/\/  |/|/\    \\
    \|\ |\|  |  | / /\/\__\\
     \ \| | /   | |__
          / |   |____)
          |_/

"""

fireExtinguisher = """

      ------------..
        ''........$$$$.
         /'.' $;$   '$$.
        !./'..$;$..  '$$
        !'.$;;;;;;;$. $$
        ' $;;;;;;;;;$ $$
          $;; ;;;;;;$ $$
          $;; ;;;;;;$ $$
          $;; ;;;;;;$ $$
          $;; ;;;;;;$ $$
          $;; ;;;;;;$ $$.
          $;; ;;;;;;$ '$$
          $;; ;;;;;;$
          $;; ;;;;;;$
          $;;;;;;;;;$
          dp;;;;;;;;$
           '$$$$$$$'

"""

enterprise = """

     ___________________        ____....-----....____
    (________________LL_)   ==============================
        ______\   \_______.--'.  `---..._____...---'
        `-------..__            ` ,/
                    `-._ -  -  - |
                        `-------'

"""

falcon = """

                c==o
              _/____\_
       _.,--'" ||^ || "`z._
      /_/^ ___\||  || _/o\ "`-._
    _/  ]. L_| || .||  \_/_  . _`--._
   /_~7  _ . " ||. || /] \ ]. (_)  . "`--.
  |__7~.(_)_ []|+--+|/____T_____________L|
  |__|  _^(_) /^   __\____ _   _|
  |__| (_){_) J ]K{__ L___ _   _]
  |__| . _(_) \v     /__________|________
  l__l_ (_). []|+-+-<\^   L  . _   - ---L|
   \__\    __. ||^l  \Y] /_]  (_) .  _,--'
     \~_]  L_| || .\ .\\/~.    _,--'"
      \_\ . __/||  |\  \`-+-<'"
        "`---._|J__L|X o~~|[\\
               \____/ \___|[// 
                `--'   `--+-'

"""

venus = """
 
                     .--------------.
                .---'  o        .    `---.
             .-'    .    O  .         .   `-.
          .-'     @@@@@@       .             `-.
        .'@@   @@@@@@@@@@@       @@@@@@@   .    `.
      .'@@@  @@@@@@@@@@@@@@     @@@@@@@@@         `.
     /@@@  o @@@@@@@@@@@@@@     @@@@@@@@@     O     \\
    /        @@@@@@@@@@@@@@  @   @@@@@@@@@ @@     .  \\
   /@  o      @@@@@@@@@@@   .  @@  @@@@@@@@@@@     @@ \\
  /@@@      .   @@@@@@ o       @  @@@@@@@@@@@@@ o @@@@ \\
 /@@@@@                  @ .      @@@@@@@@@@@@@@  @@@@@ \\
 |@@@@@    O    `.-./  .        .  @@@@@@@@@@@@@   @@@  |
/ @@@@@        --`-'       o        @@@@@@@@@@@ @@@    . \\
|@ @@@@ .  @  @    `    @            @@      . @@@@@@    |
|   @@                         o    @@   .     @@@@@@    |
|  .     @   @ @       o              @@   o   @@@@@@.   |
\     @    @       @       .-.       @@@@       @@@      /
 |  @    @  @              `-'     . @@@@     .    .    |
 \ .  o       @  @@@@  .              @@  .           . /
  \      @@@    @@@@@@       .                   o     /
   \    @@@@@   @@\@@    /        O          .        /
    \ o  @@@       \ \  /  __        .   .     .--.  /
     \      .     . \.-.---                   `--'  /
      `.             `-'      .                   .'
        `.    o     / | `           O     .     .'
          `-.      /  |        o             .-'
             `-.          .         .     .-'
                `---.        .       .---'
                     `--------------'

"""

ninjaTurtle = """



"""

class Question(object):
    def __init__(self, question, answer, hint_one, hint_two):
        self.question = question
        self.answer = answer
        self.hint_one = hint_one
        self.hint_two = hint_two
        self.hints = 0

    def checkAnswer(self, answer):
        if self.answer.lower() == answer.lower():
            return True
        else:
            return False

    def printQuestion(self):
        print self.question
        print '\n'

    def printHints(self):
        if self.hints == 0:
            print self.hint_one
            self.hints += 1
        elif self.hints == 1:
            print self.hint_two
            self.hints += 1
        else:
            print "I have no more hints :( sorrrrrry"

questions = [
    Question(overwatch + 'Who is the newest Overwatch champion?', 'Orisa', 'Its a ROBOT!', 'It starts with O'),
    Question(batman + 'What does Batman think is his greatest feature?', 'abs', 'He says they are rock hard', 'They are on his stomach'),
    Question(fireExtinguisher + 'What is Rumble\'s ultimate called?', 'Equalizer', 'It\'s a line of fire', 'It rhymes with Geek-vualizer'),
    Question(enterprise + 'Whats the name if the show featuring this spacecraft?', 'Star Trek', 'Your mum loves it', 'Not Star Wars but Star ...?'),
    Question(falcon + 'Who was the original owner of this spaceship?', 'Han Solo', 'He is a smuggler', 'He is the father of Kylo Ren'),
    Question(venus + 'Which planet is the second from the sun?', 'Venus', 'It\'s not mercury', 'It\'s not earth')
]

def getInput():
    return raw_input('Solution: ')

def greet():

    name = raw_input('\nWelcome to your birthday puzzle! What is your name? ')

    print '\nHi ' + name + ' and happy birthday, Here is your birthday giraf :)'
    
    print giraf

    print 'To get your presents you will need to answear a few questions! Yes I know... GIMME MY PRESENTSSSSSSS \n'

# Program start

greet()

for i, question in enumerate(questions):
    raw_input('Press enter to continue...')
    question.printQuestion()

    while(True):
        answer = getInput()

        print '----------------------------------------'
        print ''
        if question.checkAnswer(answer):
            print 'Correct!'
            print ''
            print '----------------------------------------'
            break
        else:
            print 'Incorrect\n'
            question.printHints()
            print ''
            print '----------------------------------------'

raw_input('You\'ve answered all of our questions correctly, press enter to continue...')
print '----------------------------------------'
print ''
print 'Now enjoy your hard earned skeleton!!'
print ''

print skeleton

print 'Your secret key is hidden behind the portrait of a smiling ninja turle somwhere in your house\n'
