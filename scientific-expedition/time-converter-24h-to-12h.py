def time_converter(time):
    hm=time.split(":")
    newtime=""
    if(int(hm[0])>12):
        newtime+=str(int(hm[0])-12)
    else:
        if(hm[0]!="00"):
            newtime+=str(int(hm[0]))
        else:
            newtime+="12"
    newtime+=":"+hm[1]
    if(int(hm[0])<12):
        newtime+=" a.m."
    else:
        newtime+=" p.m."
    return newtime

if __name__ == '__main__':
    print("Example:")
    print(time_converter('09:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
