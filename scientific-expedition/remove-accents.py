import unicodedata


def checkio(in_string):
    string = unicodedata.normalize('NFD', in_string)
    res = []
    for st in string:
        if unicodedata.category(st) != 'Mn':
            res.append(st)

    return ''.join(res)

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(u"ằẰ") == u"aA"
    assert checkio(u"áćéǵíḱĺḿńóṕŕśúẃýźÁĆÉǴÍḰĹḾŃÓṔŔŚÚẂÝŹ") == u"acegiklmnoprsuwyzACEGIKLMNOPRSUWYZ"
    assert checkio(u"ȁȅȉȍȑȕȀȄȈȌȐȔ") == u"aeioruAEIORU"
    assert checkio(u"ờỜừỪ") == u"oOuU"
    assert checkio(u"ầẦềỀồỒ") == u"aAeEoO"
    assert checkio(u"ằẰ") == u"aA"
    assert checkio(u"àèìǹòùẁỳÀÈÌǸÒÙẀỲ") == u"aeinouwyAEINOUWY"
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
