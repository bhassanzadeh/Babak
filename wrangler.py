import sys

#  length of sys.argv should be 3 (for 2 arguments)
if len(sys.argv) != 3:
    print('Error: The input should be two strings')
    sys.exit()

word1 = sys.argv[1]
word2 = sys.argv[2]

# this function reverses the word
def spellBackwards(word):
    return word[::-1]

# this function capitalizes the word
def capitalize(word):
    return word.upper()

# this function threads the wordsl
def threadTogether(w1, w2):
    # first, we find which word is shorter
    if len(w1) < len(w2):
        shorter_word = w1
        longer_word = w2
    else:
        shorter_word = w2
        longer_word = w1


    # thread the words together up to the length of the shorter word
    output = ''
    len_of_shorter = len(shorter_word)
    for i in range(len_of_shorter):
        output = output + w1[i] + w2[i]

    # finally, add any remaining characters from the longer word
    output = output + longer_word[len_of_shorter:]
    return output

# this function calls all other functions and
# prints the results
def printItOut(w1, w2):
    # find the reverse of word1
    reverse_w1 = spellBackwards(w1)
    print('The reverse of %s is %s.' %(w1, reverse_w1))

    # find the capital of word2
    capital_w2 = capitalize(w2)
    print('The capital of %s is %s.' %(w2, capital_w2))

    # thread them together
    threaded_output = threadTogether(reverse_w1, capital_w2)
    print('Threaded, they become %s.' %threaded_output)

# run the program
printItOut(word1, word2)