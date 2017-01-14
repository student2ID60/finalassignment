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


def favourites(request):
    data = Reading.objects.last()  # .last() so that you get the most current results

    return TemplateResponse(request, 'favourites.html', {'data': data})

def userView(request):
    if request.method == 'POST':  # If the forms has been sumbitted

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

        cur.execute("SELECT COUNT FROM finalassignmentapp_users WHERE us_name = %s" % (username))
        username_exists = cur.fetchone()

        if username_exists is None:
            # write data to database
            cur.execute("""INSERT INTO finalassignmentapp_users (us_name, us_password, us_loggedin)
                            VALUES (%s, %s, %s)""",
                        (username, password, loggedin))
            conn.commit()
            print("Data Written", datetime.now())
        else:
            return HttpResponse('Username already in use, try another one')

        cur.close()
        conn.close()


        return HttpResponseRedirect('../favourites.html')  # Redirect after POST

    else:
        form = UserForm()  # An unbound form
        return render(request, 'index.html', {
            'form': form,
        })