string = 'abc'

def allcomb(string):
    combs = []
    for i in range(1, 2**len(string)):
        pat = "{0:b}".format(i).zfill(len(string))
        combs.append(''.join(c for c,b in zip(string, pat) if int(b)))
    
    print(type(set(combs)))
    return list(set(combs))


print(allcomb("sdfsdf"))