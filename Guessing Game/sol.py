import random





# def guessing_game():
#     number=random.randint(0,10)
#     name=input('Enter your name: ')
#     print(f'Hello, {name}') 
#     print('Guess what number has been chosen: ')
#     while(True):
#         guessed_no=int(input('Enter the number: '))  
#         if(guessed_no>number):
#             print("Too high, try again")
#         elif(guessed_no<number):
#             print("Too low, try again")
#         else:
#             print("Perfect guess, come back again XD.")
#             break
    
        
    

    
#Second way
# def guessing_game():
#     number=random.randint(1,10)
#     name=input('Enter your name: ')
#     print(f'Hello {name}')
#     print('Guess what number has been chosen: ')
#     i=3
#     while i!=0:
#         guessed_no=int(input('Enter the number: '))
#         if(guessed_no>number):
#             print("Too high, try again")
#             i=i-1
#         elif(guessed_no<number):
#             print("Too low, try again")
#             i=i-1
#         else:
#             print("Perfect guess, come back again XD")
#     print("You ran out of time, sorry :)")
    
    

# guessing_game()


dict=['A','B','C','D','E']
#third way
def guessing_game():
    rand_choice=random.choice(dict)
    name=input('Enter your name: ')
    print(f'Hello {name}')
    print("Guess what word has been chosen")
    while True:
        guessed_word=input('Guess your word: ')
        comp_word=dict.index(rand_choice)
        your_word=dict.index(guessed_word)
        if(your_word>comp_word):
            print("Go backwards please")
        elif(your_word<comp_word):
            print("Go forward please")
        else:
            print("Perfect guess, come back again XD")
            break

        
guessing_game()
    
    
    