# imports
import random
import re

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

name = "Lao"
weather = "cloudy"

responses = {'question': ["I don't know :(", 'you tell me!'],
 'statement': ['tell me more!',
  'why do you think that?',
  'how long have you felt this way?',
  'I find that extremely interesting',
  'can you back that up?',
  'oh wow!',
  ':)']}

# standard responses
rules = {'I want (.*)': ['What would it mean if you got {0}',
  'Why do you want {0}',
  "What's stopping you from getting {0}"],
 'do you remember (.*)': ['Did you think I would forget {0}',
  "Why haven't you been able to forget {0}",
  'What about {0}',
  'Yes .. and?'],
 'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
 'if (.*)': ["Do you really think it's likely that {0}",
  'Do you wish that {0}',
  'What do you think about {0}',
  'Really--if {0}']}


# define match_rule
def match_rule(message):
    response, phrase = "default", None
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    # The original line given in the course was 'return response.format(phrase)'. But it caused an error: "ValueError: too many values to unpack (expected 2)" when the function is called in the respond function. And it makes sense that there weren't enough values (only one value was returned). So, I changed the return line to:
    return response, phrase


# define replace_pronouns
def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub("me", "you", message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub("my", "your", message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub("your", "my", message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub("you", "me", message)
    return message

# define respond
def respond(message):
    # Call match_rule
    response, phrase = match_rule(message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# define send message
# def send_message(message):
#     # Print user_template including the user_message
#     print(user_template.format(message))
#     # Get the bot's response to the message
#     response = respond(message)
#     # Print the bot template including the bot's response.
#     return bot_template.format(response)

def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


# call it
# print(match_rule("do you remember your last birthday"))
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")


## THIS PROGRAM ISN'T WORKING. SOMETHING IS WRONG WITH THE RESPOND FUNCTION. response, phrase = match_rule(rules, message) brings up the error "ValueError: too many values to unpack (expected 2 But I have the same code that is in the Datacamp lesson, and the lesson works.
