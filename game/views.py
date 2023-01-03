import mysql.connector

from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
cnx = mysql.connector.connect(user='root', password='165924545',
                              host='127.0.0.1',
                              database='game')
def main_page(request):
    if 'user' in request.session:
        return render(request, 'main_page.html', {'user': request.session['user']})
    return render(request, 'main_page.html', {'user':''})

def singleplayer(request):
    return render(request, 'singleplayer.html')

def multiplayer(request):
    return render(request, 'multiplayer.html')

def register(request):
    if 'user' in request.session:
        return render(request, 'failsession.html')
    return render(request, 'register.html', )

def login(request):
    if 'user' in request.session:
        return render(request, 'failsession.html')
    return render(request, 'login.html')

def finishregistration(request):
    if 'user' in request.session:
        return render(request, 'failsession.html')
    if not request.POST:
        return redirect('../main_page/')
    cursor = cnx.cursor()
    username = (request.POST['username'])
    password = (request.POST['password'])
    # print(username, password)
    sql = f"SELECT id FROM players WHERE '{username}' = players.username;"
    cursor.execute(sql)
    count = 0
    name = False
    ok = 'good'
    for _ in cursor:
        count += 1
    if count != 0:
        name = True
        ok = 'used'
    pw = False
    if 5 > len(password) or len(password) > 255:
        pw = True
        ok = 'pw'
    length = False
    if 3 > len(username) or len(username) > 16:
        length = True
        ok = 'username'
    if ok == 'good':
        request.session['user'] = username
        cursor.execute(f'''INSERT INTO players (username, password, money, level, hpLevel, shotgunLevel, pistolLevel, machineGunLevel, sniperLevel, rpgLevel, flamethrowerLevel, knivesLevel, grenadeLevel, shotgunAmmo, machineGunAmmo, sniperAmmo, rpgAmmo, flamethrowerAmmo, knivesAmmo, grenadeAmmo)
VALUES ('{username}', '{password}', 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);''')
        cnx.commit()
        return render(request, 'finishregistration.html')
    else:
        return render(request, 'register.html', {"name": name, "pw":pw, "length":length})

def failsession(request):
    return render(request, 'failsession.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return render(request, 'failsession.html')
    return redirect('../main_page/')

def finishlogin(request):
    if 'user' in request.session:
        return render(request, 'failsession.html')
    if not request.POST:
        return redirect('../main_page/')
    cursor = cnx.cursor()
    username = (request.POST['username'])
    password = (request.POST['password'])
    wrong = False
    sql = f"SELECT password FROM players WHERE '{username}' = players.username;"
    cursor.execute(sql)
    count = 0
    for i in cursor:
        count += 1
        if password != i[0]:
            wrong = True
        else:
            request.session['user'] = username
    if count == 0 or wrong:
        return render(request, 'login.html', {'wrong': True})
    else:
        return render(request, "finishregistration.html")
