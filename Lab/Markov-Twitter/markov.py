"""Generate Markov text from text files."""

from random import choice
import sys
import twitter
import os

N_GRAM_LENGTH = 4


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    # open the file (read mode)
    # turn content content of file in one line string
    # split string by whitespace
    # convert back one line string - for loop - concatanate list into string
    # return string

    with open(file_path) as new_file:
        lines = new_file.read()
        split_lines = lines.split()

    return split_lines


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # for loop through the range of text_string(from previous function)
    # put the i, i + 1 for key as tuple
    # value connects i + 2 for value as list (append to list)
    # when i = len(text_string - 2), value = None
    # return completed dictionary

    chains = {}

    for i in range(len(text_string)-n):
        key = ()
        for j in range(n):
            key += (text_string[i + j],)
        if key in chains:
            chains[key].append(text_string[i + n])
        else:
            chains[key] = [text_string[i + n]]

    return chains


def make_text(chains, N_GRAM_LENGTH):
    """Return text from chains."""

    title_list = []

    # create list of keys starting with title word
    new_list = chains.keys()
    for item in new_list:
        if item[0].istitle():
            title_list.append(item)

    while True:
        words = []

        # generate first key
        key = choice(title_list)
        for item in key:
            words.append(item)

        # generate rest of chain
        while key in chains:
            chosen_word = choice(chains[key])
            words.append(chosen_word)

            if chosen_word[-1] in """.?!"'""":
                break
            else:
                new_key = ()
                for i in range(N_GRAM_LENGTH-1):
                    new_key += (key[i + 1],)
                new_key += (chosen_word,)
                key = new_key
        # return " ".join(words)
        final_text = " ".join(words)

        if len(final_text) <= 140:
            return final_text


# def check_length(random_text, chains, N_GRAM_LENGTH):
#     """Check length of tweet"""

#     while len(random_text) > 140:
#         random_text = make_text(chains, N_GRAM_LENGTH)

#     return random_text

def tweet(random_text):

    api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                      consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    api.VerifyCredentials()

    # create prompt

    return api.PostUpdate(random_text)

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, N_GRAM_LENGTH)

# Produce random text
random_text = make_text(chains, N_GRAM_LENGTH)

# tweet = check_length(random_text, chains, N_GRAM_LENGTH)

tweet(random_text)

# status = api.PostUpdate(tweet)
