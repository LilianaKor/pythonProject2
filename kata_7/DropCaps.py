# def drop_caps(text):
#     # Split the text into words
#     words = text.split()
#
#     # Initialize an empty list to store modified words
#     modified_words = []
#
#     # Iterate through each word
#     for word in words:
#         # Check if the word has length greater than 2
#         if len(word) > 2:
#             # Capitalize the first letter and make the rest lowercase
#             modified_word = word[0].upper() + word[1:].lower()
#         else:
#             # Leave smaller words unchanged
#             modified_word = word
#
#         # Add the modified word to the list
#         modified_words.append(modified_word)
#
#     # Join the modified words back into a string
#     modified_text = ' '.join(modified_words)
#
#     return modified_text
#
# # Example usage:
# texts = [
#     "apple",
#     "apple of banana",
#     "one   space",
#     "   space WALK   "
# ]
#
# for text in texts:
#     result = drop_caps(text)
#     print(f'"{text}" => "{result}"')


def drop_cap(text):
    words = text.split()

    modified_words = []
    for word in words:
        if len(word) > 2:
            modified_word = word[0].upper() + word[1:].lower()
        else:
            modified_word = word

        # Preserve leading and trailing spaces
        if word.startswith(' ') or word.endswith(' '):
            modified_word = word[0] + modified_word[1:]

        modified_words.append(modified_word)

    modified_text = ' '.join(modified_words)

    # Capitalize the first letter of the resulting string if necessary
    modified_text = modified_text.strip().capitalize()

    return modified_text


# Example usage:
texts = [
    "apple",
    "apple of banana",
    "one   space",
    "   space WALK   "
]

for text in texts:
    result = drop_cap(text)
    print(f'"{text}" => "{result}"')
