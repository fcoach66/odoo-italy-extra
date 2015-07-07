UNITA = (
    '',
    'UNO ',
    'DUE ',
    'TRE ',
    'QUATTRO ',
    'CINQUE ',
    'SEI ',
    'SETTE ',
    'OTTO ',
    'NOVE ',
    'DIECI ',
    'UNDICI ',
    'DODICI ',
    'TREDICI ',
    'QUATTORDICI ',
    'QUINDICI ',
    'SEDICI ',
    'DICIASSETTE ',
    'DICIOTTO ',
    'DICIANNOVE ',
    'VENTI '
)

DECINE = (
    'VENTI',
    'TRENTA ',
    'QUARANTA ',
    'CINQUANTA ',
    'SESSANTA ',
    'SETTANTA ',
    'OTTANTA ',
    'NOVANTA ',
    'CENTO '
)

CENTINAIA = (
    'CENTO ',
    'DUECENTO ',
    'TRECENTO ',
    'QUATTROCENTO ',
    'CINQUECENTO ',
    'SEICENTO ',
    'SETTECENTO ',
    'OTTOCENTO ',
    'NOVECENTO '
)

def to_word(number):
    ans = to_word_int(int(number))
    # ans = to_word_int(int(number)) + ' EURO'
    cents = int((number - int(number)) * 100)
    if cents > 0:
        ans += ' E ' + to_word_int(cents) + ' CENTESIMI'
    return ans.title()
    

def to_word_int(number):
    """
    Converts a number into string representation
    """
    converted = ''
    
    if number == 0:
        return 'ZERO '
        
    if not (0 < number < 999999999):
        return 'Non possibile convertire il numero in lettere'
 
    number_str = str(number).zfill(9)
    millions = number_str[:3]
    miles = number_str[3:6]
    hundreds = number_str[6:]
 
    if(millions):
        if(millions == '001'):
            converted += 'UN MILIONE'
        elif(int(millions) > 0):
            converted += '%sMILIONI' % __convertNumber(millions)
 
    if(miles):
        if(miles == '001'):
            converted += 'MILLE '
        elif(int(miles) > 0):
            converted += '%sMILA' % __convertNumber(miles)
 
    if(hundreds):
        if(hundreds == '001'):
            converted += 'UN '
        elif(int(hundreds) > 0):
            converted += '%s' % __convertNumber(hundreds)
 
    #converted += 'EURO'
 
    #return converted.title()
    return converted
 
def __convertNumber(n):
    """
    Max length must be 3 digits
    """
    output = ''
 
    if(n == '100'):
        output = "CENTO "
    elif(n[0] != '0'):
        output = CENTINAIA[int(n[0])-1]
 
    k = int(n[1:])
    if(k <= 20):
        output += UNITA[k]
    else:
        if((k > 30) & (n[2] != '0')):
            output += '%sY %s' % (DECINE[int(n[1])-2], UNITA[int(n[2])])
        else:
            output += '%s%s' % (DECINE[int(n[1])-2], UNITA[int(n[2])])
 
    return output
