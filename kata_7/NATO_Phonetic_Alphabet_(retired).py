def nato(word):
    # Define the NATO phonetic alphabet dictionary
    nato_dict = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
        'Z': 'Zulu'
    }

    # Initialize an empty list to store the phonetic words
    phonetic_words = []

    # Convert each letter in the word to its corresponding phonetic word
    for letter in word.upper():
        if letter in nato_dict:
            phonetic_words.append(nato_dict[letter])

    # Join the phonetic words with a space between each word
    return ' '.join(phonetic_words)

# Test cases
print(nato("hi"))       # Output: "Hotel India"
print(nato("abc"))      # Output: "Alpha Bravo Charlie"
print(nato("babble"))   # Output: "Bravo Alpha Bravo Bravo Lima Echo"
print(nato("Banana"))   # Output: "Bravo Alpha November Alpha November Alpha"
