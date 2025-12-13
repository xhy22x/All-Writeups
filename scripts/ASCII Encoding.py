string = "3E3E20504C4159424F492043415254492054484520474F41545454"
hexa_values = { "0": 0 , "1": 1 , "2": 2 , "3": 3 , "4": 4 , "5": 5 , "6": 6 , "7": 7 , "8": 8 , "9": 9 ,
                "A": 10 , "B": 11 , "C": 12 , "D": 13 , "E": 14 , "F": 15 }

def storeInList(c):
    list = []
    for i in range(0, len(c), 2):
        list.append(c[i]+c[i+1])
    return list

def HexatoDec(hexadecimal):
    total = 0
    for i, digit in enumerate(hexadecimal[::-1]):
        total += hexa_values[digit] * 16**i
    return total

def convertToDec(listHex):
    listDec = []
    for i in range(len(listHex)):
        listDec.append(HexatoDec(listHex[i]))
    return listDec

def convertToASCII(listDec):
    contentASCII = ''
    for i in range(len(listDec)):
        ascii_value = listDec[i]
        contentASCII += chr(ascii_value)
    return contentASCII


# AFFICHAGE
x = storeInList(string)
y = convertToDec(x)
z = convertToASCII(y)
print(z)





