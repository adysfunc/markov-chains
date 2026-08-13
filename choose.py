import random

def pair3(words, chain):
    for i in range(len(words) - 3):
        key = " ".join(words[i:i+3])
        if key in chain:
            chain[key].append(words[i+3])
                    
        else:
            chain[key] = [words[i+3]]

with open("poems.txt") as f:
    text = f.read()
    words = text.split()
chain = {}
pair3(words, chain)
# print(chain)

firstword = random.choice([word for word in chain if word[0].isupper()])
output = [firstword, random.choice(chain[firstword])]
i = 0
while i <= 20:
    keypick = random.choice(list(chain))
    output.append(keypick)
    output.append(random.choice(chain[keypick]))
    # print(output)
    i+=1
    # print(i)

print(" ".join(output))
    