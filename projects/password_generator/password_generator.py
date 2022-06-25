import random
from termcolor import colored, cprint


def get_minimum(message, min_value, max_value):
    """
        We want this function to ask for an integer of what the desired minimum for words and characters is.
        It will loop until a valid response is given, or until a maximum number of attempts is reached.  If the
        maximum number of attempts is reached, the application will exit with a message stating why.
    :param message: This is the message displayed at the input prompt
    :param min_value: The number (integer) that the input should be greater than or equal to
    :param max_value: The number (integer) that the input should be less than or equal to
    :return:
    """
    valid_entry = False  # This variable is what the loop uses to know if a valid response has been given by the user.
    maximum_attempts = 3
    i = 1
    while not valid_entry:
        try:
            #   Display the message for the input prompt in a color without new-line.
            cprint(message, 'cyan', end='')
            #   Prompt for input and cast to integer
            number = int(input())

            #   Test that the integer was greater than or equal to the minimum value, and less than or equal to the
            #   maximum value. If it is, then return the result, else display the problem to the user.
            if min_value <= number <= max_value:
                results = {
                    "success": True,
                    "number": number
                }
                return results
            else:
                if number < min_value:
                    if i > maximum_attempts:
                        result_code = "Too many invalid entries were input. Program exited for stability."
                        cprint(result_code, 'red')
                        results = {
                            "success": False,
                            "result_code": result_code
                        }
                        return results
                    else:
                        display_message = "The number is too small"
                        cprint(display_message, 'red')
                elif number > max_value:
                    if i > maximum_attempts:
                        result_code = "Too many invalid entries were input. Program exited for stability."
                        cprint(result_code, 'red')
                        results = {
                            "success": False,
                            "result_code": result_code
                        }
                        return results
                    else:
                        display_message = "The number is too large"
                        cprint(display_message, 'red')
        except ValueError:
            #   If too many attempts have been reached, break the loop and return False
            if i > maximum_attempts:
                result_code = "Too many invalid entries were input. Program exited for stability."
                cprint(result_code, 'red')
                results = {
                    "success": False,
                    "result_code": result_code
                }
                return results
            #   If too many attempts has NOT been reached, tell the user what was wrong
            else:
                error_message = "That was not a number, please enter a number."
                cprint(error_message, 'red')
        except:
            #   If too many attempts have been reached, break the loop and return False
            if i > maximum_attempts:
                result_code = "Too many invalid entries were input. Program exited for stability."
                cprint(result_code, 'red')
                results = {
                    "success": False,
                    "result_code": result_code
                }
                return results
            #   If too many attempts has NOT been reached, tell the user what was wrong
            else:
                error_message = "An unhandled exception occurred."
                cprint(error_message, 'red')

        # increment by one
        i += 1
# END OF FUNCTION#######################################################################################################


def get_seperator(valid_values):
    """
        This function prompts the user for a character that should be used to separate the words that will make
        up the passphrase.
    :param valid_values: This is a list of characters that will be accepted as separators.
    :return:
    """
    valid_entry = False  # This variable is what the loop uses to know if a valid response has been given by the user.
    maximum_attempts = 3
    i = 1
    while not valid_entry:
        message = "Enter a character that exists in this list ({}) to use as a word seperator: ".format((' '.join(valid_values)))
        cprint(message, 'cyan', end='')
        try:
            seperator = input()
            if seperator in valid_values:
                results = {
                    "success": True,
                    "seperator": seperator
                }
                return results
            else:
                if i > maximum_attempts:
                    result_code = "Too many invalid entries were input. Program exited for stability."
                    cprint(result_code, 'red')
                    results = {
                        "success": False,
                        "result_code": result_code
                    }
                    return results
                #   If too many attempts has NOT been reached, tell the user what was wrong
                else:
                    error_message = "That character wasn't in the permitted list, please try again."
                    cprint(error_message, 'red')
        except:
            error_message = "An unhandled exception occurred."
            cprint(error_message, 'red')

        i += 1
# END OF FUNCTION#######################################################################################################


def get_yes_or_no(message):

    valid_responses = ["Y", "YES", "N", "NO", "TRUE", "FALSE"]
    valid_entry = False  # This variable is what the loop uses to know if a valid response has been given by the user.
    maximum_attempts = 3
    i = 1
    while not valid_entry:
        #   Display the prompt
        cprint(message, 'cyan', end='')

        #   Get the users input
        response = input().upper()

        #   Test the input for a valid response
        if response in valid_responses:
            if response in ["Y", "YES", "TRUE"]:
                results = {
                    "success": True,
                    "boolean": True
                }
                return results
            elif response in ["N", "NO", "FALSE"]:
                results = {
                    "success": True,
                    "boolean": False
                }
                return results
            else:
                error_message = "An unhandled exception occurred"
                cprint(error_message, 'red')
                results = {
                    "success": False,
                    "boolean": False
                }
                return results
        else:
            cprint("Was NOT a valid response.", 'red')
            if i > maximum_attempts:
                result_code = "Too many invalid entries were input. Program exited for stability."
                cprint(result_code, 'red')
                results = {
                    "success": False,
                    "boolean": False
                }
                return results

        i += 1
# END OF FUNCTION#######################################################################################################


def main():
    #   Open the word list and convert it to a list
    word_file = open('words_list.txt', 'r', encoding='ANSI')
    word_list = [line.rstrip('\n') for line in word_file]
    word_file.close()
    word_list_count_of_words = len(word_list)

    #   Define constraint values
    min_char = 8
    max_char = 60

    min_words = 1
    max_words = 8

    valid_separators = [",", ".", "-", "_", "=", "+", "*", "/", "^", "~", ":", ";"]

    #   Get the number of characters
    message = "Enter a number between {} and {} for the minimum length of the passphrase: ".format(min_char, max_char)
    characters_count_result = get_minimum(message, min_char, max_char)
    if characters_count_result['success']:
        characters_count = characters_count_result['number']
        can_continue = True
    else:
        can_continue = False

    #   Get the number of words
    if can_continue:
        message = "Enter a number between {} and {} for the minimum number of words: ".format(min_words,
                                                                                                       max_words)
        characters_count_result = get_minimum(message, min_words, max_words)
        if characters_count_result['success']:
            words_count = characters_count_result['number']
            can_continue = True
        else:
            can_continue = False

    #   Get the separator
    if can_continue:
        separator_result = get_seperator(valid_separators)
        if separator_result['success']:
            separator = separator_result['seperator']
            can_continue = True
        else:
            can_continue = False

    #   Get capitalization
    if can_continue:
        message = "Do you want to have the first letter of each word capitalized? Enter Y/N: "
        capitalization_result = get_yes_or_no(message)
        if capitalization_result['success']:
            capitalize = capitalization_result['boolean']
            can_continue = True
        else:
            can_continue = False

    #   Get add a number to end
    if can_continue:
        message = "Do you want to add a random number (0-9) to the end of the passphrase? Enter Y/N: "
        append_number_result = get_yes_or_no(message)
        if append_number_result['success']:
            append_number = append_number_result['boolean']
            can_continue = True
        else:
            can_continue = False

    passphrase = ""
    words = []
    passphrase_meets_conditions = False
    min_char_count_met = False
    min_word_count_met = False

    #   Construct the passphrase, and display it once complete
    if can_continue:
        while not passphrase_meets_conditions:
            #   Test if the whole passphrase is long enough
            if append_number:
                current_length_of_passphrase = len(passphrase) + 1
            else:
                current_length_of_passphrase = len(passphrase)

            #   Test if the passphrase contains enough words
            current_count_of_words = len(words)

            #   Test if conditions are met
            if current_length_of_passphrase >= characters_count:
                min_char_count_met = True
            if current_count_of_words >= words_count:
                min_word_count_met = True

            if min_char_count_met and min_word_count_met:
                passphrase_meets_conditions = True
                if append_number:
                    passphrase += str(random.randint(0, 9))
                    cprint(passphrase, 'blue')
                else:
                    cprint(passphrase, 'blue')
                break
            else:
                #   random_list_index = random.randint(0, word_list_count_of_words)
                word = random.choice(word_list)
                if capitalize:
                    word = word.capitalize()
                words.append(word)
                #   If it's the first word in the passphrase, don't add a separator
                if len(passphrase) == 0:
                    passphrase += word
                else:
                    passphrase += separator + word
# END OF FUNCTION#######################################################################################################


if __name__ == "__main__":
    main()
