##monthNumbers = {'Jan':1,'Feb':2,'Mar':3,'April':4,'May':5,
##                1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May'}
##print "The third month is",monthNumbers[3]
##dist = monthNumbers['April'] - monthNumbers['Jan']
##print "April and Jan are",dist,"months apart"



EtoF = {'John':'Jean','drinks':'boit','bread':'pain','red': 'rouge',
        'wine': 'vin','with': 'avec' ,'eats':'mange',
        'friends': 'amis', 'and': 'et', 'of' :'du' }

FtoE = {'pain': 'bread', 'vin': 'wine', 'avec': 'with' ,
'mange': 'eats', 'boit': 'drinks', 'Jean':' John',
'amis' : 'friends' , 'et' : 'and' , 'du' : 'of' , 'rouge' :'red'}

diets = {'English to French':EtoF, 'French to English':FtoE}

def translateWord(word, dictionary):
    if word in dictionary.key():
        return dictionary[word]
    elif word != '':
        return '"',word,'"'
    return word

def translate(phrase,diets,direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + LCLetters
    dictionary = diets[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word +=c
        else:
            translation = translation\
                          + translateWord(word,dictionary) + c
            word = ''

    return translation + ' '+ translateWord(word,dictionary)
print translate('John drinks red wine and eats bread.',
                diets,'English to French')
print translate("Jean bois du vin rouge.",diets,'French to English')
    
    
