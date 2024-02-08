def decode_ceaser_cypher(str):
    lag=15
    newstr=""
    for i in str:
        if i ==" ":newstr+=" ";continue
        if 65<=ord(i)<=90:
            newstr+=chr((ord(i)-65+lag)%26+65)
            continue
        if 97<=ord(i)<=122:
            newstr+=chr((ord(i)-97+lag)%26+97)
            continue
    return newstr

    
s="a"
d=int(s,17)
print(d)
print(decode_ceaser_cypher("SP TD LY LESPTDE HSZ OZPD YZE MPWTPGP TY STXDPWQ"))

# 1) EXOA TLOH EXP KL PRYPQFQRQB

# 2) SP TD LY LESPTDE HSZ OZPD YZE MPWTPGP TY STXDPWQ