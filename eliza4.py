import re
# from eliza1 import respond
from eliza2 import match_rule, rules
from eliza3 import replace_pronouns
# from echobot2 import send_message

# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response



if __name__ == "__main__":
    main()


# Send the messages
    # print(send_message("do you remember your last birthday"))
    # print(send_message("do you think humans should be worried about AI"))
    # print(send_message("I want a robot friend"))
    # print(send_message("what if you could be anything you wanted"))
