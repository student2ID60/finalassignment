from django.shortcuts import render
from django.template.response import TemplateResponse
from finalassignmentapp.models import Reading
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from finalassignmentapp.forms import UserForm
from finalassignmentapp.models import Users

import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging


def home(request):
    data = Reading.objects.last()  # .last() so that you get the most current results

    return TemplateResponse(request, 'index.html', {'data': data})

def userView(request):
    if request.method == 'POST':  # If the forms has been sumbitted

        command = request.POST.get('command', '')

        if command == "login":
            message = ""
            user_lists = []
            form = UserForm(request.POST)

            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            loggedin = True
            #user_obj = Users(us_name=username, us_password=password, us_loggedin=loggedin)
            #user_obj.save()

            # open database
            try:
                conn = psycopg2.connect(dbname='d3enlk294pbi15', user='tleawaslframmo',
                                        host='ec2-107-22-236-252.compute-1.amazonaws.com',
                                        password='6f347648c1a4b2a5aeb99ef699a0aba2d4f4a64d614b68c6159e180dc2b60e3e')
                print('Opened DB successfully')
            except:
                print(datetime.now(), "Unable to connect to the database")
                logging.exception("Unable to open the database")
                return
            else:
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            stmt = "SELECT us_password FROM finalassignmentapp_users WHERE us_name=%s"
            params = (username,)
            cur.execute(stmt,params)
            username_exists = cur.fetchone()

            current_user = {'id': 0, 'us_name': '', 'us_password': '', 'us_loggedin': False}
            username2 = ''

            if username_exists is None:
                # write data to database
                cur.execute("""INSERT INTO finalassignmentapp_users (us_name, us_password, us_loggedin)
                                VALUES (%s, %s, %s)""",
                            (username, password, loggedin))
                conn.commit()
                print("Data Written", datetime.now())
                current_user = Users.objects.last()  # niet zo netjes
                username2 = current_user.us_name

            else :
                required_password = username_exists[0]
                if password == required_password:
                    stmt = "UPDATE finalassignmentapp_users SET us_loggedin=TRUE WHERE us_name=%s"
                    params = (username,)
                    cur.execute(stmt,params)
                    conn.commit()
                    current_user = Users.objects.filter(us_name=username).first()
                    username2 = username

                    stmt = "SELECT * FROM finalassignmentapp_lists WHERE li_username=%s"
                    params = (username,)
                    cur.execute(stmt, params)
                    user_lists = cur.fetchall()

                else:
                    message = "Wrong password for chosen username, try again"


            cur.close()
            conn.close()

            return TemplateResponse(request, 'index.html', {
                'username': username2,
                'data': current_user,
                'login_message': message,
                'user_lists': user_lists,
            })
            #return HttpResponseRedirect('../lists.html')  # Redirect after POST


        elif command == "make_list":

            username = request.POST.get('username')
            listname = request.POST.get('listname')
            listid = ""
            user_lists = request.POST.get('user_lists')

            # open database
            try:
                conn = psycopg2.connect(dbname='d3enlk294pbi15', user='tleawaslframmo',
                                        host='ec2-107-22-236-252.compute-1.amazonaws.com',
                                        password='6f347648c1a4b2a5aeb99ef699a0aba2d4f4a64d614b68c6159e180dc2b60e3e')
                print('Opened DB successfully')
            except:
                print(datetime.now(), "Unable to connect to the database")
                logging.exception("Unable to open the database")
                return
            else:
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            stmt = "SELECT id FROM finalassignmentapp_lists WHERE (li_name=%s) AND (li_username=%s)"
            params = (listname, username,)
            cur.execute(stmt, params)
            listname_exists = cur.fetchone()

            if listname_exists is None:
                # write data to database
                cur.execute("""INSERT INTO finalassignmentapp_lists (li_name, li_username)
                                            VALUES (%s, %s)""",
                            (listname, username))
                conn.commit()
                print("Data Written", datetime.now())

                stmt = "SELECT id FROM finalassignmentapp_lists WHERE (li_name=%s) AND (li_username=%s)"
                params = (listname, username,)
                cur.execute(stmt, params)
                listid = str(cur.fetchone()[0])

                stmt = "SELECT * FROM finalassignmentapp_lists WHERE li_username=%s"
                params = (username,)
                cur.execute(stmt, params)
                user_lists = cur.fetchall()

                #message = "Made list with id: " + listid
                message = ""
            else:
                message = "You already made a list with this name, try another name or load a list"

            cur.close()
            conn.close()

            return TemplateResponse(request, 'index.html', {
                'username': request.POST.get('username'),
                'user_lists': user_lists,
                'make_list_message': message,
                'tab': 'lists',
                'list_id': listid,
            })

        elif command == "load_list":
            username = request.POST.get('username')
            listname = request.POST.get('listname')
            listid = request.POST.get('list_id')
            user_lists = request.POST.get('user_lists')

            # open database
            try:
                conn = psycopg2.connect(dbname='d3enlk294pbi15', user='tleawaslframmo',
                                        host='ec2-107-22-236-252.compute-1.amazonaws.com',
                                        password='6f347648c1a4b2a5aeb99ef699a0aba2d4f4a64d614b68c6159e180dc2b60e3e')
                print('Opened DB successfully')
            except:
                print(datetime.now(), "Unable to connect to the database")
                logging.exception("Unable to open the database")
                return
            else:
                cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            stmt = "SELECT * FROM finalassignmentapp_orders WHERE or_listid=%s"
            params = (int(listid),)
            cur.execute(stmt, params)
            list_orders = cur.fetchall()

            cur.close()
            conn.close()

            return TemplateResponse(request, 'index.html', {
                'username': request.POST.get('username'),
                'user_lists': user_lists,
                'make_list_message': '',
                'tab': 'lists',
                'list_id': listid,
                'list_orders': list_orders,
            })

    else:
        form = UserForm()  # An unbound form
        return render(request, 'index.html', {
            'form': form,
            'user_lists': [],
        })

def favourites(request):
    current_user = {'id': self.data.id, 'us_name': '', 'us_password': '', 'us_loggedin': False}
    return TemplateResponse(request, 'favourites.html', {'data': current_user})

def lists(request):
    current_user = Users.objects.last()  # niet zo netjes
    return TemplateResponse(request, 'lists.html', {'data': current_user})

