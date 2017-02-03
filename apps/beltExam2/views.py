from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.db.models import Count
from datetime import datetime
from dateutil.parser import *
from django.db import connection
print connection.queries


from ..LogReg.models import User
from .models import Poke



def index(request):
    user_id = request.session['logged_in_user']
    user = User.objects.get(id = request.session['logged_in_user'])

    # .annotate(countpokers=Count('poked', distinct=True))

    everything = Poke.objects.all()

    poker_history = User.objects.filter(poker_key__poked=user).annotate(counting=Count("poker_key__poked"))
    # test=len(poker_history)
    test = Poke.objects.filter(poked=user).values('poker__name').distinct().count()
    poked_history = User.objects.filter(poked_key__poker=user).annotate(counting=Count("poked_key__poker"))

    others = User.objects.annotate(poked_history=Count('poked_key')).all().exclude(id=request.session['logged_in_user'])


    # print "*" *50
    # print dir(user)
    # manytomany = user.user_set.all()


    context={
        'user': user,
        'test': test,
        'poker_history': poker_history,
        'poked_history': poked_history,
        'others': others,
        'everything': everything,
        # 'manytomany': manytomany,
        # 'user_poked': user_poked,
    }

    return render(request, "beltExam2/index.html", context)

def logout(request):
    auth.logout(request)
    return redirect("/main")


def poking(request, id):
    user = User.objects.get(id = request.session['logged_in_user'])
    user_being_poked = User.objects.get(id=id)
    Poke.objects.create(poker=user, poked=user_being_poked)


    user.poked.add(user_being_poked)
    user.save()

    return redirect('/pokes')
