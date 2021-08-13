from random import random, randrange, choice, randint
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ("com", "edu", "net", "org", "gov")

for i in range(randrange(5, 11)):
    dtint = randrange(maxsize)
    dstr = ctime(randint(0,10))
    llen = randrange(4, 8)
    login = "".join(choice(lc))
    dlen = randrange(llen, 13)
    dom = "".join(choice(lc) for i in range(dlen))
    print(
        "%s::%s@%s.%s::%d-%d-%d" % (dstr, login, dom, choice(tlds), dtint, llen, dlen)
    )
