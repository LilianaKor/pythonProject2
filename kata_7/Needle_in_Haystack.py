def find_needle(haystack):
    # Loop through the elements of the haystack
    for index, item in enumerate(haystack):
        # Check if the item is "needle"
        if item == "needle":
            # Return the message with the position of the needle
            return f"found the needle at position {index}"

# Test the function
haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(haystack))

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'


def find_needle(haystack):
	return 'found the needle at position {}'.format(haystack.index('needle'))

