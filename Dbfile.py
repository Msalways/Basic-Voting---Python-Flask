import MySQLdb._exceptions
from mysql import connector
from MySQLdb import connect

dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'password': 'password@25',
            'database': 'votingsystem'}

# conn = connector.connect(**dbconfig)
conn = connect(**dbconfig)
cursor = conn.cursor()


def insertuser(uid, name, pwd, state, region):
    _SQL = """insert into user values(%s,%s,%s,%s,%s)"""
    try:
        cursor.execute(_SQL, (uid, name, pwd, state, region))
        conn.commit()
        return True
    except MySQLdb._exceptions.IntegrityError:
        return False


def checkVisited():
    emptySQL = """select user_id from visited """
    cursor.execute(emptySQL)
    res = cursor.fetchall()
    # print(res)
    if res == ():
        print(res)
        return True
    elif res:
        print("False")
        return False


def insvisited(uid):
    _insVisited = f"""insert into visited(user_id) values("{uid}") """
    cursor.execute(_insVisited)
    conn.commit()


def checkLogDetails(uid, pwd):
    check = checkVisited()
    print("This is about visisted", check)
    _SQL = f"""select user_id from user 
            where user_id = "{uid}" and password = "{pwd}"  """
    cursor.execute(_SQL)
    conn.commit()
    res = cursor.fetchall()
    print(res[3:-5])
    print(uid)
    if check is not False:
        print("This is about verification on user", res)
        if res:
            insvisited(uid)
            return True
        else:
            return False
    elif res != () and res is not None:
        _CheckVisited = f"""select user_id from visited where user_id = "{uid}" """
        cursor.execute(_CheckVisited)
        conn.commit()
        result = cursor.fetchall()
        print(result, res)
        if result == ():
            _insVisited = f"""insert into visited(user_id) values("{uid}") """
            cursor.execute(_insVisited)
            conn.commit()
            return True
        elif result == res:
            return "voted"
    else:
        return False


# print(checkLogDetails('hel', 'hel'))


def adminCheck(aid, pwd):
    _SQL = f"""select admin_id, password from admin 
                    where admin_id = "{aid}" and password = "{pwd}" """
    cursor.execute(_SQL)
    conn.commit()
    res = cursor.fetchall()
    if res:
        return True
    else:
        return False


def insCandi(name, party, state, region):
    i = 0
    _SQL = """insert into vote values(%s,%s,%s,%s,%s)"""
    try:
        if str(name).isalpha():
            cursor.execute(_SQL, (name, party, state, region, i))
            conn.commit()
            return True
        else:
            return False
    except MySQLdb._exceptions.IntegrityError:
        return False


def deleteUser(uid):
    _SQL = f"""delete from user where user_id = "{uid}" """
    cursor.execute(_SQL)
    conn.commit()
    res = cursor.fetchall()
    if res == ():
        return True
    else:
        return False


def getLoc(userid):
    _SQL = f"""select state,region from user where user_id = '{userid}' """
    cursor.execute(_SQL)
    conn.commit()
    res = cursor.fetchone()
    res = list(res)
    state = res[0]
    region = res[1]
    print(state, region)
    return state, region


def checkCandi(userid):
    state, region = getLoc(userid)
    print(state, region)
    _SQL = f"""select candidate,party from vote where state = '{state}' and region = '{region}' """
    cursor.execute(_SQL)
    conn.commit()
    return list(cursor.fetchall())


def listCandi():
    _SQL = f"""select candidate, party from vote"""
    cursor.execute(_SQL)
    conn.commit()
    res = cursor.fetchall()
    return res


print(listCandi())


def VoteFor(id):
    getVote = f"""select vote from vote where candidate = '{id}' """
    cursor.execute(getVote)
    conn.commit()
    votes = cursor.fetchall()
    print(votes)
    if votes != "()":
        votes = str(votes)
        votes = "".join(votes[2:-4])
        castVote = int(votes) + 1
        _SQL = f""" update vote set vote = {castVote} where candidate = '{id}' """
        cursor.execute(_SQL)
        conn.commit()
        res = cursor.fetchall()
        if res == ():
            return True
        else:
            return False
    else:
        return False


def RemoveVisiteds():
    _SQL = """delete from visited"""
    cursor.execute(_SQL)
    conn.commit()
    res = cursor.fetchall()
    if res == ():
        return True
    else:
        return False


def dispResults():
    _SQL = """select candidate,vote from vote"""
    cursor.execute(_SQL)
    conn.commit()
    res = list(cursor.fetchall())
    print(res)
    if res != () and res is not None:
        return res
    else:
        return None


# print(dispResults())


def MaximumVotes():
    _SQL = """select candidate, max(vote) from vote"""
    cursor.execute(_SQL)
    conn.commit()
    res = cursor.fetchall()
    return res


def delcandi(name):
    _SQL = f"""delete from vote where candidate = '{name}' """
    cursor.execute(_SQL)
    conn.commit()
    return True
