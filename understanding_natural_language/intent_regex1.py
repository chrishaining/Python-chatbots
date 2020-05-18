import re

# create the keywords dictionary:
keywords = {'greet': ['hello', 'hi', 'hey'], 'goodbye': ['bye', 'farewell'], 'thankyou': ['thank', 'thx']}

# create the responses dictionary:
responses = {'default': 'default message', 'goodbye': 'goodbye for now', 'greet': 'Hello you! :)',
 'thankyou': 'you are very welcome'}


# Define a dictionary of patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))

# Print the patterns
print(patterns)
