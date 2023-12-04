import uuid, random, names
from datetime import datetime

letters = ['b','c','d','f','g','h','j','k','l','m','n',
           'p','q','r','s','t','v','w','x','z']
lettersVowel = ['a','e','i','o', 'u','y']

def genWord():
    word = ''
    countVowel = 0
    for i in range(random.randint(4, 9)):
        if(random.randint(1, 3) == 1 and countVowel < 2):
            word += lettersVowel[random.randint(0, len(lettersVowel) - 1)]
            countVowel += 1
        else:
            word += letters[random.randint(0, len(letters) - 1)]
            countVowel = 0
        if(i == 0):
            word = word.upper()
    return word

def genText(length):
    text = ''
    count = random.randint(10, length)
    for i in range(count):
        
        text += genWord()
        if(random.randint(1, 100) * 0.2 < 2):
            text += '\n'
        else:
            if(i != count - 1):
                text += ' '
    text = text.capitalize()
    return text

def genStatus():
    status = random.randint(1, 2)
    if(status == 1):
        return True
    else:
        return False

def genGender(gender):
    if(gender == 1):
        return "Male"
    else:
        return "Female"

def genNames(gender):
    personName = ''
    if(gender == 1):
        personName += names.get_full_name(gender='male')
    else:
        personName += names.get_full_name(gender='female')
    return personName

def generateDate():
    year = random.randint(1950, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    random_date = datetime(year, month, day)
    return random_date