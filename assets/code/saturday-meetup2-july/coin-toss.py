import random


### This should run 100

# User inputs a value
# check if value provided is equal to a randomly generated value of heads or tails
# if its not included, we'll ask the user to try again
# We'll constantly check if the person is getting a streak
# Check the percentage of the streaks



def check_streak(user_guess):
    """Function to check winning streak
    
    """

    options = ['tails', 'heads']
    
    user_guesses = []
    
    toss = random.randint(0, 1)
    
    _randomly_generated_option = options[toss]
    
    while user_guess not in (options[:]):
        print("You sure sey na this game yu dey play?")
        user_guess = input("Please enter a guess of either heads or tails... ")
        user_guesses.append(user_guess)

    for x in range(5):
        
        while user_guess == _randomly_generated_option:
            print("Yep, that's right. Do yo want to try again for a chance to win $50")
            print("PYou can play again.")
            user_guess = input()
            user_guesses.append(user_guess)
        if len(user_guesses) == 5:
            print_percentage(user_guesses)
            
        # if user_guess == _randomly_generated_option:
        #     x += 1
        #     print("Got it again, champ!")
        # else:
        #     print("Your luck's not so good.")         
            
        while user_guess != _randomly_generated_option:
            print("No. Thats not right. Try again...?")
            user_guess = input()
            user_guesses.append(user_guess)
            if user_guess == _randomly_generated_option:
                
                print("You finally got it... here's your $50... but would you like to bet that on the next try?")
                user_guess = input()
            else:
                print("Gerrarahere...You no sabi.")
        if len(user_guesses):
            print_percentage(user_guesses)


def print_percentage(all_guesses):
    tail_count = 0
    head_count = 0
    
    for g in all_guesses:
        if g == "tails":
            tail_count += 1
            
        if g == "heads":
            head_count += 1
            
                
    print('Chance of tail streak: %s%%' % (tail_count / 100))
    print('Chance of head streak: %s%%' % (head_count / 100))
        
# region
# for test in range(10,000): 
#     guess = ''
#     options = ['tails', 'heads']

#     while guess not in ('heads', 'tails'):
#         print('Guess the coin toss! Enter heads or tails:')
#         guess = input()

#     toss = random.randint(0, 1) # 0 is tails, 1 is heads
    

#     if guess == options[toss]:
#         print('You got it!')
#     else:
#         print('Nope! Guess again!')
#         guess = input()
#         if guess == options[toss]:
#             print('You got it!')
#         else:
#             print('Nope. You are really bad at this game.')
            
#         heads = options[0]
    
    # print('Chance of streak: %s%%' % (numberOfStreaks / 100))
# endregion


        
if __name__ == "__main__":
    user_input = input("Please enter a guess of either heads or tails... ")
    check_streak(user_input)
    
    
    