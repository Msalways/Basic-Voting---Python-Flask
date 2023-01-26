from Dbfile import insCandi, checkCandi, VoteFor, delcandi, listCandi

candidates = {}

def insCandidates(name, party, state, region):
    check = insCandi(name, party, state, region)
    if check:
        return True
    else:
        return False


def DisplayCandi(userid):
    disp = checkCandi(userid)
    for row in disp:
        cname = row[0]
        pname = row[1]
        if len(candidates) > 0 and row not in candidates:
            candidates[cname] = pname
        elif len(candidates) == 0:
            candidates[cname] = pname
        print(candidates)
    return candidates


print(DisplayCandi('hel'))


def voteTo(id):
    vote = VoteFor(id)
    if vote:
        return True
    else:
        return False


def delCandi(name):
    return delcandi(name)


def getCandi():
    disp = listCandi()
    if disp != ():
        return disp
    else:
        return False
