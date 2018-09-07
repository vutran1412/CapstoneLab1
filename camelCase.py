# Camel Casing Program
# Author: Vu Tran

# Function to turn a sentence user entered into a camel cased sentence
def camel_case(user_string):
    # Initialize a new list
    new_list = []
    # Initialize a new string
    new_sentence = ""
    # Splits the user sentence and saves the individual words into a list
    string_list = user_string.split()
    # Loop over the string_list and capitalize the entire word of every odd index
    for i in range(len(string_list)):
        # If index is even push everything to lower case
        if i % 2 == 0:
            # Append the newly lowered or all capped words into a list
            new_list.append(string_list[i].lower())
        # Else make everything upper case
        else:
            new_list.append(string_list[i].upper())
    # Iterate through the list and concatenate all the words to the new sentence
    for word in new_list:
        new_sentence += word
    # Return the new sentence
    return new_sentence


def display_banner():

    '''Display program name in a banner'''

    msg = 'AWESOME camelCaseGenerator PROGRAM'

    stars = '*' * len(msg)

    print('\n', stars, '\n', msg, '\n',  stars, '\n')


def main():
    # Asks user to input a sentence
    user_input = input("Enter a sentence\n")
    # Function call and save to a new string
    joined_string = camel_case(user_input)
    # Output
    print(joined_string)


main()