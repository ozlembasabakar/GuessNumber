from random import sample, seed, choice
import string

alphabet_lowercase = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase
punctuations = string.punctuation

alphabet_list = list(alphabet_lowercase + alphabet_uppercase + punctuations + ' ')


def guessNumber(guess_number, n):
    if len(guess_number) == 4:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        seed(n)
        current_list = sample(numbers, 4)
        current_string = ''.join(str(s) for s in current_list)
        # print(current_string)

        result = []
        for i in range(len(guess_number)):
            if guess_number[i] == current_string[i]:
                result.append('+')
            elif guess_number[i] in current_string:
                result.append('-')

        result_string = ''.join(str(r) for r in result)

        return result_string, current_string

    else:
        return 'You should write 4 characters.'


guess_list = []
seed_number = int(choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
size = 5
for g in range(0, size):
    try:
        guess = input()
        guess_list.append(str(guess))
        number = guessNumber(guess, 0)
        if number == 'You should write 4 characters.':
            result_list = number
        else:
            result_number = number[1]
            result_list = number[0]
        x = str(guess).isdigit()
        if x:
            if str(guess) in guess_list and result_list == '++++':
                print('YOU GUESSED IT RIGHT!!')
                break
            if str(guess) in guess_list and result_list != '++++':
                if int(g) == int(4):
                    print('You failed. The number was', result_number,'.')
                elif int(g) != int(4):
                    print(result_list)
        else:
            print('Type error. You should write a number.')
    except NameError:
        print('FAILED!!! You did not write 4 characters.')


