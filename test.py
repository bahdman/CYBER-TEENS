def Users_guide():
    usage_options= ('''
   TO QUIT THE GAME INPUT -> STOP
   TO GO BACK TO MAIN MENU INPUT -> BACK 
   TO ANSWER QUESTIONS -> Answer according to thier options
                          e.g a, b, c or d. ''' )
    return usage_options
      
def main():
    print('''Which quiz would you like:
    (1) Sciences
    (2) Arts
    (3) Commercial''' )
    users_choice = input('Which would you like: ').upper()
    if users_choice == 'SCIENCES' or users_choice == 'SCIENCE' or users_choice == '1':
        Science_questions()
    elif users_choice == 'ARTS' or users_choice == 'ART' or users_choice == '2':
        Art_questions()       
    elif users_choice == 'COMMERCIAL' or users_choice == '3':
        Commercial_questions()
    elif users_choice == 'HELP':
        print(Users_guide())
        main()
    elif users_choice == 'STOP' :
        pass
    else:
        print('INVALID RESPONSE')
        main()    
   

def play_again():
    while True :
        choice= input('do you want to play again(yes/no): ').lower()
        if choice == 'yes':
            main()
        if choice == 'no':
            print('Thank you for playing')
        else:
            print('INVALID RESPONSE')
            play_again()
        return
        
def Science_questions():
    from random import sample
    score = 0
    science_questions =[
''' \n What is the full meaning of L.C.M :

 (a) Lowest converter multitude
               
 (b) Lowest common multiple
                  
 (c) Low common mutiple  \n Your answer: ''',

''' \n Which of the following is the correct definition of diffusion:

 (a) It is the movement of molecules from region of lower concentration 
     to higher concentration.
 
 (b) It is the movement of molecules from region of lower concentration 
     to higher concentration involving a semi permeable membrane.

 (c) It is the movement of molecules from region of higher concentration
     to lower concentration till they are evenly seperated. \n Your answer:  ''',

''' \n In the periodic table the 20th element is :

 (a) pottasium
            
 (b) argon
                  
 (c) calcium \n Your answer ''',

''' \n Issac newton's first law of motion(inertia) states that :

 (a) A body continues to be at motion unless an external force is
     applied.
     
 (b) A body continues to be at rest untill an external force is 
     applied.
     
 (c) The rate of change of a body is directly proportional to
     the impressed or applied force that takes place in the
     direction of force. \n Your answer:  ''',

''' \n Ships haves line painted on thier hulls which must be above water to dectect if 
 the upthrust is equal to the total weight of the ship, this line is called :

 (a) Buoyancy

 (b) Plimsol line

 (c) Cargo line \n Your answer:  ''',

''' \n Seisometers are used to measure? :

 (a) Days of the year
                 
 (b) Transverse wave

 (c) Huge amount of energy many thousands of kilometers
     underground. \n Your answer:  ''',             

''' \n A diagonal matrix is :

 (a) A matrix which has a 1 in every element of the leading diagonal,
     and 0 elsewhere.

 (b) A square matrix which all the elements are 0 except those on the 
     the diagonal from the top to bottom right.
                  
  (c) A matrix with all elements 0. \n Your answer: ''',

''' \n Among the listed formulas below which is the correct formula for the 
   total surface area of a pyramid:
                 
 (a) 1/3 base area x height
                 
 (b) area of triangular cross-section x lenght/height

 (c) sum of the area of four congruent triangular faces and
     area of the base. \n Your answer:  ''',

''' \n Calculate the rate percent per annum at which #4500 will earn
   #500 in 4 years:

 (a) 2.89%

 (b) 2.78%

 (c) 3% \n Your answer:  ''',

''' \n The first stage of cell division is :

 (a) Metaphase

 (b) Interphase

 (c) Anaphase \n Your answer:  ''',

''' \n When male gamete and the female gamete fuse it forms :

 (a) White blood cells

 (b) Zygote

 (c) Placenta \n Your answer:  ''',

''' \n The full meaning of DNA is :

 (a) Deribionucliec antigens

 (b) Deoxyribonucliec acid
                 
 (c) Deoxrybonucliec acid \n Your answer:  ''',

''' \n Which of the following element is an alkali earth metal :

 (a) Mg

 (b) Rb

 (c) Li  \n Your answer:  ''',
               
''' \n The center of the earth is very hot

 (a) True

 (b) False

 (c) Not sure \n Your answer:  ''',

''' \n The continents in which we live in have been stagnant sinse the begin of the world

 (a) True

 (b) False

 (c) Not sure \n Your answer: ''',

''' \n Which of this statements is true

 (a) The sun goes around the earth

 (b) The earth goes around the sun

 (c) The earth and the sun goes around the moon \n Your answer: ''',

''' \n How many bones do sharks have in their body

 (a) 1023

 (b) 452

 (c) 0 \n Your answer: ''',

''' \n The molten rock that comes from a volcano after it has erupted is known as what

 (a) Lava

 (b) sedimentary

 (c) Non of the stated \n Your answer: ''',

''' \n What is the closest star to the earth

 (a) Sun

 (b) Acrux

 (c) Edasich \n Your answer: ''', 

'''\n What is thr radius of the sun

 (a) 695632

 (b) 695359

 (c) 695143 \n Your answer: ''',
               ]
    science_answers= ['B',
                      'C',
                      'C',
                      'B',
                      'B',
                      'C',
                      'C',
                      'C',
                      'B',
                      'B',
                      'B',
                      'B',
                      'A',
                      'A',
                      'B',
                      'B',
                      'C',
                      'A',
                      'A',
                      'B'
                      ]
    science_question = sample(science_questions,len(science_questions))
    for check in range(len(science_question)) :
        user_answer = input(science_question[check]).upper()
        confirmation = science_questions.index(science_question[check])
        correct_answer = science_answers[confirmation]
        print(correct_answer)
        if user_answer == 'HELP':
            print(Users_guide())
            main()
        elif user_answer == 'BACK':
            main()
        elif user_answer == 'STOP':
            break
        elif user_answer == correct_answer:
           score += 1
        elif user_answer != correct_answer :
            score += 0
        else:
            print('INVALID INPUT')
        
            
    print(' ')
    print(f'You scored {score}')        
    play_again()
    



def Art_questions():
    from random import sample
    score = 0
    art_questions = [
''' \n The character matched against the hero of a play is the?

 (a) Antagonist

 (b) Protagonist

 (c) Clown

 (d) Round Character \n Your answer:  ''',
                   
''' \n He bleats like a goat is a example of?

 (a) Simile

 (b) Hyperbole

 (c) Metaphor

 (d) Euphemism \n Your answer:  ''',
                             
''' \n A simple story with a deeper meaning is called?

 (a) An allegory

 (b) An elegy

 (c) An epic

 (d) A farce \n Your answer:  ''',
                       
''' \n A poetic device which exaggerate situations or objects is known as?

 (a) Exaggeration

 (b) Romance

 (c) Hyperbole

 (d) Pun \n Your answer:  ''',
                             
''' \n The period of laughter or amusement in a tragic play is known as?
 
 (a) Comic Relief

 (b) Comedy Relief

 (c) Climax

 (d) Paradox \n Your answer:  ''',
                             
''' \n The first eight lines of a sonnet is called?

 (a) A couplet

 (b) An octave

 (c) A quatrain

 (d) A sestet \n Your answer:  ''',
                             
''' \n The last part of a literary work is known as?

 (a) Acknowledgement

 (b) Epilogue

 (c) Prologue

 (d) Conclusion \n Your answer:  ''',
             
''' \n The identical sound at the end of a poem is known as?

 (a) Mere

 (b) Refrain

 (c) Rhyme

 (d) Rhythm  \n Your answer: ''',
                             
''' \n Community development projects can be best achieved if the people are?
 (a) Cooperative

 (b) Religious

 (c) Optimistic

 (d) Knowledgeable \n Your answer:  ''',
                             
''' \n The civic obligation of a citizen includes

 (a) Political socialization

 (b) Political participation

 (c) Engaging in family planning

 (d) Engaging in business ventures \n Your answer: ''',
        
''' \n HIV/AIDS is spread mainly through
 (a) Indiscriminate sexual intercourse

 (b) Kissing and hugging

 (c) Sharing toiletries with victims

 (d) Handshake with victims \n Your answer:  ''',
                       
''' \n People living with HIV/AIDS could be assisted by

 (a) Isolating them

 (b) Showing them love

 (c) Blaming them

 (d) Avoiding them \n Your answer:  ''',
        
''' \n The system of govt whereby the powers and authorities are controlled by a single central govt is called what?
 (a)Unitary system

 (b)Federal system

 (c)Confederal system

 (d)presidential system \n Your answer: ''',
        
''' \n Which of the following countries practised mixed economy?

 (a)USA

 (b)Britain

 (c)China

 (d)Nigeria \n Your answer:  ''',
        
''' \n Theocracy is a govt ruled by who?
 (a)Nobles

 (b)Priests and religious

 (c)Old people

 (d)The military \n Your answer:  ''',
        
''' \n The Father of Nigeria Nationalism is who?

 (a)Nnamdi Azikiwe

 (b)Obafemi Awolowo

 (c)Herbert Macaulay

 (d)Ahmadu Bello \n Your answer:  ''',
        
''' \n The first executive president of Nigeria was who?

 (a)Gen.Aguiyi Ironsi

 (b)Nnamdi Azikiwe

 (c)Alhaji Shehu Shagari

 (d)Olusegun Obasanjo \n Your answer:  ''',
        
''' \n The sons of King Saul who were murdered during the battle against the Philistines were who?

 (a)Peter,James and John

 (b)Jonathan,Abinadab and Malchishua

 (c)Shem,Ham and Japhat

 (d)Joab, Abishai and Ammon \n Your answer:  ''',
        
''' \n The king of Judah who set himself ablaze in his palace and died was who?

 (a)King Ahab

 (b)King David

 (c)King Zimri

 (d)King Cyrus \n Your answer:  ''',
        
'''  The prophet who is known for true religion and social justice was who?

 (a)Prophet Elijah

 (b)Prophet Micah

 (c)Prophet Hosea

 (d)Prophet Amos \n Your answer:  '''
        ]
    
    art_answers = [
        'A',
        'A',
        'A',
        'C',
        'A',
        'B',
        'B',
        'D',
        'A',
        'B',
        'A',
        'B',
        'A',
        'D',
        'B',
        'C',
        'C',
        'B',
        'C',
        'D'
        ]
    art_question = sample(art_questions,len(art_questions))
    for check in range(len(art_question)) :
        user_answer = input(art_question[check]).upper()
        confirmation = art_questions.index(art_question[check])
        correct_answer = art_answers[confirmation]
        if user_answer == correct_answer:
            score += 1
        elif user_answer != correct_answer :
            score += 0
        if user_answer == 'HELP':
            print(Users_guide())
            main()
        elif user_answer == 'BACK':
            main()
        elif user_answer == 'STOP' :
            break
        elif user_answer == correct_answer:
           score += 1
        elif user_answer != correct_answer :
            score += 0
        else:
            print('INVALID INPUT')
        
            
    print(' ')
    print(f'You scored {score}')        
    play_again()    

    
def Commercial_questions():
    from random import sample
    score= 0 
    commercial_questions = ['''
-The act of selling in a foreign market at a price lower than cost is called

A. Dumping   
B. hedging
C. fair trading
d. under sale \n Your answer: ''',
'''
-Current account holders withdraw money through

A. Credit card
B. cheque     
C. Transfer
D. Withdrawal form \n Your answer: ''',
'''
-One of thee major problems of a sole proprietor is sourcing for

A. funds      
B. Labour
C. Raw materials
D. machineries \n Your answer: ''',
'''
Which of the following is a verbal means of communication

A. Telephone      
B. Express mail
C. Business reply services
D. Telex \n Your answer: ''',
'''
-Trade fair in nigeria are organized by

A. Ministry of commerce and industry
B. Chambers of commerce     
C. The fedral government
D. Manufacturer's association of nigeria \n Your answer: ''',
'''
-Privatization is

A. Transfer of ownership yo individual or government
B. Transfer of ownership from government to stakeholders
C. Transfer of ownership from government to individuals    
D. Government taking charge of all buisness \n Your answer:  ''',
'''
-In the law of contact, acounter officer opperates as

A. A contact
B. an acceptance
C. a rejection       
D. a receptionist \n Your answer: ''',
'''
-What is a quota

A. Tax paid on goods produced within a country
B. A  physical restriction placed on quantity of goods that can be imported  
C. Tax paid on goods produced outside a country
D. Ban on all imported goods \n Your answer: ''',
'''
-Which of the following funtion is not perform by the warehousing

A. Stabilization of price
B. production of head demand
C. creating scarcity of goods
D. storage of goods \n Your answer: ''',
f'''
-One of these is a current asset

A. fittings
B. machineries
C. motor vehincles
D. stock  \n Your answer: '''
              ]
    commercial_answers = ['A',
                          'B',
                          'A',
                          'A',
                          'B',
                          'C',
                          'C',
                          'B',
                          'C',
                          'D'
                          ]
    commercial_question = sample(commercial_questions,len(commercial_questions))
    for check in range(len(commercial_question)) :
        user_answer = input(commercial_question[check]).upper()
        confirmation = commercial_questions.index(commercial_question[check])
        correct_answer = commercial_answers[confirmation]
        if user_answer == 'HELP':
            print(Users_guide())
            main()
        elif user_answer == 'BACK':
            main()
        elif user_answer == 'STOP' :
            break
        elif user_answer == correct_answer:
            score += 1
        elif user_answer != correct_answer :
            score += 0
        else:
            print('INVALID INPUT')
    print(' ')
    print(f'You scored {score}')
    play_again()
    

    
   

print('WELCOME TO CYBER TEENS QUIZ')
print(' ')
print('''FOR INSTRUCTIONS ON HOW GAME SHOULD BE PLAYED
AND HOW TO EXIT GAME INPUT 'HELP' OR TYPE 'HELP' ''')
print(' ')
main()

