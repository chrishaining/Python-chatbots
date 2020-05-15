# from chitchat2 import respond
from eliza4 import respond

from eliza2 import match_rule, rules
from eliza3 import replace_pronouns

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    return bot_template.format(response)



if __name__ == "__main__":
    # print(send_message("hello!"))
    # print(send_message("what's your favorite color?"))
    # print(send_message("what's today's weather?"))
    # print(send_message("what's your name?"))

    # Send messages ending in a question mark

    # Send messages which don't end with a question mark
    # print(send_message("I love building chatbots"))
    # print(send_message("I love building chatbots"))
        print(send_message("do you remember your last birthday"))
        print(send_message("do you think humans should be worried about AI"))
        print(send_message("I want a robot friend"))
        print(send_message("what if you could be anything you wanted"))
