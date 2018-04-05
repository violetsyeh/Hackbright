
def print_deliveries(file, day):

    
    print "Day {}".format(day)
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)
    the_file.close()



print_deliveries(file = "um-deliveries-20140519.txt", day = '1')
print_deliveries(file = "um-deliveries-20140520.txt", day = '2')
print_deliveries(file = "um-deliveries-20140521.txt", day = '3')
    