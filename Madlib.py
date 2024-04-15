#       MADLIP APPLICATION 
# Opening the text document for reading the passage 
# "r"- read mode
with open("passage.txt","r") as f:
    story = f.read()
f.close()

# My Story    
#story = "In a distant [place], there lived an adventurous [person] known as [name]. Accompanied by a faithful [companion], a majestic [animal] named [pet's name], [name] roamed freely across the [landscape]. One fateful day, [name] decided to undertake a perilous [journey]. Equipped with only a sturdy [item], [name] ventured into the uncharted [terrain]. Along the way, an enigmatic [figure] appeared, offering an ancient [object] in exchange for a rare [item]. Will [name] accept the offer and press on with the [quest], or will doubt linger in [name]'s heart, leading to a retreat back [home]?"

# Declaring placeholders to get all the bracket spaces to replace with different other words
# Declaration is done in set inorder to prevent duplication and repeation
placeholders = set()

index = -1

# Loop to find all the placeholders in the passage
for i,char in enumerate(story):
    if char == "[": #finding the start of each placeholder
        index = i

    if char == "]" and index != -1 :
        placeholder = story[index:i+1]
        placeholders.add(placeholder)
        index = -1

# Getting the solution, i.e.,the words to replace the placeholder in the passage with. 
# The declaration is done in dictionary to make use of its key:value feature for replacing the words
solutions = {}

for placeholder in placeholders:
    solution = input("Enter a word to replace " + placeholder + ": ")
    solutions[placeholder] = solution

# Replacing the placeholders with the solutions in the passage 
for placeholder in placeholders:
    story = story.replace(placeholder,solutions[placeholder])

#print(story)   

# Writing the answer after replacement of the placeholders in another text document
# "w" - write mode
with open("answers.txt", "w")as fw:
    fw.write(story)
fw.close() 

# Answers for the Placeholders
# - [place]: Jungle
# - [person]: Explorer
# - [name]: Sara
# - [companion]: Guide
# - [animal]: Tiger
# - [pet's name]: Roxy
# - [landscape]: Savannah
# - [journey]: Expedition
# - [item]: Map
# - [terrain]: Wilderness
# - [figure]: Shaman
# - [object]: Amulet
# - [quest]: Quest
# - [home]: Campsite
