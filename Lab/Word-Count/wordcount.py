# put your code here.
# open file
# remove whitespace
# separate by each space
# empty dictionary
# .iteritems/.items iterate through each word of file
# one function that prints out each occurence of the word in the file
# close file

def remove_punctuation(word):
    punctuation = ".,?"
    string = ""
    for letter in word:
        if letter not in punctuation:
            string = string + letter 
    return string


def word_count(file_name):
    word_count = {}
    with open(file_name) as word_file:
    

        for line in word_file:
            line = line.rstrip()
            words = line.split(' ')

            for word in words:                
                word = remove_punctuation(word)
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + 1
                

        for word, number in word_count.iteritems():
            print "{} {}".format(word, number)


word_count("test.txt")

