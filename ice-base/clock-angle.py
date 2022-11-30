def clock_angle(time):
    deg_mins = 360 / 60
    deg_hour = 360 / 12

    hour = int(time[:2])
    mins = int(time[3:])
    hour -= 12 if hour > 12 else 0

    min_pos = mins * deg_mins
    hour_pos = hour * deg_hour

    angle = hour_pos + (1 / (60 / mins)) * deg_hour if mins != 0 else hour_pos
    angle = abs(angle - min_pos)

    if angle > 180: angle = 360 - angle

    return angle


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("08:15") == 157.5, "08:15"
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
