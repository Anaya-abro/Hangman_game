
import random
print('Hangman Game')

secret = ['Kingdom','beautiful','python','laptop','computer','science','apple','mother','door','park','car','school']
computer = random.choice(secret).lower()
display = ['_']*len(computer)

lives = 5
guessed = []
while lives>0:
    print(display)
    print('letter guessed so far:',guessed)
    user = input('guess a letter:').lower()
    guessed.append(user)


    if user in computer:
        for i in range(len(computer)):
            if computer[i] == user:
                display[i] = user
                
    else:
        lives-=1
        print(f'wrong! remaining lives: {lives}')    

    if '_' not in display:
        print('you win🎉')
        break

if lives == 0:
    print('Game Over! the word was',computer)
