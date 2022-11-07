from typing import List


def tomins(secs):
    return secs // 60 + (1 if secs % 60 != 0 else 0)


def total_cost(calls: List[str]) -> int:
    aux = tomins(int(calls[0].split(' ')[2]))
    mins = []
    for i in range(1, len(calls)):
        secs = int(calls[i].split(' ')[2])
        if calls[i].split(' ')[0] != calls[i - 1].split(' ')[0]:
            mins.append(aux)
            aux = tomins(secs)
        else:
            aux += tomins(secs)
    mins.append(aux)

    coins = 0
    for m in mins:
        if m > 100:
            coins += 100 + (m - 100) * 2
        else:
            coins += m

    return coins


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
