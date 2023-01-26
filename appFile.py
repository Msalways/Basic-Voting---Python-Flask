import time

from flask import Flask, render_template, request, url_for

from admin import adminVerify
from candidates import insCandidates, DisplayCandi, voteTo, delCandi, getCandi
from results import DispResults, maxi
from users import addUser, checkLogin, RemoveUser, removeVisited

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def home():
    title = ""
    return render_template('Enter_Login.html', title=title)


@app.route('/loginVerification', methods=['POST'])
def loginVerify():
    userid = str(request.form['id'])
    pwd = str(request.form['password'])
    if len(userid) != 0 and len(pwd) != 0:
        check = checkLogin(userid, pwd)
        dispCandi = DisplayCandi(userid)
        print("This is at app file", check)
        time.sleep(1)
        if check is True and check != "voted":
            return render_template('candidate.html', candidate=dispCandi)
        elif check == "voted":
            return render_template('Enter_Login.html', title="Already Voted")
        else:
            return render_template('Enter_Login.html', title="Invalid data")
    else:
        return render_template('Enter_Login.html', title="Fill the details")


@app.route('/sign_up')
def sign_up():
    return render_template('signup.html')


@app.route('/sign_up/adduser', methods=['POST'])
def add():
    userId = str(request.form['id'])
    uname = str(request.form['uname'])
    pwd = str(request.form['password'])
    repwd = str(request.form['repassword'])
    state = str(request.form['state'])
    region = str(request.form['region'])
    if pwd == repwd:
        verify = addUser(userId, uname, pwd, state, region)
        if verify:
            return render_template('home.html', title="Account Created")
        else:
            return render_template('home.html', title="Account already exist")


@app.route('/admin')
def admin():
    return render_template('admin.html', title="admin")


@app.route('/adminVerification', methods=['POST'])
def adminVerification():
    aid = str(request.form['id'])
    pwd = str(request.form['password'])
    check = adminVerify(aid, pwd)
    if check:
        return render_template('adminWorks.html')
    else:
        return render_template('admin.html', title='Invalid')


@app.route('/addCandidates')
def addCandidates():
    return render_template("addCandidates.html", command="add details")


@app.route('/insertCandidates', methods=['POST'])
def insertCandidates():
    name = str(request.form['cname'])
    party = str(request.form['party'])
    state = str(request.form['state'])
    region = str(request.form['region'])
    ins = insCandidates(name, party, state, region)
    if ins:
        return render_template("addCandidates.html", command=ins)
    else:
        return render_template("addCandidates.html", command="Not inserted give correct data")


@app.route('/removeUsers')
def removeUsers():
    return render_template("removeUsers.html")


@app.route('/deleteUsers', methods=['POST'])
def deleteUsers():
    uid = request.form['uid']
    check = RemoveUser(uid)
    if not check:
        return render_template("removeUsers.html", command=check)
    else:
        return render_template("removeUsers.html", command="No user found")


@app.route('/addVote', methods=['POST'])
def addVote():
    vote = request.form['Candidates']
    voted = voteTo(vote)
    if voted:
        return render_template("Enter_Login.html", title="Voted successfully")
    else:
        return render_template("Enter_login.html", title="Vote not Casted")


@app.route('/deleteVisited')
def deleteVisited():
    if removeVisited():
        return render_template("adminWorks.html", command="Deleted Successfully")
    else:
        return render_template("adminWorks.html", command="No Visited data")


@app.route('/results')
def results():
    can = DispResults()
    check = maxi()
    if check is not None:
        return render_template("results.html", can=can, maxi=check)
    else:
        return render_template("home.html", title="Poll not yet started")


@app.route('/removeCandi')
def removeCandi():
    return render_template("removeCandidates.html")


@app.route('/DeleteCandidates', methods=['POST'])
def deleteCandi():
    name = str(request.form['name'])
    if delCandi(name):
        return render_template("adminWorks.html", command='deleted')
    else:
        return render_template("adminWorks.html", command='No Candidates found')


@app.route('/DisplayCandidates')
def displayCandidates():
    res = getCandi()
    if not res:
        return render_template("adminWorks.html", command="No candidates")
    else:
        return render_template("displayCandidates.html", disp=res)


@app.route('/adminTimer')
def adminTimer():
    return render_template("adminTimer.html")

@app.route('/adminTimerStart')
def adminTimerStart():
    return render_template("Enter_Login.html")