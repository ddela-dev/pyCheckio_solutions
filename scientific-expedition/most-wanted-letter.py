def checkio(text: str) -> str:
    novalid=[' ','-',',','!','?','0','1','2','3','4','5','6','7','8','9']
    aux=list(text.lower())
    chars=list(text.lower())
    ldic={}
    for a in aux:
        if a in novalid:
            chars.remove(a)
    for c in chars:
        ldic[c]=0
    for c in chars:
        ldic[c]+=1
    ldic={k: v for k, v in sorted(ldic.items(), key=lambda item: item[1], reverse=True)}
    lldic=list(ldic)
    maxcount=lldic[0]
    pop=[]
    for l in ldic:
        if ldic[l] == ldic[maxcount]:
            pop.append(l)
    pop.sort()
    return pop[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Lorem ipsum dolor sit amet 0000000000000000000"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
