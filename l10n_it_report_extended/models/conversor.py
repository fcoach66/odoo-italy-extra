UNITA = (
    '',
    'UNO ',
    'DUE ',
    'TRE ',
    'QUATTRO ',
    'CINQUE ',
    'SEI ',
    'SETTA ',
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
    # arreglamos error de redondeo de la versión de abajo, por ej. para número
    # 178.099,57
    import math
    frac, whole = math.modf(number)
    ans = to_word_int(int(whole))
    centavos = int(round(frac * 100))
    if centavos > 0:
        ans += ' E ' + to_word_int(centavos) + 'CENTESIMI'

    # ans = to_word_int(int(number))conversor.to_word(
    # # ans = to_word_int(int(number)) + 'PESOS'
    # centavos = int(round((number - int(number)), 2) * 100)
    # if centavos > 0:
    #     ans += ' CON ' + to_word_int(centavos) + 'CENTAVOS'
    # # return ans.title()
    # # we prefer only first letter in upper case
    return ans.capitalize()


def to_word_int(number):
    """
    Converts a number into string representation
    """
    converted = ''

    if number == 0:
        return 'ZERO '

    if not (0 < number < 999999999):
        return 'Non è possibile convertire il numero in lettere'

    number_str = str(number).zfill(9)
    millones = number_str[:3]
    miles = number_str[3:6]
    cientos = number_str[6:]

    if(millones):
        if(millones == '001'):
            converted += 'UN MILIONE '
        elif(int(millones) > 0):
            converted += '%sMILIONI ' % __convertNumber(millones)

    if(miles):
        if(miles == '001'):
            converted += 'MILLE '
        elif(int(miles) > 0):
            converted += '%sMILA ' % __convertNumber(miles)

    if(cientos):
        if(cientos == '001'):
            converted += 'UN '
        elif(int(cientos) > 0):
            converted += '%s' % __convertNumber(cientos)

    # converted += 'PESOS'

    # return converted.title()
    return converted


def __convertNumber(n):
    """
    Max length must be 3 digits
    """
    output = ''

    if(n == '100'):
        output = "CENTO "
    elif(n[0] != '0'):
        output = CENTINAIA[int(n[0]) - 1]

    k = int(n[1:])
    if(k <= 20):
        output += UNITA[k]
    else:
        if((k > 30) & (n[2] != '0')):
            output += '%sY %s' % (DECINE[int(n[1]) - 2], UNITA[int(n[2])])
        else:
            output += '%s%s' % (DECINE[int(n[1]) - 2], UNITA[int(n[2])])

    return output