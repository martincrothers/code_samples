import random


def input_count(message, min, max):
    """
        We want this function to ask for an integer of what the desired minimum for words and characters is.
        It will loop until a valid response is given, or until a maximum number of attempts is reached.  If the
        maximum number of attempts is reached, the application will exit with a message stating why.
    :param message:
    :param min:
    :param max:
    :return:
    """
    valid_entry = False  # This variable is what the loop uses to know if a valid response has been given by the user.
    maximum_attempts = 3
    i = 1
    while not valid_entry:
        try:
            int(input(message))
        except ValueError:
            error_message = "That was not a number, please enter a number."
            print(error_message)


        # increment by one
        i += 1
        # determine if the maximum attempts has been breached, and exit if so.
        if i >= maximum_attempts:
            result_code = "Too many invalid entries were input. Program exited for stability."
            return False, result_code
    """
    try:
        int(input(message))
    except ValueError:
    """


def main():
    #   Open the word list and convert it to a list
    word_file = open('words_list.txt', 'r', encoding='ANSI')
    word_list = [line.rstrip('\n') for line in word_file]
    word_file.close()

    #   Define minimum and maximum values
    min_words = 1
    max_words = 8

    min_char = 8
    max_char = 60
