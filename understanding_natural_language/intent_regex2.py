import re

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# create the keywords dictionary:
keywords = {'greet': ['hello', 'hi', 'hey'], 'goodbye': ['bye', 'farewell'], 'thankyou': ['thank', 'thx']}

# create the responses dictionary:
responses = {'default': 'default message', 'goodbye': 'goodbye for now', 'greet': 'Hello you! :)',
 'thankyou': 'you are very welcome'}

# create patterns dictionary
patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))


# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message
        if pattern.search(message):
            matched_intent = intent
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

# define a send_message function
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    return bot_template.format(response)

# Send messages
# send_message("hello!")
# send_message("bye byeee")
# send_message("thanks very much!")


print(send_message("hello!"))
print(send_message("bye byeee"))
print(send_message("thanks very much!"))
