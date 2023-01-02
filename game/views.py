import mysql.connector

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
cnx = mysql.connector.connect(user='root', password='165924545',
                              host='127.0.0.1',
                              database='game')
def main_page(request):
    return render(request, 'main_page.html')

def singleplayer(request):
    return render(request, 'singleplayer.html')

def multiplayer(request):
    return render(request, 'multiplayer.html')

def register(request):
    return render(request, 'register.html', )

def login(request):
    return render(request, 'login.html')

def finishregistration(request):

    cursor = cnx.cursor()
    username = (request.POST['username'])
    password = (request.POST['password'])
    print(username, password)
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
