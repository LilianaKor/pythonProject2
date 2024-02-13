# def to_jaden_case(sentence):
#     # Split the sentence into words
#     words = sentence.split()
#
#     # Capitalize the first letter of each word
#     jaden_cased_words = [word.capitalize() for word in words]
#
#     # Join the capitalized words back into a sentence
#     jaden_cased_sentence = ' '.join(jaden_cased_words)
#
#     return jaden_cased_sentence
#
# # Example usage:
# quote = "How can mirrors be real if our eyes aren't real"
# jaden_cased_quote = to_jaden_case(quote)
# print("Jaden-Cased:", jaden_cased_quote)
#
# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.split())

def to_jaden_case(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)

quote = "How can mirrors be real if our eyes aren't real"
jaden_cased_quote = to_jaden_case(quote)
print("Jaden-Cased:", jaden_cased_quote)

import string


def to_jaden_case(my_text):
    return string.capwords(my_text)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
# How Can Mirrors Be Real If Our Eyes Aren't Real


print(to_jaden_case("How Can Mirrors Be Real If Our Eyes Aren't Real"))
# How Can Mirrors Be Real If Our Eyes Aren't Real