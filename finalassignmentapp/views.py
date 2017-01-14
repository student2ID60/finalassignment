from django.template.response import TemplateResponse
from finalassignmentapp.models import Reading

from finalassignmentapp.forms import UserForm
from finalassignmentapp.models import Users


def home(request):
    data = Reading.objects.last() # .last() so that you get the most current results

    return TemplateResponse(request, 'index.html', {'data': data})


def favourites(request):
    data = Reading.objects.last() # .last() so that you get the most current results

    return TemplateResponse(request, 'favourites.html', {'data': data})

def userView(request):
    if request.method == 'POST': # If the forms has been sumbitted

        form = UserForm(request.POST)
        if form.is_valid(): # All validation rules pass
            usernaam = request.POST.get('username', '')
            wachtwoord = request.POST.get('password', '')
            ingelogd = True
            user_obj = Users(us_name = usernaam, us_password = wachtwoord, us_loggedin = ingelogd)
            user_obj.save()

            return HttpResponseRedirect(reverse('finalassignment:index.html')) # Redirect after POST
    else:
        form = UserForm() # An unbound form

    return render(request, 'index.html', {
        'form' : form,
    })