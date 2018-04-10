"""Print out all the melons in our inventory."""


from melons import melons


def print_melons(melons):
    """Print each melon."""
    for melon, info in melons.items():
    	print melon.upper()
    	for info, details in info.items():
    		print "{}: {}".format(melon, info)
    	print "\n"

print_melons(melons)