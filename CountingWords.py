introString = input("Enter your introduction :")
print(introString)

characterCount = 0
wordCount = 1
for i in introString:
    characterCount = characterCount+1

    if(i == ' '):
        wordCount = wordCount+1

print("NO.OF WORDS IN THE STRING : ")
print(wordCount)

print("NO.OF CHARACTERS")
print(characterCount)
