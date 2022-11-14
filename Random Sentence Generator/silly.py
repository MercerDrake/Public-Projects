import random
import words
import time

def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)
    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0
    lengthOfSub = 8
    # Add a while loop here.
    while index < len(template):
        if template[index:index+lengthOfSub] == "{{noun}}":
            noun = random.choice(nouns)
            #output.append(random.choice(nouns))
            index+=lengthOfSub
            output.append(noun)
        elif template[index:index+lengthOfSub] == "{{verb}}":
            verb=random.choice(verbs)
            index+=lengthOfSub
            output.append(verb)
        else:
            output.append(template[index])
            index+=1
    return "".join(output)
    # After the loop has finished, join the output and return it.


# To see the results, we need to call the funtion and print what it returns:
while True:
    print(silly_string(words.nouns, words.verbs, words.templates), flush=True)
    time.sleep(1)