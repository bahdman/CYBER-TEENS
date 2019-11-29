introduction=('''WELCOME TO CYBER TEENS QUIZ)
             Which quiz would you like:
              (1) Sciences
              (2) Arts
              (3) Commercial ''')
print(introduction)
print(' ')
print('''FOR INSTRUCTIONS ON HOW GAME SHOULD BE PLAYED
AND HOW TO EXIT GAME INPUT 'HELP' OR TYPE 'HELP' ''')
      

def Science_questions():
    score = 0
    science_questions =[
'''What is the full meaning of L.C.M :

 (a) Lowest converter multitude
               
 (b) Lowest common multiple
                  
 (c) Low common mutiple  \n Your answer: ''',

'''Which of the following is the correct definition of diffusion:

 (a) It is the movement of molecules from region of lower concentration 
     to higher concentration.
 
 (b) It is the movement of molecules from region of lower concentration 
     to higher concentration involving a semi permeable membrane.

 (c) It is the movement of molecules from region of higher concentration
     to lower concentration till they are evenly seperated. \n Your answer:  ''',

'''In the periodic table the 20th element is :

 (a) pottasium
            
 (b) argon
                  
 (c) calcium \n Your answer ''',

'''Issac newton's first law of motion(inertia) states that :

 (a) A body continues to be at motion unless an external force is
     applied.
     
 (b) A body continues to be at rest untill an external force is 
     applied.
     
 (c) The rate of change of a body is directly proportional to
     the impressed or applied force that takes place in the
     direction of force. \n Your answer:  '''

'''Ships haves line painted on thier hulls which must be above water to dectect if 
 the upthrust is equal to the total weight of the ship, this line is called :

 (a) Buoyancy

 (b) Plimsol line

 (c) Cargo line \n Your answer:  ''',

'''Seisometers are used to measure? :

 (a) Days of the year
                 
 (b) Transverse wave

 (c) Huge amount of energy many thousands of kilometers
     underground. \n Your answer:  ''',             

'''A diagonal matrix is :

 (a) A matrix which has a 1 in every element of the leading diagonal,
     and 0 elsewhere.

 (b) A square matrix which all the elements are 0 except those on the 
     the diagonal from the top to bottom right.
                  
  (c) A matrix with all elements 0. \n Your answer: ''',

'''Among the listed formulas below which is the correct formula for the 
   total surface area of a pyramid:
                 
 (a) 1/3 base area x height
                 
 (b) area of triangular cross-section x lenght/height

 (c) sum of the area of four congruent triangular faces and
     area of the base. \n Your answer:  ''',

'''Calculate the rate percent per annum at which #4500 will earn
   #500 in 4 years:

 (a) 2.89%

 (b) 2.78%

 (c) 3% \n Your answer:  ''',

'''The first stage of cell division is :

 (a) Metaphase

 (b) Interphase

 (c) Anaphase \n Your answer:  ''',

'''When male gamete and the female gamete fuse it forms :

 (a) White blood cells

 (b) Zygote

 (c) Placenta \n Your answer:  ''',

'''The full meaning of DNA is :

 (a) Deribionucliec antigens

 (b) Deoxyribonucliec acid
                 
 (c) Deoxrybonucliec acid \n Your answer:  ''',

'''Which of the following element is an alkali earth metal :

 (a) Mg

 (b) Rb

 (c) Li  \n Your answer:  ''',
               
'''The center of the earth is very hot

 (a) True

 (b) False

 (c) Not sure \n Your answer:  ''',

'''The continents in which we live in have been stagnant sinse the begin of the world

 (a) True

 (b) False

 (c) Not sure \n Your answer: ''',

'''Which of this statements is true

 (a) The sun goes around the earth

 (b) The earth goes around the sun

 (c) The earth and the sun goes around the moon \n Your answer: ''',

'''How many bones do sharks have in their body

 (a) 1023

 (b) 452

 (c) 0 \n Your answer: ''',

'''The molten rock that comes from a volcano after it has erupted is known as what

 (a) Lava

 (b) sedimentary

 (c) Non of the stated \n Your answer: ''',

'''What is the closest star to the earth

 (a) Sun

 (b) Acrux

 (c) Edasich \n Your answer: ''', 

'''What is thr radius of the sun

 (a) 695632

 (b) 695359

 (c) 695143 \n Your answer: ''',
               ]
    science_answers= ['b',
                      'c',
                      'c',
                      'b',
                      'b',
                      'c',
                      'b',
                      'c',
                      'b',
                      'b',
                      'b',
                      'b',
                      'a',
                      'a',
                      'b',
                      'b',
                      'c',
                      'a',
                      'a',
                      'b'
                      ]
    
    for check in range(len(science_questions)) :
        user_answer = input(science_questions[check]).upper()
        confirmation = science_questions.index(science_questions[check])
        correct_answer = science_answers[confirmation]
        #if user_answer == correct_answer:
         #   score += 1
        #elif user_answer != correct_answer :
         #   score += 0
        if user_answer == 'HELP':
            Users_guide()
            user_response(users_response)
        elif user_answer == 'BACK':
            print(introduction)
            break
    print(' ')
    print(f'Your score is {score}')        
    response =''        
    while response != 'stop' :
        response = input('Do you want to continue with the science quiz (yes/no) : ').lower()
        if response == 'yes' :
            Science_questions()
        elif response == 'no':
            user_response(users_response)
    #print(introduction)
            
  
    return


def Art_questions():
    score = 0
    art_questions = [
'''The character matched against the hero of a play is the?

 (a) Antagonist

 (b) Protagonist

 (c) Clown

 (d) Round Character \n Your answer:  ''',
                   
'''He bleats like a goat is a example of?

 (a) Simile

 (b) Hyperbole

 (c) Metaphor

 (d) Euphemism \n Your answer:  ''',
                             
'''A simple story with a deeper meaning is called?

 (a) An allegory

 (b) An elegy

 (c) An epic

 (d) A farce \n Your answer:  ''',
                       
'''A poetic device which exaggerate situations or objects is known as?

 (a) Exaggeration

 (b) Romance

 (c) Hyperbole

 (d) Pun \n Your answer:  ''',
                             
'''The period of laughter or amusement in a tragic play is known as?
 
 (a) Comic Relief

 (b) Comedy Relief

 (c) Climax

 (d) Paradox \n Your answer:  ''',
                             
'''The first eight lines of a sonnet is called?

 (a) A couplet

 (b) An octave

 (c) A quatrain

 (d) A sestet \n Your answer:  ''',
                             
'''The last part of a literary work is known as?

 (a) Acknowledgement

 (b) Epilogue

 (c) Prologue

 (d) Conclusion \n Your answer:  ''',
             
'''The identical sound at the end of a poem is known as?

 (a) Mere

 (b) Refrain

 (c) Rhyme

 (d) Rhythm  \n Your answer: ''',
                             
'''Community development projects can be best achieved if the people are?
 (a) Cooperative

 (b) Religious

 (c) Optimistic

 (d) Knowledgeable \n Your answer:  ''',
                             
'''The civic obligation of a citizen includes

 (a) Political socialization

 (b) Political participation

 (c) Engaging in family planning

 (d) Engaging in business ventures \n Your answer: ''',
        
'''HIV/AIDS is spread mainly through
 (a) Indiscriminate sexual intercourse

 (b) Kissing and hugging

 (c) Sharing toiletries with victims

 (d) Handshake with victims \n Your answer:  ''',
                       
''' People living with HIV/AIDS could be assisted by

 (a) Isolating them

 (b) Showing them love

 (c) Blaming them

 (d) Avoiding them \n Your answer:  ''',
        
'''The system of govt whereby the powers and authorities are controlled by a single central govt is called what?
 (a)Unitary system

 (b)Federal system

 (c)Confederal system

 (d)presidential system \n Your answer: ''',
        
'''Which of the following countries practised mixed economy?

 (a)USA

 (b)Britain

 (c)China

 (d)Nigeria \n Your answer:  ''',
        
'''Theocracy is a govt ruled by who?
 (a)Nobles

 (b)Priests and religious

 (c)Old people

 (d)The military \n Your answer:  ''',
        
'''The Father of Nigeria Nationalism is who?

 (a)Nnamdi Azikiwe

 (b)Obafemi Awolowo

 (c)Herbert Macaulay

 (d)Ahmadu Bello \n Your answer:  ''',
        
'''The first executive president of Nigeria was who?

 (a)Gen.Aguiyi Ironsi

 (b)Nnamdi Azikiwe

 (c)Alhaji Shehu Shagari

 (d)Olusegun Obasanjo \n Your answer:  ''',
        
'''The sons of King Saul who were murdered during the battle against the Philistines were who?

 (a)Peter,James and John

 (b)Jonathan,Abinadab and Malchishua

 (c)Shem,Ham and Japhat

 (d)Joab, Abishai and Ammon \n Your answer:  ''',
        
'''The king of Judah who set himself ablaze in his palace and died was who?

 (a)King Ahab

 (b)King David

 (c)King Zimri

 (d)King Cyrus \n Your answer:  ''',
        
'''The prophet who is known for true religion and social justice was who?

 (a)Prophet Elijah

 (b)Prophet Micah

 (c)Prophet Hosea

 (d)Prophet Amos \n Your answer:  '''
        ]
    
    art_answers = [
        'a',
        'a',
        'a',
        'c',
        'a',
        'b',
        'b',
        'd',
        'a',
        'b',
        'a',
        'b',
        'a',
        'd',
        'b',
        'c',
        'c',
        'b',
        'c',
        'd'
        ]
    for check in range(len(art_questions)) :
        user_answer = input(art_questions[check]).lower()
        confirmation = art_questions.index(art_questions[check])
        correct_answer = art_answers[confirmation]
        if user_answer == correct_answer:
            score += 1
        elif user_answer != correct_answer :
            score += 0
    print(' ')
    print(f'Your final score is {score}')
    return


def Users_guide():
    usage_options= ('''
   TO QUIT THE GAME INPUT -> STOP
   TO GO BACK TO MAIN MENU INPUT -> BACK 
   TO ANSWER QUESTIONS -> Answer according to thier options
                          e.g a, b, c or d. ''' )
    print(usage_options)
   


users_response = input('Your response: ').upper()
def user_response(users_response):
   #while users_response != 'stop':
    if users_response == 'SCIENCES' or users_response == 'SCIENCE' or users_response == '1':
       Science_questions()
    elif users_response == 'ARTS' or users_response == 'ART' or users_response == '2':
       Art_questions()       
#  elif users_response == 'commercial' or users_response == '3':
       #     pass
    elif users_response == 'HELP':
        Users_guide()
    return    
user_response(users_response)  
#Science_questions()     
#Art_questions()
