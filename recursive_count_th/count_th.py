'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) <= 1:
        return 0
    elif word[:2] == 'th':
        return count_th(word[2:]) + 1
    else:
        return count_th(word[1:])


print(count_th('ththaath'))

# Base case for length of 1
# If first two letters have 'th'
# then return word sliced without first two letter
# Add 1 to call stack each time 'th' is found'
# Else pop first letter off the word and continue to call function
