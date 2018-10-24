from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from datetime import datetime
from .models import *


###---GET---------------------------INDEX ROUTE
def index(request):
    try:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            "wishes": Wish.objects.filter(wisher=user,granted_at__isnull=True),
            "grantedwishes": Wish.objects.filter(granted_at__isnull=False)
        }
        wishes = Wish.objects.filter(wisher=user)
        return render(request, 'wishes_app/index.html', context)
    except:
        return redirect('/')


###---GET---------------------------NEW ROUTE
def new(request):
    return render(request, 'wishes_app/new.html')


###---POST---------------------------CREATE ROUTE
def create(request):
    errors = Wish.objects.basic_validator(request.POST)
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wishes/new')
    else:
        user = User.objects.get(id=request.session['user_id'])

        new_wish = Wish.objects.create(
            item = request.POST['item'],
            description = request.POST['description'],
            wisher = user
        )

        messages.add_message(
            request, messages.SUCCESS,
            'Your wish has been stored.'
        )

    return redirect('/wishes')


###---GET-----------------------------EDIT ROUTE
def edit(request,id):
    try:
        user = User.objects.get(id=request.session['user_id'])
    
        return render(request, 'wishes_app/edit.html', {"wish": Wish.objects.get(id=id, wisher=user)}) 
    except:
        messages.add_message(
            request, messages.ERROR,
            "You cannot edit a wish that is not yours."
        )
        
        return redirect('/wishes')

###---POST------------------------------UPDATE ROUTE
def update(request):
    errors = Wish.objects.basic_validator(request.POST)
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/wishes/<wish_id>/edit/",wish_id=request.POST['wish_id'] )
    else:
        w = Wish.objects.get(id=request.POST['wish_id'])
        w.item = request.POST['item']
        w.description = request.POST['description']
        w.save()

        messages.add_message(
            request, messages.SUCCESS,
            'Your wish has been updated.'
        )

    return redirect('/wishes')

###---POST------------------------------DESTROY ROUTE
def destroy(request,id):
    try:
        user = User.objects.get(id=request.session['user_id'])
        checkwish = Wish.objects.get(id=id, wisher=user) 
        if checkwish:
            Wish.objects.get(id=id).delete()
            print("Deleted wish_id = " + id)

            return redirect('/wishes')
    except:
        messages.add_message(
            request, messages.ERROR,
            "You cannot delete a wish that is not yours."
        )
            
        return redirect('/wishes')

###---POST-------------------------------GRANT A WISH
def grant(request,id):
        user = User.objects.get(id=request.session['user_id'])
        checkwish = Wish.objects.get(id=id, wisher=user) 
        if checkwish:
            w = Wish.objects.get(id=id)
            w.granted_at = datetime.now()
            w.save()

            return redirect('/wishes')
    
        messages.add_message(
            request, messages.ERROR,
            "You cannot edit a wish that is not yours."
        )
            
        return redirect('/wishes')

###---GET--------------------------------STATS
def stats(request):
    try:
        user = User.objects.get(id=request.session['user_id'])

        context = {
            "total_wishes": Wish.objects.all,
            "my_pending": Wish.objects.filter(wisher=user,granted_at__isnull=True),
            "my_granted": Wish.objects.filter(wisher=user,granted_at__isnull=False)
        }
        print(user.id)
        return render(request, 'wishes_app/stats.html',context)
    
    except:
        return redirect('/')


def like(request,id):
    try:
        user = User.objects.get(id=request.session['user_id'])
        checkliked = Wish.objects.filter(liker=user, id = id)

        if checkliked.count() > 0:
            messages.add_message(
                request, messages.ERROR,
             "You've already liked that wish."
            )
            print(checkliked.likes.count)
            return redirect('/wishes')
        else:

            this_wish = Wish.objects.get(id=id)
            user.likes.add(this_wish)

            return redirect('/wishes')
    
    except:
        print("exception")
        return redirect('/wishes')