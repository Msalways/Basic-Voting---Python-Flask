from Dbfile import adminCheck


def adminVerify(aid, pwd):
    check = adminCheck(aid, pwd)
    if check:
        return True
    else:
        return False
