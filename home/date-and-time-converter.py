import datetime


def date_time(time: str) -> str:
    date = datetime.datetime.strptime(time, "%d.%m.%Y %H:%M")
    strdate = ""

    strdate += str(int(date.strftime("%d")))

    strdate += date.strftime(" %B %Y ")
    strdate += "year "
    strdate += str(int(date.strftime("%H")))

    if int(date.strftime("%H")) == 1:
        strdate += " hour "
    else:
        strdate += " hours "

    strdate += str(int(date.strftime("%M")))

    if int(date.strftime("%M")) == 1:
        strdate += " minute"
    else:
        strdate += " minutes"

    return strdate


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
            date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
            date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
            date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
