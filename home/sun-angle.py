from typing import Union

def sun_angle(time: str) -> Union[int, str]:
    hm=time.split(":")
    if(int(hm[0])<6 or (int(hm[0])>=18 and int(hm[1])>0)):
        return "I don't see the sun!"
    else:
        angle=(((int(hm[0])-6)*60)+int(hm[1]))*0.25
        return angle

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
