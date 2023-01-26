from Dbfile import insertuser, checkLogDetails, deleteUser, RemoveVisiteds


def addUser(uid, name, password, state, region):
    check = insertuser(uid, name, password, state, region)
    return check


def checkLogin(uid, password):
    check = checkLogDetails(uid, password)
    print("This is on user.py", check)
    if check != "voted" and check is True:
        return True
    elif check == "voted":
        return "voted"
    elif check is False:
        return False


def RemoveUser(uid):
    delete = deleteUser(uid)
    if delete:
        return True
    else:
        return False


def removeVisited():
    if RemoveVisiteds():
        return True
    else:
        return False
