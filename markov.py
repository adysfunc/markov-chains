from collections import defaultdict
import random


def pair2(words, chain):
    for i in range(len(words) -2):
        key = " ".join(words[i:i+2])
        if key not in chain:
            chain[key][words[i+2]] = 1
            
        #if the word after n-gram is not in the nested dict
        elif words[i+2] not in chain[key]:
            chain[key][words[i+2]] = 1

        else:
            chain[key][words[i+2]] += 1


with open("jekyll.txt") as f:
    text = f.read()
    words = text.split()

chain = defaultdict(dict)
pair2(words, chain)
regular_dict = {k: dict(v) for k,v in chain.items()}
# print(regular_dict)

#choose a world with capital first letter
firstword = random.choice([word for word in regular_dict if word[0].isupper() and word[-1] != "."])
output = firstword.split()
# print(firstword, regular_dict[firstword])

# pick acc to the frquency
next_word = random.choices(list(regular_dict[firstword]),weights=list(regular_dict[firstword].values()))

# print(next_word)
output.append(next_word[0])
# print(output)

i = 1
while i <= 50:
    new_key = " ".join(output[-2:])
    if new_key in regular_dict:
        # print(new_key)
        # print(regular_dict[new_key])
        next_word = random.choices(list(regular_dict[new_key]),weights=list(regular_dict[new_key].values()), cum_weights=None)
        output.append(next_word[0])

    else:
        break
    
    i+=1

print(" ".join(output))
# print(len(output))
    