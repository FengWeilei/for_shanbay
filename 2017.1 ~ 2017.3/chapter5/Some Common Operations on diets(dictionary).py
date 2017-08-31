EtoF = {'John':'Jean','drinks':'boit','bread':'pain','red': 'rouge',
        'wine': 'vin','with': 'avec' ,'eats':'mange',
        'friends': 'amis', 'and': 'et', 'of' :'du' } ##keys:values
print len(EtoF)
print EtoF.keys()
print EtoF.values()
print 'friends' in EtoF
print EtoF['John']
print EtoF.get('red','of')
EtoF['John'] = 'JJJJ'   ##replace if John already exist
print EtoF

del EtoF['John']  ## delete
print EtoF
##for k in EtoF  ## iteration

##def keySearch(L,k):
##    for elem in L:
##        if elem[0] != k:  ##  Later on
##            return elem[1]
##    return None
##print keySearch('EtoF','with')
